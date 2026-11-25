import asyncio
import hashlib
import json
import os
import re
import edge_tts

# Two voice engines:
# 1. "cz_studio" (DEFAULT): Native Czech voices (Antonín & Vlasta) with sentence-level dynamic prosody
#    and 100% Czech phonetic transcription of all English acronyms/brands so nothing is ever spelled out robotically.
# 2. "multi_hd": European MultilingualNeural voices (Florian & Seraphina) with clean technical spellings.
ENGINES = {
    "cz_studio": {
        "Marek": {"voice": "cs-CZ-AntoninNeural", "base_rate": 4, "base_pitch": -1},
        "Tereza": {"voice": "cs-CZ-VlastaNeural", "base_rate": 3, "base_pitch": 1},
        "tts_field": "tts_cz",
        "filename": "podcast_satelity_cz.mp3",
    },
    "multi_hd": {
        "Marek": {"voice": "de-DE-FlorianMultilingualNeural", "base_rate": 3, "base_pitch": -1},
        "Tereza": {"voice": "de-DE-SeraphinaMultilingualNeural", "base_rate": 2, "base_pitch": 1},
        "tts_field": "tts_multi",
        "filename": "podcast_satelity_multi.mp3",
    },
}

# Valid silent 24kHz 48kbps mono MP3 frame (144 bytes = 24ms)
SILENT_MP3_FRAME = bytes([0xFF, 0xF3, 0x64, 0xC4]) + bytes(140)
PAUSE_SENTENCE = SILENT_MP3_FRAME * 5   # 120ms between sentences inside one turn
PAUSE_TURN = SILENT_MP3_FRAME * 11      # 264ms between speaker turns
PAUSE_CHAPTER = SILENT_MP3_FRAME * 20   # 480ms when switching to a new chapter

SCRIPT = [
    # --- INTRO ---
    {
        "speaker": "Tereza",
        "question_id": "intro",
        "display": "Ahoj Marku! Hele, čeká mě test na **satelitní komunikace a oběžné dráhy**. Je to pro mě spíš okrajové téma a nemám přesné otázky – projdeme spolu všechno podstatné ze skript i z prezentace **GiTySAT** tak, aby mi to v hlavě hned secvaklo?",
        "tts_cz": "Ahoj Marku! Hele, čeká mě test na satelitní komunikace a oběžné dráhy. Je to pro mě spíš okrajové téma a nemám přesné otázky. Projdeme spolu všechno podstatné ze skript i z prezentace dží-ty-sat tak, aby mi to v hlavě hned secvaklo?",
        "tts_multi": "Ahoj Marku! Hele, čeká mě test na satelitní komunikace a oběžné dráhy. Je to pro mě spíš okrajové téma a nemám přesné otázky. Projdeme spolu všechno podstatné ze skript i z prezentace GiTySAT tak, aby mi to v hlavě hned secvaklo?"
    },
    {
        "speaker": "Marek",
        "question_id": "intro",
        "display": "Jasně Terezo, dáme to úplně v klidu! Žádné zbytečné odvozování vzorců – půjdeme po logice věci, srovnáních a chytácích, na které se učitelé ptají nejčastěji. Rozdělili jsme si to do devíti přehledných kapitol. Jdeme na **orbitální mechaniku**?",
        "tts_cz": "Jasně Terezo, dáme to úplně v klidu! Žádné zbytečné odvozování vzorců. Půjdeme po logice věci, srovnáních a chytácích, na které se učitelé ptají nejčastěji. Rozdělili jsme si to do devíti přehledných kapitol. Jdeme na orbitální mechaniku?",
        "tts_multi": "Jasně Terezo, dáme to úplně v klidu! Žádné zbytečné odvozování vzorců. Půjdeme po logice věci, srovnáních a chytácích, na které se učitelé ptají nejčastěji. Rozdělili jsme si to do devíti přehledných kapitol. Jdeme na orbitální mechaniku?"
    },

    # --- SAT-1: Orbitální mechanika a Keplerovy zákony ---
    {
        "speaker": "Tereza",
        "question_id": "sat-1",
        "display": "Pojďme! Proč vlastně družice drží na oběžné dráze a nespadne na Zem, když nemá pořád zapnuté motory?",
        "tts_cz": "Pojďme! Proč vlastně družice drží na oběžné dráze a nespadne na Zem, když nemá pořád zapnuté motory?",
        "tts_multi": "Pojďme! Proč vlastně družice drží na oběžné dráze a nespadne na Zem, když nemá pořád zapnuté motory?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-1",
        "display": "Je to čistá rovnováha dvou věcí: **zemská gravitace** družici neustále přitahuje ke středu Země (a slábne se čtvercem vzdálenosti $r^2$), a tím zajišťuje potřebnou **dostředivou sílu**, která zakřivuje její let. Družice má totiž tak vysokou tečnou rychlost, že jakoby pořád padá k Zemi, ale Země se pod ní stejně rychle zakřivuje!",
        "tts_cz": "Je to čistá rovnováha dvou věcí: zemská gravitace družici neustále přitahuje ke středu Země, a slábne se čtvercem vzdálenosti. Tím zajišťuje potřebnou dostředivou sílu, která zakřivuje její let. Družice má totiž tak vysokou tečnou rychlost, že jakoby pořád padá k Zemi, ale Země se pod ní stejně rychle zakřivuje!",
        "tts_multi": "Je to čistá rovnováha dvou věcí: zemská gravitace družici neustále přitahuje ke středu Země a slábne se čtvercem vzdálenosti. Tím zajišťuje potřebnou dostředivou sílu, která zakřivuje její let. Družice má totiž tak vysokou tečnou rychlost, že jakoby pořád padá k Zemi, ale Země se pod ní stejně rychle zakřivuje!"
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-1",
        "display": "A co **odstředivá síla**? Někdy se říká, že ji vyrovnává.",
        "tts_cz": "A co odstředivá síla? Někdy se říká, že ji vyrovnává.",
        "tts_multi": "A co odstředivá síla? Někdy se říká, že ji vyrovnává."
    },
    {
        "speaker": "Marek",
        "question_id": "sat-1",
        "display": "Pozor na terminologii ze skript: **odstředivá síla** není žádná nová skutečná síla – je to jen zdánlivá setrvačná síla v neinerciální soustavě, která rotuje s družicí. A ještě jedna intuice, co se plete: **čím výš je kruhová dráha, tím POMALEJI družice letí** a tím **DELŠÍ má oběžnou dobu**! Nízko letí přes 7,5 km/s, na geostacionární dráze jen asi 3,1 km/s.",
        "tts_cz": "Pozor na terminologii ze skript! Odstředivá síla není žádná nová skutečná síla. Je to jen zdánlivá setrvačná síla v soustavě, která rotuje s družicí. A ještě jedna intuice, co se plete: čím výš je kruhová dráha, tím pomaleji družice letí a tím delší má oběžnou dobu! Nízko letí přes sedm a půl kilometru za sekundu, na geostacionární dráze jen asi tři celé jedna kilometru za sekundu.",
        "tts_multi": "Pozor na terminologii ze skript! Odstředivá síla není žádná nová skutečná síla. Je to jen zdánlivá setrvačná síla v soustavě, která rotuje s družicí. A ještě jedna intuice, co se plete: čím výš je kruhová dráha, tím pomaleji družice letí a tím delší má oběžnou dobu! Nízko letí přes sedm a půl kilometru za sekundu, na geostacionární dráze jen asi tři celé jedna kilometru za sekundu."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-1",
        "display": "Jasně, takže výš znamená pomaleji a delší oběh. A co **úniková rychlost** a **Keplerovy zákony**?",
        "tts_cz": "Jasně, takže výš znamená pomaleji a delší oběh. A co úniková rychlost a Keplerovy zákony?",
        "tts_multi": "Jasně, takže výš znamená pomaleji a delší oběh. A co úniková rychlost a Keplerovy zákony?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-1",
        "display": "**Úniková rychlost** je $\\sqrt{2}$-krát větší než kruhová – u povrchu Země asi **11,2 km/s**. Když ji dosáhneš, přejdeš na otevřenou parabolickou dráhu a Zemi opustíš. A **Keplerovy zákony** jsou tři: **První** říká, že dráha je **elipsa** se Zemí v jednom ohnisku (kruh je jen speciální případ s nulovou excentricitou). **Druhý** je zákon ploch – z něj plyne, že družice letí **nejrychleji v perigeu** (nejblíž Zemi) a **nejpomaleji v apogeu** (nejdál od Země). A **třetí** dává do poměru druhou mocninu oběžné doby se třetí mocninou hlavní poloosy.",
        "tts_cz": "Úniková rychlost je odmocnina ze dvou krát větší než kruhová, u povrchu Země asi jedenáct celé dva kilometru za sekundu. Když ji dosáhneš, přejdeš na otevřenou parabolickou dráhu a Zemi opustíš. A Keplerovy zákony jsou tři! První říká, že dráha je elipsa se Zemí v jednom ohnisku. Druhý je zákon ploch, z něj plyne, že družice letí nejrychleji v perigeu, tedy nejblíž Zemi, a nejpomaleji v apogeu, tedy nejdál od Země. A třetí dává do poměru druhou mocninu oběžné doby se třetí mocninou hlavní poloosy.",
        "tts_multi": "Úniková rychlost je odmocnina ze dvou krát větší než kruhová, u povrchu Země asi jedenáct celé dva kilometru za sekundu. Když ji dosáhneš, přejdeš na otevřenou parabolickou dráhu a Zemi opustíš. A Keplerovy zákony jsou tři! První říká, že dráha je elipsa se Zemí v jednom ohnisku. Druhý je zákon ploch, z něj plyne, že družice letí nejrychleji v perigeu, tedy nejblíž Zemi, a nejpomaleji v apogeu, tedy nejdál od Země. A třetí dává do poměru druhou mocninu oběžné doby se třetí mocninou hlavní poloosy."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-1",
        "display": "A v realitě asi nejde o dokonalou Keplerovu elipsu, že? Co tu dráhu nejvíc ruší?",
        "tts_cz": "A v realitě asi nejde o dokonalou Keplerovu elipsu, že? Co tu dráhu nejvíc ruší?",
        "tts_multi": "A v realitě asi nejde o dokonalou Keplerovu elipsu, že? Co tu dráhu nejvíc ruší?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-1",
        "display": "Přesně tak. Hlavní poruchy jsou čtyři: **zploštění Země** (nesférické gravitační pole, známé přes koeficient $J_2$), **odpor zbytkové atmosféry** u nízkých drah, **gravitace Slunce a Měsíce** a **tlak slunečního záření**.",
        "tts_cz": "Přesně tak. Hlavní poruchy jsou čtyři: zploštění Země neboli nesférické gravitační pole, dále odpor zbytkové atmosféry u nízkých drah, gravitace Slunce a Měsíce a tlak slunečního záření.",
        "tts_multi": "Přesně tak. Hlavní poruchy jsou čtyři: zploštění Země neboli nesférické gravitační pole, dále odpor zbytkové atmosféry u nízkých drah, gravitace Slunce a Měsíce a tlak slunečního záření."
    },

    # --- SAT-2: Orbitální elementy a orientace drah ---
    {
        "speaker": "Tereza",
        "question_id": "sat-2",
        "display": "Super. V druhé kapitole jsou **orbitální elementy**. Potřebuju umět všech šest prvků, co popisují dráhu v prostoru?",
        "tts_cz": "Super. V druhé kapitole jsou orbitální elementy. Potřebuju umět všech šest prvků, co popisují dráhu v prostoru?",
        "tts_multi": "Super. V druhé kapitole jsou orbitální elementy. Potřebuju umět všech šest prvků, co popisují dráhu v prostoru?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-2",
        "display": "Stačí přesně vědět, co který dělá! Jsou to tři dvojice: První dvě určují **velikost a tvar** – tedy **hlavní poloosa $a$** (velikost) a **excentricita $e$** (tvar: $0$ je kružnice, $0 < e < 1$ je elipsa). Druhé dvě určují **natočení v prostoru** – **inklinace $i$** (sklon roviny dráhy vůči rovníku, od $0^\circ$ do $180^\circ$) a **RAAN $\Omega$** (rektascenze vzestupného uzlu, která říká, jak je rovina dráhy pootočená kolem osy Země).",
        "tts_cz": "Stačí přesně vědět, co který dělá! Jsou to tři dvojice. První dvě určují velikost a tvar: tedy hlavní poloosa á a excentricita é, kde nula je kružnice a mezi nulou a jedničkou je elipsa. Druhé dvě určují natočení v prostoru: inklinace í, což je sklon vůči rovníku od nuly do sto osmdesáti stupňů, a rektascenze vzestupného uzlu omega, která říká, jak je rovina dráhy pootočená kolem osy Země.",
        "tts_multi": "Stačí přesně vědět, co který dělá! Jsou to tři dvojice. První dvě určují velikost a tvar: tedy hlavní poloosa a, a excentricita e, kde nula je kružnice a mezi nulou a jedničkou je elipsa. Druhé dvě určují natočení v prostoru: inklinace i, což je sklon vůči rovníku od nuly do sto osmdesáti stupňů, a rektascenze vzestupného uzlu RAAN, která říká, jak je rovina dráhy pootočená kolem osy Země."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-2",
        "display": "A ta třetí dvojice? To bude asi poloha perigea a samotné družice!",
        "tts_cz": "A ta třetí dvojice? To bude asi poloha perigea a samotné družice!",
        "tts_multi": "A ta třetí dvojice? To bude asi poloha perigea a samotné družice!"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-2",
        "display": "Přesně! Pátý prvek je **argument perigea $\omega$** – úhel uvnitř samotné roviny dráhy od vzestupného uzlu k perigeu. A šestý je **pravá anomálie $\nu$** (případně střední anomálie), která udává **okamžitou polohu družice** na dráze v čase. Drobný chyták: u přesně rovníkové dráhy není definován vzestupný uzel, a u přesně kruhové dráhy není definován argument perigea!",
        "tts_cz": "Přesně! Pátý prvek je argument perigea, který určuje polohu perigea uvnitř samotné roviny dráhy. A šestý je pravá anomálie, která udává okamžitou polohu družice na dráze v čase. Drobný chyták: u přesně rovníkové dráhy není definován vzestupný uzel, a u přesně kruhové dráhy není definován argument perigea!",
        "tts_multi": "Přesně! Pátý prvek je argument perigea, který určuje polohu perigea uvnitř samotné roviny dráhy. A šestý je pravá anomálie, která udává okamžitou polohu družice na dráze v čase. Drobný chyták: u přesně rovníkové dráhy není definován vzestupný uzel, a u přesně kruhové dráhy není definován argument perigea!"
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-2",
        "display": "A jak se dráhy dělí podle **inklinace**? Rovníková, polární, nakloněná… a pak tam byla ještě ta **slunečně synchronní SSO**.",
        "tts_cz": "A jak se dráhy dělí podle inklinace? Rovníková, polární, nakloněná, a pak tam byla ještě ta slunečně synchronní es-es-ó.",
        "tts_multi": "A jak se dráhy dělí podle inklinace? Rovníková, polární, nakloněná, a pak tam byla ještě ta slunečně synchronní SSO."
    },
    {
        "speaker": "Marek",
        "question_id": "sat-2",
        "display": "Jo, je to přehledné: **$i = 0^\circ$** je rovníková prográdní (po směru rotace Země). Když je **$0^\circ < i < 90^\circ$**, jde o šikmou **prográdní** dráhu (Země jí jakoby pomáhá při startu). **$i \approx 90^\circ$** je **polární dráha** přes oba póly – ideální pro meteo, SAR radary a průzkum, protože Země se pod ní otáčí a družice postupně nasnímá celý svět. A **$90^\circ < i \le 180^\circ$** je **retrográdní** dráha – tedy proti rotaci Země!",
        "tts_cz": "Jo, je to přehledné! Nula stupňů je rovníková prográdní, tedy po směru rotace Země. Mezi nulou a devadesáti stupni jde o šikmou prográdní dráhu, kde Země družici pomáhá při startu. Kolem devadesáti stupňů je polární dráha přes oba póly, ideální pro meteo a průzkum, protože Země se pod ní otáčí a družice postupně nasnímá celý svět. A nad devadesát stupňů je retrográdní dráha, tedy proti rotaci Země!",
        "tts_multi": "Jo, je to přehledné! Nula stupňů je rovníková prográdní, tedy po směru rotace Země. Mezi nulou a devadesáti stupni jde o šikmou prográdní dráhu, kde Země družici pomáhá při startu. Kolem devadesáti stupňů je polární dráha přes oba póly, ideální pro meteo a průzkum, protože Země se pod ní otáčí a družice postupně nasnímá celý svět. A nad devadesát stupňů je retrográdní dráha, tedy proti rotaci Země!"
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-2",
        "display": "A právě ta **SSO – slunečně synchronní dráha** má sklon asi **97° až 99°**, takže je lehce retrográdní! Proč se to dělá?",
        "tts_cz": "A právě ta es-es-ó, slunečně synchronní dráha, má sklon asi devadesát sedm až devadesát devět stupňů, takže je lehce retrográdní! Proč se to dělá?",
        "tts_multi": "A právě ta SSO, slunečně synchronní dráha, má sklon asi devadesát sedm až devadesát devět stupňů, takže je lehce retrográdní! Proč se to dělá?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-2",
        "display": "To je parádní trik: využije se **zploštění Země ($J_2$)**, aby se rovina dráhy pomalu stáčela tempem asi **1 stupeň za den** (přesně $+0{,}9856^\circ/\text{den}$), což přesně kopíruje roční pohyb Slunce. Výsledek? Družice přelétá nad stejným místem vždy ve **stejný místní sluneční čas**, takže stíny na fotkách jsou srovnatelné! Používá se to pro optické snímkování Země ve výškách 500 až 900 km, třeba u konstelace PlanetScope.",
        "tts_cz": "To je parádní trik! Využije se zploštění Země, aby se rovina dráhy pomalu stáčela tempem zhruba jeden stupeň za den, přesně nula celá devět osm pět šest stupně za den, což kopíruje roční pohyb Slunce. Výsledek? Družice přelétá nad stejným místem vždy ve stejný místní sluneční čas, takže stíny na fotkách jsou srovnatelné! Používá se to pro optické snímkování Země ve výškách pět set až devět set kilometrů.",
        "tts_multi": "To je parádní trik! Využije se zploštění Země, aby se rovina dráhy pomalu stáčela tempem zhruba jeden stupeň za den, přesně nula celá devět osm pět šest stupně za den, což kopíruje roční pohyb Slunce. Výsledek? Družice přelétá nad stejným místem vždy ve stejný místní sluneční čas, takže stíny na fotkách jsou srovnatelné! Používá se to pro optické snímkování Země ve výškách pět set až devět set kilometrů, třeba u konstelace PlanetScope."
    },

    # --- SAT-3: LEO, MEO, GEO a speciální dráhy (GSO, Molnija, Tundra) ---
    {
        "speaker": "Tereza",
        "question_id": "sat-3",
        "display": "Teď asi nejčastější zkoušková klasika: **rozdělení drah podle výšky – LEO, MEO a GEO**, plus speciální dráhy **GSO, Molnija a Tundra**!",
        "tts_cz": "Teď asi nejčastější zkoušková klasika: rozdělení drah podle výšky, tedy leo, meo a geo, plus speciální dráhy gé-es-ó, Molnija a Tundra!",
        "tts_multi": "Teď asi nejčastější zkoušková klasika: rozdělení drah podle výšky, tedy LEO, MEO a GEO, plus speciální dráhy GSO, Molnija a Tundra!"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-3",
        "display": "Jdeme na to! **LEO (Low Earth Orbit)** je nejníž, zhruba **160 až 2 000 km**. Družice tam letí asi 7,6 km/s, Zemi obletí za **90 až 130 minut** a má super nízkou latenci kolem **20 až 50 ms**. Nevýhoda? Z tak malé výšky vidí jen malý kousek Země (na 500 km asi 3,6 % povrchu) a rychle zmizí za horizontem, takže potřebuješ **stovky až tisíce družic** a neustálé předávání spojení.",
        "tts_cz": "Jdeme na to! Nízká dráha leo je nejníž, zhruba sto šedesát až dva tisíce kilometrů. Družice tam letí asi sedm celých šest kilometru za sekundu, Zemi obletí za devadesát až sto třicet minut a má super nízkou latenci kolem dvaceti až padesáti milisekund. Nevýhoda? Z tak malé výšky vidí jen malý kousek Země a rychle zmizí za horizontem, takže potřebuješ stovky až tisíce družic a neustálé předávání spojení.",
        "tts_multi": "Jdeme na to! Nízká dráha LEO je nejníž, zhruba sto šedesát až dva tisíce kilometrů. Družice tam letí asi sedm celých šest kilometru za sekundu, Zemi obletí za devadesát až sto třicet minut a má super nízkou latenci kolem dvaceti až padesáti milisekund. Nevýhoda? Z tak malé výšky vidí jen malý kousek Země a rychle zmizí za horizontem, takže potřebuješ stovky až tisíce družic a neustálé předávání spojení."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-3",
        "display": "Pak je **MEO (Medium Earth Orbit)** od **2 000 do 35 786 km**. Co je pro ni typické?",
        "tts_cz": "Pak je střední dráha meo od dvou tisíc do třiceti pěti tisíc sedmi set osmdesáti šesti kilometrů. Co je pro ni typické?",
        "tts_multi": "Pak je střední dráha MEO od dvou tisíc do třiceti pěti tisíc sedmi set osmdesáti šesti kilometrů. Co je pro ni typické?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-3",
        "display": "MEO je zlatý střed: oběžná doba je **2 až 24 hodin**, latence kolem **50 až 150 ms** a na globální pokrytí stačí jen **desítky družic**. Je to království navigací **GNSS** – třeba GPS ve výšce 20 200 km nebo evropské Galileo – ale i komunikační sítě **O3b** kolem 8 000 km. Pozor jen na **Van Allenovy radiační pásy**, které v některých výškách MEO vyžadují vyšší radiační odolnost elektroniky.",
        "tts_cz": "Střední dráha meo je zlatý střed: oběžná doba je dvě až dvacet čtyři hodin, latence kolem padesáti až sto padesáti milisekund a na globální pokrytí stačí jen desítky družic. Je to království navigací, třeba dží-pí-es ve výšce dvacet tisíc dvě stě kilometrů nebo evropské Galileo, ale i komunikační sítě ó-tři-bé kolem osmi tisíc kilometrů. Pozor jen na Van Allenovy radiační pásy, které v některých výškách vyžadují vyšší radiační odolnost elektroniky.",
        "tts_multi": "MEO je zlatý střed: oběžná doba je dvě až dvacet čtyři hodin, latence kolem padesáti až sto padesáti milisekund a na globální pokrytí stačí jen desítky družic. Je to království navigací GNSS, třeba GPS ve výšce dvacet tisíc dvě stě kilometrů nebo evropské Galileo, ale i komunikační sítě O3b kolem osmi tisíc kilometrů. Pozor jen na Van Allenovy radiační pásy, které v některých výškách vyžadují vyšší radiační odolnost elektroniky."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-3",
        "display": "A nahoře kraluje **GEO** ve výšce **35 786 km**! Jaké tři nebo čtyři podmínky musí splnit, aby na obloze stála jako přibitá?",
        "tts_cz": "A nahoře kraluje dráha geo ve výšce třicet pět tisíc sedm set osmdesát šest kilometrů! Jaké podmínky musí splnit, aby na obloze stála jako přibitá?",
        "tts_multi": "A nahoře kraluje GEO ve výšce třicet pět tisíc sedm set osmdesát šest kilometrů! Jaké podmínky musí splnit, aby na obloze stála jako přibitá?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-3",
        "display": "Tohle je jistá zkoušková otázka! Aby byla družice geostacionární (**GEO**), musí být: **1. kruhová** ($e = 0$), **2. rovníková** ($i = 0^\circ$), **3. prográdní** (letět po směru otáčení Země) a **4. mít periodu rovnou siderickému dni**, tedy **23 hodin 56 minut a 4 sekundy**. Pak stačí **3 družice**, aby pokryly většinu Země (jedna vidí až ~42 % povrchu), a na Zemi ti stačí **pevná anténa** bez natáčení. Jenže v polárních oblastech má strašně nízkou elevaci a nepokryje póly.",
        "tts_cz": "Tohle je jistá zkoušková otázka! Aby byla družice geostacionární, musí být: zaprvé kruhová, tedy nulová excentricita; zadruhé rovníková s nulovým sklonem; zatřetí prográdní, tedy po směru otáčení Země; a začtvrté mít periodu rovnou siderickému dni, tedy dvacet tři hodin padesát šest minut a čtyři sekundy. Pak stačí tři družice na většinu planety a na Zemi použiješ pevnou anténu bez natáčení. Jenže v polárních oblastech má nízkou elevaci a póly nepokryje.",
        "tts_multi": "Tohle je jistá zkoušková otázka! Aby byla družice geostacionární, musí být: zaprvé kruhová s nulovou excentricitou, zadruhé rovníková s nulovým sklonem, zatřetí prográdní a začtvrté mít periodu rovnou siderickému dni, tedy dvacet tři hodin padesát šest minut a čtyři sekundy. Pak stačí tři družice na většinu planety a na Zemi použiješ pevnou anténu bez natáčení. Jenže v polárních oblastech má nízkou elevaci a póly nepokryje."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-3",
        "display": "A rozdíl mezi **GEO** a **GSO**? To je taky častý chyták!",
        "tts_cz": "A rozdíl mezi geo a gé-es-ó? To je taky častý chyták!",
        "tts_multi": "A rozdíl mezi GEO a GSO? To je taky častý chyták!"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-3",
        "display": "**GEO je jen speciální případ GSO.** **GSO (geosynchronní dráha)** má také periodu 23 h 56 min, ale může mít **nenulový sklon $i > 0^\circ$ nebo excentricitu $e > 0$**. Z pohledu pozorovatele na Zemi pak družice nestojí v jednom bodě, ale každý den na obloze opisuje **osmičku neboli analemu**!",
        "tts_cz": "Geo je jen speciální případ gé-es-ó. Geosynchronní dráha má také periodu dvacet tři hodin padesát šest minut, ale může být nakloněná nebo eliptická. Z pohledu pozorovatele na Zemi pak družice nestojí v jednom bodě, ale každý den na obloze opisuje osmičku, takzvanou analemu!",
        "tts_multi": "GEO je jen speciální případ GSO. Geosynchronní dráha má také periodu dvacet tři hodin padesát šest minut, ale může být nakloněná nebo eliptická. Z pohledu pozorovatele na Zemi pak družice nestojí v jednom bodě, ale každý den na obloze opisuje osmičku, takzvanou analemu!"
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-3",
        "display": "A jak vyřešili pokrytí Arktidy a severních oblastí? Těmi eliptickými drahami **Molnija** a **Tundra**, že?",
        "tts_cz": "A jak vyřešili pokrytí Arktidy a severních oblastí? Těmi eliptickými drahami Molnija a Tundra, že?",
        "tts_multi": "A jak vyřešili pokrytí Arktidy a severních oblastí? Těmi eliptickými drahami Molnija a Tundra, že?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-3",
        "display": "Přesně! Obě využívají **2. Keplerův zákon** – družice letí rychle nízko nad jižní polokoulí a pak se dlouhé hodiny „loudá“ vysoko v apogeu nad severní polokoulí. Obě mají magický sklon **$63{,}4^\circ$** (aby se jim nestáčelo apogeum). Rozdíl je v periodě a tvaru: **Molnija** má **12hodinovou** dráhu a extrémní excentricitu (~0,7 až 0,75), visí nad severem přes 8 hodin. **Tundra** je **24hodinová** (geosynchronní) s mírnější excentricitou (~0,2 až 0,4) a pokrývá oblast 12 až 16 hodin.",
        "tts_cz": "Přesně! Obě využívají druhý Keplerův zákon: družice proletí rychle nízko nad jižní polokoulí a pak se dlouhé hodiny loudá vysoko v apogeu nad severní polokoulí. Obě mají charakteristický sklon šedesát tři celé čtyři stupně. Rozdíl je v periodě a tvaru: Molnija má dvanáctihodinovou dráhu a obrovskou excentricitu kolem nula celých sedmdesát čtyři, visí nad severem přes osm hodin. Tundra je dvacetičtyřhodinová geosynchronní s menší excentricitou a pokrývá oblast dvanáct až šestnáct hodin.",
        "tts_multi": "Přesně! Obě využívají druhý Keplerův zákon: družice proletí rychle nízko nad jižní polokoulí a pak se dlouhé hodiny loudá vysoko v apogeu nad severní polokoulí. Obě mají charakteristický sklon šedesát tři celé čtyři stupně. Rozdíl je v periodě a tvaru: Molnija má dvanáctihodinovou dráhu a obrovskou excentricitu kolem nula celých sedmdesát čtyři, visí nad severem přes osm hodin. Tundra je dvacetičtyřhodinová geosynchronní s menší excentricitou a pokrývá oblast dvanáct až šestnáct hodin."
    },

    # --- SAT-4: Vliv dráhy na spoj (Footprint, Latence, Doppler, FSPL) ---
    {
        "speaker": "Tereza",
        "question_id": "sat-4",
        "display": "Skvělé! Teď čtvrtá kapitola: **jak oběžná dráha ovlivňuje samotný rádiový spoj** – tedy footprint, latenci, Dopplerův jev a útlum.",
        "tts_cz": "Skvělé! Teď čtvrtá kapitola: jak oběžná dráha ovlivňuje samotný rádiový spoj, tedy fútprint, latenci, Dopplerův jev a útlum.",
        "tts_multi": "Skvělé! Teď čtvrtá kapitola: jak oběžná dráha ovlivňuje samotný rádiový spoj, tedy footprint, latenci, Dopplerův jev a útlum."
    },
    {
        "speaker": "Marek",
        "question_id": "sat-4",
        "display": "**Footprint** je stopa pokrytí na Zemi. Pozor na rozdíl: **geometrická viditelnost** znamená jen to, že družice není pod obzorem, kdežto **skutečný footprint** je vždy menší – omezuje ho minimální elevační úhel antény (jinak signál prochází moc dlouho atmosférou a stíní ho terén), tvar anténního svazku a výkonová bilance.",
        "tts_cz": "Fútprint je stopa pokrytí na Zemi. Pozor na rozdíl: geometrická viditelnost znamená jen to, že družice není pod obzorem, kdežto skutečný fútprint je vždy menší. Omezuje ho minimální elevační úhel antény, tvar svazku a výkonová bilance.",
        "tts_multi": "Footprint je stopa pokrytí na Zemi. Pozor na rozdíl: geometrická viditelnost znamená jen to, že družice není pod obzorem, kdežto skutečný footprint je vždy menší. Omezuje ho minimální elevační úhel antény, tvar svazku a výkonová bilance."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-4",
        "display": "A u **latence** u GEO si lidi často pletou jeden skok a zpáteční cestu RTT, že?",
        "tts_cz": "A u latence u dráhy geo si lidi často pletou jeden skok a zpáteční cestu er-té-té, že?",
        "tts_multi": "A u latence u dráhy GEO si lidi často pletou jeden skok a zpáteční cestu RTT, že?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-4",
        "display": "Jo! Jeden směr ze Země na GEO (35 786 km rychlostí světla) trvá asi **120 ms**. Spojení od uživatele přes družici k druhému uživateli (dva úseky) dá minimálně **239 ms**. A obousměrné **RTT (tam a zpět)** včetně zpracování a protokolů vychází v praxi na **500 až 650 ms**! Oproti tomu MEO (třeba O3b) má RTT kolem **150 ms** a nízké LEO jako Starlink jen **25 až 50 ms**.",
        "tts_cz": "Jo! Jeden směr ze Země na geo trvá rychlostí světla asi sto dvacet milisekund. Spojení od uživatele přes družici k druhému uživateli dá minimálně dvě stě třicet devět milisekund. A obousměrné er-té-té tam a zpět včetně zpracování vychází v praxi na pět set až šest set padesát milisekund! Oproti tomu meo má kolem sto padesáti milisekund a nízké leo jako star-link jen dvacet pět až padesát milisekund.",
        "tts_multi": "Jo! Jeden směr ze Země na GEO trvá rychlostí světla asi sto dvacet milisekund. Spojení od uživatele přes družici k druhému uživateli dá minimálně dvě stě třicet devět milisekund. A obousměrné RTT tam a zpět včetně zpracování vychází v praxi na pět set až šest set padesát milisekund! Oproti tomu MEO má kolem sto padesáti milisekund a nízké LEO jako Starlink jen dvacet pět až padesát milisekund."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-4",
        "display": "A jak je to s **Dopplerovým jevem** a **útlumem volného prostoru FSPL**?",
        "tts_cz": "A jak je to s Dopplerovým jevem a útlumem volného prostoru ef-es-pé-el?",
        "tts_multi": "A jak je to s Dopplerovým jevem a útlumem volného prostoru FSPL?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-4",
        "display": "**Dopplerův posuv** způsobuje radiální složka rychlosti: když se družice přibližuje, frekvence roste, když se vzdaluje, klesá. U pevné **GEO** družice je vůči pevnému terminálu v podstatě **nulový**, kdežto u rychlého **LEO** v pásmech Ku/Ka skáče o **desítky až stovky kHz**, takže ho terminál musí průběžně kompenzovat! A **FSPL (útlum volného prostoru)** roste se **čtvercem vzdálenosti $d^2$ a čtvercem frekvence $f^2$** – mezi LEO a GEO je na stejné frekvenci rozdíl kolem **36 dB**, což je přes čtyři tisíce krát víc výkonu!",
        "tts_cz": "Dopplerův posuv způsobuje radiální složka rychlosti: když se družice přibližuje, frekvence roste, když se vzdaluje, klesá. U pevné geo družice je vůči pevnému terminálu v podstatě nulový, kdežto u rychlého leo skáče o desítky až stovky kilohertzů, takže ho terminál musí průběžně kompenzovat! A útlum volného prostoru ef-es-pé-el roste se čtvercem vzdálenosti a čtvercem frekvence. Mezi leo a geo je na stejné frekvenci rozdíl kolem třiceti šesti decibelů!",
        "tts_multi": "Dopplerův posuv způsobuje radiální složka rychlosti: když se družice přibližuje, frekvence roste, když se vzdaluje, klesá. U pevné GEO družice je vůči pevnému terminálu v podstatě nulový, kdežto u rychlého LEO skáče o desítky až stovky kilohertzů, takže ho terminál musí průběžně kompenzovat! A útlum volného prostoru FSPL roste se čtvercem vzdálenosti a čtvercem frekvence. Mezi LEO a GEO je na stejné frekvenci rozdíl kolem třiceti šesti decibelů!"
    },

    # --- SAT-5: Konstelace (Walker Delta & Star), Spolehlivost, Laserové ISL ---
    {
        "speaker": "Tereza",
        "question_id": "sat-5",
        "display": "Jasné! Pátá kapitola řeší **satelitní konstelace**. Jaký je rozdíl mezi **Walker Delta** a **Walker Star**?",
        "tts_cz": "Jasné! Pátá kapitola řeší satelitní konstelace. Jaký je rozdíl mezi Vólkr Delta a Vólkr Stár?",
        "tts_multi": "Jasné! Pátá kapitola řeší satelitní konstelace. Jaký je rozdíl mezi Walker Delta a Walker Star?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-5",
        "display": "Tohle si zapamatuješ snadno podle čísel $360^\circ$ a $180^\circ$: **Walker Delta** má orbitální roviny rozprostřené rovnoměrně po celých **360 stupních** kolem rovníku – typicky šikmé dráhy pro navigace, třeba Galileo ($56^\circ:24/6/1$, tedy 6 rovin po 4 družicích, po $60^\circ$). Naproti tomu **Walker Star** používá téměř **polární dráhy**, jejichž roviny jsou rozloženy v rozsahu **180 stupňů** – pokrývá i póly (třeba **Iridium**: 66 družic v 6 rovinách ve výšce 780 km).",
        "tts_cz": "Tohle si zapamatuješ snadno podle čísel tři sta šedesát a sto osmdesát stupňů! Vólkr Delta má orbitální roviny rozprostřené rovnoměrně po celých třech stech šedesáti stupních kolem rovníku, typicky šikmé dráhy pro navigace jako Galileo. Naproti tomu Vólkr Stár používá téměř polární dráhy, jejichž roviny jsou rozloženy v rozsahu sto osmdesáti stupňů, takže pokrývá i póly, příkladem je Iridium s šedesáti šesti družicemi v šesti rovinách.",
        "tts_multi": "Tohle si zapamatuješ snadno podle čísel tři sta šedesát a sto osmdesát stupňů! Walker Delta má orbitální roviny rozprostřené rovnoměrně po celých třech stech šedesáti stupních kolem rovníku, typicky šikmé dráhy pro navigace jako Galileo. Naproti tomu Walker Star používá téměř polární dráhy, jejichž roviny jsou rozloženy v rozsahu sto osmdesáti stupňů, takže pokrývá i póly, příkladem je Iridium s šedesáti šesti družicemi v šesti rovinách."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-5",
        "display": "A pak tam jsou **mezisatelitní spoje ISL** – hlavně ty **laserové**!",
        "tts_cz": "A pak tam jsou mezisatelitní spoje í-es-el, hlavně ty laserové!",
        "tts_multi": "A pak tam jsou mezisatelitní spoje ISL, hlavně ty laserové!"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-5",
        "display": "**ISL (Inter-Satellite Links)** dovolí družicím posílat si data přímo ve vesmíru (často laserem na vlnové délce **1550 nm** rychlostí jednotek až desítek Gb/s) bez nutnosti skákat na pozemní bránu v každé oblasti. Výhody jsou obrovská kapacita a úzký svazek bez rušení. Nevýhody? Extrémní nároky na přesné míření a stabilizaci proti vibracím. A chyták ze skript: úzký laserový svazek sice ztěžuje odposlech, ale **sám o sobě nezaručuje bezpečnost – data se musí pořád šifrovat!**",
        "tts_cz": "Mezisatelitní spoje í-es-el dovolí družicím posílat si data přímo ve vesmíru, často laserem na vlnové délce tisíc pět set padesát nanometrů rychlostí desítek gigabitů za sekundu, bez pozemní brány na každém kroku. Výhodou je obrovská kapacita a úzký svazek bez rušení, nevýhodou extrémní nároky na přesné míření. A chyták ze skript: úzký laserový svazek sice ztěžuje odposlech, ale sám o sobě nezaručuje bezpečnost. Data se musí pořád šifrovat!",
        "tts_multi": "Mezisatelitní spoje ISL dovolí družicím posílat si data přímo ve vesmíru, často laserem na vlnové délce tisíc pět set padesát nanometrů rychlostí desítek gigabitů za sekundu, bez pozemní brány na každém kroku. Výhodou je obrovská kapacita a úzký svazek bez rušení, nevýhodou extrémní nároky na přesné míření. A chyták ze skript: úzký laserový svazek sice ztěžuje odposlech, ale sám o sobě nezaručuje bezpečnost. Data se musí pořád šifrovat!"
    },

    # --- SAT-6: Kosmický segment, Transpondéry a Kmitočtová pásma (GiTySAT) ---
    {
        "speaker": "Tereza",
        "question_id": "sat-6",
        "display": "Teď se přesouváme do prezentace **GiTySAT**! V šesté kapitole máme **kosmický segment, transpondéry a kmitočtová pásma**. Jaký je rozdíl mezi standardní družicí a **HTS**?",
        "tts_cz": "Teď se přesouváme do prezentace dží-ty-sat! V šesté kapitole máme kosmický segment, transpondéry a kmitočtová pásma. Jaký je rozdíl mezi standardní družicí a há-té-es?",
        "tts_multi": "Teď se přesouváme do prezentace GiTySAT! V šesté kapitole máme kosmický segment, transpondéry a kmitočtová pásma. Jaký je rozdíl mezi standardní družicí a HTS?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-6",
        "display": "**Standardní družice** svítí širokým svazkem na celý kontinent. **HTS (High Throughput Satellite)** pokryje oblast mnoha úzkými bodovými svazky (spot-beamy) a díky tomu může stejné frekvence opakovaně využívat – má tak mnohonásobně vyšší kapacitu! A co se týče **transpondérů**, známe tři druhy: **Bend pipe** (jen hloupá „ohnutá trubka“, co signál přijme, posune frekvenci a zesílí), **Cross type** (křížové propojení mezi svazky/pásmy) a **On-board switching** (chytré přepínání přímo na palubě družice).",
        "tts_cz": "Standardní družice svítí širokým svazkem na celý kontinent. Družice há-té-es pokryje oblast mnoha úzkými bodovými svazky, a díky tomu může stejné frekvence opakovaně využívat, takže má mnohonásobně vyšší kapacitu! A transpondéry známe tři: bend pajp, což je jen průchozí zesilovač s posunem frekvence; kros tajp, tedy křížové propojení mezi svazky; a on-bórd svičink, tedy přepínání přímo na palubě družice.",
        "tts_multi": "Standardní družice svítí širokým svazkem na celý kontinent. Družice HTS pokryje oblast mnoha úzkými bodovými svazky, a díky tomu může stejné frekvence opakovaně využívat, takže má mnohonásobně vyšší kapacitu! A transpondéry známe tři: bend pipe, což je jen průchozí zesilovač s posunem frekvence; cross type, tedy křížové propojení mezi svazky; a on-board switching, tedy přepínání přímo na palubě družice."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-6",
        "display": "A teď ta tabulka **satelitních pásem** od C až po E band! Co z ní musím v testu bezpečně vědět?",
        "tts_cz": "A teď ta tabulka satelitních pásem od cé až po é bend! Co z ní musím v testu bezpečně vědět?",
        "tts_multi": "A teď ta tabulka satelitních pásem od C až po E band! Co z ní musím v testu bezpečně vědět?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-6",
        "display": "Drž se posloupnosti frekvencí: **C band (4–8 GHz)** – klasická sat. komunikace a meteo radary, odolný dešti. **X band (8–12 GHz)** – vojenské/vládní satelitní komunikace, radary, hluboký vesmír. **Ku band (11–18 GHz)** – satelitní TV vysílání a běžný VSAT. **K band (18–27 GHz)** – obří chyták: **silný útlum vodní párou při 22,23 GHz**! **Ka band (27–40 GHz)** – moderní rychlý internet (HTS, O3b, brány LEO) a 5G. A úplně nahoře **V band (40–75 GHz)** a **E band (60–90 GHz)** pro experimenty a ultraširokopásmové brány.",
        "tts_cz": "Drž se posloupnosti frekvencí! Cé bend, čtyři až osm gigahertzů, je klasická komunikace odolná dešti. Iks bend, osm až dvanáct gigahertzů, je pro armádu, radary a hluboký vesmír. Ká-ú bend, jedenáct až osmnáct gigahertzů, je satelitní televize a běžný ví-sat. Ká bend, osmnáct až dvacet sedm gigahertzů, má velký chyták: silný útlum vodní párou přesně na dvaceti dvou celých dvaceti třech gigahertzích! Ká-á bend, dvacet sedm až čtyřicet gigahertzů, je moderní rychlý internet a pět gé. A úplně nahoře jsou vé bend a é bend pro experimenty a brány.",
        "tts_multi": "Drž se posloupnosti frekvencí! C band, čtyři až osm gigahertzů, je klasická komunikace odolná dešti. X band, osm až dvanáct gigahertzů, je pro armádu, radary a hluboký vesmír. Ku band, jedenáct až osmnáct gigahertzů, je satelitní televize a běžný VSAT. K band, osmnáct až dvacet sedm gigahertzů, má velký chyták: silný útlum vodní párou přesně na dvaceti dvou celých dvaceti třech gigahertzích! Ka band, dvacet sedm až čtyřicet gigahertzů, je moderní rychlý internet a 5G. A úplně nahoře jsou V band a E band pro experimenty a brány."
    },

    # --- SAT-7: GEO sítě a služby GiTySAT ---
    {
        "speaker": "Tereza",
        "question_id": "sat-7",
        "display": "Pěkně! V sedmé kapitole jsou **GEO sítě, topologie a firma GiTy**. Co je důležité o **GiTy** a jaké jsou **čtyři topologie GEO sítí**?",
        "tts_cz": "Pěkně! V sedmé kapitole jsou geo sítě, topologie a firma dží-ty. Co je důležité o dží-ty a jaké jsou čtyři topologie geo sítí?",
        "tts_multi": "Pěkně! V sedmé kapitole jsou GEO sítě, topologie a firma GiTy. Co je důležité o GiTy a jaké jsou čtyři topologie GEO sítí?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-7",
        "display": "**GiTy, a.s.** má vlastní satelitní **teleport (HUB)** přímo v ČR, vlastní pozemní **MPLS síť** v ČR a na Slovensku, nepřetržitý dohled 24/7 s garancí SLA a bezpečnostní **certifikaci NBÚ – Tajné**. A ty **čtyři topologie GEO sítí** jsou: **1. Broadcast** (jednosměrná distribuce dat), **2. Bod–Bod** pomocí technologie **SCPC** (vyhrazený kanál pro dva modemy/routery), **3. Hvězdicová síť** ($1\times$ VSAT HUB a $n\times$ terminálů, asymetrický provoz přes **TDMA/FDMA**) a **4. MESH** (terminály spolu mluví přímo jedním skokem bez dvojího průchodu přes HUB).",
        "tts_cz": "Společnost dží-ty má vlastní satelitní teleport neboli hab přímo v Česku, pozemní em-pé-el-es síť v Česku a na Slovensku, nepřetržitý dohled dvacet čtyři sedm a certifikaci en-bé-ú na stupeň Tajné. A ty čtyři topologie geo sítí jsou: zaprvé broudkást pro jednosměrnou distribuci; zadruhé bod–bod pomocí technologie es-cé-pé-cé s vyhrazeným kanálem; zatřetí hvězdicová síť s jedním ví-sat habem a mnoha terminály přes té-dé-em-á a ef-dé-em-á; a začtvrté meš, kde spolu terminály mluví přímo jedním skokem.",
        "tts_multi": "Společnost GiTy má vlastní satelitní teleport neboli HUB přímo v Česku, pozemní MPLS síť v Česku a na Slovensku, nepřetržitý dohled dvacet čtyři sedm a certifikaci NBÚ na stupeň Tajné. A ty čtyři topologie GEO sítí jsou: zaprvé broadcast pro jednosměrnou distribuci; zadruhé bod–bod pomocí technologie SCPC s vyhrazeným kanálem; zatřetí hvězdicová síť s jedním VSAT HUBem a mnoha terminály přes TDMA a FDMA; a začtvrté MESH, kde spolu terminály mluví přímo jedním skokem."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-7",
        "display": "A ještě srovnání **internetová konfigurace vs. privátní satelitní síť**!",
        "tts_cz": "A ještě srovnání internetová konfigurace versus privátní satelitní síť!",
        "tts_multi": "A ještě srovnání internetová konfigurace versus privátní satelitní síť!"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-7",
        "display": "**Internetová konfigurace** je pro velké množství terminálů, unifikovaná služba do Internetu s agregací, **FUP** a jen omezeným dohledem. Naproti tomu **privátní satelitní síť** propojuje pobočky s centrálou přímo do firemní **MPLS WAN**, má garantovanou kvalitu **QoS**, přídavné šifrování a plný **End-to-End dohled** přes SNMP.",
        "tts_cz": "Internetová konfigurace je pro velké množství terminálů, unifikovaná služba do Internetu s agregací, ef-ú-pé a jen omezeným dohledem. Naproti tomu privátní satelitní síť propojuje pobočky s centrálou přímo do firemní em-pé-el-es sítě, má garantovanou kvalitu ku-ó-es, přídavné šifrování a plný koncový dohled.",
        "tts_multi": "Internetová konfigurace je pro velké množství terminálů, unifikovaná služba do Internetu s agregací, FUP a jen omezeným dohledem. Naproti tomu privátní satelitní síť propojuje pobočky s centrálou přímo do firemní MPLS WAN, má garantovanou kvalitu QoS, přídavné šifrování a plný End-to-End dohled přes SNMP."
    },

    # --- SAT-8: Praxe: MEO (O3b) a LEO konstelace (OneWeb, Starlink, Amazon, Telesat) ---
    {
        "speaker": "Tereza",
        "question_id": "sat-8",
        "display": "V osmé kapitole jsou konkrétní moderní konstelace z prezentace: **O3b, OneWeb, Starlink, Amazon LEO a Telesat Lightspeed**. Jak si je rychle odlišit?",
        "tts_cz": "V osmé kapitole jsou konkrétní moderní konstelace z prezentace: ó-tři-bé, uan-veb, star-link, amazon leo a telesat lajtspíd. Jak si je rychle odlišit?",
        "tts_multi": "V osmé kapitole jsou konkrétní moderní konstelace z prezentace: O3b, OneWeb, Starlink, Amazon LEO a Telesat Lightspeed. Jak si je rychle odlišit?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-8",
        "display": "Dejme každé jasnou nálepku: **O3b / O3b mPOWER** od SES je jediná velká **MEO** konstelace v přehledu – výška **8 000 km**, Ka-band, RTT **150 ms**, pokrytí zhruba $\pm 50^\circ$ šířky (takže ne póly!), až 1,6 Gbps na svazek. Pak máme **OneWeb** (Eutelsat): **LEO ve 1 200 km**, **652 družic**, RTT kolem **100 ms**, k terminálům jde **Ku-band** a k branám Ka-band; nabízí firemní **MIR** (maximální) i garantovanou **CIR** rychlost.",
        "tts_cz": "Dejme každé jasnou nálepku! Ó-tři-bé em-pauer od es-é-es je jediná velká střední meo konstelace v přehledu: výška osm tisíc kilometrů, ká-á bend, latence sto padesát milisekund, pokrytí plus mínus padesát stupňů šířky a rychlost až jedna celá šest gigabitu za sekundu na svazek. Pak máme uan-veb: nízká dráha ve dvanácti stech kilometrech, šest set padesát dva družic, latence kolem sta milisekund, k terminálům jde ká-ú bend a nabízí i garantované firemní rychlosti cí-áj-ár.",
        "tts_multi": "Dejme každé jasnou nálepku! O3b mPOWER od SES je jediná velká MEO konstelace v přehledu: výška osm tisíc kilometrů, Ka-band, latence sto padesát milisekund, pokrytí plus mínus padesát stupňů šířky a rychlost až jedna celá šest gigabitu za sekundu na svazek. Pak máme OneWeb: LEO ve dvanácti stech kilometrech, šest set padesát dva družic, latence kolem sta milisekund, k terminálům jde Ku-band a nabízí i garantované firemní rychlosti CIR."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-8",
        "display": "A **Starlink** od SpaceX versus nováčci **Amazon LEO** a **Telesat Lightspeed**?",
        "tts_cz": "A star-link od spejs-iks versus nováčci amazon leo a telesat lajtspíd?",
        "tts_multi": "A Starlink od SpaceX versus nováčci Amazon LEO a Telesat Lightspeed?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-8",
        "display": "**Starlink** je největší aktivní konstelace (přes 9 800 družic, typicky **550 km**, RTT jen **25–50 ms**), využívá **laserové spoje mezi družicemi**, 13km svazky a terminály Mini, Standard, Enterprise a Performance. **Amazon LEO** (dříve Kuiper, 590–630 km, komerční start 2026/2027) má mít 3 232 družic, lasery a terminály Nano, Pro a Ultra až do 1 Gbps. A **Telesat Lightspeed** (start 2028, 1 015 a 1 325 km, Ka-band + lasery) cílí čistě na B2B, letectví a **L2 služby** až do 3 Gbps s pokrytím včetně pólů.",
        "tts_cz": "Star-link je největší aktivní konstelace, přes devět tisíc osm set družic typicky ve výšce pět set padesát kilometrů, latence jen dvacet pět až padesát milisekund, využívá laserové spoje mezi družicemi a terminály mini, standart, enterprajs a performans. Amazon leo kolem šesti set kilometrů má mít přes tři tisíce družic, lasery a terminály až do jednoho gigabitu, komerční start kolem roku dva tisíce dvacet sedm. A telesat lajtspíd se startem v roce dva tisíce dvacet osm cílí na firmy, letectví a el-dva služby až do tří gigabitů včetně pólů.",
        "tts_multi": "Starlink je největší aktivní konstelace, přes devět tisíc osm set družic typicky ve výšce pět set padesát kilometrů, latence jen dvacet pět až padesát milisekund, využívá laserové spoje mezi družicemi a terminály Mini, Standard, Enterprise a Performance. Amazon LEO kolem šesti set kilometrů má mít přes tři tisíce družic, lasery a terminály až do jednoho gigabitu, komerční start kolem roku dva tisíce dvacet sedm. A Telesat Lightspeed se startem v roce dva tisíce dvacet osm cílí na firmy, letectví a L2 služby až do tří gigabitů včetně pólů."
    },

    # --- SAT-9: Terminály, Zabezpečení, DVB-S2X ACM a Hybridní sítě ---
    {
        "speaker": "Tereza",
        "question_id": "sat-9",
        "display": "A jsme u deváté, poslední kapitoly! **Terminály, zabezpečení, trendy DVB-S2X a hybridní síť GiTySAT**. Co tvoří klasický VSAT terminál?",
        "tts_cz": "A jsme u deváté, poslední kapitoly! Terminály, zabezpečení, trendy dé-vé-bé es dva iks a hybridní síť dží-ty-sat. Co tvoří klasický ví-sat terminál?",
        "tts_multi": "A jsme u deváté, poslední kapitoly! Terminály, zabezpečení, trendy DVB-S2X a hybridní síť GiTySAT. Co tvoří klasický VSAT terminál?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-9",
        "display": "Dvě části: **venkovní** je **anténa** (pevná parabola 0,7–2,4 m, mobilní *Drive Away* na auto, *Quick Deploy* nebo přenosný *Manpack*) a **RF jednotka** (C, X, Ku nebo Ka). **Vnitřní část** je samotný **VSAT modem/router** (třeba iDirect 950mp, 9530 nebo Newtec MDM3315). A pro vysokou bezpečnost používá GiTy **iDirect TRANSEC** (skrytí aktivity kanálu, **AES-256 na L2**, certifikát **X.509**), **Spread spectrum**, moduly **FIPS 140-2 Level 3** a systém **CSIR** proti úmyslnému rušení (anti-jamming).",
        "tts_cz": "Dvě části! Venkovní je anténa, třeba pevná parabola, mobilní anténa na auto nebo přenosný batoh men-pek, a k tomu vysokofrekvenční jednotka. Vnitřní část je samotný ví-sat modem nebo router. A pro vysokou bezpečnost používá dží-ty technologii trans-sek se skrytou aktivitou kanálu, šifrováním á-é-es dvě stě padesát šest na druhé vrstvě a certifikátem iks pět set devět, dále rozprostřené spektrum, certifikované moduly fips a systém cé-es-í-er proti úmyslnému rušení.",
        "tts_multi": "Dvě části! Venkovní je anténa, třeba pevná parabola, mobilní Drive Away na auto nebo přenosný Manpack, a k tomu RF jednotka. Vnitřní část je samotný VSAT modem nebo router. A pro vysokou bezpečnost používá GiTy technologii iDirect TRANSEC se skrytou aktivitou kanálu, šifrováním AES-256 na L2 a certifikátem X.509, dále Spread spectrum, moduly FIPS 140-2 Level 3 a systém CSIR proti rušení."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-9",
        "display": "A co v trendech znamená **DVB-S2X s ACM** a jak funguje **hybridní síť** v posledním slidu?",
        "tts_cz": "A co v trendech znamená dé-vé-bé es dva iks s á-cé-em a jak funguje hybridní síť v posledním slidu?",
        "tts_multi": "A co v trendech znamená DVB-S2X s ACM a jak funguje hybridní síť v posledním slidu?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-9",
        "display": "**ACM (Adaptive Coding and Modulation)** je geniální v tom, že když přijde bouřka a zhorší se signál, spoj nespadne – modem v reálném čase přepne z vysoké modulace (třeba 256APSK) na odolnější QPSK a zpátky, jakmile vysvitne slunce! A **hybridní síť GiTySAT** chytře kombinuje **GEO + LEO + Internet**: **kritický a citlivý provoz** jde zabezpečeným GEO VSATem do centrály, **standardní provoz** letí rychlým LEO terminálem přes privátní propoj NNI do MPLS sítě G-Net, a **nekritický internetový provoz** jde lokálně přes firewall rovnou do Internetu. Tím máš v kapse všechno!",
        "tts_cz": "Adaptivní kódování a modulace á-cé-em je geniální v tom, že když přijde bouřka a zhorší se signál, spoj nespadne. Modem v reálném čase přepne z vysoké modulace na odolnější a zpátky, jakmile vysvitne slunce! A hybridní síť dží-ty-sat chytře kombinuje geo, leo a Internet: kritický a citlivý provoz jde zabezpečeným geo ví-satem do centrály, standardní provoz letí rychlým leo terminálem přes privátní propoj do sítě dží-net, a nekritický internetový provoz jde lokálně přes fajervol rovnou do Internetu. Tím máš v kapse všechno!",
        "tts_multi": "Adaptivní kódování a modulace ACM je geniální v tom, že když přijde bouřka a zhorší se signál, spoj nespadne. Modem v reálném čase přepne z vysoké modulace na odolnější a zpátky, jakmile vysvitne slunce! A hybridní síť GiTySAT chytře kombinuje GEO, LEO a Internet: kritický a citlivý provoz jde zabezpečeným GEO VSATem do centrály, standardní provoz letí rychlým LEO terminálem přes privátní propoj NNI do MPLS sítě G-Net, a nekritický internetový provoz jde lokálně přes firewall rovnou do Internetu. Tím máš v kapse všechno!"
    }
]


def split_sentences(text: str):
    parts = [s.strip() for s in re.split(r"(?<=[.!?…])\s+", text.strip()) if s.strip()]
    return parts if parts else [text.strip()]


def sentence_prosody(sentence: str, base_rate: int, base_pitch: int):
    # Subtle natural variation per sentence type without distorting Czech timbre
    if sentence.endswith("?"):
        r = base_rate + 2
        p = base_pitch + 2
    elif len(sentence) <= 45 and sentence.endswith("!"):
        r = base_rate + 2
        p = base_pitch + 1
    else:
        r = base_rate
        p = base_pitch
    rate_str = f"{r:+d}%"
    pitch_str = f"{p:+d}Hz"
    return rate_str, pitch_str


async def synthesize_sentence(voice: str, sentence: str, rate: str, pitch: str, cache_dir: str, prefix: str):
    key = hashlib.md5(f"v3|{voice}|{rate}|{pitch}|{sentence}".encode("utf-8")).hexdigest()[:14]
    seg_path = os.path.join(cache_dir, f"{prefix}_{key}.mp3")
    if not os.path.exists(seg_path) or os.path.getsize(seg_path) == 0:
        for attempt in range(4):
            try:
                communicate = edge_tts.Communicate(sentence, voice, rate=rate, pitch=pitch)
                await communicate.save(seg_path)
                break
            except Exception:
                if attempt == 3:
                    raise
                await asyncio.sleep(0.8 * (attempt + 1))
    with open(seg_path, "rb") as f:
        data = f.read()
    return data


async def generate_turn(engine_name: str, index: int, item: dict, cache_dir: str):
    eng = ENGINES[engine_name]
    cfg = eng[item["speaker"]]
    text = item[eng["tts_field"]]
    sentences = split_sentences(text)

    chunks = []
    for s_idx, sent in enumerate(sentences):
        rate_str, pitch_str = sentence_prosody(sent, cfg["base_rate"], cfg["base_pitch"])
        audio_bytes = await synthesize_sentence(
            cfg["voice"], sent, rate_str, pitch_str, cache_dir, f"{engine_name}_{index:02d}_{s_idx:02d}"
        )
        chunks.append(audio_bytes)
        if s_idx < len(sentences) - 1:
            chunks.append(PAUSE_SENTENCE)

    combined = b"".join(chunks)
    dur = len(combined) / 6000.0  # edge-tts outputs 48kbps CBR MP3 => 6000 bytes/sec
    return combined, dur


async def build_engine_track(engine_name: str, out_dir: str, seg_dir: str):
    print(f"=== Generating track: {engine_name} ({len(SCRIPT)} turns) ===")
    results = [None] * len(SCRIPT)
    batch_size = 4
    for start in range(0, len(SCRIPT), batch_size):
        tasks = [
            generate_turn(engine_name, idx, SCRIPT[idx], seg_dir)
            for idx in range(start, min(start + batch_size, len(SCRIPT)))
        ]
        batch_res = await asyncio.gather(*tasks)
        for offset, res in enumerate(batch_res):
            results[start + offset] = res
        print(f"  [{engine_name}] {min(start + batch_size, len(SCRIPT))}/{len(SCRIPT)} turns done")

    final_mp3 = os.path.join(out_dir, ENGINES[engine_name]["filename"])
    current_time = 0.0
    timeline = []

    with open(final_mp3, "wb") as outfile:
        for idx, (turn_bytes, dur) in enumerate(results):
            outfile.write(turn_bytes)
            next_q = SCRIPT[idx + 1]["question_id"] if idx + 1 < len(SCRIPT) else None
            pause = PAUSE_CHAPTER if (next_q and next_q != SCRIPT[idx]["question_id"]) else PAUSE_TURN
            outfile.write(pause)
            pause_dur = len(pause) / 6000.0

            item = SCRIPT[idx]
            start_t = round(current_time, 2)
            end_t = round(current_time + dur, 2)
            timeline.append({
                "index": idx,
                "speaker": item["speaker"],
                "question_id": item["question_id"],
                "display": item["display"],
                "start": start_t,
                "end": end_t,
                "duration": round(dur, 2),
            })
            current_time += dur + pause_dur

    print(f"  -> Saved {final_mp3} ({round(current_time / 60.0, 2)} min)")
    return {
        "engine": engine_name,
        "filename": ENGINES[engine_name]["filename"],
        "total_duration": round(current_time, 2),
        "segments": timeline,
    }


async def main():
    out_dir = r"k:\podPorn"
    seg_dir = os.path.join(out_dir, "segments_sat")
    os.makedirs(seg_dir, exist_ok=True)

    track_cz = await build_engine_track("cz_studio", out_dir, seg_dir)
    track_multi = await build_engine_track("multi_hd", out_dir, seg_dir)

    meta_path = os.path.join(out_dir, "podcast_data.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "default_engine": "cz_studio",
                "tracks": {
                    "cz_studio": track_cz,
                    "multi_hd": track_multi,
                },
                "total_duration": track_cz["total_duration"],
                "segments": track_cz["segments"],
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    print("All satellite podcast tracks generated successfully!")


if __name__ == "__main__":
    asyncio.run(main())

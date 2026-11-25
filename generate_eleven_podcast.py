"""
Generate natural, lifelike Czech podcast using ElevenLabs Multilingual Turbo v2.5.
Voices:
- Marek: Brian (nPczCjzI2devNBz1zQrb) - Deep, resonant, comforting
- Tereza: Sarah (EXAVITQu4vr4xnSDxMaL) - Mature, reassuring, confident
Includes natural speech mannerisms, sighs, pauses, and clear pronunciation.
"""
import asyncio
import hashlib
import json
import os
import re
import ssl
import urllib.request
import urllib.error

API_KEY = "sk_4ecc54cc20486545a6ed4ead7dbb2d20744a7aeb97f1f292"
ctx = ssl.create_default_context()

VOICES = {
    "Marek": {
        "voice_id": "nPczCjzI2devNBz1zQrb",
        "settings": {
            "stability": 0.42,
            "similarity_boost": 0.82,
            "style": 0.35,
            "use_speaker_boost": True
        }
    },
    "Tereza": {
        "voice_id": "EXAVITQu4vr4xnSDxMaL",
        "settings": {
            "stability": 0.45,
            "similarity_boost": 0.80,
            "style": 0.30,
            "use_speaker_boost": True
        }
    }
}

OUT_DIR = r"k:\podPorn"
CACHE_DIR = os.path.join(OUT_DIR, "segments_eleven")
os.makedirs(CACHE_DIR, exist_ok=True)

# 54 turns enriched with subtle natural speech expressions (pauses, sighs, laughs, coughing/throat-clearing, affirmations)
ENRICHED_SCRIPT = [
    # --- INTRO ---
    {
        "speaker": "Tereza",
        "question_id": "intro",
        "display": "Ahoj Marku! Hele, čeká mě test na **satelitní komunikace a oběžné dráhy**. Je to pro mě spíš okrajové téma a nemám přesné otázky – projdeme spolu všechno podstatné ze skript i z prezentace **GiTySAT** tak, aby mi to v hlavě hned secvaklo?",
        "text": "Ahoj Marku! [sighs] Hele, čeká mě zkouška na satelitní komunikace a oběžné dráhy... Je to pro mě spíš okrajové téma a nemám k tomu přesné otázky. Projdeme spolu všechno podstatné ze skript i z prezentace GiTySAT tak, aby mi to v hlavě hned secvaklo?"
    },
    {
        "speaker": "Marek",
        "question_id": "intro",
        "display": "Jasně Terezo, dáme to úplně v klidu! Žádné zbytečné odvozování vzorců – půjdeme po logice věci, srovnáních a chytácích, na které se učitelé ptají nejčastěji. Rozdělili jsme si to do devíti přehledných kapitol. Jdeme na **orbitální mechaniku**?",
        "text": "Jasně Terezo, dáme to úplně v klidu! [laughs] Žádné zbytečné odvozování vzorců. Půjdeme po čisté logice věci, srovnáních a hlavně chytácích, na které se u zkoušky ptají nejčastěji. Rozdělili jsme si to do devíti přehledných kapitol... Můžeme jít na orbitální mechaniku?"
    },

    # --- SAT-1: Orbitální mechanika a Keplerovy zákony ---
    {
        "speaker": "Tereza",
        "question_id": "sat-1",
        "display": "Pojďme! Proč vlastně družice drží na oběžné dráze a nespadne na Zem, když nemá pořád zapnuté motory?",
        "text": "Určitě, pojďme na to! Proč vlastně družice drží na oběžné dráze a nespadne na Zem, když nemá pořád zapnuté motory?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-1",
        "display": "Je to čistá rovnováha dvou věcí: **zemská gravitace** družici neustále přitahuje ke středu Země (a slábne se čtvercem vzdálenosti $r^2$), a tím zajišťuje potřebnou **dostředivou sílu**, která zakřivuje její let. Družice má totiž tak vysokou tečnou rychlost, že jakoby pořád padá k Zemi, ale Země se pod ní stejně rychle zakřivuje!",
        "text": "Je to v podstatě čistá rovnováha: zemská gravitace družici neustále přitahuje ke středu Země... a slábne se čtvercem vzdálenosti. Tím zajišťuje potřebnou dostředivou sílu, která zakřivuje její let. Družice má totiž tak obrovskou tečnou rychlost, že jakoby pořád padá k Zemi, ale Země se pod ní stejně rychle zakřivuje!"
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-1",
        "display": "A co **odstředivá síla**? Někdy se říká, že ji vyrovnává.",
        "text": "A co odstředivá síla? Někdy se říká, že ji vyrovnává..."
    },
    {
        "speaker": "Marek",
        "question_id": "sat-1",
        "display": "Pozor na terminologii ze skript: **odstředivá síla** není žádná nová skutečná síla – je to jen zdánlivá setrvačná síla v neinerciální soustavě, která rotuje s družicí. A ještě jedna intuice, co se plete: **čím výš je kruhová dráha, tím POMALEJI družice letí** a tím **DELŠÍ má oběžnou dobu**! Nízko letí přes 7,5 km/s, na geostacionární dráze jen asi 3,1 km/s.",
        "text": "Pozor na terminologii ze skript! [clears throat] Odstředivá síla není žádná nová skutečná síla... Je to jen zdánlivá setrvačná síla v soustavě, která rotuje s družicí. A ještě jedna důležitá intuice, co se hrozně často plete: čím výš je kruhová dráha, tím pomaleji družice letí a tím delší má oběžnou dobu! Nízko letí přes sedm a půl kilometru za sekundu, ale nahoře na geostacionární dráze jen asi tři celé jedna kilometru za sekundu."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-1",
        "display": "Jasně, takže výš znamená pomaleji a delší oběh. A co **úniková rychlost** a **Keplerovy zákony**?",
        "text": "Jasně... takže výš znamená pomaleji a delší oběh. A co úniková rychlost a Keplerovy zákony?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-1",
        "display": "**Úniková rychlost** je $\\sqrt{2}$-krát větší než kruhová – u povrchu Země asi **11,2 km/s**. Když ji dosáhneš, přejdeš na otevřenou parabolickou dráhu a Zemi opustíš. A **Keplerovy zákony** jsou tři: **První** říká, že dráha je **elipsa** se Zemí v jednom ohnisku (kruh je jen speciální případ s nulovou excentricitou). **Druhý** je zákon ploch – z něj plyne, že družice letí **nejrychleji v perigeu** (nejblíž Zemi) a **nejpomaleji v apogeu** (nejdál od Země). A **třetí** dává do poměru druhou mocninu oběžné doby se třetí mocninou hlavní poloosy.",
        "text": "Úniková rychlost je odmocnina ze dvou krát větší než kruhová... u povrchu Země je to asi jedenáct celé dva kilometru za sekundu. Když ji dosáhneš, přejdeš na parabolickou dráhu a Zemi opustíš. A Keplerovy zákony jsou tři! První říká, že dráha je elipsa se Zemí v jednom ohnisku. Druhý je zákon ploch... z něj plyne, že družice letí nejrychleji v perigeu, tedy nejblíž Zemi, a nejpomaleji v apogeu, tedy nejdál od Země. A třetí dává do poměru druhou mocninu oběžné doby se třetí mocninou hlavní poloosy."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-1",
        "display": "A v realitě asi nejde o dokonalou Keplerovu elipsu, že? Co tu dráhu nejvíc ruší?",
        "text": "A v realitě asi nejde o úplně dokonalou Keplerovu elipsu, že? Co tu dráhu nejvíc ruší?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-1",
        "display": "Přesně tak. Hlavní poruchy jsou čtyři: **zploštění Země** (nesférické gravitační pole, známé přes koeficient $J_2$), **odpor zbytkové atmosféry** u nízkých drah, **gravitace Slunce a Měsíce** a **tlak slunečního záření**.",
        "text": "Přesně tak. Hlavní poruchy jsou čtyři: zaprvé zploštění Země neboli gravitační koeficient J2, dále odpor zbytkové atmosféry u nízkých drah, gravitace Slunce a Měsíce... a tlak slunečního záření."
    },

    # --- SAT-2: Orbitální elementy a orientace drah ---
    {
        "speaker": "Tereza",
        "question_id": "sat-2",
        "display": "Super. V druhé kapitole jsou **orbitální elementy**. Potřebuju umět všech šest prvků, co popisují dráhu v prostoru?",
        "text": "Super! V druhé kapitole jsou orbitální elementy. Potřebuju z hlavy umět všech šest prvků, co popisují dráhu v prostoru?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-2",
        "display": "Stačí přesně vědět, co který dělá! Jsou to tři dvojice: První dvě určují **velikost a tvar** – tedy **hlavní poloosa $a$** (velikost) a **excentricita $e$** (tvar: $0$ je kružnice, $0 < e < 1$ je elipsa). Druhé dvě určují **natočení v prostoru** – **inklinace $i$** (sklon roviny dráhy vůči rovníku, od $0^\circ$ do $180^\circ$) a **RAAN $\Omega$** (rektascenze vzestupného uzlu, která říká, jak je rovina dráhy pootočená kolem osy Země).",
        "text": "Stačí přesně vědět, co který dělá! Jsou to vlastně tři dvojice... První dvě určují velikost a tvar: tedy hlavní poloosa a, a excentricita e, kde nula je kružnice a mezi nulou a jedničkou elipsa. Druhé dvě určují natočení v prostoru: inklinace i, což je sklon vůči rovníku od nuly do sto osmdesáti stupňů, a rektascenze vzestupného uzlu RAAN, která říká, jak je celá rovina pootočená kolem zemské osy."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-2",
        "display": "A ta třetí dvojice? To bude asi poloha perigea a samotné družice!",
        "text": "A ta třetí dvojice? [gasps] To bude asi poloha perigea a samotné družice!"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-2",
        "display": "Přesně! Pátý prvek je **argument perigea $\omega$** – úhel uvnitř samotné roviny dráhy od vzestupného uzlu k perigeu. A šestý je **pravá anomálie $\nu$** (případně střední anomálie), která udává **okamžitou polohu družice** na dráze v čase. Drobný chyták: u přesně rovníkové dráhy není definován vzestupný uzel, a u přesně kruhové dráhy není definován argument perigea!",
        "text": "Přesně tak! Pátý prvek je argument perigea omega, který udává polohu perigea v rovině dráhy. A šestý je pravá anomálie, což je okamžitá poloha družice na dráze v daném čase. Drobný chyták: u přesně rovníkové dráhy není definován vzestupný uzel, a u dokonale kruhové dráhy zase není definován argument perigea."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-2",
        "display": "A jak se dráhy dělí podle **inklinace**? Rovníková, polární, nakloněná… a pak tam byla ještě ta **slunečně synchronní SSO**.",
        "text": "A jak se dráhy dělí podle inklinace? Rovníková, polární, nakloněná... a pak tam byla ještě ta slunečně synchronní SSO dráha."
    },
    {
        "speaker": "Marek",
        "question_id": "sat-2",
        "display": "Jo, je to přehledné: **$i = 0^\circ$** je rovníková prográdní (po směru rotace Země). Když je **$0^\circ < i < 90^\circ$**, jde o šikmou **prográdní** dráhu (Země jí jakoby pomáhá při startu). **$i \approx 90^\circ$** je **polární dráha** přes oba póly – ideální pro meteo, SAR radary a průzkum, protože Země se pod ní otáčí a družice postupně nasnímá celý svět. A **$90^\circ < i \le 180^\circ$** je **retrográdní** dráha – tedy proti rotaci Země!",
        "text": "Je to přehledné: nula stupňů je rovníková prográdní, tedy po směru rotace Země. Mezi nulou a devadesáti stupni jde o šikmou prográdní dráhu, kde rotace Země pomáhá při startu. Kolem devadesáti stupňů je polární dráha přes oba póly... ideální pro meteo a průzkum, protože Země se pod ní otáčí a družice postupně nasnímá celý svět. A nad devadesát stupňů je retrográdní dráha, tedy proti rotaci Země!"
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-2",
        "display": "A právě ta **SSO – slunečně synchronní dráha** má sklon asi **97° až 99°**, takže je lehce retrográdní! Proč se to dělá?",
        "text": "A právě ta SSO dráha má sklon asi devadesát sedm až devadesát devět stupňů, takže je lehce retrográdní! Proč se to vlastně dělá?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-2",
        "display": "To je parádní trik: využije se **zploštění Země ($J_2$)**, aby se rovina dráhy pomalu stáčela tempem asi **1 stupeň za den** (přesně $+0{,}9856^\circ/\text{den}$), což přesně kopíruje roční pohyb Slunce. Výsledek? Družice přelétá nad stejným místem vždy ve **stejný místní sluneční čas**, takže stíny na fotkách jsou srovnatelné! Používá se to pro optické snímkování Země ve výškách 500 až 900 km, třeba u konstelace PlanetScope.",
        "text": "To je parádní trik! Využije se zploštění Země, aby se rovina dráhy pomalu stáčela tempem zhruba jeden stupeň za den... přesně nula celá devět osm pět šest stupně za den, což kopíruje roční oběh Slunce. Výsledek? Družice přelétá nad stejným místem vždy ve stejný místní sluneční čas, takže stíny na snímcích jsou dokonale srovnatelné! Používá se to pro optické snímkování Země ve výškách pět set až devět set kilometrů."
    },

    # --- SAT-3: LEO, MEO, GEO a speciální dráhy (GSO, Molnija, Tundra) ---
    {
        "speaker": "Tereza",
        "question_id": "sat-3",
        "display": "Teď asi nejčastější zkoušková klasika: **rozdělení drah podle výšky – LEO, MEO a GEO**, plus speciální dráhy **GSO, Molnija a Tundra**!",
        "text": "Teď asi nejčastější klasika ze zkoušek: rozdělení drah podle výšky na LEO, MEO a GEO... plus speciální dráhy GSO, Molnija a Tundra!"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-3",
        "display": "Jdeme na to! **LEO (Low Earth Orbit)** je nejníž, zhruba **160 až 2 000 km**. Družice tam letí asi 7,6 km/s, Zemi obletí za **90 až 130 minut** a má super nízkou latenci kolem **20 až 50 ms**. Nevýhoda? Z tak malé výšky vidí jen malý kousek Země (na 500 km asi 3,6 % povrchu) a rychle zmizí za horizontem, takže potřebuješ **stovky až tisíce družic** a neustálé předávání spojení.",
        "text": "Jdeme na to! Nízká dráha LEO je nejníž, zhruba sto šedesát až dva tisíce kilometrů. Družice tam letí přes sedm a půl kilometru za sekundu, Zemi obletí za devadesát až sto třicet minut a má super nízkou latenci kolem dvaceti až padesáti milisekund. Nevýhoda? [sighs] Z malé výšky vidí jen malý kousek povrchu a rychle zmizí za obzorem, takže potřebuješ stovky až tisíce družic a neustálý handover."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-3",
        "display": "Pak je **MEO (Medium Earth Orbit)** od **2 000 do 35 786 km**. Co je pro ni typické?",
        "text": "Pak je střední dráha MEO, od dvou tisíc do třiceti pěti tisíc sedmi set osmdesáti šesti kilometrů. Co je pro ni typické?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-3",
        "display": "MEO je zlatý střed: oběžná doba je **2 až 24 hodin**, latence kolem **50 až 150 ms** a na globální pokrytí stačí jen **desítky družic**. Je to království navigací **GNSS** – třeba GPS ve výšce 20 200 km nebo evropské Galileo – ale i komunikační sítě **O3b** kolem 8 000 km. Pozor jen na **Van Allenovy radiační pásy**, které v některých výškách MEO vyžadují vyšší radiační odolnost elektroniky.",
        "text": "MEO je takový zlatý střed: oběžná doba je dvě až dvacet čtyři hodin, latence kolem padesáti až sto padesáti milisekund a na globální pokrytí stačí desítky družic. Je to království navigací jako GPS ve výšce dvacet tisíc dvě stě kilometrů nebo evropské Galileo, ale i komunikační sítě O3b. Jen pozor na Van Allenovy radiační pásy, které vyžadují vyšší radiační odolnost součástek."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-3",
        "display": "A nahoře kraluje **GEO** ve výšce **35 786 km**! Jaké tři nebo čtyři podmínky musí splnit, aby na obloze stála jako přibitá?",
        "text": "A nahoře kraluje GEO ve výšce třicet pět tisíc sedm set osmdesát šest kilometrů! Jaké podmínky musí splnit, aby stála na obloze jako přibitá?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-3",
        "display": "Tohle je jistá zkoušková otázka! Aby byla družice geostacionární (**GEO**), musí být: **1. kruhová** ($e = 0$), **2. rovníková** ($i = 0^\circ$), **3. prográdní** (letět po směru otáčení Země) a **4. mít periodu rovnou siderickému dni**, tedy **23 hodin 56 minut a 4 sekundy**. Pak stačí **3 družice**, aby pokryly většinu Země (jedna vidí až ~42 % povrchu), a na Zemi ti stačí **pevná anténa** bez natáčení. Jenže v polárních oblastech má strašně nízkou elevaci a nepokryje póly.",
        "text": "Tohle je naprostá klasika u zkoušky! Aby byla družice geostacionární, musí splnit čtyři věci: zaprvé kruhová dráha, zadruhé rovníková s nulovým sklonem, zatřetí letět po směru rotace Země, a začtvrté perioda přesně dvacet tři hodin, padesát šest minut a čtyři sekundy. Pak stačí jen tři družice na většinu planety a pevná anténa bez natáčení. Ale v polárních oblastech má hrozně nízkou elevaci a póly nepokryje."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-3",
        "display": "A rozdíl mezi **GEO** a **GSO**? To je taky častý chyták!",
        "text": "A rozdíl mezi GEO a GSO? To je taky častý chyták, že?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-3",
        "display": "**GEO je jen speciální případ GSO.** **GSO (geosynchronní dráha)** má také periodu 23 h 56 min, ale může mít **nenulový sklon $i > 0^\circ$ nebo excentricitu $e > 0$**. Z pohledu pozorovatele na Zemi pak družice nestojí v jednom bodě, ale každý den na obloze opisuje **osmičku neboli analemu**!",
        "text": "GEO je jen speciální případ GSO. Geosynchronní dráha má také periodu dvacet tři hodin padesát šest minut, ale může mít sklon nebo elipticitu. Z pohledu ze Země pak družice nestojí v jednom bodě, ale každý den na obloze opisuje osmičku... takzvanou analemu!"
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-3",
        "display": "A jak vyřešili pokrytí Arktidy a severních oblastí? Těmi eliptickými drahami **Molnija** a **Tundra**, že?",
        "text": "A jak se vyřešilo pokrytí Arktidy a polárních oblastí? Těmi eliptickými drahami Molnija a Tundra?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-3",
        "display": "Přesně! Obě využívají **2. Keplerův zákon** – družice letí rychle nízko nad jižní polokoulí a pak se dlouhé hodiny „loudá“ vysoko v apogeu nad severní polokoulí. Obě mají magický sklon **$63{,}4^\circ$** (aby se jim nestáčelo apogeum). Rozdíl je v periodě a tvaru: **Molnija** má **12hodinovou** dráhu a extrémní excentricitu (~0,7 až 0,75), visí nad severem přes 8 hodin. **Tundra** je **24hodinová** (geosynchronní) s mírnější excentricitou (~0,2 až 0,4) a pokrývá oblast 12 až 16 hodin.",
        "text": "Přesně tak! Obě geniálně využívají druhý Keplerův zákon: družice rychle proletí nízko nad jihem a pak se dlouhé hodiny loudá vysoko v apogeu nad severem. Obě mají magický sklon šedesát tři celé čtyři stupně... Rozdíl je v periodě: Molnija má dvanáctihodinovou dráhu a visí nad severem přes osm hodin. Tundra je dvacetičtyřhodinová a pokrývá oblast dvanáct až šestnáct hodin."
    },

    # --- SAT-4: Vliv dráhy na spoj (Footprint, Latence, Doppler, FSPL) ---
    {
        "speaker": "Tereza",
        "question_id": "sat-4",
        "display": "Skvělé! Teď čtvrtá kapitola: **jak oběžná dráha ovlivňuje samotný rádiový spoj** – tedy footprint, latenci, Dopplerův jev a útlum.",
        "text": "Skvělé! [sighs] Teď čtvrtá kapitola: jak oběžná dráha ovlivňuje samotný rádiový spoj... tedy footprint, latenci, Dopplerův jev a útlum."
    },
    {
        "speaker": "Marek",
        "question_id": "sat-4",
        "display": "**Footprint** je stopa pokrytí na Zemi. Pozor na rozdíl: **geometrická viditelnost** znamená jen to, že družice není pod obzorem, kdežto **skutečný footprint** je vždy menší – omezuje ho minimální elevační úhel antény (jinak signál prochází moc dlouho atmosférou a stíní ho terén), tvar anténního svazku a výkonová bilance.",
        "text": "Footprint je stopa pokrytí na Zemi. Pozor na zásadní rozdíl: geometrická viditelnost znamená jen to, že družice je nad obzorem. Ale skutečný footprint je vždy menší... omezuje ho minimální elevační úhel antény, tvar svazku a výkonová bilance."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-4",
        "display": "A u **latence** u GEO si lidi často pletou jeden skok a zpáteční cestu RTT, že?",
        "text": "A u latence u GEO si lidi často pletou jeden směr a zpáteční cestu RTT, že?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-4",
        "display": "Jo! Jeden směr ze Země na GEO (35 786 km rychlostí světla) trvá asi **120 ms**. Spojení od uživatele přes družici k druhému uživateli (dva úseky) dá minimálně **239 ms**. A obousměrné **RTT (tam a zpět)** včetně zpracování a protokolů vychází v praxi na **500 až 650 ms**! Oproti tomu MEO (třeba O3b) má RTT kolem **150 ms** a nízké LEO jako Starlink jen **25 až 50 ms**.",
        "text": "Přesně tak! Jeden směr na GEO rychlostí světla trvá zhruba sto dvacet milisekund. Jeden skok od uživatele přes družici k druhému dá dvě stě třicet devět milisekund. A obousměrné RTT tam a zpět se zpracováním v praxi vychází na pět set až šest set padesát milisekund! Oproti tomu MEO má kolem sto padesáti a LEO jako Starlink jen dvacet pět až padesát milisekund."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-4",
        "display": "A jak je to s **Dopplerovým jevem** a **útlumem volného prostoru FSPL**?",
        "text": "A jak je to s Dopplerovým jevem a útlumem volného prostoru FSPL?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-4",
        "display": "**Dopplerův posuv** způsobuje radiální složka rychlosti: když se družice přibližuje, frekvence roste, když se vzdaluje, klesá. U pevné **GEO** družice je vůči pevnému terminálu v podstatě **nulový**, kdežto u rychlého **LEO** v pásmech Ku/Ka skáče o **desítky až stovky kHz**, takže ho terminál musí průběžně kompenzovat! A **FSPL (útlum volného prostoru)** roste se **čtvercem vzdálenosti $d^2$ a čtvercem frekvence $f^2$** – mezi LEO a GEO je na stejné frekvenci rozdíl kolem **36 dB**, což je přes čtyři tisíce krát víc výkonu!",
        "text": "Dopplerův posuv způsobuje radiální rychlost: když se družice blíží, frekvence roste, když se vzdaluje, klesá. U pevné GEO družice je vůči terminálu v podstatě nulový. Ale u rychlého LEO skáče o desítky až stovky kilohertzů, takže ho terminál musí neustále dolaďovat! A útlum volného prostoru FSPL roste se čtvercem vzdálenosti a čtvercem frekvence... Mezi LEO a GEO je rozdíl kolem třiceti šesti decibelů!"
    },

    # --- SAT-5: Konstelace (Walker Delta & Star), Spolehlivost, Laserové ISL ---
    {
        "speaker": "Tereza",
        "question_id": "sat-5",
        "display": "Jasné! Pátá kapitola řeší **satelitní konstelace**. Jaký je rozdíl mezi **Walker Delta** a **Walker Star**?",
        "text": "Jasně. Pátá kapitola řeší satelitní konstelace. Jaký je rozdíl mezi Walker Delta a Walker Star?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-5",
        "display": "Tohle si zapamatuješ snadno podle čísel $360^\circ$ a $180^\circ$: **Walker Delta** má orbitální roviny rozprostřené rovnoměrně po celých **360 stupních** kolem rovníku – typicky šikmé dráhy pro navigace, třeba Galileo ($56^\circ:24/6/1$, tedy 6 rovin po 4 družicích, po $60^\circ$). Naproti tomu **Walker Star** používá téměř **polární dráhy**, jejichž roviny jsou rozloženy v rozsahu **180 stupňů** – pokrývá i póly (třeba **Iridium**: 66 družic v 6 rovinách ve výšce 780 km).",
        "text": "Tohle si zapamatuješ snadno: tři sta šedesát versus sto osmdesát stupňů. Walker Delta má orbitální roviny rozprostřené po celých třech stech šedesáti stupních kolem rovníku... typicky navigace jako Galileo. Naproti tomu Walker Star používá polární dráhy v rozsahu sto osmdesáti stupňů, takže pokrývá i póly, jako třeba Iridium."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-5",
        "display": "A pak tam jsou **mezisatelitní spoje ISL** – hlavně ty **laserové**!",
        "text": "A pak tam jsou mezisatelitní spoje ISL... hlavně ty laserové!"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-5",
        "display": "**ISL (Inter-Satellite Links)** dovolí družicím posílat si data přímo ve vesmíru (často laserem na vlnové délce **1550 nm** rychlostí jednotek až desítek Gb/s) bez nutnosti skákat na pozemní bránu v každé oblasti. Výhody jsou obrovská kapacita a úzký svazek bez rušení. Nevýhody? Extrémní nároky na přesné míření a stabilizaci proti vibracím. A chyták ze skript: úzký laserový svazek sice ztěžuje odposlech, ale **sám o sobě nezaručuje bezpečnost – data se musí pořád šifrovat!**",
        "text": "ISL dovolí družicím posílat data přímo ve vesmíru, laserem na vlnové délce patnáct set padesát nanometrů... bez nutnosti skákat na pozemní bránu. Výhodou je obrovská rychlost a žádné rádiové rušení. Nevýhodou extrémní nároky na míření. A pozor na chyták: úzký paprsek sice ztěžuje odposlech, ale sám o sobě nezaručuje bezpečnost! Data se musí pořád šifrovat."
    },

    # --- SAT-6: Kosmický segment, Transpondéry a Kmitočtová pásma (GiTySAT) ---
    {
        "speaker": "Tereza",
        "question_id": "sat-6",
        "display": "Teď se přesouváme do prezentace **GiTySAT**! V šesté kapitole máme **kosmický segment, transpondéry a kmitočtová pásma**. Jaký je rozdíl mezi standardní družicí a **HTS**?",
        "text": "Teď k prezentaci GiTySAT! V šesté kapitole máme kosmický segment, transpondéry a pásma... Jaký je rozdíl mezi standardní družicí a HTS?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-6",
        "display": "**Standardní družice** svítí širokým svazkem na celý kontinent. **HTS (High Throughput Satellite)** pokryje oblast mnoha úzkými bodovými svazky (spot-beamy) a díky tomu může stejné frekvence opakovaně využívat – má tak mnohonásobně vyšší kapacitu! A co se týče **transpondérů**, známe tři druhy: **Bend pipe** (jen hloupá „ohnutá trubka“, co signál přijme, posune frekvenci a zesílí), **Cross type** (křížové propojení mezi svazky/pásmy) a **On-board switching** (chytré přepínání přímo na palubě družice).",
        "text": "Standardní družice svítí širokým svazkem na celý kontinent. Družice HTS pokryje oblast desítkami úzkých bodových svazků, a díky tomu může frekvence opakovaně využívat... má tak mnohonásobně vyšší kapacitu! A transpondéry máme tři: Bend pipe, což je jen průchozí zesilovač s posunem frekvence; Cross type s křížovým propojením; a On-board switching, tedy chytré přepínání na palubě."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-6",
        "display": "A teď ta tabulka **satelitních pásem** od C až po E band! Co z ní musím v testu bezpečně vědět?",
        "text": "A co ta tabulka satelitních pásem od C až po E band? Co z ní musím v testu bezpečně vědět?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-6",
        "display": "Drž se posloupnosti frekvencí: **C band (4–8 GHz)** – klasická sat. komunikace a meteo radary, odolný dešti. **X band (8–12 GHz)** – vojenské/vládní satelitní komunikace, radary, hluboký vesmír. **Ku band (11–18 GHz)** – satelitní TV vysílání a běžný VSAT. **K band (18–27 GHz)** – obří chyták: **silný útlum vodní párou při 22,23 GHz**! **Ka band (27–40 GHz)** – moderní rychlý internet (HTS, O3b, brány LEO) a 5G. A úplně nahoře **V band (40–75 GHz)** a **E band (60–90 GHz)** pro experimenty a ultraširokopásmové brány.",
        "text": "Drž se pořadí frekvencí: C band, čtyři až osm gigahertzů, je klasická komunikace odolná dešti. X band, osm až dvanáct gigahertzů, je armáda a hluboký vesmír. Ku band, jedenáct až osmnáct gigahertzů, satelitní televize a VSAT. K band má obří chyták: silný útlum vodní párou na dvaceti dvou celých dvaceti třech gigahertzích! Ka band, dvacet sedm až čtyřicet gigahertzů, je rychlý internet a Starlink brány. A nahoře jsou V a E band."
    },

    # --- SAT-7: GEO sítě a služby GiTySAT ---
    {
        "speaker": "Tereza",
        "question_id": "sat-7",
        "display": "Pěkně! V sedmé kapitole jsou **GEO sítě, topologie a firma GiTy**. Co je důležité o **GiTy** a jaké jsou **čtyři topologie GEO sítí**?",
        "text": "Pěkně shrnuto! V sedmé kapitole jsou GEO sítě, topologie a firma GiTy. Co je důležité vědět o GiTy a jaké jsou čtyři topologie sítí?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-7",
        "display": "**GiTy, a.s.** má vlastní satelitní **teleport (HUB)** přímo v ČR, vlastní pozemní **MPLS síť** v ČR a na Slovensku, nepřetržitý dohled 24/7 s garancí SLA a bezpečnostní **certifikaci NBÚ – Tajné**. A ty **čtyři topologie GEO sítí** jsou: **1. Broadcast** (jednosměrná distribuce dat), **2. Bod–Bod** pomocí technologie **SCPC** (vyhrazený kanál pro dva modemy/routery), **3. Hvězdicová síť** ($1\times$ VSAT HUB a $n\times$ terminálů, asymetrický provoz přes **TDMA/FDMA**) a **4. MESH** (terminály spolu mluví přímo jedním skokem bez dvojího průchodu přes HUB).",
        "text": "Firma GiTy má vlastní satelitní teleport přímo u nás v Česku, pozemní MPLS síť, nepřetržitý dohled dvacet čtyři sedm a certifikaci NBÚ na stupeň Tajné. A ty čtyři topologie: zaprvé Broadcast pro jednosměrné šíření; zadruhé Bod-Bod přes SCPC s vyhrazeným kanálem; zatřetí Hvězdicová síť s jedním hubem a terminály přes TDMA a FDMA; a začtvrté MESH, kde terminály komunikují přímo na jeden skok."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-7",
        "display": "A ještě srovnání **internetová konfigurace vs. privátní satelitní síť**!",
        "text": "A ještě srovnání: internetová konfigurace versus privátní satelitní síť!"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-7",
        "display": "**Internetová konfigurace** je pro velké množství terminálů, unifikovaná služba do Internetu s agregací, **FUP** a jen omezeným dohledem. Naproti tomu **privátní satelitní síť** propojuje pobočky s centrálou přímo do firemní **MPLS WAN**, má garantovanou kvalitu **QoS**, přídavné šifrování a plný **End-to-End dohled** přes SNMP.",
        "text": "Internetová konfigurace je pro masy terminálů: sdílená služba s agregací, limitem FUP a základním dohledem. Naproti tomu privátní satelitní síť propojuje pobočky do firemní MPLS WAN, má garantovanou kvalitu QoS, šifrování a plný dohled od konce ke konci."
    },

    # --- SAT-8: Praxe: MEO (O3b) a LEO konstelace (OneWeb, Starlink, Amazon, Telesat) ---
    {
        "speaker": "Tereza",
        "question_id": "sat-8",
        "display": "V osmé kapitole jsou konkrétní moderní konstelace z prezentace: **O3b, OneWeb, Starlink, Amazon LEO a Telesat Lightspeed**. Jak si je rychle odlišit?",
        "text": "V osmé kapitole jsou moderní konstelace: O3b, OneWeb, Starlink, Amazon LEO a Telesat Lightspeed. Jak si je rychle odlišit?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-8",
        "display": "Dejme každé jasnou nálepku: **O3b / O3b mPOWER** od SES je jediná velká **MEO** konstelace v přehledu – výška **8 000 km**, Ka-band, RTT **150 ms**, pokrytí zhruba $\pm 50^\circ$ šířky (takže ne póly!), až 1,6 Gbps na svazek. Pak máme **OneWeb** (Eutelsat): **LEO ve 1 200 km**, **652 družic**, RTT kolem **100 ms**, k terminálům jde **Ku-band** a k branám Ka-band; nabízí firemní **MIR** (maximální) i garantovanou **CIR** rychlost.",
        "text": "Dejme každé jasnou nálepku: O3b od operátora SES je jediná velká MEO konstelace... výška osm tisíc kilometrů, latence sto padesát milisekund, nepokrývá póly. Pak OneWeb: nízké LEO ve dvanácti stech kilometrech, šest set padesát dva družic, k terminálům Ku band a nabízí i garantovanou rychlost CIR."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-8",
        "display": "A **Starlink** od SpaceX versus nováčci **Amazon LEO** a **Telesat Lightspeed**?",
        "text": "A Starlink od SpaceX versus Amazon LEO a Telesat Lightspeed?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-8",
        "display": "**Starlink** je největší aktivní konstelace (přes 9 800 družic, typicky **550 km**, RTT jen **25–50 ms**), využívá **laserové spoje mezi družicemi**, 13km svazky a terminály Mini, Standard, Enterprise a Performance. **Amazon LEO** (dříve Kuiper, 590–630 km, komerční start 2026/2027) má mít 3 232 družic, lasery a terminály Nano, Pro a Ultra až do 1 Gbps. A **Telesat Lightspeed** (start 2028, 1 015 a 1 325 km, Ka-band + lasery) cílí čistě na B2B, letectví a **L2 služby** až do 3 Gbps s pokrytím včetně pólů.",
        "text": "Starlink je největší aktivní konstelace: tisíce družic ve výšce pět set padesát kilometrů, latence jen dvacet pět až padesát milisekund, laserové mezisatelitní spoje a terminály Mini, Standard a Enterprise. Amazon LEO bude mít přes tři tisíce družic s komerčním startem kolem roku dvacet dvacet sedm. A kanadský Telesat Lightspeed se startem dvacet dvacet osm cílí čistě na firemní sektor, letectví a vrstvu L2."
    },

    # --- SAT-9: Terminály, Zabezpečení, DVB-S2X ACM a Hybridní sítě ---
    {
        "speaker": "Tereza",
        "question_id": "sat-9",
        "display": "A jsme u deváté, poslední kapitoly! **Terminály, zabezpečení, trendy DVB-S2X a hybridní síť GiTySAT**. Co tvoří klasický VSAT terminál?",
        "text": "A jsme u deváté, poslední kapitoly! [sighs] Terminály, zabezpečení, standard DVB-S2X a hybridní síť GiTySAT. Co tvoří klasický VSAT terminál?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-9",
        "display": "Dvě části: **venkovní** je **anténa** (pevná parabola 0,7–2,4 m, mobilní *Drive Away* na auto, *Quick Deploy* nebo přenosný *Manpack*) a **RF jednotka** (C, X, Ku nebo Ka). **Vnitřní část** je samotný **VSAT modem/router** (třeba iDirect 950mp, 9530 nebo Newtec MDM3315). A pro vysokou bezpečnost používá GiTy **iDirect TRANSEC** (skrytí aktivity kanálu, **AES-256 na L2**, certifikát **X.509**), **Spread spectrum**, moduly **FIPS 140-2 Level 3** a systém **CSIR** proti úmyslnému rušení (anti-jamming).",
        "text": "Dvě části: venkovní je anténa, buď pevná parabola nebo mobilní Drive Away na auto či batoh Manpack, plus RF jednotka. Vnitřní část je samotný VSAT modem nebo router. A pro vysokou bezpečnost používá GiTy technologii TRANSEC se skrytou aktivitou kanálu, šifrováním AES dvě stě padesát šest na druhé vrstvě, certifikátem X.509 a ochranou proti rušení."
    },
    {
        "speaker": "Tereza",
        "question_id": "sat-9",
        "display": "A co v trendech znamená **DVB-S2X s ACM** a jak funguje **hybridní síť** v posledním slidu?",
        "text": "A co v trendech znamená DVB-S2X s ACM a jak přesně funguje ta hybridní síť?"
    },
    {
        "speaker": "Marek",
        "question_id": "sat-9",
        "display": "**ACM (Adaptive Coding and Modulation)** je geniální v tom, že když přijde bouřka a zhorší se signál, spoj nespadne – modem v reálném čase přepne z vysoké modulace (třeba 256APSK) na odolnější QPSK a zpátky, jakmile vysvitne slunce! A **hybridní síť GiTySAT** chytře kombinuje **GEO + LEO + Internet**: **kritický a citlivý provoz** jde zabezpečeným GEO VSATem do centrály, **standardní provoz** letí rychlým LEO terminálem přes privátní propoj NNI do MPLS sítě G-Net, a **nekritický internetový provoz** jde lokálně přes firewall rovnou do Internetu. Tím máš v kapse všechno!",
        "text": "Adaptivní modulace ACM je geniální v tom, že když přijde bouřka a zhorší se signál, spoj nespadne! Modem v reálném čase přepne na robustnější modulaci a zpět, jakmile vysvitne slunce. A hybridní síť GiTySAT chytře kombinuje GEO, LEO a Internet: kritický provoz jde zabezpečeným GEO VSATem, běžný provoz rychlým LEO spojením do sítě G-Net, a internetový provoz jde lokálně přes firewall. Tím máš pokryté úplně všechno!"
    }
]


def synthesize_turn(turn_idx, item):
    speaker = item["speaker"]
    text = item["text"]
    voice_info = VOICES[speaker]
    voice_id = voice_info["voice_id"]
    settings = voice_info["settings"]

    # Cache key
    h = hashlib.sha256(f"{voice_id}_{json.dumps(settings)}_{text}".encode("utf-8")).hexdigest()[:16]
    seg_file = os.path.join(CACHE_DIR, f"seg_{turn_idx:02d}_{speaker}_{h}.mp3")

    if os.path.exists(seg_file) and os.path.getsize(seg_file) > 1000:
        with open(seg_file, "rb") as f:
            data = f.read()
        return data

    payload = json.dumps({
        "text": text,
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": settings
    }).encode("utf-8")

    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        data=payload,
        headers={
            "xi-api-key": API_KEY,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg"
        }
    )

    try:
        with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
            audio_bytes = r.read()
        with open(seg_file, "wb") as f:
            f.write(audio_bytes)
        return audio_bytes
    except Exception as e:
        print(f"Error on turn {turn_idx} ({speaker}): {e}")
        raise e


async def main():
    print(f"Synthesizing {len(ENRICHED_SCRIPT)} turns with ElevenLabs Turbo v2.5...")
    results = []

    for idx, item in enumerate(ENRICHED_SCRIPT):
        print(f"Turn {idx+1}/{len(ENRICHED_SCRIPT)}: {item['speaker']} ({item['question_id']})...")
        audio_data = synthesize_turn(idx, item)
        # Approximate duration by mp3 size (128kbps = 16000 bytes/sec)
        # ElevenLabs Turbo v2.5 output is 128kbps mp3 (~16000 bytes/sec)
        dur = len(audio_data) / 16000.0
        results.append((audio_data, dur))
        print(f"   Done: {dur:.2f}s ({len(audio_data)/1024:.1f} KB)")

    # Assemble final master MP3: podcast_satelity_eleven.mp3
    final_mp3 = os.path.join(OUT_DIR, "podcast_satelity_eleven.mp3")
    timeline = []
    current_time = 0.0

    # Silent MP3 padding frame
    SILENT_MP3_FRAME = bytes([0xFF, 0xF3, 0x64, 0xC4]) + bytes(140)
    PAUSE_TURN = SILENT_MP3_FRAME * 10       # ~240ms
    PAUSE_CHAPTER = SILENT_MP3_FRAME * 22    # ~528ms

    with open(final_mp3, "wb") as outfile:
        for idx, (turn_bytes, dur) in enumerate(results):
            outfile.write(turn_bytes)
            next_q = ENRICHED_SCRIPT[idx + 1]["question_id"] if idx + 1 < len(ENRICHED_SCRIPT) else None
            pause = PAUSE_CHAPTER if (next_q and next_q != ENRICHED_SCRIPT[idx]["question_id"]) else PAUSE_TURN
            outfile.write(pause)
            pause_dur = len(pause) / 6000.0

            item = ENRICHED_SCRIPT[idx]
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

    print(f"\nSuccessfully generated {final_mp3}!")
    print(f"Total duration: {current_time/60.0:.2f} min ({current_time:.2f} s)")

    # Save metadata JSON for the player
    meta_path = os.path.join(OUT_DIR, "podcast_eleven_data.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump({
            "engine": "elevenlabs_hd",
            "filename": "podcast_satelity_eleven.mp3",
            "total_duration": round(current_time, 2),
            "segments": timeline
        }, f, ensure_ascii=False, indent=2)
    print("Metadata written to", meta_path)

if __name__ == "__main__":
    asyncio.run(main())

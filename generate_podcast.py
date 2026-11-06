import asyncio
import hashlib
import json
import os
import edge_tts

# Two voice engines:
# 1. "copilot_v2": Microsoft Copilot Conversational V2 Multilingual voices (Andrew & Ava)
# 2. "cz_studio": Native Czech voices with tuned pitch/rate and 100% Czech phonetic transcription of all English terms
ENGINES = {
    "copilot_v2": {
        "Tomáš": {"voice": "en-US-AndrewMultilingualNeural", "rate": "+2%", "pitch": "-1Hz"},
        "Klára": {"voice": "en-US-AvaMultilingualNeural", "rate": "+2%", "pitch": "+0Hz"},
        "filename": "podcast_copilot_v2.mp3"
    },
    "cz_studio": {
        "Tomáš": {"voice": "cs-CZ-AntoninNeural", "rate": "+3%", "pitch": "-2Hz"},
        "Klára": {"voice": "cs-CZ-VlastaNeural", "rate": "+2%", "pitch": "+1Hz"},
        "filename": "podcast_optika_kabelaz.mp3"
    }
}

# 180ms of valid silent 24kHz 48kbps mono MP3 frames between turns for natural studio breathing room
# Each frame for MPEG-2 Layer 3 24kHz 48kbps is 144 bytes (24ms per frame). 8 frames = 192ms.
SILENT_MP3_FRAME = bytes([0xFF, 0xF3, 0x64, 0xC4]) + bytes(140)
PAUSE_BYTES = SILENT_MP3_FRAME * 8  # ~0.19s natural pause between turns

# Natural, conversational NotebookLM-style script with 100% phonetic Czech in `tts` (no raw English words!)
SCRIPT = [
    # --- ÚVOD ---
    {
        "speaker": "Klára",
        "question_id": "intro",
        "display": "Ahoj Tome! Hele, zítra mě čeká ten velký test na optiku a strukturovanou kabeláž. Mám tu fotky loňského testu i přesný výpis z našich hodin – projdeme to spolu tak, abych tam zítra nechala plný počet bodů?",
        "tts": "Ahoj Tome! Hele, zítra mě čeká ten velký test na optiku a strukturovanou kabeláž. Mám tu fotky loňského testu i přesný výpis z našich hodin – projdeme to spolu tak, abych tam zítra nechala plný počet bodů?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "intro",
        "display": "Jasně Kláro, jdeme na to! Vezmeme to úplně bez omáčky, přesně podle otázek z testu a tvých zápisků z hodin. Ukážeme si i všechny chytáky, na kterých lidi zbytečně ztrácejí body. Začneme optikou, jo?",
        "tts": "Jasně Kláro, jdeme na to! Vezmeme to úplně bez omáčky, přesně podle otázek z testu a tvých zápisků z hodin. Ukážeme si i všechny chytáky, na kterých lidi zbytečně ztrácejí body. Začneme optikou, jo?"
    },

    # --- OTÁZKA O1: Základní typy optických vláken, vlnové délky, struktura vlákna ---
    {
        "speaker": "Klára",
        "question_id": "opt-1",
        "display": "Super! Takže první otázka z optiky: **„Základní typy optických vláken, vlnové délky. Nakreslete typickou strukturu optického vlákna.“** Jak mám nakreslit a popsat ten průřez vláknem?",
        "tts": "Super! Takže první otázka z optiky: Základní typy optických vláken, vlnové délky, a nakreslete typickou strukturu optického vlákna. Jak mám nakreslit a popsat ten průřez vláknem?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "opt-1",
        "display": "Představ si, že ten optický kabel rozřízneš a koukáš na něj zepředu. Nakreslíš **čtyři soustředné kružnice** od středu ven. Úplně uprostřed je **jádro (Core)** z křemičitého skla s příměsemi, které zvyšují jeho index lomu $n_1$. A teď bacha na průměr jádra: u jednovidového vlákna je to **9 µm** (obecně 8 až 10 µm), a u mnohovidového **50 µm** nebo **62,5 µm**.",
        "tts": "Představ si, že ten optický kabel rozřízneš a koukáš na něj zepředu. Nakreslíš čtyři soustředné kružnice od středu ven. Úplně uprostřed je jádro, anglicky kór, z křemičitého skla s příměsemi, které zvyšují jeho index lomu en jedna. A teď bacha na průměr jádra: u jednovidového vlákna je to devět mikrometrů, obecně osm až deset mikrometrů, a u mnohovidového padesát, nebo šedesát dva a půl mikrometru."
    },
    {
        "speaker": "Klára",
        "question_id": "opt-1",
        "display": "Dobře, to je jádro. Hned kolem něj je druhá vrstva – **plášť (Cladding)** s nižším indexem lomu $n_2$. Ten má prý průměr vždycky stejný?",
        "tts": "Dobře, to je jádro. Hned kolem něj je druhá vrstva – plášť, anglicky kleding, s nižším indexem lomu en dva. Ten má prý průměr vždycky stejný?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "opt-1",
        "display": "Přesně tak! Plášť má vždycky průměr **125 µm**, ať je to singlemode nebo multimode – proto se vlákna značí třeba **9/125** nebo **50/125 µm**. Kolem pláště je pak třetí vrstva: **primární ochrana** z akrylátového laku o průměru **250 µm**, která chrání sklo před vlhkostí a mikroohyby. A čtvrtá vrstva je **sekundární ochrana**, plastová trubička o průměru **900 µm**.",
        "tts": "Přesně tak! Plášť má vždycky průměr sto dvacet pět mikrometrů, ať je to singlmód nebo multimód – proto se vlákna značí třeba devět lomeno sto dvacet pět, nebo padesát lomeno sto dvacet pět mikrometrů. Kolem pláště je pak třetí vrstva: primární ochrana z akrylátového laku o průměru dvě stě padesát mikrometrů, která chrání sklo před vlhkostí a mikroohyby. A čtvrtá vrstva je sekundární ochrana, plastová trubička o průměru devět set mikrometrů."
    },
    {
        "speaker": "Klára",
        "question_id": "opt-1",
        "display": "Takže čtyři čísla od středu ven: **9 nebo 50/62,5 µm** jádro, **125 µm** plášť, **250 µm** primární ochrana a **900 µm** sekundární ochrana. A jak v testu popsat ty **základní typy vláken**?",
        "tts": "Takže čtyři čísla od středu ven: devět, nebo padesát či šedesát dva a půl mikrometru jádro, sto dvacet pět mikrometrů plášť, dvě stě padesát mikrometrů primární ochrana a devět set mikrometrů sekundární ochrana. A jak v testu popsat ty základní typy vláken?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "opt-1",
        "display": "Rozdělíš je na **mnohovidová (Multimode – MM)** a **jednovidová (Singlemode – SM)**. U mnohovidových je jádro široké (50 nebo 62,5 µm), takže jím letí spousta paprsků – vidů – pod různými úhly najednou. Jenže paprsek, co letí rovně středem, dorazí do cíle dřív než ten, co se pořád odráží od stěn. Tím se světelný pulz po cestě rozplizne a vzniká **vidová (modální) disperze**.",
        "tts": "Rozdělíš je na mnohovidová, neboli multimód, a jednovidová, neboli singlmód. U mnohovidových je jádro široké, padesát nebo šedesát dva a půl mikrometru, takže jím letí spousta paprsků – takzvaných vidů – pod různými úhly najednou. Jenže paprsek, co letí rovně středem, dorazí do cíle dřív než ten, co se pořád odráží od stěn. Tím se světelný pulz po cestě rozplizne a vzniká vidová, neboli modální disperze."
    },
    {
        "speaker": "Klára",
        "question_id": "opt-1",
        "display": "A proto se mnohovidová vlákna dělí ještě na dva podtypy: se **skokovou změnou indexu lomu (Step-Index)** a s **gradientní změnou (Graded-Index)**, že jo?",
        "tts": "A proto se mnohovidová vlákna dělí ještě na dva podtypy: se skokovou změnou indexu lomu, step index, a s gradientní změnou, grejdid index, že jo?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "opt-1",
        "display": "Přesně! U **skokového** je index lomu v celém jádře stejný a na kraji skokově klesne, takže paprsky létají ostře cik-cak a disperze je velká. Kdežto u **gradientního** index lomu od středu jádra k plášti plynule parabolicky klesá. Paprsek, který letí dál od osy, má sice delší dráhu, ale v místech s nižším indexem lomu letí světlo rychleji! Takže oba paprsky dorazí do cíle skoro nastejno.",
        "tts": "Přesně! U skokového je index lomu v celém jádře stejný a na kraji skokově klesne, takže paprsky létají ostře cik-cak a disperze je velká. Kdežto u gradientního index lomu od středu jádra k plášti plynule parabolicky klesá. Paprsek, který letí dál od osy, má sice delší dráhu, ale v místech s nižším indexem lomu letí světlo rychleji! Takže oba paprsky dorazí do cíle skoro nastejno."
    },
    {
        "speaker": "Klára",
        "question_id": "opt-1",
        "display": "A u **jednovidového (Singlemode)** vlákna s jádrem **9 µm** se vejde jen jeden jediný přímý vid, takže vidová disperze úplně odpadá a můžeme posílat data na desítky kilometrů. A co ty **vlnové délky**?",
        "tts": "A u jednovidového singlmód vlákna s jádrem devět mikrometrů se vejde jen jeden jediný přímý vid, takže vidová disperze úplně odpadá a můžeme posílat data na desítky kilometrů. A co ty vlnové délky?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "opt-1",
        "display": "Zapamatuj si tři přenosová okna, kde má křemičité sklo nejmenší útlum: **1. okno je 850 nm** (pro multimode, útlum kolem $2{,}5\text{ až }3\text{ dB/km}$). **2. okno je 1300 nm** u multimode a **1310 nm** u singlemode (nulová chromatická disperze, útlum kolem $0{,}35\text{ až }0{,}5\text{ dB/km}$). A **3. okno je 1550 nm** u singlemode – tam je absolutně nejmenší útlum skla, jen asi **$0{,}2\text{ dB/km}$**! Jo a jak máte v zápiscích: frekvence světla v optice se udává v **terahertzích (THz)**.",
        "tts": "Zapamatuj si tři přenosová okna, kde má křemičité sklo nejmenší útlum: První okno je osm set padesát nanometrů, to je pro multimód, útlum kolem dvou a půl až tří decibelů na kilometr. Druhé okno je tisíc tři sta nanometrů u multimódu a tisíc tři sta deset nanometrů u singlmódu, kde je nulová chromatická disperze a útlum kolem nula celá třicet pět až nula celá pět decibelu na kilometr. A třetí okno je tisíc pět set padesát nanometrů u singlmódu – tam je absolutně nejmenší útlum skla, jen asi nula celá dva decibelu na kilometr! Jo a jak máte v zápiscích: frekvence světla v optice se udává v terahertzích."
    },

    # --- OTÁZKA O2: Podmínka přenosu, index lomu, NA, úhel navázání, vložný útlum ---
    {
        "speaker": "Klára",
        "question_id": "opt-2",
        "display": "Jedničku máme! Teď druhá otázka z optiky: **„Co je základní podmínkou pro přenos světla v optickém vlákně? Co je index lomu (i vzorec)? Co je numerická apertura (i vzorec), jakou ji požadujeme, souvisí s průměrem vlákna? Co je maximální úhel navázání? Co je vložný útlum, jak vzniká?“**",
        "tts": "Jedničku máme! Teď druhá otázka z optiky: Co je základní podmínkou pro přenos světla v optickém vlákně? Co je index lomu a jeho vzorec? Co je numerická apertura, jakou ji požadujeme a souvisí s průměrem vlákna? Co je maximální úhel navázání? A co je vložný útlum a jak vzniká?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "opt-2",
        "display": "Takže popořadě: **Základní podmínkou přenosu světla** ve vlákně je **totální (úplný) vnitřní odraz** na rozhraní jádra a pláště. Aby nastal, musí platit dvě věci: zaprvé, **index lomu jádra musí být větší než index lomu pláště ($n_1 > n_2$)**, a zadruhé, **úhel dopadu paprsku $\\alpha$ musí být větší než mezní úhel $\\alpha_m$** (kde $\\sin \\alpha_m = n_2 / n_1$).",
        "tts": "Takže popořadě: Základní podmínkou přenosu světla ve vlákně je totální, neboli úplný vnitřní odraz na rozhraní jádra a pláště. Aby nastal, musí platit dvě věci: zaprvé, index lomu jádra musí být větší než index lomu pláště, tedy en jedna je větší než en dva, a zadruhé, úhel dopadu paprsku alfa musí být větší než mezní úhel alfa em, kde sinus alfa em se rovná en dva lomeno en jedna."
    },
    {
        "speaker": "Klára",
        "question_id": "opt-2",
        "display": "Jasně. A samotný **index lomu $n$**? To je poměr rychlosti světla ve vakuu ku rychlosti v daném prostředí, tedy **$n = c / v$**, že?",
        "tts": "Jasně. A samotný index lomu en? To je poměr rychlosti světla ve vakuu ku rychlosti v daném prostředí, tedy en se rovná cé lomeno vé, že?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "opt-2",
        "display": "Přesně tak! Bezrozměrné číslo $n = c / v$, které udává, kolikrát pomaleji letí světlo v daném materiálu než ve vakuu ($c \\approx 3 \\cdot 10^8\\text{ m/s}$). Ve skle je $n \\approx 1{,}46$, takže tam světlo letí zhruba $200\\,000\\text{ km/s}$. A teď **maximální úhel navázání $\\theta_{\\max}$**: to je největší úhel vůči ose vlákna, pod kterým může paprsek ze vzduchu vstoupit do čela jádra, aby se uvnitř na plášti ještě totálně odrazil a neutekl ven.",
        "tts": "Přesně tak! Bezrozměrné číslo en se rovná cé lomeno vé, které udává, kolikrát pomaleji letí světlo v daném materiálu než ve vakuu. Ve skle je index lomu zhruba jedna celá čtyřicet šest, takže tam světlo letí rychlostí kolem dvou set tisíc kilometrů za sekundu. A teď maximální úhel navázání théta max: to je největší úhel vůči ose vlákna, pod kterým může paprsek ze vzduchu vstoupit do čela jádra, aby se uvnitř na plášti ještě totálně odrazil a neutekl ven."
    },
    {
        "speaker": "Klára",
        "question_id": "opt-2",
        "display": "A z něj rovnou plyne **numerická apertura $NA$**! Vzorec je **$NA = \\sin \\theta_{\\max} = \\sqrt{n_1^2 - n_2^2}$**. A teď ten slavný chyták: souvisí numerická apertura s průměrem vlákna?",
        "tts": "A z něj rovnou plyne numerická apertura EN Á! Vzorec je EN Á se rovná sinus théta max, což se rovná odmocnině z en jedna na druhou mínus en dva na druhou. A teď ten slavný chyták: souvisí numerická apertura s průměrem vlákna?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "opt-2",
        "display": "**Vůbec nesouvisí!** Podívej se na ten vzorec $\\sqrt{n_1^2 - n_2^2}$ – žádný průměr v něm není! Numerická apertura závisí **výhradně na indexech lomu jádra a pláště**. A když se ptají, **jakou $NA$ požadujeme**, napiš, že je to **kompromis**: pro snadné navázání světla ze zdroje bychom chtěli $NA$ co největší, ale pro velkou šířku pásma a malou vidovou disperzi potřebujeme $NA$ co nejmenší (aby paprsky nelétaly pod velkými úhly).",
        "tts": "Vůbec nesouvisí! Podívej se na ten vzorec odmocnina z en jedna na druhou mínus en dva na druhou – žádný průměr v něm není! Numerická apertura závisí výhradně na indexech lomu jádra a pláště. A když se ptají, jakou numerickou aperturu požadujeme, napiš, že je to kompromis: pro snadné navázání světla ze zdroje bychom chtěli aperturu co největší, ale pro velkou šířku pásma a malou vidovou disperzi potřebujeme aperturu co nejmenší, aby paprsky nelétaly pod velkými úhly."
    },
    {
        "speaker": "Klára",
        "question_id": "opt-2",
        "display": "A poslední podotázka u optiky: **co je vložný útlum a jak vzniká?**",
        "tts": "A poslední podotázka u optiky: co je vložný útlum a jak vzniká?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "opt-2",
        "display": "**Vložný útlum** je ztráta optického výkonu v decibelech, která vznikne vložením konektoru, sváru nebo jiného prvku do optické trasy. A vzniká hlavně třemi způsoby: **1. Fresnelovým odrazem** na vzduchové mezeře mezi čely vláken, **2. geometrickou nepřesností spoje** (osovým přesazením jader, zešikmením os nebo mezerou) a **3. nečistotami na čele konektoru** nebo spojením vláken s různým průměrem jádra či různou $NA$.",
        "tts": "Vložný útlum je ztráta optického výkonu v decibelech, která vznikne vložením konektoru, sváru nebo jiného prvku do optické trasy. A vzniká hlavně třemi způsoby: zaprvé Fresnelovým odrazem na vzduchové mezeře mezi čely vláken, zadruhé geometrickou nepřesností spoje, tedy osovým přesazením jader, zešikmením os nebo mezerou, a zatřetí nečistotami na čele konektoru, případně spojením vláken s různým průměrem jádra či různou numerickou aperturou."
    },

    # --- OTÁZKA SK 8: Normy strukturované kabeláže v ČR ---
    {
        "speaker": "Klára",
        "question_id": "sk-8",
        "display": "Paráda, optiku máme kompletní! Jdeme na **Strukturovanou kabeláž** přesně podle našeho výpisu z hodin. Otázka 8: **„Podle jakých norem můžeme v ČR vytvořit strukturovanou kabeláž?“**",
        "tts": "Paráda, optiku máme kompletní! Jdeme na Strukturovanou kabeláž přesně podle našeho výpisu z hodin. Otázka osm: Podle jakých norem můžeme v České republice vytvořit strukturovanou kabeláž?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "sk-8",
        "display": "Přesně podle tvých zápisků: v ČR ji vytváříme podle norem **ČSN EN 50173 a ČSN EN 50174** – jde o české převzetí evropských norem EN (kde 50173 řeší samotný návrh univerzální kabeláže a 50174 její instalaci). A můžeš připsat i mezinárodní normu **ISO/IEC 11801**, ze které evropská norma vychází.",
        "tts": "Přesně podle tvých zápisků: v České republice ji vytváříme podle norem ČSN EN padesát sto sedmdesát tři a ČSN EN padesát sto sedmdesát čtyři – jde o české převzetí evropských norem EN, kde padesát sto sedmdesát tři řeší samotný návrh univerzální kabeláže a padesát sto sedmdesát čtyři její instalaci. A můžeš připsat i mezinárodní normu ISO IEC jedenáct osm set jedna, ze které evropská norma vychází."
    },

    # --- OTÁZKA SK 9: Popište kabel STP a UTP. Do které kategorie UTP? ---
    {
        "speaker": "Klára",
        "question_id": "sk-9",
        "display": "Jasně: **ČSN EN 50173 a 50174**! Devátá otázka: **„Popište kabel STP a UTP. Do které kategorie se mohou používat nestíněné kabely a komponenty?“** V hodinách jsme brali UTP, FTP, STP a taky ten plastový kříž!",
        "tts": "Jasně: ČSN EN padesát sto sedmdesát tři a padesát sto sedmdesát čtyři! Devátá otázka: Popište kabel es-té-pé a ú-té-pé. Do které kategorie se mohou používat nestíněné kabely a komponenty? V hodinách jsme brali ú-té-pé, ef-té-pé, es-té-pé a taky ten plastový kříž!"
    },
    {
        "speaker": "Tomáš",
        "question_id": "sk-9",
        "display": "Tak to řekneme přesně tak, jak to chce váš vyučující:\n- **UTP (Unshielded Twisted Pair)** je **nestíněná kroucená dvojlinka** – nemá žádné kovové stínění. Skládá se ze **4 párů (8 žil/vodičů)**, které jsou vzájemně zkrouceny, čímž se omezuje elektromagnetické rušení a přeslechy. Barvy vodičů vidíme rovnou vlastním okem, je levnější a jednodušší na instalaci. A podle vašich hodin: **nestíněné UTP se využívá do kategorie 6 (třída E)**!",
        "tts": "Tak to řekneme přesně tak, jak to chce váš vyučující: Ú-té-pé, anglicky anšíldid tvistid pér, je nestíněná kroucená dvojlinka – nemá žádné kovové stínění. Skládá se ze čtyř párů, tedy osmi žil neboli vodičů, které jsou vzájemně zkrouceny, čímž se omezuje elektromagnetické rušení a přeslechy. Barvy vodičů vidíme rovnou vlastním okem, je levnější a jednodušší na instalaci. A podle vašich hodin: nestíněné ú-té-pé se využívá do kategorie šest, tedy třídy E!"
    },
    {
        "speaker": "Klára",
        "question_id": "sk-9",
        "display": "Pak máme kompromis **FTP (Foiled Twisted Pair)** – ten má celkové stínění z hliníkové fólie kolem všech 4 párů dohromady, ale jednotlivé páry stíněné nejsou. A teď **STP**!",
        "tts": "Pak máme kompromis ef-té-pé, fójlid tvistid pér – ten má celkové stínění z hliníkové fólie kolem všech čtyř párů dohromady, ale jednotlivé páry stíněné nejsou. A teď es-té-pé!"
    },
    {
        "speaker": "Tomáš",
        "question_id": "sk-9",
        "display": "**STP (Shielded Twisted Pair)** je **stíněná kroucená dvojlinka** – má stejnou strukturu jako UTP, ale **každý pár je samostatně stíněný** kovovou fólií! Využívá se **v kategorii 6a a výš (třída Ea a výš)**. A nezapomeň na ten bonus z hodiny: u **kategorie 6** je uvnitř kabelu **plastový kříž (tzv. rybí kost)**, aby se jednotlivé páry k sobě moc nepřibližovaly.",
        "tts": "Es-té-pé, šíldid tvistid pér, je stíněná kroucená dvojlinka – má stejnou strukturu jako ú-té-pé, ale každý pár je samostatně stíněný kovovou fólií! Využívá se v kategorii šest á a výš, tedy třída E á a výš. A nezapomeň na ten bonus z hodiny: u kategorie šest je uvnitř kabelu plastový kříž, takzvaná rybí kost, aby se jednotlivé páry k sobě moc nepřibližovaly."
    },

    # --- OTÁZKA SK 10: Proč používáme technologii kroucených párů? ---
    {
        "speaker": "Klára",
        "question_id": "sk-10",
        "display": "Super! Desátá otázka: **„Proč používáme technologii kroucených párů?“**",
        "tts": "Super! Desátá otázka: Proč používáme technologii kroucených párů?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "sk-10",
        "display": "Napiš tam přesně tyhle tři věci z vašeho sešitu:\n1. Abychom **omezili elektromagnetické rušení a přeslechy** mezi jednotlivými vodiči a páry a zajistili spolehlivější přenos dat.\n2. **Každý ze 4 párů má jinou hustotu zákrutů**, aby se sousední páry navzájem nerušily.\n3. V každém páru se přenáší signál pomocí dvou vodičů: **jeden vodič přenáší kladnou polaritu signálu ($+U$), druhý vodič opačnou polaritu ($-U$)** a **přijímač vyhodnocuje rozdíl napětí mezi vodiči**.",
        "tts": "Napiš tam přesně tyhle tři věci z vašeho sešitu: Zaprvé, abychom omezili elektromagnetické rušení a přeslechy mezi jednotlivými vodiči a páry a zajistili spolehlivější přenos dat. Zadruhé, každý ze čtyř párů má jinou hustotu zákrutů, aby se sousední páry navzájem nerušily. A zatřetí, v každém páru se přenáší signál pomocí dvou vodičů: jeden vodič přenáší kladnou polaritu signálu, druhý vodič opačnou polaritu a přijímač vyhodnocuje rozdíl napětí mezi vodiči."
    },

    # --- OTÁZKA SK 11: Které normy definují třídy linek? Vyjmenujte třídy linek a frekvenční rozsahy ---
    {
        "speaker": "Klára",
        "question_id": "sk-11",
        "display": "Jedenáctá otázka: **„Které normy definují třídy linek? Vyjmenujte třídy linek a uveďte frekvenční rozsahy.“**",
        "tts": "Jedenáctá otázka: Které normy definují třídy linek? Vyjmenujte třídy linek a uveďte frekvenční rozsahy."
    },
    {
        "speaker": "Tomáš",
        "question_id": "sk-11",
        "display": "Třídy linek definují normy **ČSN EN 50173** (evropská norma) a **ISO/IEC 11801** (mezinárodní norma, kde **ISO** je Mezinárodní organizace pro normalizaci a **IEC** je Mezinárodní elektrotechnická komise). A teď si projdeme frekvenční rozsahy jednotlivých tříd přesně podle vaší tabulky z hodiny!",
        "tts": "Třídy linek definují normy ČSN EN padesát sto sedmdesát tři, to je evropská norma, a ISO IEC jedenáct osm set jedna, to je mezinárodní norma, kde ISO je Mezinárodní organizace pro normalizaci a IEC je Mezinárodní elektrotechnická komise. A teď si projdeme frekvenční rozsahy jednotlivých tříd přesně podle vaší tabulky z hodiny!"
    },
    {
        "speaker": "Klára",
        "question_id": "sk-11",
        "display": "Dobře, vezmu prvních pět:\n- **Třída A** (Cat 1): do **100 kHz** (analogový telefon),\n- **Třída B** (Cat 2): do **1 MHz** (ISDN, 10Base-T, Token Ring 4 MB),\n- **Třída C** (Cat 3): do **16 MHz** (10 Mbps, Token Ring 16 MB),\n- **Třída D** (Cat 5): do **100 MHz** (100 Mbps Fast Ethernet),\n- **Třída D 2002** (Cat 5e): **100 MHz (v závorce 350 MHz)** pro 1 Gbps Gigabit Ethernet!",
        "tts": "Dobře, vezmu prvních pět: Třída A, kategorie jedna, je do sta kilohertzů pro analogový telefon. Třída B, kategorie dva, je do jednoho megahertzu. Třída C, kategorie tři, je do šestnácti megahertzů, deset megabitů za sekundu. Třída D, kategorie pět, je do sta megahertzů, sto megabitů fást eternet. A třída D dva tisíce dva, kategorie pět e, má sto megahertzů, v závorce tři sta padesát megahertzů, pro jeden gigabit eternet!"
    },
    {
        "speaker": "Tomáš",
        "question_id": "sk-11",
        "display": "Skvěle! A druhá polovina tabulky:\n- **Třída E** (Cat 6): do **250 MHz** (1 Gbps Gigabit Ethernet),\n- **Třída Ea** (Cat 6a): do **500 MHz** (10 Gbps – 10GBase-T),\n- **Třída F** (Cat 7): do **600 MHz** (10 Gbps),\n- **Třída Fa** (Cat 7a): do **1000 MHz** (10 Gbps),\n- **Třída I & II** (Cat 8): **1600 / 2000 MHz** (40 Gbps do 30 m),\n- a **optické třídy**: nad 10 MHz (přičemž frekvence světla u optiky se udává v **THz**).",
        "tts": "Skvěle! A druhá polovina tabulky: Třída E, kategorie šest, je do dvou set padesáti megahertzů, jeden gigabit. Třída E á, kategorie šest á, je do pěti set megahertzů, deset gigabitů. Třída F, kategorie sedm, je do šesti set megahertzů, deset gigabitů. Třída F á, kategorie sedm á, je do tisíce megahertzů, deset gigabitů. Třída jedna a dvě, kategorie osm, má tisíc šest set až dva tisíce megahertzů pro čtyřicet gigabitů do třiceti metrů. A optické třídy jsou nad deset megahertzů, přičemž frekvence světla u optiky se udává v terahertzích."
    },

    # --- OTÁZKA SK 12: Co je to FEXT? Jaký útlum FEXT požadujeme? ---
    {
        "speaker": "Klára",
        "question_id": "sk-12",
        "display": "Dvanáctá otázka: **„Co je to FEXT? Jaký útlum FEXT požadujeme?“**",
        "tts": "Dvanáctá otázka: Co je to FEXT? A jaký útlum FEXT požadujeme?"
    },
    {
        "speaker": "Tomáš",
        "question_id": "sk-12",
        "display": "**FEXT (Far-End Crosstalk)** je **přeslech na vzdáleném konci kabelu**. Jde o nežádoucí rušení, kdy signál z jednoho páru ovlivňuje jiný pár a rušení se měří na **opačném konci kabelu**, než kde signál vzniká. A teď pozor na to zvýrazněné pravidlo z vašeho sešitu: **U FEXT požadujeme co nejvyšší hodnotu útlumu v decibelech (dB)**, aby bylo vzájemné rušení mezi páry co nejmenší!",
        "tts": "FEXT, anglicky fár end krostók, je přeslech na vzdáleném konci kabelu. Jde o nežádoucí rušení, kdy signál z jednoho páru ovlivňuje jiný pár a rušení se měří na opačném konci kabelu, než kde signál vzniká. A teď pozor na to zvýrazněné pravidlo z vašeho sešitu: U FEXT požadujeme co nejvyšší hodnotu útlumu v decibelech, aby bylo vzájemné rušení mezi páry co nejmenší!"
    },

    # --- OTÁZKA SK 13: Tři základní subsystémy generické kabeláže + maximální délky (1500m, 500m, 90m + šňůry A, B, E) ---
    {
        "speaker": "Klára",
        "question_id": "sk-13",
        "display": "Třináctá otázka: **„Vyjmenujte tři základní subsystémy generické kabeláže. Jaké jsou maximální délky kabelů metalických a optických?“** Tady máme v sešitě přesná čísla 1500 m, 500 m, 90 m a přídavné šňůry A, B, E!",
        "tts": "Třináctá otázka: Vyjmenujte tři základní subsystémy generické kabeláže. Jaké jsou maximální délky kabelů metalických a optických? Tady máme v sešitě přesná čísla tisíc pět set metrů, pět set metrů, devadesát metrů a přídavné šňůry A, B a E!"
    },
    {
        "speaker": "Tomáš",
        "question_id": "sk-13",
        "display": "Přesně tahle čísla z hodin tam napiš:\n1. **Subsystém páteřní kabeláže areálu**: **optika, maximální délka 1500 m**, spojuje rozvaděč areálu **CD** (*Campus Distributor*) $\\rightarrow$ rozvaděč budovy **BD** (*Building Distributor*).\n2. **Subsystém páteřní kabeláže budovy**: **optika, maximální délka 500 m**, spojuje rozvaděč budovy **BD** $\\rightarrow$ patrový rozvaděč **FD** (*Floor Distributor*).\n3. **Subsystém horizontální kabeláže**: **metalické kabely, maximální délka 90 m**, spojuje patrový rozvaděč **FD** $\\rightarrow$ telekomunikační zásuvku **TO** (případně přes konsolidační bod **CP**).",
        "tts": "Přesně tahle čísla z hodin tam napiš: První je subsystém páteřní kabeláže areálu: to je optika, maximální délka tisíc pět set metrů, spojuje rozvaděč areálu cé-dé a rozvaděč budovy bé-dé. Druhý je subsystém páteřní kabeláže budovy: to je optika, maximální délka pět set metrů, spojuje rozvaděč budovy bé-dé a patrový rozvaděč ef-dé. A třetí je subsystém horizontální kabeláže: to jsou metalické kabely, maximální délka devadesát metrů, spojuje patrový rozvaděč ef-dé a telekomunikační zásuvku té-ó, případně přes konsolidační bod cé-pé."
    },
    {
        "speaker": "Klára",
        "question_id": "sk-13",
        "display": "A navíc k těm 90 metrům horizontální kabeláže existují **přídavné šňůry A, B a E**:\n- **Šňůra A** (na pracovní ploše, zásuvka TO $\\rightarrow$ PC): **max. 5 m**,\n- **Šňůra B** (v rozvaděči FD, panel $\\leftrightarrow$ panel): **max. 10 m** (jen když A a E jsou nulové),\n- **Šňůra E** (v rozvaděči FD, panel $\\rightarrow$ switch): **max. 5 m**.\nA součet přídavných šňůr **$A + B + E \\le 10\\text{ m}$**, takže celý kanál má **$90 + 10 = 100\\text{ m}$**!",
        "tts": "A navíc k těm devadesáti metrům horizontální kabeláže existují přídavné šňůry A, B a E: Šňůra A na pracovní ploše, od zásuvky té-ó k počítači, má maximálně pět metrů. Šňůra B v rozvaděči ef-dé, mezi panelem a panelem, má maximálně deset metrů. A šňůra E v rozvaděči ef-dé, od panelu ke sviči, má maximálně pět metrů. Součet přídavných šňůr A plus B plus E musí být do deseti metrů, takže celý kanál má devadesát plus deset, tedy sto metrů!"
    },

    # --- OTÁZKA SK 14 & 15: Pracovní plocha, počet portů, vlastnosti, patří do GSK? ---
    {
        "speaker": "Tomáš",
        "question_id": "sk-14",
        "display": "Přesně tak! Teď čtrnáctka a patnáctka: **„14. Co je to pracovní plocha? Kolik portů se přiděluje na jednu pracovní plochu? Jejich vlastnosti.“** a **„15. Patří kabely pracovní plochy do generické strukturované kabeláže?“**",
        "tts": "Přesně tak! Teď čtrnáctka a patnáctka: Čtrnáct: Co je to pracovní plocha? Kolik portů se přiděluje na jednu pracovní plochu a jaké mají vlastnosti? A patnáct: Patří kabely pracovní plochy do generické strukturované kabeláže?"
    },
    {
        "speaker": "Klára",
        "question_id": "sk-14",
        "display": "**Pracovní plocha** je prostor, kde uživatelé pracují s koncovými zařízeními (PC, tiskárna, IP kamera). **Začíná telekomunikační zásuvkou (TO)**, zahrnuje propojovací kabel k zařízení (**max. 5 m**) a samotné koncové zařízení. Na **1 pracovní plochu (10 $\\text{m}^2$)** se přidělují **2 zásuvky / porty (nebo 1 dvojzásuvka)** a ty musí odpovídat kategorii kabeláže (Cat 6, 6a atd.).",
        "tts": "Pracovní plocha je prostor, kde uživatelé pracují s koncovými zařízeními, jako je počítač, tiskárna nebo IP kamera. Začíná telekomunikační zásuvkou té-ó, zahrnuje propojovací kabel k zařízení, maximálně pět metrů, a samotné koncové zařízení. Na jednu pracovní plochu o velikosti deset metrů čtverečních se přidělují dvě zásuvky, nebo jedna dvojzásuvka, a ty musí odpovídat kategorii kabeláže, třeba šest nebo šest á."
    },
    {
        "speaker": "Tomáš",
        "question_id": "sk-15",
        "display": "A u patnáctky napiš přesně: **Ne, kabeláž pracovní plochy (přídavné šňůry od zásuvky ke koncovému zařízení) není součástí generické strukturované kabeláže!** Generická SK končí na zásuvce TO, která do SK ještě patří.",
        "tts": "A u patnáctky napiš přesně: Ne, kabeláž pracovní plochy, tedy přídavné šňůry od zásuvky ke koncovému zařízení, není součástí generické strukturované kabeláže! Generická strukturovaná kabeláž končí na zásuvce té-ó, která do ní ještě patří."
    },

    # --- OTÁZKA SK 16: Zapojení konektorů pro zásuvku typu B (T568B) ---
    {
        "speaker": "Klára",
        "question_id": "sk-16",
        "display": "A poslední, šestnáctá otázka: **„Popište zapojení konektorů pro zásuvku typu B.“** V Evropě používáme typ B (T568B), 1 pin = 1 vodič = 1 barva = 1 drátek, a máme skvělou pomůcku: **zelené piny jsou „rozházené“ na pozicích 3 a 6**!",
        "tts": "A poslední, šestnáctá otázka: Popište zapojení konektorů pro zásuvku typu B. V Evropě používáme typ B, jeden pin rovná se jeden vodič, jedna barva, jeden drátek, a máme skvělou pomůcku: zelené piny jsou rozházené na pozicích tři a šest!"
    },
    {
        "speaker": "Tomáš",
        "question_id": "sk-16",
        "display": "Přesně! Ostatní barvy jsou pěkně vedle sebe: oranžová na 1 a 2, modrá na 4 a 5 (pozor, na čtyřce je plná modrá a na pětce bílo-modrá!) a hnědá na 7 a 8. Takže všech 8 pinů **T568B** popořadě:\n- **1 – Bílo-oranžová**\n- **2 – Oranžová**\n- **3 – Bílo-zelená**\n- **4 – Modrá**\n- **5 – Bílo-modrá**\n- **6 – Zelená**\n- **7 – Bílo-hnědá**\n- **8 – Hnědá**.\nA tím máš kompletně hotové všechny otázky na zítřejší test, Kláro! Držím palce!",
        "tts": "Přesně! Ostatní barvy jsou pěkně vedle sebe: oranžová na jedničce a dvojce, modrá na čtyřce a pětce – pozor, na čtyřce je plná modrá a na pětce bílo-modrá! – a hnědá na sedmičce a osmičce. Takže všech osm pinů typu B popořadě: Jedna: bílo-oranžová. Dva: oranžová. Tři: bílo-zelená. Čtyři: modrá. Pět: bílo-modrá. Šest: zelená. Sedm: bílo-hnědá. Osm: hnědá. A tím máš kompletně hotové všechny otázky na zítřejší test, Kláro! Držím palce!"
    }
]


def get_mp3_duration(filepath: str) -> float:
    size = os.path.getsize(filepath)
    return size / 6000.0


async def generate_segment(engine_name: str, index: int, item: dict, cache_dir: str):
    cfg = ENGINES[engine_name][item["speaker"]]
    voice = cfg["voice"]
    rate = cfg["rate"]
    pitch = cfg["pitch"]
    key = hashlib.md5(f"cz_ssml|{voice}|{rate}|{pitch}|{item['tts']}".encode("utf-8")).hexdigest()[:12]
    seg_path = os.path.join(cache_dir, f"{engine_name}_{index:02d}_{key}.mp3")
    if not os.path.exists(seg_path) or os.path.getsize(seg_path) == 0:
        for attempt in range(4):
            try:
                communicate = edge_tts.Communicate(item["tts"], voice, rate=rate, pitch=pitch)
                await communicate.save(seg_path)
                break
            except Exception as e:
                if attempt == 3:
                    raise
                await asyncio.sleep(0.8 * (attempt + 1))
    dur = get_mp3_duration(seg_path)
    return seg_path, dur


async def build_engine_track(engine_name: str, out_dir: str, seg_dir: str):
    print(f"=== Generating track for engine: {engine_name} ({len(SCRIPT)} turns) ===")
    results = [None] * len(SCRIPT)
    batch_size = 4
    for start in range(0, len(SCRIPT), batch_size):
        tasks = []
        for idx in range(start, min(start + batch_size, len(SCRIPT))):
            tasks.append(generate_segment(engine_name, idx, SCRIPT[idx], seg_dir))
        batch_res = await asyncio.gather(*tasks)
        for offset, res in enumerate(batch_res):
            results[start + offset] = res
        print(f"  [{engine_name}] {min(start + batch_size, len(SCRIPT))}/{len(SCRIPT)} done")

    final_mp3 = os.path.join(out_dir, ENGINES[engine_name]["filename"])
    current_time = 0.0
    pause_dur = len(PAUSE_BYTES) / 6000.0
    timeline = []

    with open(final_mp3, "wb") as outfile:
        for idx, (seg_path, dur) in enumerate(results):
            with open(seg_path, "rb") as infile:
                data = infile.read()
                outfile.write(data)
            outfile.write(PAUSE_BYTES)
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
                "duration": round(dur, 2)
            })
            current_time += dur + pause_dur

    return {
        "engine": engine_name,
        "filename": ENGINES[engine_name]["filename"],
        "total_duration": round(current_time, 2),
        "segments": timeline
    }


async def main():
    out_dir = r"k:\podPorn"
    seg_dir = os.path.join(out_dir, "segments_v2")
    os.makedirs(seg_dir, exist_ok=True)

    track_copilot = await build_engine_track("copilot_v2", out_dir, seg_dir)
    track_cz = await build_engine_track("cz_studio", out_dir, seg_dir)

    meta_path = os.path.join(out_dir, "podcast_data.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump({
            "default_engine": "copilot_v2",
            "tracks": {
                "copilot_v2": track_copilot,
                "cz_studio": track_cz
            },
            # Backward compat fields
            "total_duration": track_copilot["total_duration"],
            "segments": track_copilot["segments"]
        }, f, ensure_ascii=False, indent=2)

    print("All tracks generated successfully!")


if __name__ == "__main__":
    asyncio.run(main())

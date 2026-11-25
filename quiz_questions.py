# 99 ABCD otázek pokrývajících všech 9 kapitol (11 otázek na každé téma)
# Každý klíčový pojem, srovnání i zkouškový chyták je procvičen ~3x z různých úhlů.

QUIZ_QUESTIONS = [
    # =========================================================================
    # SAT-1: Orbitální mechanika a Keplerovy zákony (11 otázek)
    # =========================================================================
    {
        "id": 1, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Jaká fyzikální síla v inerciální vztažné soustavě poskytuje potřebnou dostředivou sílu pro udržení družice na kruhové oběžné dráze?",
        "options": [
            "Gravitační působení Země směrem ke středu Země",
            "Odstředivá reakční síla vyvolaná tečnou rychlostí družice",
            "Elektromagnetická interakce mezi ionosférou a tělesem družice",
            "Aerodynamický vztlak zbytkové atmosféry v horní termosféře"
        ],
        "ans": 0,
        "exp": "V inerciální soustavě poskytuje potřebnou dostředivou sílu výhradně gravitační síla Země."
    },
    {
        "id": 2, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Jak je správně chápaný pojem „odstředivá síla“ při popisu pohybu družice?",
        "options": [
            "Zdánlivá setrvačná síla zaváděná pouze v neinerciální soustavě rotující společně s družicí",
            "Skutečná radiální síla vznikající v inerciální soustavě jako reakce na gravitační přitažlivost",
            "Skutečná odpudivá síla vyvolaná magnetickým polem Země a rotací zemského jádra",
            "Korekční síla korekčních trysek, která vyrovnává pokles dráhy vlivem odporu atmosféry"
        ],
        "ans": 0,
        "exp": "Odstředivá síla není další skutečnou mechanickou či gravitační silou – je to jen setrvačná síla v rotující neinerciální soustavě."
    },
    {
        "id": 3, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Jak se změní oběžná rychlost a oběžná doba družice, pokud ji přesuneme na vyšší kruhovou oběžnou dráhu?",
        "options": [
            "Oběžná rychlost klesne a oběžná doba vzroste",
            "Oběžná rychlost vzroste a oběžná doba klesne",
            "Oběžná rychlost klesne, ale oběžná doba zůstane stejná",
            "Oběžná rychlost vzroste a oběžná doba také vzroste"
        ],
        "ans": 0,
        "exp": "Se zvyšujícím se poloměrem dráhy klesá gravitační přitažlivost, takže stačí nižší kruhová rychlost (např. LEO ~7,6 km/s vs. GEO ~3,1 km/s), zatímco dráha je delší a oběžná doba roste."
    },
    {
        "id": 4, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Jak klesá velikost gravitační síly působící na družici se vzdáleností r od středu Země?",
        "options": [
            "Se druhou mocninou vzdálenosti (1 / r²)",
            "Lineárně se vzdáleností od středu (1 / r)",
            "Se třetí mocninou vzdálenosti (1 / r³)",
            "Exponenciálně s nadmořskou výškou nad rovníkem"
        ],
        "ans": 0,
        "exp": "Podle Newtonova gravitačního zákona Fg = μ·m / r² klesá gravitační síla se čtvercem vzdálenosti r."
    },
    {
        "id": 5, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Jaký poměr platí mezi únikovou rychlostí v_esc a kruhovou oběžnou rychlostí v_c ve stejné vzdálenosti od středu Země?",
        "options": [
            "Úniková rychlost je √2-krát větší než kruhová (u povrchu Země cca 11,2 km/s)",
            "Úniková rychlost je přesně 2krát větší než kruhová (u povrchu Země cca 15,8 km/s)",
            "Úniková rychlost je √3-krát větší než kruhová podle třetího Keplerova zákona",
            "Úniková rychlost je rovna kruhové rychlosti zvětšené o rotační rychlost rovníku"
        ],
        "ans": 0,
        "exp": "Platí v_esc = √2 · v_c. U zemského povrchu je úniková rychlost přibližně 11,2 km/s."
    },
    {
        "id": 6, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Co říká První Keplerův zákon pro vázanou oběžnou dráhu družice kolem Země?",
        "options": [
            "Družice opisuje elipsu, v jejímž jednom ohnisku se nachází střed Země (kružnice je speciální případ elipsy)",
            "Družice opisuje elipsu, jejíž geometrický střed přesně splývá s hmotným středem Země",
            "Družice opisuje vždy dokonalou kružnici, pokud není brzděna odporem zbytkové atmosféry",
            "Družice se pohybuje po parabole se Zemí v ohnisku, dokud nepřekročí únikovou rychlost"
        ],
        "ans": 0,
        "exp": "1. Keplerův zákon: vázaná dráha má tvar elipsy (případně kružnice pro e = 0) se Zemí v jednom ohnisku."
    },
    {
        "id": 7, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Jaký je přímý důsledek Druhého Keplerova zákona (zákona ploch) pro rychlost družice na eliptické dráze?",
        "options": [
            "Družice se pohybuje nejrychleji v perigeu (nejblíže Zemi) a nejpomaleji v apogeu (nejdále od Země)",
            "Družice se pohybuje konstantní úhlovou i obvodovou rychlostí v každém bodě své elipsy",
            "Družice letí nejrychleji v apogeu (nejdále od Země) a nejpomaleji v perigeu (nejblíže Zemi)",
            "Družice dosahuje maximální rychlosti přesně při průchodu vzestupným a sestupným uzlem"
        ],
        "ans": 0,
        "exp": "Průvodič opíše za stejný čas stejnou plochu – blíže Zemi (perigeum) musí tedy družice letět rychleji, daleko od Země (apogeum) pomaleji."
    },
    {
        "id": 8, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Co vyjadřuje Třetí Keplerův zákon pro oběžnou dráhu družice?",
        "options": [
            "Druhá mocnina oběžné doby T² je přímo úměrná třetí mocnině hlavní poloosy a³",
            "Třetí mocnina oběžné doby T³ je přímo úměrná druhé mocnině hlavní poloosy a²",
            "Druhá mocnina oběžné doby T² je nepřímo úměrná třetí mocnině výšky apogea",
            "Oběžná doba T roste lineárně s hlavní poloosou a nezávisí na gravitačním parametru μ"
        ],
        "ans": 0,
        "exp": "3. Keplerův zákon: T² = (4π² / μ) · a³, tedy čím větší hlavní poloosa, tím delší oběžná doba."
    },
    {
        "id": 9, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Co se stane s družicí na kruhové dráze, pokud krátce snížíme její tečnou rychlost?",
        "options": [
            "Přejde na eliptickou dráhu s nižším perigeem",
            "Přejde na eliptickou dráhu s vyšším apogeem",
            "Zůstane na stejné kruhové dráze s delší periodou",
            "Okamžitě sestoupí na nižší kruhovou dráhu bez elipsy"
        ],
        "ans": 0,
        "exp": "Snížení tečné rychlosti z kruhové dráhy vede k přechodu na elipsu s nižším perigeem; zvýšení rychlosti pod únikovou naopak zvedá apogeum."
    },
    {
        "id": 10, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Který z následujících jevů NEPATŘÍ mezi hlavní reálné poruchy narušující ideální Keplerovu dráhu družice?",
        "options": [
            "Útlum rádiových vln vodní párou v pásmu 22,23 GHz",
            "Nesférické gravitační pole (zploštění) Země (koeficient J₂)",
            "Odpor zbytkové atmosféry na nízkých oběžných drahách",
            "Gravitační působení Slunce, Měsíce a tlak slunečního záření"
        ],
        "ans": 0,
        "exp": "Útlum vodní párou ovlivňuje rádiový signál, nikoli mechanický pohyb družice. Pohyb narušují zploštění Země (J₂), odpor atmosféry, Slunce/Měsíc a tlak slunečního záření."
    },
    {
        "id": 11, "topic": "sat-1", "topic_label": "1. Orbitální mechanika & Kepler",
        "q": "Kdy přejde těleso v idealizovaném dvoutělesovém modelu na parabolickou únikovou dráhu?",
        "options": [
            "Při dosažení únikové rychlosti (e = 1)",
            "Při překročení únikové rychlosti (e > 1)",
            "Při poklesu pod kruhovou rychlost (e < 1)",
            "Při přechodu na polární dráhu (i = 90°)"
        ],
        "ans": 0,
        "exp": "Při únikové rychlosti je excentricita e = 1 a dráha je parabolická; při vyšší rychlosti je hyperbolická (e > 1)."
    },

    # =========================================================================
    # SAT-2: Orbitální elementy a orientace drah (11 otázek)
    # =========================================================================
    {
        "id": 12, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "Kolik klasických Keplerových orbitálních elementů je potřeba k úplnému určení ideální dráhy a polohy družice na ní v daném čase?",
        "options": [
            "Šest (a, e, i, Ω, ω, ν)",
            "Pět (a, e, i, Ω, ω)",
            "Čtyři (perigeum, apogeum, i, Ω)",
            "Sedm (včetně koeficientu J₂)"
        ],
        "ans": 0,
        "exp": "Klasická sada obsahuje 6 prvků: hlavní poloosu a, excentricitu e, inklinaci i, RAAN Ω, argument perigea ω a pravou (příp. střední) anomálii ν."
    },
    {
        "id": 13, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "Která dvojice Keplerových elementů určuje čistě VELIKOST a TVAR oběžné dráhy?",
        "options": [
            "Hlavní poloosa (a) a excentricita (e)",
            "Inklinace (i) a rektascenze vzestupného uzlu (Ω)",
            "Argument perigea (ω) a pravá anomálie (ν)",
            "Hlavní poloosa (a) a argument perigea (ω)"
        ],
        "ans": 0,
        "exp": "Hlavní poloosa a udává velikost dráhy, excentricita e určuje její tvar (e = 0 kružnice, 0 < e < 1 elipsa)."
    },
    {
        "id": 14, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "Co přesně vyjadřuje rektascenze vzestupného uzlu (RAAN, Ω)?",
        "options": [
            "Natočení celé roviny oběžné dráhy kolem rotační osy Země (úhel v rovníkové rovině od jarního bodu ke vzestupnému uzlu)",
            "Úhel sklonu roviny oběžné dráhy vůči rovině zemského rovníku měřený ve vzestupném uzlu směrem na sever",
            "Úhel v rovině oběžné dráhy měřený od směru vzestupného uzlu ke směru perigea ve směru pohybu družice",
            "Okamžitou polohu družice na elipse měřenou v rovině dráhy od směru perigea k aktuálnímu průvodiči"
        ],
        "ans": 0,
        "exp": "RAAN (Ω) popisuje prostorové natočení celé roviny dráhy kolem osy Země; vzestupný uzel je bod, kde družice přelétá rovník z jihu na sever."
    },
    {
        "id": 15, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "Jaký je rozdíl mezi rektascenzí vzestupného uzlu (Ω) a argumentem perigea (ω)?",
        "options": [
            "Ω určuje natočení celé roviny dráhy v prostoru, zatímco ω určuje orientaci elipsy (polohu perigea) uvnitř této roviny",
            "Ω určuje sklon roviny dráhy vůči rovníku, zatímco ω udává okamžitou úhlovou vzdálenost družice od perigea",
            "Ω definuje tvar a velikost eliptické dráhy, zatímco ω určuje natočení její roviny kolem zemské osy",
            "Ω se používá pouze pro retrográdní dráhy s inklinací nad 90° a ω výhradně pro prográdní dráhy"
        ],
        "ans": 0,
        "exp": "Ω natáčí celou rovinu dráhy kolem Země; ω natáčí elipsu uvnitř již zadané roviny (od vzestupného uzlu k perigeu)."
    },
    {
        "id": 16, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "Který orbitální element udává okamžitou polohu družice na její oběžné dráze v daném čase?",
        "options": [
            "Pravá anomálie ν (případně střední anomálie M k referenční epoše)",
            "Argument perigea ω (úhel mezi vzestupným uzlem a bodem perigea)",
            "Rektascenze vzestupného uzlu Ω (orientace roviny dráhy vůči jarnímu bodu)",
            "Excentricita e společně s hlavní poloosou a (parametry tvaru elipsy)"
        ],
        "ans": 0,
        "exp": "Pravá anomálie ν je úhel mezi směrem perigea a aktuálním průvodičem družice."
    },
    {
        "id": 17, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "CHYTÁK: U kterého typu dráhy NENÍ jednoznačně definován argument perigea (ω)?",
        "options": [
            "U přesně kruhové dráhy (e = 0), protože všechny body mají stejnou vzdálenost od středu Země",
            "U rovníkové eliptické dráhy (i = 0°, e > 0), protože rovina dráhy splývá s rovníkem",
            "U vysoce eliptické dráhy Molnija (i ≈ 63,4°), protože apogeum leží vysoko nad severní polokoulí",
            "U slunečně synchronní dráhy SSO (i ≈ 98°), protože její rovina precesuje kolem osy Země"
        ],
        "ans": 0,
        "exp": "Na přesně kruhové dráze (e = 0) neexistuje jediné perigeum, takže argument perigea ω není jednoznačně definován (podobně u rovníkové dráhy i = 0° není definován vzestupný uzel Ω)."
    },
    {
        "id": 18, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "Jak dělíme šikmé oběžné dráhy podle inklinace i vzhledem k směru rotace Země?",
        "options": [
            "Prográdní (0° < i < 90°, po směru rotace Země) a retrográdní (90° < i < 180°, proti směru rotace Země)",
            "Prográdní (90° < i < 180°, proti rotaci Země) a retrográdní (0° < i < 90°, po směru rotace Země)",
            "Polární (0° < i < 45°, kolem rovníku) a rovníkové (45° < i < 90°, nad zemskými póly)",
            "Geosynchronní (0° < i < 90°, s periodou 24 h) a heliosynchronní (90° < i < 180°, s periodou 12 h)"
        ],
        "ans": 0,
        "exp": "Prográdní dráhy mají i < 90° (letí ve smyslu rotace Země), retrográdní mají i > 90° (proti rotaci Země)."
    },
    {
        "id": 19, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "Která vlastnost je charakteristická pro polární oběžnou dráhu (i ≈ 90°)?",
        "options": [
            "Družice přelétá nad oblastmi severního a jižního pólu a díky rotaci Země postupně snímá téměř celý zemský povrch",
            "Družice se pohybuje v rovině rovníku a z pohledu pozemního pozorovatele zůstává nad jedním poledníkem",
            "Družice opisuje na obloze symetrickou osmičku (analemu) pouze nad severní polokoulí bez přeletu nad jižním pólem",
            "Družice má nulovou radiální rychlost vůči všem pozemním stanicím, takže nedochází k Dopplerovu posuvu"
        ],
        "ans": 0,
        "exp": "Polární dráhy (i ≈ 90°) procházejí nad oběma póly a při rotaci Země pod nimi pokrývají postupně celou planetu (meteo, SAR, průzkum)."
    },
    {
        "id": 20, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "Proč je slunečně synchronní dráha (SSO) tak ceněná pro optické snímkování Země?",
        "options": [
            "Družice přelétá nad danou oblastí přibližně ve stejný místní sluneční čas, takže pořízené snímky z různých dnů mají srovnatelné světelné podmínky",
            "Družice letí v rovníkové rovině přesně v zákrytu se Sluncem, takže může snímat stejný bod planety nepřetržitě 24 hodin denně",
            "Družice se pohybuje ve výšce 35 786 km nad terminátorem, čímž zcela eliminuje atmosférický útlum i stíny oblačnosti",
            "Družice mění svou výšku mezi 500 a 900 km tak, aby vždy letěla pouze nad neosvětlenou noční stranou zemského povrchu"
        ],
        "ans": 0,
        "exp": "SSO udržuje přibližně konstantní úhel roviny dráhy vůči Slunci (precese ~+0,9856°/den), takže odpovídající přelety probíhají ve stejnou místní sluneční hodinu."
    },
    {
        "id": 21, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "Jaký fyzikální jev využívá slunečně synchronní dráha (SSO) k tomu, aby se její rovina stáčela o cca +0,9856°/den, a jakou mívá inklinaci?",
        "options": [
            "Zploštění Země (koeficient J₂) způsobující precesi uzlů; dráha je téměř polární a lehce retrográdní (i ≈ 97°–99°)",
            "Odpor zbytkové atmosféry na LEO; dráha je téměř polární a lehce prográdní (i ≈ 81°–83°)",
            "Gravitační poruchy Slunce a Měsíce; dráha má kritický sklon přesně i ≈ 63,4° bez precese perigea",
            "Tlak slunečního záření na panely; dráha je rovníková s nulovou inklinací (i = 0°) ve výšce 500–900 km"
        ],
        "ans": 0,
        "exp": "Precesi orbitální roviny zajišťuje zploštění Země (J₂). Pro správný směr precese musí být SSO mírně retrográdní (typicky i ≈ 97°–99°, výška 500–900 km)."
    },
    {
        "id": 22, "topic": "sat-2", "topic_label": "2. Elementy & Orientace drah",
        "q": "Pokud má družice inklinaci i = 55°, v jakém rozsahu zeměpisných šířek se pohybuje její poddružicový bod (subsatellite point)?",
        "options": [
            "Přibližně mezi −55° a +55° zeměpisné šířky (ovšem rádiově může být viditelná i z vyšších šířek)",
            "Pouze mezi 0° a +55° severní šířky, protože vzestupný uzel leží vždy na nultém poledníku",
            "Od −90° do +90° zeměpisné šířky včetně obou pólů díky postupné rotaci Země pod dráhou",
            "Pouze mezi +35° a +90° zeměpisné šířky (doplněk inklinace k pravému úhlu 90°)"
        ],
        "ans": 0,
        "exp": "Maximální absolutní šířka poddružicového bodu je min(i, 180° − i), zde tedy ±55°. Rádiová viditelnost však sahá i o něco dál podle výšky a elevace."
    },

    # =========================================================================
    # SAT-3: LEO, MEO, GEO a speciální dráhy GSO, Molnija, Tundra (11 otázek)
    # =========================================================================
    {
        "id": 23, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Jaké přibližné výškové pásmo a oběžná doba jsou typické pro nízkou oběžnou dráhu LEO?",
        "options": [
            "Výška cca 160 až 2 000 km, oběžná doba cca 90 až 130 minut",
            "Výška cca 2 000 až 10 000 km, oběžná doba cca 4 až 6 hodin",
            "Výška cca 20 200 km, oběžná doba přesně 12 hodin",
            "Výška 35 786 km, oběžná doba 23 hodin 56 minut"
        ],
        "ans": 0,
        "exp": "LEO pokrývá přibližně 160–2 000 km nad Zemí, rychlost ~6,9–7,8 km/s a oběžná doba ~88–127 min."
    },
    {
        "id": 24, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Proč musí komunikační systémy na dráze LEO (jako Starlink nebo OneWeb) využívat stovky až tisíce družic?",
        "options": [
            "Každá LEO družice má malý footprint (na 500 km jen ~3,6 % povrchu Země) a velmi rychle přelétá za horizont, takže pro nepřetržité pokrytí je nutné neustálé předávání spojení v husté konstelaci",
            "Protože v pásmech Ku a Ka na dráze LEO dochází k tak silnému útlumu FSPL (přes 190 dB), že signál jedné družice nedosáhne dále než na vzdálenost 100 km od poddružicového bodu",
            "Protože zbytková atmosféra na dráze LEO omezuje životnost každé družice na několik týdnů a většina družic v konstelaci slouží pouze jako pasivní záloha na oběžné dráze",
            "Protože každá LEO družice má oběžnou dobu 24 hodin a z pohledu pozemního terminálu pokrývá vždy jen úzký pruh kolem rovníku o šířce několika kilometrů"
        ],
        "ans": 0,
        "exp": "Malá výška LEO znamená malé pokrytí jedné družice a krátkou dobu viditelnosti (~několik minut), proto je nutná rozsáhlá konstelace."
    },
    {
        "id": 25, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Která z následujících skupin systémů je typickým zástupcem střední oběžné dráhy MEO (2 000–35 786 km)?",
        "options": [
            "Navigační systémy GNSS (GPS 20 200 km, Galileo 23 222 km, GLONASS 19 100 km) a komunikační síť O3b (~8 000 km)",
            "Nízkoletící širokopásmové konstelace SpaceX Starlink (550 km), Eutelsat OneWeb (1 200 km) a Iridium (780 km)",
            "Geostacionární televizní a datové družice Astra, Eutelsat Hot Bird a Inmarsat ve výšce 35 786 km",
            "Vysoce eliptické dráhy Molnija (12h perioda) a slunečně synchronní meteorologické družice (500–900 km)"
        ],
        "ans": 0,
        "exp": "MEO je doménou globálních navigací GNSS a středněorbitální datové sítě SES O3b."
    },
    {
        "id": 26, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Které specifické kosmické riziko ovlivňuje družice na střední oběžné dráze MEO více než na nízkých drahách pod 1 000 km?",
        "options": [
            "Vyšší radiační zátěž ve Van Allenových radiačních pásech",
            "Výrazně silnější aerodynamický odpor zbytkové atmosféry",
            "Častější precese roviny dráhy vyvolaná koeficientem J₂",
            "Extrémně vysoký Dopplerův posuv v řádu stovek kHz v Ka pásmu"
        ],
        "ans": 0,
        "exp": "V oblastech MEO procházejí dráhy Van Allenovými radiačními pásy, což klade nároky na radiační odolnost elektroniky."
    },
    {
        "id": 27, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Jaká sada podmínek musí platit současně, aby se družice nacházela na geostacionární dráze (GEO)?",
        "options": [
            "Kruhová dráha (e = 0), nulová inklinace (i = 0° nad rovníkem), prográdní směr a perioda rovna siderickému dni (23 h 56 min 4 s)",
            "Eliptická dráha (e = 0,74), kritická inklinace (i = 63,4° nad rovníkem), prográdní směr a oběžná perioda přesně 12 hodin",
            "Kruhová dráha (e = 0), polární inklinace (i = 90° přes oba póly), retrográdní směr a oběžná perioda rovna slunečnímu dni (24 h 00 min)",
            "Jakákoli eliptická či kruhová dráha ve výšce 35 786 km se siderickou periodou 23 h 56 min 4 s bez ohledu na inklinaci i"
        ],
        "ans": 0,
        "exp": "Všechny 4 podmínky jsou nutné: kruhová (e=0), rovníková (i=0°), prográdní a siderická perioda 23 h 56 min 4 s (~výška 35 786 km)."
    },
    {
        "id": 28, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Jaký je hlavní rozdíl mezi geostacionární (GEO) a obecnou geosynchronní (GSO) dráhou?",
        "options": [
            "Obě mají periodu ~23 h 56 min, ale GSO může být skloněná (i > 0°) nebo eliptická (e > 0), takže družice na obloze opisuje osmičku (analemu), zatímco GEO stojí v jednom bodě",
            "GEO má siderickou periodu 23 h 56 min nad rovníkem, zatímco GSO má přesně 12hodinovou periodu ve výšce 20 200 km a přelétá každé místo dvakrát denně",
            "GSO je nízkoletící dráha ve výšce 500–900 km synchronizovaná se Sluncem (SSO), zatímco GEO leží výhradně ve výšce 35 786 km nad rovníkem",
            "GEO umožňuje používat pouze úzké spot-beamy HTS družic, zatímco GSO označuje výhradně širokopásmové konstelace s laserovými spoji ISL"
        ],
        "ans": 0,
        "exp": "GEO je speciální případ GSO pro i = 0° a e = 0. Jakmile má GSO nenulový sklon nebo excentricitu, na obloze se pohybuje po analemě (osmičce)."
    },
    {
        "id": 29, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Kolik procent zemského povrchu může být v ideálním geometrickém modelu (elevace 0°) viditelné z jedné geostacionární družice GEO, a kolik GEO družic zhruba stačí pro většinu obydlené planety?",
        "options": [
            "Až ~42 % povrchu z jedné družice; 3 vhodně rozmístěné družice pokryjí většinu Země mimo polární oblasti",
            "Asi 18 % povrchu z jedné družice; pro pokrytí planety mimo póly je potřeba minimálně 6 až 8 družic",
            "Přesně 50 % povrchu z jedné družice; 2 protilehlé družice tak spolehlivě pokryjí 100 % povrchu včetně pólů",
            "Asi 3,6 % povrchu z jedné družice; pro nepřetržité pokrytí planety je nutné nasadit stovky družic"
        ],
        "ans": 0,
        "exp": "Z výšky 35 786 km je geometrická viditelnost ~42,4 % povrchu Země. Tři družice pokryjí většinu planety (kromě polárních oblastí)."
    },
    {
        "id": 30, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Proč byly vyvinuty vysoce eliptické dráhy typu Molnija a Tundra?",
        "options": [
            "Pro kvalitní pokrytí vysokých zeměpisných šířek (Arktida, sever Ruska, Kanada, Skandinávie), kde mají GEO družice příliš nízký elevační úhel",
            "Pro snížení obousměrné latence (RTT) pod 25 ms v rovníkových oblastech při zachování pevných nepřenosných parabolických antén",
            "Pro optické snímkování zemského povrchu ve stejný místní sluneční čas pomocí precese roviny dráhy vyvolané koeficientem J₂",
            "Pro minimalizaci radiační zátěže ve Van Allenových pásech u navigačních systémů GNSS typu GPS a Galileo"
        ],
        "ans": 0,
        "exp": "GEO družice mají nad 60°–70° šířky velmi nízkou elevaci. Molnija a Tundra umístí apogeum vysoko nad severní polokouli, takže nad ní družice tráví většinu času."
    },
    {
        "id": 31, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Jak se liší parametry dráhy Molnija od dráhy Tundra (obě mají typický sklon i ≈ 63,4°)?",
        "options": [
            "Molnija má oběžnou dobu ~12 h a vysokou excentricitu (~0,7–0,75), zatímco Tundra má 24hodinovou geosynchronní dobu (~23 h 56 min) a obvykle nižší excentricitu (~0,2–0,4)",
            "Molnija je rovníková kruhová dráha (i = 0°, e = 0) ve výšce 35 786 km, zatímco Tundra je polární dráha (i = 90°) ve výšce 1 200 km s oběžnou dobou 110 minut",
            "Molnija má 24hodinovou geosynchronní periodu s nižší excentricitou (~0,2–0,4), zatímco Tundra oběhne Zemi za ~12 hodin s vysokou excentricitou (~0,7–0,75)",
            "Molnija i Tundra jsou obě dokonale kruhové dráhy (e = 0) na hranici MEO a liší se pouze tím, zda obíhají prográdně nebo retrográdně"
        ],
        "ans": 0,
        "exp": "Molnija = 12h vysoce eliptická dráha (viditelnost > 8 h v apogeu); Tundra = 24h geosynchronní eliptická dráha (viditelnost 12–16 h, quasi-geostacionární)."
    },
    {
        "id": 32, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Proč se družice na drahách Molnija a Tundra udrží tak dlouho nad sledovanou severní oblastí?",
        "options": [
            "V okolí apogea (nejdále od Země) se podle 2. Keplerova zákona pohybují nejpomaleji, takže tam tráví většinu své oběžné doby",
            "V okolí perigea (nejblíže Zemi) se podle 2. Keplerova zákona pohybují nejpomaleji a apogeum proletí během několika minut",
            "V okolí apogea dosahují únikové rychlosti 11,2 km/s a krátkodobě tak vyrovnávají rotační rychlost zemského povrchu",
            "Protože jejich rovina dráhy precesuje vlivem zploštění Země přesně o 0,9856° za den proti směru rotace Země"
        ],
        "ans": 0,
        "exp": "Z 2. Keplerova zákona plyne nejpomalejší pohyb v apogeu – nad severní polokoulí tak družice „visí“ 8+ hodin (Molnija) či 12–16 hodin (Tundra)."
    },
    {
        "id": 33, "topic": "sat-3", "topic_label": "3. LEO, MEO, GEO & Speciální dráhy",
        "q": "Co je největší uživatelská výhoda GEO družice pro pozemní terminál oproti LEO a MEO?",
        "options": [
            "Stálá poloha na obloze umožňuje použít jednoduchou pevně nasměrovanou anténu bez průběžného sledování pohybu družice",
            "Výrazně nižší útlum volného prostoru (FSPL) umožňuje vysílat s mnohem nižším výkonem než u LEO terminálů",
            "Minimální obousměrné zpoždění (RTT pod 50 ms) vhodné pro vysoce interaktivní hlasové a herní aplikace",
            "Vysoký elevační úhel nad oběma zeměpisnými póly zaručující spolehlivé spojení i v arktických oblastech"
        ],
        "ans": 0,
        "exp": "Díky zdánlivě nehybné poloze GEO družice stačí pevná anténa (např. satelitní parabola na domě či pevný VSAT)."
    },

    # =========================================================================
    # SAT-4: Vliv dráhy na rádiový spoj (Footprint, Latence, Doppler, FSPL) (11 otázek)
    # =========================================================================
    {
        "id": 34, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "Jaký je rozdíl mezi geometrickou oblastí viditelnosti družice a skutečným footprintem (stopou pokrytí)?",
        "options": [
            "Geometrická viditelnost znamená jen přímý výhled nad obzor (0° elevace), kdežto skutečný footprint je menší a závisí na minimálním elevačním úhlu, směrovém diagramu antén a výkonové bilanci spoje",
            "Skutečný footprint je vždy větší než geometrická viditelnost, protože refrakce v troposféře ohýbá rádiové vlny v pásmech Ku a Ka hluboko za geometrický horizont",
            "Geometrická viditelnost platí pouze pro nízkoletící družice LEO a MEO, zatímco pojem footprint se používá výhradně pro celosvětové pokrytí tří geostacionárních družic",
            "Oba pojmy vyjadřují totožnou kruhovou oblast na povrchu Země vymezenou čistě výškou družice nad rovníkem bez vlivu anténního svazku či elevace"
        ],
        "ans": 0,
        "exp": "Praktická služba vyžaduje nenulovou minimální elevaci (aby se omezilo stínění a průchod atmosférou) a dostatečný výkon anténního svazku."
    },
    {
        "id": 35, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "Jaké je přibližné jednosměrné zpoždění šíření signálu pro jeden úsek Země → GEO družice (35 786 km) a jaká je reálná obousměrná síťová latence (RTT)?",
        "options": [
            "Jeden úsek ~119 ms; spojení A→GEO→B ~239 ms; minimální fyzikální RTT ~478 ms a reálné síťové RTT typicky 500–650 ms",
            "Jeden úsek ~25 ms; spojení A→GEO→B ~50 ms; minimální fyzikální RTT ~100 ms a reálné síťové RTT typicky 120–150 ms",
            "Jeden úsek ~60 ms; spojení A→GEO→B ~120 ms; minimální fyzikální RTT ~240 ms a reálné síťové RTT typicky 250–300 ms",
            "Jeden úsek ~239 ms; spojení A→GEO→B ~478 ms; minimální fyzikální RTT ~956 ms a reálné síťové RTT přes 1 100 ms"
        ],
        "ans": 0,
        "exp": "Ze 35 786 km / c plyne ~119,4 ms na jeden skok, ~238,7 ms jednosměrně A→GEO→B, ~477,5 ms min. RTT a 500–650 ms v reálném provozu."
    },
    {
        "id": 36, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "Seřaďte správně typy oběžných drah od NEJNIŽŠÍ po NEJVYŠŠÍ typickou obousměrnou latenci (RTT):",
        "options": [
            "LEO (20–100 ms) < MEO (50–150 ms) < GEO (500–650 ms)",
            "MEO (20–100 ms) < LEO (50–150 ms) < GEO (500–650 ms)",
            "LEO (20–100 ms) < GEO (150–250 ms) < MEO (500–650 ms)",
            "GEO (20–100 ms) < MEO (150–300 ms) < LEO (500–650 ms)"
        ],
        "ans": 0,
        "exp": "Latence roste se vzdáleností: Starlink (LEO) ~25–50 ms, OneWeb (LEO) ~100 ms, O3b (MEO) ~150 ms, GEO ~500–650 ms."
    },
    {
        "id": 37, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "Co způsobuje Dopplerův frekvenční posuv v družicové komunikaci a jak se projevuje při přibližování družice?",
        "options": [
            "Způsobuje ho radiální složka relativní rychlosti mezi družicí a terminálem; při přibližování přijímaná frekvence roste (kladný posuv)",
            "Způsobuje ho radiální složka relativní rychlosti mezi družicí a terminálem; při přibližování přijímaná frekvence klesá (záporný posuv)",
            "Způsobuje ho výhradně tečná rychlost družice kolmá na spojnici s terminálem; při přibližování se frekvence nemění",
            "Způsobuje ho průchod signálu ionosférou a troposférou (zejména v dešti); posuv roste se snižující se frekvencí nosné"
        ],
        "ans": 0,
        "exp": "Dopplerův jev je dán časovou změnou vzdálenosti (radiální rychlostí v_r). Přibližování frekvenci zvyšuje, vzdalování snižuje."
    },
    {
        "id": 38, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "U které oběžné dráhy je Dopplerův posuv pro pevný pozemní terminál NEJVÝRAZNĚJŠÍ (desítky až stovky kHz v pásmech Ku/Ka) a u které je ZANEDBATELNÝ?",
        "options": [
            "Nejvýraznější u rychlých LEO družic (nutná průběžná kompenzace); zanedbatelný až nulový u ideální GEO družice",
            "Nejvýraznější u vysokých GEO družic (vzdálenost 35 786 km); zanedbatelný u LEO družic díky krátké době přeletu",
            "Nejvýraznější na střední dráze MEO ve Van Allenových pásech; zcela nulový u všech vysoce eliptických drah Molnija",
            "Stejně výrazný u LEO, MEO i GEO drah, protože všechny družice se pohybují vůči Slunci podobnou úhlovou rychlostí"
        ],
        "ans": 0,
        "exp": "LEO družice letí ~7–8 km/s a rychle mění úhel i radiální rychlost (v Ku/Ka až stovky kHz posuvu). Ideální GEO vůči pevnému terminálu stojí (nulová v_r)."
    },
    {
        "id": 39, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "Na čem závisí útlum ve volném prostoru FSPL (Free-Space Path Loss) v modelu volného prostoru?",
        "options": [
            "Roste se čtvercem vzdálenosti d² a se čtvercem pracovní frekvence f² (v dB roste s 20·log₁₀)",
            "Roste lineárně se vzdáleností d a nepřímo úměrně s druhou mocninou pracovní frekvence f²",
            "Roste se čtvercem vzdálenosti d², ale s rostoucí pracovní frekvencí f klesá díky užšímu svazku",
            "Závisí výhradně na vzdálenosti d a obsahu vodní páry v atmosféře, nikoli na pracovní frekvenci"
        ],
        "ans": 0,
        "exp": "L_FS = (4πd / λ)² = (4πdf / c)², tedy útlum roste kvadraticky se vzdáleností d i frekvencí f."
    },
    {
        "id": 40, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "Jaký je přibližný rozdíl v útlumu volného prostoru (FSPL) na stejné frekvenci 2 GHz mezi družicí LEO (550 km) a družicí GEO (35 786 km)?",
        "options": [
            "Přibližně 36 dB ve prospěch LEO (cca 4 200násobný rozdíl lineárního činitele útlumu)",
            "Přibližně 12 dB ve prospěch LEO (cca 16násobný rozdíl lineárního činitele útlumu)",
            "Přibližně 36 dB ve prospěch GEO, protože signál na vyšší dráze méně rozptyluje atmosféra",
            "Přibližně 6 dB ve prospěch LEO, protože vzdálenost GEO je zhruba dvojnásobkem MEO"
        ],
        "ans": 0,
        "exp": "Dle tabulky ze skript na 2 GHz: LEO (550 km) ~153,3 dB, MEO (20 200 km) ~184,6 dB, GEO (35 786 km) ~189,5 dB → rozdíl LEO vs. GEO ~36,3 dB."
    },
    {
        "id": 41, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "Proč vysoká frekvence (např. pásmo Ka) nemusí v celkové výkonové bilanci vždy prohrát s nižší frekvencí, přestože má vyšší FSPL?",
        "options": [
            "Protože při stejných fyzických rozměrech antény dosahuje vyšší frekvence většího anténního zisku a navíc poskytuje širší dostupné přenosové pásmo",
            "Protože v pásmu Ka (27–40 GHz) klesá útlum deštěm i atmosférickou vodní párou na zanedbatelnou hodnotu oproti pásmům C a Ku",
            "Protože vyšší frekvence nevyžaduje u parabolických ani plošných antén přesné směrování a je imunní vůči Dopplerovu posuvu",
            "Protože u vysokých frekvencí se uplatňuje ionosférický odraz, který v celkové výkonové bilanci snižuje efektivní vzdálenost k GEO"
        ],
        "ans": 0,
        "exp": "Zisk parabolické antény roste s f², takže při stejné velikosti antény vyšší zisk kompenzuje vyšší FSPL; daň za Ka pásmo je ale větší citlivost na déšť."
    },
    {
        "id": 42, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "Jaký praktický dopad má nižší útlum volného prostoru a kratší vzdálenost u LEO systémů na uživatelské terminály?",
        "options": [
            "Umožňuje použít menší, kompaktní antény (flat panely) a nižší vysílací výkony při dosažení vysokých datových rychlostí",
            "Vyžaduje použití rozměrných pevných parabol o průměru nejméně 2,4 m bez možnosti elektronického směrování svazku",
            "Umožňuje provozovat terminály zcela bez vysílače, pouze s pasivním odrazem signálu od centrálního VSAT HUBu",
            "Zvyšuje obousměrnou latenci (RTT) nad 500 ms výměnou za nižší spotřebu energie v RF jednotce terminálu"
        ],
        "ans": 0,
        "exp": "Příznivější výkonová bilance na LEO umožňuje kompaktní uživatelské terminály (např. Starlink Mini/Standard)."
    },
    {
        "id": 43, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "Proč mají geostacionární družice horší kvalitu spojení ve vysokých zeměpisných šířkách (blízko polárních oblastí)?",
        "options": [
            "Družice je nízko nad obzorem (nízký elevační úhel), signál prochází delší vrstvou atmosféry a snadno jej stíní terén či budovy",
            "Družice nad rovníkem má vůči polárním oblastem extrémní radiální rychlost, což vyvolává Dopplerův posuv v řádu stovek kHz",
            "Vysoké zeměpisné šířky leží mimo gravitační dosah geostacionárních družic, takže antény musí mít trojnásobný průměr",
            "Zemská ionosféra nad 60° šířky zcela pohlcuje pásma Ku a Ka a propouští výhradně laserové spoje na 1 550 nm"
        ],
        "ans": 0,
        "exp": "Nízký elevační úhel znamená delší průchod atmosférou (vyšší útlum a scintilace) a vysoké riziko zastínění překážkami."
    },
    {
        "id": 44, "topic": "sat-4", "topic_label": "4. Spoj: Footprint, Latence, Doppler, FSPL",
        "q": "Jak ovlivňuje typ oběžné dráhy řízení spojení u pozemního terminálu při přechodu z GEO na LEO?",
        "options": [
            "Pevné nasměrování antény již nestačí – terminál musí elektronicky nebo mechanicky sledovat pohybující se družice a provádět časté předávání spojení (handover)",
            "Terminál na LEO nepotřebuje sledovat pohyb družice, stačí jej nastavit pevně do zenitu a využít všesměrový svazek bez handoveru",
            "Předávání spojení (handover) je nutné pouze u geostacionárních družic kvůli jejich dennímu pohybu po analemě na obloze",
            "Při přechodu na LEO lze zachovat původní pevnou GEO parabolu bez úprav, pouze se sníží vysílací výkon modemu"
        ],
        "ans": 0,
        "exp": "LEO družice rychle přelétají po obloze (~95 min oběh), proto je nutné sledování svazkem (phased array / flat panel) a handover mezi družicemi."
    },

    # =========================================================================
    # SAT-5: Satelitní konstelace (Walker Delta & Star), Spolehlivost, ISL (11 otázek)
    # =========================================================================
    {
        "id": 45, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "Co znamená zápis konstelace Walker Delta ve tvaru i : T / P / F (např. Galileo 56° : 24 / 6 / 1)?",
        "options": [
            "i = inklinace (56°), T = celkový počet družic (24), P = počet orbitálních rovin (6), F = fázový index (1)",
            "i = inklinace (56°), T = oběžná doba v hodinách (24), P = počet družic v rovině (6), F = frekvenční pásmo (1)",
            "i = index precese (56°), T = celkový počet rovin (24), P = počet pozemních bran (6), F = faktor útlumu (1)",
            "i = inklinace (56°), T = celkový počet družic (24), P = perigeum v tisících km (6), F = počet spot-beamů (1)"
        ],
        "ans": 0,
        "exp": "U zápisu i : T/P/F znamená T celkový počet družic, P počet orbitálních rovin (v každé je pak T/P družic) a F fázový posun mezi rovinami."
    },
    {
        "id": 46, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "Kolik družic je v jedné orbitální rovině a jaký je úhlový rozestup rovin u konstelace Walker Delta 56° : 24 / 6 / 1?",
        "options": [
            "4 družice v každé rovině (24 / 6) a rozestup rovin 60° (360° / 6)",
            "6 družic v každé rovině (24 / 4) a rozestup rovin 30° (180° / 6)",
            "4 družice v každé rovině (24 / 6) a rozestup rovin 30° (180° / 6)",
            "6 družic v každé rovině a rozestup rovin 90° kolem rovníku"
        ],
        "ans": 0,
        "exp": "S = T / P = 24 / 6 = 4 družice v rovině. U Walker Delta jsou roviny rozmístěny po 360°, takže ΔΩ = 360° / 6 = 60°."
    },
    {
        "id": 47, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "Jaký je hlavní geometrický rozdíl mezi konstelací Walker Delta a konstelací Walker Star?",
        "options": [
            "Walker Delta rozmisťuje roviny po 360° (typicky šikmé dráhy např. pro GNSS), kdežto Walker Star používá téměř polární dráhy rozložené v rozsahu 180° pro pokrytí včetně pólů",
            "Walker Star rozmisťuje šikmé roviny po 360° nad rovníkem, kdežto Walker Delta používá výhradně polární dráhy rozložené v rozsahu 180° bez pokrytí rovníku",
            "Walker Delta umisťuje všechny družice na jedinou geostacionární kružnici ve výšce 35 786 km, zatímco Walker Star využívá eliptické dráhy Molnija",
            "Walker Star označuje konstelace bez mezisatelitních spojů ISL, zatímco Walker Delta je název výhradně pro sítě s laserovými spoji na 1 550 nm"
        ],
        "ans": 0,
        "exp": "Walker Delta = roviny po 360° (Galileo); Walker Star = téměř polární roviny rozložené po 180° (např. Iridium)."
    },
    {
        "id": 48, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "Který známý komunikační systém využívá téměř polární konstelaci typu Walker Star se 66 provozními družicemi v 6 orbitálních rovinách (780 km)?",
        "options": [
            "Iridium (globální mobilní komunikace včetně polárních oblastí)",
            "SES O3b mPOWER (středněorbitální MEO datová síť v ±50° šířky)",
            "Eutelsat OneWeb (1200km konstelace se 652 družicemi v Ku/Ka)",
            "Galileo (evropský navigační systém na MEO v konstelaci Delta)"
        ],
        "ans": 0,
        "exp": "Iridium má 66 družic (6 rovin × 11 družic) ve výšce ~780 km a inklinaci ~86,4° (Walker Star)."
    },
    {
        "id": 49, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "Jakou provozní zvláštnost musí řešit konstelace Walker Star v blízkosti severního a jižního pólu?",
        "options": [
            "Téměř polární orbitální roviny se u pólů geometricky sbližují a kříží, což komplikuje řízení některých mezisatelitních spojů a předávání provozu",
            "U pólů dochází ke změně směru gravitace a družice musí provádět korekční zážehy proti přitažlivosti Měsíce",
            "Nad 80° zeměpisné šířky klesá hustota pokrytí natolik, že signál nedosáhne na zem a musí se přepínat na GEO",
            "Roviny dráhy se u pólů od sebe maximálně vzdalují, čímž se prodlužuje vzdálenost pro ISL nad dosah laseru"
        ],
        "ans": 0,
        "exp": "Poledníkové (téměř polární) dráhy se sbíhají u pólů, což mění vzájemné úhlové rychlosti pro ISL."
    },
    {
        "id": 50, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "Pokud má jedna družice pravděpodobnost provozuschopnosti p = 0,9 a v daném místě je nezávisle dostupných N = 5 redundantních družic, jak se vypočítá pravděpodobnost, že alespoň jedna funguje?",
        "options": [
            "P = 1 − (1 − p)ᴺ = 1 − (0,1)⁵ = 0,99999 (99,999 %)",
            "P = pᴺ = (0,9)⁵ = 0,59049 (59,049 %)",
            "P = 1 − pᴺ = 1 − (0,9)⁵ = 0,40951 (40,951 %)",
            "P = (1 − p)ᴺ = (0,1)⁵ = 0,00001 (0,001 %)"
        ],
        "ans": 0,
        "exp": "Aby systém selhal, musí selhat všechny N nezávislé družice najednou s pravděpodobností (1 − p)ᴺ. Funkčnost alespoň jedné je 1 − (1 − p)ᴺ."
    },
    {
        "id": 51, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "Co jsou to mezisatelitní spoje (ISL – Inter-Satellite Links) a jakou hlavní výhodu přinášejí?",
        "options": [
            "Přímý přenos dat mezi družicemi ve vesmíru (rádiově nebo laserem) bez nutnosti okamžitě směrovat provoz přes pozemní bránu v každém úseku",
            "Přímé bezdrátové propojení dvou sousedních pozemních VSAT terminálů bez účasti družice na oběžné dráze v režimu MESH",
            "Vyhrazený záložní kanál mezi centrálním teleportem (HUB) a pozemní páteřní MPLS sítí pro případ výpadku optické trasy",
            "Automatické řízení handoveru na úrovni koncového uživatelského modemu při přepínání mezi GEO a LEO sítí"
        ],
        "ans": 0,
        "exp": "ISL vytváří páteřní síť přímo v kosmickém segmentu – snižuje závislost na hustotě pozemních bran (např. nad oceány)."
    },
    {
        "id": 52, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "Jaká typická vlnová délka se používá u optických (laserových) mezisatelitních spojů ISL?",
        "options": [
            "Blízká infračervená oblast, typicky λ = 1 550 nm",
            "Ultrafialová oblast kolem λ = 250 nm",
            "Milimetrové rádiové vlny v pásmu Ka (λ ≈ 10 mm)",
            "Viditelné červené světlo kolem λ = 650 nm"
        ],
        "ans": 0,
        "exp": "Laserové ISL běžně pracují v blízké IR oblasti kolem λ = 1550 nm a dosahují rychlostí jednotek až desítek Gb/s."
    },
    {
        "id": 53, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "Co je hlavní technickou nevýhodou laserových mezisatelitních spojů oproti rádiovým ISL?",
        "options": [
            "Extrémně úzký svazek klade vysoké nároky na přesnost zaměření, sledování a potlačení mechanických vibrací družice",
            "Výrazně nižší přenosová kapacita omezená na jednotky Mbps a silné vzájemné rušení s okolními spoji",
            "Vysoký útlum volného prostoru ve vakuu způsobený absorpcí infračerveného záření vodní párou ve vesmíru",
            "Nemožnost použití u polárních a šikmých LEO konstelací kvůli silnému Dopplerovu posuvu v optickém pásmu"
        ],
        "ans": 0,
        "exp": "Úzký laserový svazek nabízí obří kapacitu a minimální rušení, ale vyžaduje extrémně přesný systém akvizice, sledování a stabilizace (PAT)."
    },
    {
        "id": 54, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "CHYTÁK ZE SKRIPT: Zaručuje velmi úzký paprsek laserového mezisatelitního spoje sám o sobě dostatečnou bezpečnost přenášených dat?",
        "options": [
            "Ne – úzký svazek sice ztěžuje nežádoucí zachycení signálu, ale nezajišťuje kryptografickou důvěrnost ani integritu; data je nutné šifrovat",
            "Ano – vzhledem k úzkému svazku na vlnové délce 1 550 nm nelze paprsek v kosmu zachytit bez zničení přenosu, takže šifrování není nutné",
            "Ano – fyzikální vlastnosti laserového přenosu ve vakuu splňují samy o sobě požadavky standardu FIPS 140-2 Level 3 bez L2 kryptování",
            "Ne – protože laserový paprsek se ve vakuu rozptyluje všesměrově jako rádiový signál a pokrývá celou polokouli Země"
        ],
        "ans": 0,
        "exp": "Fyzikální směrovost snižuje riziko odposlechu, ale nikdy nenahrazuje kryptografické zabezpečení (šifrování a autentizaci)."
    },
    {
        "id": 55, "topic": "sat-5", "topic_label": "5. Konstelace Walker & Laser ISL",
        "q": "Jakou roli hrají moderní LEO konstelace v perspektivních mobilních sítích 5G a 6G podle standardizace 3GPP?",
        "options": [
            "Jsou integrovány jako nepozemní sítě NTN (Non-Terrestrial Networks) pro rozšíření pokrytí a přímou komunikaci",
            "Slouží výhradně jako pasivní záloha páteřních optických tras mezi pozemními ústřednami mimo standard 3GPP",
            "Jsou využívány pouze pro jednosměrné televizní vysílání (Broadcast) v pásmu C bez zpětného datového kanálu",
            "Nahrazují pozemní základnové stanice ve městech díky nulové latenci a absenci útlumu v budovách"
        ],
        "ans": 0,
        "exp": "Koncept NTN (Non-Terrestrial Networks) v rámci 3GPP propojuje satelitní konstelace se sítěmi 5G a budoucími 6G."
    },

    # =========================================================================
    # SAT-6: Kosmický segment, Transpondéry a Kmitočtová pásma (GiTySAT) (11 otázek)
    # =========================================================================
    {
        "id": 56, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "Jaký je hlavní rozdíl mezi standardní telekomunikační družicí a družicí typu HTS (High Throughput Satellite)?",
        "options": [
            "HTS využívá mnoho úzkých bodových svazků (spot-beamů) s opakovaným využitím frekvencí, čímž dosahuje řádově vyšší celkové kapacity než široký svazek standardní družice",
            "HTS vysílá jedním širokým kontinentálním svazkem s mnohem vyšším výkonem v pásmu C, čímž nahrazuje potřebu frekvenčního reuse a úzkých buněk",
            "Standardní družice používají digitální palubní přepínání (On-board switching), kdežto HTS je omezena výhradně na jednoduché analogové transpondéry Bend pipe",
            "Označení HTS se vztahuje výhradně na nízkoletící družice LEO ve výšce 550 km, zatímco standardní telekomunikační družice operují jen na GEO"
        ],
        "ans": 0,
        "exp": "HTS (High Throughput Satellite) násobí přenosovou kapacitu pomocí desítek až stovek úzkých spot-beamů a frekvenčního reuse."
    },
    {
        "id": 57, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "Jak funguje nejjednodušší typ satelitního transpondéru označovaný jako „Bend pipe“?",
        "options": [
            "Transparentně přijme signál z uplinku, posune jeho frekvenci do downlinku, zesílí ho a vyšle zpět na Zemi bez digitálního zpracování obsahu",
            "Demoduluje přijatý signál do základního pásma, vyhodnotí IP hlavičky a digitálně je přepne do jiného bodového svazku na palubě",
            "Přepíná signál mezi různými frekvenčními pásmy (např. z Ku do Ka) pomocí interní křížové matice bez změny jeho polarizace",
            "Ukládá přijaté datové pakety do vyrovnávací paměti družice a postupně je předává laserovým ISL spojem až nad cílovou oblastí"
        ],
        "ans": 0,
        "exp": "Bend pipe („ohnutá trubka“) je transparentní analogový/RF opakovač – bez demodulace a palubního přepínání."
    },
    {
        "id": 58, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "Který typ transpondéru z prezentace GiTySAT umožňuje přímé přepínání či směrování signálu přímo na palubě družice?",
        "options": [
            "On-board switching",
            "Bend pipe transpondér",
            "Cross type transpondér",
            "Transparent RF repeater"
        ],
        "ans": 0,
        "exp": "Prezentace uvádí 3 druhy transpondérů: Bend pipe, Cross type (křížové propojení) a On-board switching (palubní přepínání)."
    },
    {
        "id": 59, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "Jaký je orientační frekvenční rozsah pásma C (C band) podle tabulky z prezentace GiTySAT?",
        "options": [
            "4 – 8 GHz (satelitní komunikace, Wi-Fi, meteorologické radary)",
            "8 – 12 GHz (radary, armádní komunikace, hluboký vesmír)",
            "11 – 18 GHz (satelitní TV vysílání a běžné sítě VSAT)",
            "18 – 27 GHz (radary a satelitní spoje u útlumu vodní párou)"
        ],
        "ans": 0,
        "exp": "C band pokrývá 4–8 GHz; díky nízké frekvenci je vysoce odolný proti dešti."
    },
    {
        "id": 60, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "Které satelitní pásmo (8 – 12 GHz) je typické pro armádní/vládní fixní a mobilní satelitní komunikace, radary a komunikaci s hlubokým vesmírem?",
        "options": [
            "X band (8 – 12 GHz)",
            "C band (4 – 8 GHz)",
            "Ku band (11 – 18 GHz)",
            "K band (18 – 27 GHz)"
        ],
        "ans": 0,
        "exp": "X band (8–12 GHz) je klasické pásmo pro radary, vládní/vojenské satelitní spoje a hluboký vesmír."
    },
    {
        "id": 61, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "Jaký rozsah má pásmo Ku (Ku band) a kde se s ním nejčastěji setkáme v praxi?",
        "options": [
            "11 – 18 GHz; satelitní TV vysílání (downlink), běžné VSAT sítě a terminály OneWeb",
            "4 – 8 GHz; vysoce odolné spoje v tropických deštích, Wi-Fi a meteorologické radary",
            "18 – 27 GHz; širokopásmové spoje citlivé na rezonanční útlum vodní párou při 22,23 GHz",
            "27 – 40 GHz; moderní HTS družice, brány systémů O3b/Starlink a mobilní sítě 5G"
        ],
        "ans": 0,
        "exp": "Ku band (11–18 GHz) je nejrozšířenější pásmo pro satelitní televizi i komerční VSAT spoje."
    },
    {
        "id": 62, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "CHYTÁK Z PREZENTACE: Proč je v pásmu K (18 – 27 GHz) nutné dávat pozor právě na frekvenci 22,23 GHz?",
        "options": [
            "Dochází tam k výraznému rezonančnímu útlumu signálu vodní párou v atmosféře",
            "Dochází tam k maximálnímu rušení od pozemních automobilových radarů a 5G sítí",
            "Na této frekvenci nastává úplný odraz signálu od spodní vrstvy zemské ionosféry",
            "Tato frekvence je mezinárodně vyhrazena výhradně pro navigační signály GNSS"
        ],
        "ans": 0,
        "exp": "Tabulka satelitních pásem GiTySAT výslovně upozorňuje: K band (18–27 GHz) – pozor na útlum vodní párou při 22,23 GHz!"
    },
    {
        "id": 63, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "Které frekvenční pásmo (27 – 40 GHz) používají moderní vysokokapacitní systémy jako O3b mPOWER, brány OneWeb/Starlink a také sítě 5G?",
        "options": [
            "Ka band (27 – 40 GHz)",
            "K band (18 – 27 GHz)",
            "V band (40 – 75 GHz)",
            "Ku band (11 – 18 GHz)"
        ],
        "ans": 0,
        "exp": "Ka band (27–40 GHz) nabízí velkou šířku pásma pro moderní datové satelity (uplink/downlink) i 5G."
    },
    {
        "id": 64, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "Jaké orientační frekvenční rozsahy mají nejvyšší experimentální satelitní pásma V band a E band?",
        "options": [
            "V band: 40 – 75 GHz; E band: 60 – 90 GHz",
            "V band: 18 – 27 GHz; E band: 27 – 40 GHz",
            "V band: 27 – 40 GHz; E band: 40 – 75 GHz",
            "V band: 60 – 90 GHz; E band: 90 – 120 GHz"
        ],
        "ans": 0,
        "exp": "Dle tabulky z prezentace: V band = 40–75 GHz (experimentální sat. komunikace, auto radary) a E band = 60–90 GHz (experimentální sat. komunikace, využívaná i v bránách moderních LEO)."
    },
    {
        "id": 65, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "Seřaďte správně satelitní pásma od NEJNIŽŠÍ po NEJVYŠŠÍ frekvenci:",
        "options": [
            "C band → X band → Ku band → K band → Ka band → V band → E band",
            "C band → X band → K band → Ku band → Ka band → E band → V band",
            "X band → C band → Ku band → Ka band → K band → V band → E band",
            "C band → Ku band → X band → K band → Ka band → V band → E band"
        ],
        "ans": 0,
        "exp": "Správné pořadí: C (4–8), X (8–12), Ku (11–18), K (18–27), Ka (27–40), V (40–75), E (60–90 GHz)."
    },
    {
        "id": 66, "topic": "sat-6", "topic_label": "6. Kosmický segment & Pásma",
        "q": "Jaký je typický kompromis při přechodu z nižšího pásma (např. C) na vyšší pásmo (např. Ka)?",
        "options": [
            "Získáme mnohem větší šířku pásma a menší antény, ale signál je citlivější na atmosférický útlum a déšť (rain fade)",
            "Získáme vyšší odolnost proti dešti a menší antény, ale za cenu výrazně užšího přenosového kanálu a nižší rychlosti",
            "Sníží se útlum ve volném prostoru (FSPL), ale pro příjem na Zemi musíme použít rozměrnější parabolické antény",
            "Získáme nižší obousměrnou latenci (RTT), ale musíme družici přesunout z geostacionární dráhy na střední dráhu MEO"
        ],
        "ans": 0,
        "exp": "Vyšší pásma (Ku/Ka) přinášejí široké kanály a kompaktní antény, ale vyžadují řešení útlumu deštěm (např. pomocí ACM)."
    },

    # =========================================================================
    # SAT-7: GEO sítě a služby GiTySAT (Topologie, VSAT, Internet vs Privátní) (11 otázek)
    # =========================================================================
    {
        "id": 67, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "Která fakta o infrastruktuře a certifikaci společnosti GiTy, a.s. uvádí prezentace GiTySAT?",
        "options": [
            "Vlastní satelitní teleport (HUB) v ČR, pozemní MPLS síť v ČR a SR, dohled 24/7 se SLA a certifikace NBÚ – Tajné",
            "Vlastní konstelace 20 MEO družic, pronajatý teleport v zahraničí, dohled v pracovní dny a certifikace pouze pro veřejný Internet",
            "Pronajaté kapacity bez vlastního HUBu, propojení přes veřejné Wi-Fi uzly a dohledové centrum se SLA bez bezpečnostní prověrky",
            "Vlastní LEO gateway stanice na každém kontinentu bez pozemní MPLS páteře a bez integrace s dohledovým centrem 24/7"
        ],
        "ans": 0,
        "exp": "GiTy disponuje vlastním satelitním HUBem v ČR, pozemní MPLS sítí v ČR/SR, dohledovým centrem 24/7/365 a certifikací NBÚ na stupeň Tajné."
    },
    {
        "id": 68, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "Jaké 4 topologické typy GEO satelitních spojů a sítí rozlišuje prezentace GiTySAT?",
        "options": [
            "Broadcast (jednosměrná distribuce), Bod–Bod (SCPC), Hvězdicová síť (1× VSAT HUB, n× terminál) a MESH struktura",
            "Broadcast (jednosměrná distribuce), Kruhová síť (Token Ring), Sběrnice (Bus) a Stromová síť bez VSAT HUBu",
            "Bod–Bod (SCPC), Walker Delta, Walker Star a laserová mezisatelitní páteř ISL v pásmu 1 550 nm",
            "Hvězdicová síť (1× HUB), Hybridní NNI propoj, Privátní MPLS WAN a Veřejná internetová konfigurace s FUP"
        ],
        "ans": 0,
        "exp": "Čtyři GEO topologie ze slidu 7: Broadcast, Bod–Bod (SCPC), Hvězdicová (Star s VSAT HUBem) a MESH."
    },
    {
        "id": 69, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "Která technologie se typicky používá pro vyhrazené GEO satelitní spoje typu „Bod – Bod“ mezi dvěma modemy / IP routery?",
        "options": [
            "SCPC (Single Channel Per Carrier)",
            "TDMA se sdíleným kanálem přes HUB",
            "Asymetrické FDMA s jednosměrným Broadcastem",
            "Dynamické přepínání On-board switching v LEO"
        ],
        "ans": 0,
        "exp": "Spoje Bod–Bod využívají technologii SCPC (každý směr má svou vyhrazenou nosnou) se satelitními modemy či IP routery."
    },
    {
        "id": 70, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "Jaká je typická konfigurace a komunikační schéma satelitní sítě s HVĚZDICOVOU (Star) strukturou?",
        "options": [
            "1× centrální VSAT HUB a n× VSAT terminálů; asymetrické schéma (distribuční kanál z HUBu a zpětný kanál od terminálů přes TDMA/FDMA)",
            "Vzájemné přímé propojení všech n terminálů jedním skokem bez centrálního VSAT HUBu se symetrickým provozem přes vyhrazené SCPC nosné",
            "Jednosměrný distribuční kanál z centrálního teleportu ke všem n přijímacím parabolám bez jakéhokoli zpětného satelitního kanálu",
            "Dva rovnocenné IP routery propojené symetrickým vyhrazeným kanálem SCPC mimo centrální dohledové centrum a VSAT HUB"
        ],
        "ans": 0,
        "exp": "Hvězdicová síť má 1 centrální VSAT HUB a n koncových VSAT terminálů; využívá sdílené nebo vyhrazené kanály s přístupem TDMA/FDMA."
    },
    {
        "id": 71, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "V čem spočívá hlavní výhoda satelitní sítě s MESH strukturou oproti hvězdicové síti při komunikaci dvou poboček?",
        "options": [
            "Terminály mohou komunikovat napřímo jedním satelitním skokem (bez nutnosti dvojitého skoku přes centrální VSAT HUB), čímž se snižuje zpoždění na polovinu",
            "Veškerý provoz poboček prochází dvojitým skokem přes centrální VSAT HUB, což umožňuje centrálně aplikovat silnější QoS a hlubší inspekci paketů",
            "Pobočky jsou propojeny výhradně jednosměrným Broadcast kanálem, takže nepotřebují žádný zpětný kanál ani satelitní modem v terénu",
            "MESH struktura nevyužívá geostacionární družici, ale automaticky směruje pakety mezi pozemními terminály přes pozemní MPLS síť G-Net"
        ],
        "ans": 0,
        "exp": "Ve hvězdicové síti musí provoz pobočka→pobočka přes HUB (dva skoky přes GEO = ~1 s), zatímco v MESH jde přímo jedním skokem."
    },
    {
        "id": 72, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "Které vlastnosti jsou typické pro INTERNETOVOU konfiguraci GEO satelitních služeb?",
        "options": [
            "Velké množství terminálů, unifikované služby, přístup do Internetu, FUP, agregace a omezené možnosti dohledu",
            "Malé specifické sítě, privátní služby dle požadavku, přídavné zabezpečení, QoS a End-to-End SNMP dohled",
            "Garantovaná nesdílená kapacita CIR bez agregace a bez FUP limitů propojená přímo do firemní MPLS WAN",
            "Přímé propojení poboček s firemní centrálou přes privátní NNI uzel bez jakéhokoli přístupu do veřejného Internetu"
        ],
        "ans": 0,
        "exp": "Internetová konfigurace cílí na masové/unifikované připojení do Internetu s agregací, FUP a omezeným dohledem."
    },
    {
        "id": 73, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "Čím se odlišuje PRIVÁTNÍ satelitní síť GiTySAT od běžné internetové konfigurace?",
        "options": [
            "Propojuje pobočky s centrálou (např. do MPLS WAN), nabízí privátní služby dle požadavku, přídavné zabezpečení, QoS, End-to-End dohled (SNMP) a integraci s dalšími službami",
            "Cílí na velké množství terminálů v mezinárodním prostředí s unifikovanými tarify, uplatňuje FUP, vysokou agregaci a poskytuje pouze omezené možnosti dohledu",
            "Připojuje pobočky výhradně do veřejného Internetu přes sdílený rezidenční tarif bez garance SLA, bez QoS a bez napojení na dohledové centrum",
            "Obejde se zcela bez pozemního VSAT HUBu a teleportu, protože pobočky komunikují s centrálou pouze přes veřejnou mobilní síť LTE"
        ],
        "ans": 0,
        "exp": "Privátní síť je šitá na míru podnikovým/vládním zákazníkům: vlastní MPLS WAN integrace, QoS, extra šifrování a End-to-End SNMP dohled."
    },
    {
        "id": 74, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "Co znamená v kontextu VSAT sítí zkratka HUB (Teleport)?",
        "options": [
            "Centrální pozemní stanice provozovatele sítě, přes kterou prochází provoz terminálů ve hvězdicové síti a která řídí přístup ke kanálům",
            "Venkovní RF jednotka umístěná přímo na ozařovači parabolické antény koncového uživatele pro převod frekvence do L-pásma",
            "Palubní přepínací jednotka na geostacionární družici, která směruje spot-beamy bez účasti jakékoli pozemní infrastruktury",
            "Vnitřní pasivní síťový rozbočovač u zákazníka, který spojuje satelitní modem iDirect s lokálními počítači"
        ],
        "ans": 0,
        "exp": "Teleport (VSAT HUB) je hlavní pozemní brána a řídicí uzel hvězdicové satelitní sítě napojený na páteřní síť operátora (u GiTy na G-Net MPLS)."
    },
    {
        "id": 75, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "Které typy služeb podle prezentace GiTySAT nabízí společnost GiTy svým zákazníkům?",
        "options": [
            "Internetové, intranetové, hlasové, videokonferenční, telemetrické a telematické služby (vč. systémové integrace a ICT bezpečnosti)",
            "Výhradně hromadné satelitní televizní vysílání (Broadcast) v pásmu Ku pro domácnosti bez zpětného datového kanálu",
            "Pouze pronájem surové transpondérové kapacity na oběžné dráze bez pozemního teleportu, koncových terminálů a dohledu",
            "Výhradně veřejný mobilní přístup pro spotřebitele s FUP limitem bez firemních MPLS sítí a bez bezpečnostních služeb"
        ],
        "ans": 0,
        "exp": "Slide 3 uvádí internetové, intranetové, hlasové, videokonferenční, telemetrické a telematické služby + systémovou integraci a bezpečnost."
    },
    {
        "id": 76, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "K čemu slouží v satelitní síti metody vícenásobného přístupu TDMA a FDMA?",
        "options": [
            "Umožňují více VSAT terminálům sdílet satelitní kapacitu (časové sloty u TDMA, frekvenční kanály u FDMA) ve zpětném či distribučním směru",
            "Slouží k dynamické změně modulace a kódování podle aktuálního počasí (od QPSK po 256APSK), aby spojení v silném dešti nespadlo",
            "Zajišťují kryptografické utajení aktivity kanálu pomocí AES-256 na 2. vrstvě a autentizaci terminálů certifikátem X.509",
            "Určují způsob prostorového rozmístění orbitálních rovin v konstelacích Walker Delta a Walker Star po 360°, resp. 180°"
        ],
        "ans": 0,
        "exp": "FDMA dělí sdílené pásmo na frekvenční podkanály, TDMA dělí čas na sloty pro jednotlivé terminály."
    },
    {
        "id": 77, "topic": "sat-7", "topic_label": "7. GEO sítě, Topologie & GiTy",
        "q": "Jaká síťová technologie tvoří pozemní páteř společnosti GiTy v ČR a SR, do které ústí satelitní teleport?",
        "options": [
            "Pozemní MPLS síť (G-Net)",
            "Kruhová síť Token Ring",
            "Veřejná mobilní síť LTE",
            "Bezdrátová síť Wi-Fi v pásmu C"
        ],
        "ans": 0,
        "exp": "GiTy provozuje vlastní pozemní MPLS síť G-Net v ČR a na Slovensku propojenou s jejím satelitním teleportem."
    },

    # =========================================================================
    # SAT-8: Praxe: MEO (O3b) a LEO konstelace (OneWeb, Starlink, Amazon, Telesat) (11 otázek)
    # =========================================================================
    {
        "id": 78, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Který z moderních datových systémů z prezentace GiTySAT operuje na střední oběžné dráze MEO (~8 000 km) s RTT kolem 150 ms?",
        "options": [
            "SES O3b / O3b mPOWER",
            "SpaceX Starlink",
            "Eutelsat OneWeb",
            "Telesat Lightspeed"
        ],
        "ans": 0,
        "exp": "O3b / O3b mPOWER je MEO konstelace (~8 000 km, RTT 150 ms, Ka-band, pokrytí ±50° šířky, až 1,6 Gbps/beam)."
    },
    {
        "id": 79, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Jaké geografické omezení má základní pokrytí sítě O3b / O3b mPOWER (MEO na rovníkové/nízkosklonné dráze)?",
        "options": [
            "Pokrytí je omezeno přibližně na ±50° zeměpisné šířky (nepokrývá polární oblasti)",
            "Pokrývá pouze oblasti nad ±60° zeměpisné šířky (Arktidu a Antarktidu)",
            "Pokrývá výhradně střední Evropu a Blízký východ pomocí pevných GEO svazků",
            "Poskytuje plné globální pokrytí včetně obou pólů díky polárním drahám (i = 90°)"
        ],
        "ans": 0,
        "exp": "Standardní O3b/mPOWER pokrývá pás ±50° zeměpisné šířky (limitované služby až ±62°), s velmi vysokou propustností až 1,6 Gbps/beam."
    },
    {
        "id": 80, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Jaké jsou klíčové parametry LEO konstelace Eutelsat OneWeb?",
        "options": [
            "Výška ~1 200 km, 652 družic, RTT ~100 ms, globální pokrytí, Ka-band k GW stanicím a Ku-band k terminálům",
            "Výška ~550 km, přes 9 800 družic, RTT 25–50 ms, globální pokrytí, Ku/Ka/E-band a laserové ISL spoje",
            "Výška ~8 000 km, 20 družic, RTT 150 ms, pokrytí ±50° zeměpisné šířky a přenos výhradně v pásmu Ka",
            "Výška ~610 km, plánováno 3 232 družic, uplink v Ka-bandu, downlink v K-bandu a laserové ISL spoje"
        ],
        "ans": 0,
        "exp": "OneWeb: LEO ~1 200 km, 652 družic, RTT ~100 ms, >40 GW stanic, Ka-band (GW) + Ku-band (terminál)."
    },
    {
        "id": 81, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Jakou důležitou obchodně-technickou výhodu nabízí OneWeb pro firemní a privátní zákazníky oproti běžným rezidenčním tarifům?",
        "options": [
            "Kromě maximální rychlosti MIR (až 150/30 Mbps) nabízí i garantovanou rychlost CIR (až 40/8 Mbps)",
            "Nabízí garantovanou latenci pod 15 ms díky laserovým mezisatelitním spojům mezi všemi 652 družicemi",
            "Umožňuje přímou komunikaci terminálů bez jakýchkoli pozemních GW stanic i bez dohledu operátora",
            "Poskytuje symetrickou rychlost 3 Gbps / 2 Gbps na malých plochých anténách bez jakékoli agregace"
        ],
        "ans": 0,
        "exp": "OneWeb umožňuje firemní služby s garantovanou rychlostí CIR (Committed Information Rate) až 40/8 Mbps i MIR až 150/30 Mbps."
    },
    {
        "id": 82, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Jaký je rozdíl mezi „technickou dostupností“ a „komerční dostupností“ u map OneWeb v prezentaci GiTySAT?",
        "options": [
            "Technická dostupnost znamená, že oblast pokrývá signál družic, ale komerční dostupnost vyžaduje navíc platné regulatorní/licenční povolení a smluvní otevření v dané zemi",
            "Komerční dostupnost znamená pouze pokrytí rádiovým signálem na mapě, zatímco technická dostupnost vyžaduje fyzickou instalaci místní GW stanice přímo v daném státě",
            "Technická dostupnost platí výhradně pro námořní a letecké terminály na oceánech, kdežto komerční dostupnost označuje pevnou pozemní síť MPLS",
            "Oba pojmy označují totéž – jakmile družice OneWeb přelétají nad státem, je služba automaticky legálně i komerčně dostupná pro všechny zákazníky"
        ],
        "ans": 0,
        "exp": "Družice může technicky pokrývat téměř celý svět, ale v některých státech (např. Rusko, Čína aj.) není služba komerčně ani regulatorně povolena."
    },
    {
        "id": 83, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Jaké parametry jsou charakteristické pro síť SpaceX Starlink?",
        "options": [
            "LEO (typicky 550 km, 12 slupek 335–1 200 km), přes 9 800 aktivních družic, RTT 25–50 ms, Ku/Ka/E-band + laserové spoje mezi družicemi",
            "LEO (cca 1 200 km, jedna slupka), 652 aktivních družic, RTT ~100 ms, Ka-band ke GW a Ku-band k terminálu bez laserů",
            "MEO (cca 8 000 km), 13 družic mPOWER s formovatelnými 250km beamy, RTT 150 ms a pokrytí v pásmu ±50° zeměpisné šířky",
            "LEO (1 015 a 1 325 km), úvodní fáze 198 družic, Ka-band + lasery ISL, zaměření na B2B/L2 služby a komerční start 2028"
        ],
        "ans": 0,
        "exp": "Starlink má nejnižší latenci (25–50 ms), nejvíce družic (>9 800, plán 12 000), 13km beamy a laserové ISL."
    },
    {
        "id": 84, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Jak jsou rozděleny polomobilní a mobilní internetové služby u Starlinku?",
        "options": [
            "Buď datově neomezené (ale geograficky omezené), nebo datově omezené (ale geograficky neomezené)",
            "Buď rychlostně garantované (CIR), nebo s pevnou latencí pod 10 ms pro námořní a letecký provoz",
            "Všechny mobilní tarify jsou zároveň datově neomezené i geograficky zcela neomezené po celém světě",
            "Polomobilní tarify fungují pouze v pásmu C přes GEO teleport a mobilní pouze v pásmu K přes OneWeb"
        ],
        "ans": 0,
        "exp": "Slide 11 jasně dělí mobilní/polomobilní tarify na: 1) Datově neomezené, geograficky omezené a 2) Datově omezené, geograficky neomezené."
    },
    {
        "id": 85, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Co platí pro připravovanou konstelaci Amazon LEO (Project Kuiper)?",
        "options": [
            "3 orbitální slupky (590, 610, 630 km), plánováno 3 232 družic, lasery ISL, terminály Nano/Pro/Ultra až do 1 Gbps, komerční start cca konec 2026 / 2Q 2027",
            "2 orbitální slupky (1 015 a 1 325 km), úvodní fáze 198 družic, terminály Performance/Ultimate/Aviation až do 3 Gbps a komerční start v roce 2028",
            "12 orbitálních slupek (335–1 200 km), přes 9 800 družic na oběžné dráze, terminály Mini/Standard/Enterprise/Performance a E-band brány",
            "MEO dráha ve výšce 8 000 km s 13 družicemi mPOWER, tisíce formovatelných 250km beamů v Ka-bandu a pokrytí ±50° zeměpisné šířky"
        ],
        "ans": 0,
        "exp": "Amazon LEO cílí na 3 232 družic (590–630 km), uplink Ka / downlink K-band, 10km beamy, lasery a terminály až 1 Gbps (reálný start 2Q 2027)."
    },
    {
        "id": 86, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Na jaký segment a jaké technologie se zaměřuje budoucí LEO konstelace Telesat Lightspeed (start 2028)?",
        "options": [
            "B2B, L2 služby a letectví/námořnictví; 198 družic (1 015 a 1 325 km), globální pokrytí včetně pólů, Ka-band + lasery, terminály až 3 Gbps",
            "Masový rezidenční trh pro domácnosti; 3 232 družic ve výšce 590–630 km, downlink v K-bandu, 10km beamy a terminály Nano/Pro/Ultra",
            "Výhradně státní a vojenské spoje v pásmu X na dráze MEO (20 200 km) s latencí 150 ms a bez mezisatelitních laserových spojů",
            "Pouze střední Evropa a Blízký východ přes geostacionární HTS družice s terminály iDirect 9530 a modulací DVB-S2X"
        ],
        "ans": 0,
        "exp": "Telesat Lightspeed (2028) staví na kombinaci polárních a inklinovaných drah, L2 službách, Ka-bandu, laserech a vysokokapacitních terminálech (1 až 3 Gbps)."
    },
    {
        "id": 87, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Které z následujících konstelací využívají nebo plánují využívat laserové mezisatelitní spoje (družice ↔ družice)?",
        "options": [
            "Starlink, Amazon LEO i Telesat Lightspeed",
            "Pouze Eutelsat OneWeb a SES O3b mPOWER",
            "Pouze Starlink; Amazon LEO i Telesat používají výhradně pásmo C",
            "Žádná LEO konstelace nepoužívá laserové ISL"
        ],
        "ans": 0,
        "exp": "Laserové ISL (družice ↔ družice) jsou společným prvkem moderních konstelací Starlink, Amazon LEO i Telesat Lightspeed."
    },
    {
        "id": 88, "topic": "sat-8", "topic_label": "8. O3b, OneWeb, Starlink, Amazon, Telesat",
        "q": "Seřaďte správně uvedené systémy od NEJNIŽŠÍ po NEJVYŠŠÍ typickou obousměrnou latenci (RTT):",
        "options": [
            "Starlink (25–50 ms) < OneWeb (~100 ms) < O3b MEO (150 ms) < GEO GiTySAT (500–650 ms)",
            "OneWeb (~100 ms) < Starlink (25–50 ms) < O3b MEO (150 ms) < GEO GiTySAT (500–650 ms)",
            "Starlink (25–50 ms) < O3b MEO (150 ms) < OneWeb (~100 ms) < GEO GiTySAT (500–650 ms)",
            "O3b MEO (150 ms) < OneWeb (~100 ms) < Starlink (25–50 ms) < GEO GiTySAT (500–650 ms)"
        ],
        "ans": 0,
        "exp": "Starlink (550 km) má 25–50 ms, OneWeb (1 200 km) ~100 ms, O3b MEO (8 000 km) ~150 ms a GEO (35 786 km) ~500–650 ms."
    },

    # =========================================================================
    # SAT-9: Terminály, Zabezpečení (TRANSEC, CSIR), DVB-S2X ACM a Hybridní sítě (11 otázek)
    # =========================================================================
    {
        "id": 89, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "Z jakých dvou hlavních částí se skládá klasický GEO satelitní terminál (např. technologie ST Engineering / iDirect u GiTySAT)?",
        "options": [
            "Venkovní část (anténa + RF jednotka Ku/X/Ka/C) a vnitřní část (VSAT terminál / modem, např. iDirect 950mp, 9530, Newtec MDM3315)",
            "Vysílací část (parabola na budově + laserový modul) a přijímací část (samostatný pozemní VSAT HUB umístěný v centrále operátora)",
            "Kosmická část (transpondér Bend pipe na družici) a pozemní páteřní část (MPLS síť G-Net včetně dohledového centra 24/7)",
            "Anténní část (pouze pasivní reflektor bez RF jednotky) a síťová část (běžný domácí Wi-Fi router připojený přes NNI rozhraní)"
        ],
        "ans": 0,
        "exp": "Terminál má venkovní část (parabola 0,7–2,4 m / Drive Away / Quick Deploy / Manpack + RF jednotka) a vnitřní část (VSAT modem)."
    },
    {
        "id": 90, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "Co znamená typ mobilní satelitní antény „Manpack“ oproti „Drive Away“ a fixní parabole?",
        "options": [
            "Manpack je kompaktní přenosný terminál v kufru/batohu pro jednotlivce v terénu; Drive Away je anténa namontovaná na vozidle",
            "Manpack je pevná parabolická anténa (0,7–2,4 m) kotvená na střeše budovy; Drive Away je ruční rozložitelná anténa v batohu",
            "Manpack je automatická anténa pevně instalovaná na střeše zásahového vozidla; Drive Away je označení pro pevný teleport HUB",
            "Manpack označuje rychle rozložitelnou anténu na trojnožce (Quick Deploy) bez RF jednotky; Drive Away je vnitřní VSAT modem"
        ],
        "ans": 0,
        "exp": "Fixní parabola = na budově; Drive Away = na střeše vozidla; Quick Deploy = rychle rozložitelná na trojnožce; Manpack = přenosná v batohu/kufru."
    },
    {
        "id": 91, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "Jaké bezpečnostní prvky zajišťuje technologie iDirect TRANSEC (Transmission Security) u GEO služeb GiTySAT?",
        "options": [
            "Skrytou aktivitu komunikačního kanálu, šifrování AES-256 na 2. vrstvě (L2) a autentizaci certifikátem X.509",
            "Automatické potlačení záměrného rušení (anti-jamming) na fyzické vrstvě bez kryptografického šifrování a bez certifikátů",
            "Šifrování přenosu výhradně na aplikační vrstvě (L7) pomocí TLS bez utajení aktivity satelitního kanálu a bez L2 ochrany",
            "Dynamickou změnu modulace podle počasí (ACM z 256APSK na QPSK), která nahrazuje potřebu certifikátů a šifrovacích klíčů"
        ],
        "ans": 0,
        "exp": "TRANSEC chrání samotný přenosový kanál: skrývá aktivitu kanálu, šifruje pomocí AES-256 na L2 a ověřuje stanice certifikátem X.509."
    },
    {
        "id": 92, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "K čemu slouží technologie CSIR u zabezpečených satelitních služeb GiTySAT?",
        "options": [
            "Anti-jamming a potlačení nežádoucího rušení (interference removal system)",
            "Šifrování datového provozu pomocí AES-256 na L2 a autentizace X.509",
            "Certifikace odolnosti kryptovacího modulu dle normy FIPS 140-2 Level 3",
            "Adaptivní změna modulace (ACM) v normě DVB-S2X při útlumu deštěm"
        ],
        "ans": 0,
        "exp": "Prezentace uvádí: CSIR = Anti jamming a interference removal system, vedle Spread spectrum a FIPS 140-2 Level 3 kryptomodulů."
    },
    {
        "id": 93, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "Co v přehledu zabezpečení GEO služeb GiTySAT vyjadřuje norma FIPS 140-2 Level 3?",
        "options": [
            "Přísné bezpečnostní požadavky na hardwarový kryptovací modul (ochrana proti fyzické manipulaci a neoprávněnému vyčtení klíčů)",
            "Specifikaci pro systém potlačení úmyslného rušení (anti-jamming) a eliminaci cizího signálu v satelitním pásmu Ka",
            "Mezinárodní standard pro adaptivní kódování a modulaci DVB-S2X zajišťující zachování spoje při silné bouřce",
            "Telekomunikační směrnici definující maximální přípustnou obousměrnou latenci (RTT) pro vládní a armádní sítě"
        ],
        "ans": 0,
        "exp": "FIPS 140-2 Level 3 je standard definující vysoké bezpečnostní požadavky na kryptografické moduly."
    },
    {
        "id": 94, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "Jak funguje moderní funkce ACM (Adaptive Coding and Modulation) ve standardu DVB-S2X při zhoršení počasí (déšť, bouřka)?",
        "options": [
            "Modem dynamicky přepne na nižší, odolnější modulaci a silnější kódování (např. z 256APSK na QPSK), aby spoj nespadl; po vyjasnění se vrátí k vyšší rychlosti",
            "Modem okamžitě přepne na vyšší řád modulace (z QPSK na 256APSK), aby zvýšil vysílací rychlost a protlačil data skrze dešťovou clonu před výpadkem",
            "Modem zcela přeruší satelitní spojení v pásmech Ku/Ka a automaticky přesměruje kritický provoz do veřejné internetové sítě bez zapojení HUBu",
            "Modem přeladí anténu z geostacionární družice na nejbližší průlet LEO družice Starlink, kde je útlum deštěm nižší díky menší vzdálenosti"
        ],
        "ans": 0,
        "exp": "ACM (Adaptive Coding and Modulation) přizpůsobuje modulaci (Rx až 256APSK, Tx až 16QAM) a kódování aktuálnímu odstupu signál/šum – spoj tak zůstane živý i v dešti."
    },
    {
        "id": 95, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "Jakých modulací může podle prezentace trendů GiTySAT dosahovat standard DVB-S2X v příjmu (Rx) a vysílání (Tx)?",
        "options": [
            "Rx: QPSK až 256APSK; Tx: BPSK až 16QAM",
            "Rx: BPSK až 16QAM; Tx: QPSK až 256APSK",
            "Rx: QPSK až 64QAM; Tx: výhradně BPSK",
            "Rx: 16APSK až 1024QAM; Tx: 8PSK až 64APSK"
        ],
        "ans": 0,
        "exp": "Dle slidu 22 (Trendy GiTySAT): DVB-S2X pracuje v příjmu s QPSK až 256APSK a ve zpětném vysílání s BPSK až 16QAM s podporou ACM."
    },
    {
        "id": 96, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "Jak v hybridní síti GiTySAT (kombinující GEO a LEO) probíhá směrování KRITICKÉHO a citlivého provozu pobočky?",
        "options": [
            "Přes zabezpečený GEO VSAT terminál a GEO družici do VSAT HUBu a MPLS sítě G-Net až na centrálu",
            "Přes LEO terminál a LEO gateway dále přes privátní NNI propoj do MPLS sítě G-Net až na centrálu",
            "Lokálně přes firewall pobočky přímo do veřejného Internetu a následně přes druhý firewall do centrály",
            "Výhradně přes záložní mobilní síť LTE mimo dohledové centrum GiTy a bez zapojení MPLS páteře"
        ],
        "ans": 0,
        "exp": "Podle schématu hybridní sítě (slide 25) jde kritický/citlivý provoz (červená trasa) vysoce spolehlivou a zabezpečenou cestou přes GEO VSAT."
    },
    {
        "id": 97, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "Kudy je v hybridní síti GiTySAT směrován STANDARDNÍ firemní provoz mezi pobočkou a centrálou?",
        "options": [
            "Přes LEO terminál a LEO družici na LEO gateway, odtud přes privátní NNI propoj do G-Net MPLS sítě až na centrálu",
            "Přes zabezpečený GEO VSAT terminál a GEO družici do centrálního VSAT HUBu a následně do MPLS sítě G-Net",
            "Lokálně přes firewall pobočky rovnou do veřejného Internetu bez využití privátního NNI propoje do sítě G-Net",
            "Přímým MESH skokem mezi LEO terminálem pobočky a centrálou bez účasti pozemní LEO gateway stanice"
        ],
        "ans": 0,
        "exp": "Standardní provoz (modrá trasa) využívá nízkou latenci a vysokou rychlost LEO a privátní propojení LEO GW – G-Net (NNI) do centrály."
    },
    {
        "id": 98, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "Jak je v hybridní síti GiTySAT řešen NEKRITICKÝ a internetový provoz pobočky?",
        "options": [
            "Odchází lokálně přes firewall do veřejného Internetu (a přes další firewall případně do G-Netu), aby nezatěžoval drahocennou vyhrazenou GEO/privátní kapacitu",
            "Směruje se výhradně přes zabezpečený GEO VSAT terminál s aktivovaným TRANSEC AES-256 přes centrální teleport do G-Netu",
            "Směruje se přes LEO terminál na LEO gateway a odtud vždy přes vyhrazený privátní NNI propoj přímo na centrálu zákazníka",
            "Prochází dvojitým satelitním skokem přes GEO družici v režimu MESH tak, aby byl centrálně filtrován v dohledovém centru GiTy"
        ],
        "ans": 0,
        "exp": "Nekritický internetový provoz (zelená trasa) odtéká mimo prioritní satelitní tunely přes firewall do Internetu."
    },
    {
        "id": 99, "topic": "sat-9", "topic_label": "9. Terminály, Bezpečnost, ACM & Hybrid",
        "q": "Jaký je hlavní přínos mobilního řešení „GiTySAT MS usecase“ pro zásahové složky (např. hasiči, IZS v terénu)?",
        "options": [
            "Zásahové vozidlo se v krizové oblasti bez pozemní infrastruktury spojí přes družici a VSAT HUB (příp. záložně přes mobilní síť) s dispečinkem, videoserverem a dohledem GiTy",
            "Zásahové vozidlo funguje jako lokální veřejný Wi-Fi hotspot s FUP limitem bez jakéhokoli napojení na videoserver, tracking a dispečink",
            "Systém slouží výhradně pro jednosměrný příjem meteorologického vysílání (Broadcast) v kabině vozidla bez možnosti odesílat video z místa zásahu",
            "Řešení vyžaduje pevnou 2,4m betonovanou parabolu na místě zásahu a není možné jej provozovat při výpadku pozemních elektrických sítí"
        ],
        "ans": 0,
        "exp": "Zásahové vozidlo (MS usecase, slide 23) zajišťuje přenos videa, trackingu a dat ze zásahové oblasti přes satelit i při výpadku pozemních sítí."
    }
]

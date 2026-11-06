# 125+ ABCD questions covering every single detail from Optika (Q1-Q2) and Strukturovaná kabeláž (Q8-Q16)
# Each fact is tested at least 3-4 times from different angles (direct, reverse, trap/chyták, scenario/formula).

QUIZ_QUESTIONS = [
    # =========================================================================
    # OKRUH: OPTIKA 1 – Struktura vlákna, typy vláken (MM/SM, SI/GI), vlnové délky
    # =========================================================================
    {
        "id": 1, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Jaké je správné pořadí vrstev typického optického vlákna směrem od středu ven?",
        "options": [
            "Jádro (Core) → Plášť (Cladding) → Primární ochrana (Coating) → Sekundární ochrana (Buffer)",
            "Plášť (Cladding) → Jádro (Core) → Sekundární ochrana → Primární ochrana",
            "Jádro (Core) → Primární ochrana → Plášť (Cladding) → Sekundární ochrana",
            "Primární jádro → Sekundární jádro → Optický plášť → Akrylátový lak"
        ],
        "ans": 0,
        "exp": "Od středu ven: 1. Jádro (Core, n₁), 2. Plášť (Cladding, n₂), 3. Primární ochrana (250 µm akrylát), 4. Sekundární ochrana (900 µm)."
    },
    {
        "id": 2, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Jaké jsou typické průměry jednotlivých vrstev jednovidového (SM) optického vlákna od středu ven?",
        "options": [
            "9 µm (jádro) → 125 µm (plášť) → 250 µm (primární ochrana) → 900 µm (sekundární ochrana)",
            "50 µm (jádro) → 125 µm (plášť) → 500 µm (primární ochrana) → 900 µm (sekundární ochrana)",
            "9 µm (jádro) → 62,5 µm (plášť) → 125 µm (primární ochrana) → 250 µm (sekundární ochrana)",
            "8 µm (jádro) → 100 µm (plášť) → 200 µm (primární ochrana) → 1000 µm (sekundární ochrana)"
        ],
        "ans": 0,
        "exp": "Jednovidové vlákno má jádro 9 µm (8–10 µm), plášť vždy 125 µm, primární ochranu 250 µm a sekundární ochranu 900 µm."
    },
    {
        "id": 3, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Jaký je průměr optického pláště (Cladding) u standardních telekomunikačních vláken (SM i MM)?",
        "options": [
            "125 µm",
            "250 µm",
            "50 µm nebo 62,5 µm",
            "900 µm"
        ],
        "ans": 0,
        "exp": "Optický plášť (Cladding) z čistého křemičitého skla má vždy standardizovaný průměr 125 µm, aby šla vlákna snadno svařovat a konektorovat."
    },
    {
        "id": 4, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Která vrstva optického vlákna má typický vnější průměr 250 µm?",
        "options": [
            "Primární ochrana (Primary Coating – akrylátový lak)",
            "Optický plášť (Cladding)",
            "Sekundární ochrana (Tight Buffer)",
            "Jádro mnohovidového vlákna (Core)"
        ],
        "ans": 0,
        "exp": "Primární ochrana z akrylátového laku obklopuje 125µm plášť a má vnější průměr 250 µm."
    },
    {
        "id": 5, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Která vrstva optického vlákna má u těsné konstrukce (tight buffer) typický průměr 900 µm?",
        "options": [
            "Sekundární ochrana (Buffer)",
            "Primární ochrana (Coating)",
            "Optický plášť (Cladding)",
            "Optické jádro (Core)"
        ],
        "ans": 0,
        "exp": "Sekundární ochrana (plastová trubička / tight buffer) má průměr 900 µm (0,9 mm)."
    },
    {
        "id": 6, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Jaké jsou standardní průměry jádra u mnohovidových (Multimode – MM) optických vláken?",
        "options": [
            "50 µm nebo 62,5 µm",
            "8 µm nebo 9 µm",
            "125 µm nebo 250 µm",
            "10 µm nebo 125 µm"
        ],
        "ans": 0,
        "exp": "Mnohovidová vlákna mají průměr jádra 50 µm (50/125 µm) nebo 62,5 µm (62,5/125 µm)."
    },
    {
        "id": 7, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Co znamená označení optického vlákna 50/125 µm?",
        "options": [
            "Mnohovidové vlákno s průměrem jádra 50 µm a průměrem pláště 125 µm",
            "Jednovidové vlákno s průměrem pláště 50 µm a primární ochranou 125 µm",
            "Vlákno pro vlnovou délku 50 nm s délkou trasy 125 m",
            "Mnohovidové vlákno s 50 vidy a numerickou aperturou 1,25"
        ],
        "ans": 0,
        "exp": "Zápis X/Y µm vždy udává průměr jádra (50 µm) lomeno průměr pláště (125 µm)."
    },
    {
        "id": 8, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Co znamená označení optického vlákna 9/125 µm?",
        "options": [
            "Jednovidové (Singlemode) vlákno s průměrem jádra 9 µm a průměrem pláště 125 µm",
            "Mnohovidové (Multimode) vlákno s 9 vidy a průměrem jádra 125 µm",
            "Gradientní vlákno s 9 vrstvami pláště",
            "Plastové vlákno s útlumem 9 dB na 125 km"
        ],
        "ans": 0,
        "exp": "9/125 µm je standardní jednovidové (SM) vlákno: jádro má průměr 9 µm a plášť 125 µm."
    },
    {
        "id": 9, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Proč mají příměsi (např. GeO₂) v křemičitém skle jádra optického vlákna zásadní význam?",
        "options": [
            "Zvyšují index lomu jádra n₁ tak, aby platilo n₁ > n₂ (podmínka pro totální vnitřní odraz)",
            "Snižují index lomu jádra n₁ pod hodnotu pláště n₂",
            "Slouží k elektrickému uzemnění statického náboje ve vlákně",
            "Zabraňují šíření základního osového vidu"
        ],
        "ans": 0,
        "exp": "Jádro musí být opticky hustší než plášť (n₁ > n₂), čehož se dosahuje legováním čistého SiO₂ příměsemi (např. GeO₂)."
    },
    {
        "id": 10, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Jak se dělí optická vlákna podle počtu šířených vidů a profilu indexu lomu?",
        "options": [
            "Mnohovidová (skoková Step-Index a gradientní Graded-Index) a Jednovidová (Singlemode)",
            "Jednovidová (skoková a parabolická) a Bezvodičová (UTP a STP)",
            "Pouze na skoková (9/125 µm) a gradientní (850 nm)",
            "Symetrická, koaxiální a kroucená optická vlákna"
        ],
        "ans": 0,
        "exp": "Základní dělení: Mnohovidová (MM – Step-Index se skokovou změnou a Graded-Index s gradientní změnou indexu lomu) a Jednovidová (SM)."
    },
    {
        "id": 11, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Jaký je hlavní rozdíl mezi mnohovidovým skokovým (Step-Index) a gradientním (Graded-Index) vláknem?",
        "options": [
            "U gradientního vlákna index lomu v jádře plynule (parabolicky) klesá od osy k plášti, což vyrovnává časy průchodu paprsků a potlačuje vidovou disperzi",
            "U skokového vlákna se šíří pouze jeden vid, zatímco u gradientního více vidů",
            "U gradientního vlákna je index lomu v jádře konstantní a paprsky se odrážejí po lomených přímkách",
            "Gradientní vlákno má jádro 9 µm, zatímco skokové má jádro 50 µm"
        ],
        "ans": 0,
        "exp": "Graded-Index má parabolický profil indexu lomu v jádře – paprsky dále od osy mají delší dráhu, ale v oblasti s nižším indexem lomu letí rychleji, což minimalizuje vidovou disperzi."
    },
    {
        "id": 12, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Proč v gradientním (Graded-Index) vlákně dorazí paprsky šířící se po delší zvlněné dráze téměř současně s osovým paprskem?",
        "options": [
            "Protože směrem k okraji jádra klesá index lomu n₁, a podle v = c/n se tam světlo šíří vyšší fázovou rychlostí",
            "Protože osový paprsek je v jádře úmyslně brzděn kovovou mřížkou",
            "Protože v plášti je rychlost světla nulová",
            "Protože paprsky na okraji mají kratší geometrickou dráhu než paprsek v ose"
        ],
        "ans": 0,
        "exp": "Rychlost světla v prostředí je nepřímo úměrná indexu lomu (v = c/n). Nižší index lomu u okraje jádra znamená vyšší rychlost šíření, která vykompenzuje delší dráhu."
    },
    {
        "id": 13, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Který typ optického vlákna zcela eliminuje vidovou (modální) disperzi?",
        "options": [
            "Jednovidové vlákno (Singlemode – SM, 9/125 µm)",
            "Mnohovidové vlákno se skokovou změnou indexu lomu (MM Step-Index)",
            "Mnohovidové gradientní vlákno (MM Graded-Index 62,5/125 µm)",
            "Plastové mnohovidové vlákno (POF)"
        ],
        "ans": 0,
        "exp": "V jednovidovém (SM) vlákně se díky malému průměru jádra (9 µm) šíří pouze jediný (základní) vid, takže vidová disperze je nulová."
    },
    {
        "id": 14, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Jaké tři základní vlnové délky (přenosová okna) se standardně používají v optických sítích?",
        "options": [
            "850 nm, 1300/1310 nm a 1550 nm",
            "400 nm, 550 nm a 700 nm",
            "100 MHz, 250 MHz a 500 MHz",
            "650 nm, 980 nm a 2400 nm"
        ],
        "ans": 0,
        "exp": "Tři hlavní přenosová okna v infračervené oblasti jsou: 1. okno 850 nm (MM), 2. okno 1300 nm (MM) / 1310 nm (SM) a 3. okno 1550 nm (SM)."
    },
    {
        "id": 15, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Které přenosové okno vykazuje v křemičitém skle absolutně nejnižší měrný útlum (cca 0,2 dB/km) a používá se pro dálkové jednovidové (SM) trasy?",
        "options": [
            "1550 nm (3. přenosové okno)",
            "850 nm (1. přenosové okno)",
            "1300 nm (u mnohovidových vláken)",
            "62,5 nm"
        ],
        "ans": 0,
        "exp": "Ve 3. okně na vlnové délce 1550 nm má křemičité sklo absolutní minimum útlumu kolem 0,2 dB/km."
    },
    {
        "id": 16, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Které vlnové délky se typicky používají u mnohovidových (Multimode – MM) optických vláken?",
        "options": [
            "850 nm a 1300 nm",
            "1310 nm a 1550 nm",
            "1550 nm a 1625 nm",
            "Pouze 1550 nm"
        ],
        "ans": 0,
        "exp": "Mnohovidová (MM) vlákna pracují v 1. a 2. okně na vlnových délkách 850 nm a 1300 nm (jednovidová SM na 1310 nm a 1550 nm)."
    },
    {
        "id": 17, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "V jakých jednotkách se podle zápisků z hodin běžně udává frekvence světla v optických vláknech?",
        "options": [
            "V terahertzích (THz)",
            "V kilohertzích (kHz)",
            "V megahertzích (MHz)",
            "V decibelech (dB)"
        ],
        "ans": 0,
        "exp": "Zatímco metalické kabely pracují v kHz až MHz (max. GHz), frekvence světla v optice leží v řádu stovek terahertzů (THz)."
    },

    # =========================================================================
    # OKRUH: OPTIKA 2 – Podmínka přenosu, index lomu, NA, úhel navázání, vložný útlum
    # =========================================================================
    {
        "id": 18, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Co je základní fyzikální podmínkou pro přenos světla v optickém vlákně?",
        "options": [
            "Jev totálního (úplného) vnitřního odrazu na rozhraní jádra a pláště (n₁ > n₂ a úhel dopadu α > α_m)",
            "Jev částečného lomu paprsku do primární ochrany (n₁ < n₂)",
            "Supravodivost křemičitého skla při průchodu elektrického proudu",
            "Odraz světla od vnějšího kovového stínění STP"
        ],
        "ans": 0,
        "exp": "Světlo je ve vlákně vedeno díky totálnímu vnitřnímu odrazu na rozhraní jádro/plášť, což vyžaduje n₁ > n₂ a úhel dopadu větší než mezní úhel (α > α_m)."
    },
    {
        "id": 19, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Jaký vztah musí platit mezi indexem lomu jádra (n₁) a indexem lomu pláště (n₂), aby mohlo v optickém vlákně dojít k totálnímu odrazu?",
        "options": [
            "n₁ > n₂ (jádro musí mít vyšší index lomu než plášť)",
            "n₁ < n₂ (plášť musí mít vyšší index lomu než jádro)",
            "n₁ = n₂ (oba indexy lomu musí být shodné)",
            "n₁ · n₂ = 0"
        ],
        "ans": 0,
        "exp": "Totální odraz nastává pouze při přechodu světla z opticky hustšího prostředí (jádro n₁) do opticky řidšího prostředí (plášť n₂), tedy n₁ > n₂."
    },
    {
        "id": 20, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Co musí platit pro úhel dopadu paprsku α na rozhraní jádro–plášť, aby nastal totální vnitřní odraz?",
        "options": [
            "Úhel dopadu α musí být větší než mezní (kritický) úhel α_m (kde sin α_m = n₂ / n₁)",
            "Úhel dopadu α musí být menší než mezní úhel α_m (α < α_m)",
            "Úhel dopadu α musí být roven 0° (kolmý dopad na plášť)",
            "Úhel dopadu α musí být přesně 45° bez ohledu na indexy lomu"
        ],
        "ans": 0,
        "exp": "Při α > α_m se paprsek již neláme do pláště, ale 100% se odráží zpět do jádra."
    },
    {
        "id": 21, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Co je to index lomu (n) a jaký je jeho vzorec?",
        "options": [
            "Poměr rychlosti světla ve vakuu (c) k fázové rychlosti světla v daném prostředí (v), tedy n = c / v",
            "Poměr průměru pláště k průměru jádra, tedy n = d₂ / d₁",
            "Součin rychlosti světla a vlnové délky, tedy n = c · λ",
            "Rozdíl útlumu na vstupu a výstupu vlákna v decibelech"
        ],
        "ans": 0,
        "exp": "Index lomu n = c / v je bezrozměrná veličina udávající, kolikrát pomaleji se světlo šíří v daném prostředí než ve vakuu."
    },
    {
        "id": 22, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Pokud je index lomu křemičitého skla v jádře přibližně n = 1,5 a rychlost světla ve vakuu c = 300 000 km/s, jakou rychlostí v se světlo šíří ve skle?",
        "options": [
            "Přibližně 200 000 km/s (protože v = c / n)",
            "Přibližně 450 000 km/s (protože v = c · n)",
            "Stále 300 000 km/s",
            "Přibližně 150 000 m/s"
        ],
        "ans": 0,
        "exp": "Ze vzorce n = c / v plyne v = c / n = 300 000 / 1,5 = 200 000 km/s."
    },
    {
        "id": 23, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Co vyjadřuje maximální úhel navázání (θ_max, akceptační úhel) u optického vlákna?",
        "options": [
            "Maximální úhel vůči podélné ose vlákna, pod kterým může paprsek vstoupit do čela jádra, aby uvnitř ještě nastal totální odraz",
            "Maximální úhel, o který lze optický kabel ohnout v rozvaděči bez zlomení",
            "Úhel, pod kterým se brousí čelo konektoru APC (8°)",
            "Minimální úhel dopadu na rozhraní primární a sekundární ochrany"
        ],
        "ans": 0,
        "exp": "Paprsky vstupující do čela vlákna pod úhlem menším nebo rovným θ_max (uvnitř akceptačního kužele) splní uvnitř vlákna podmínku totálního odrazu."
    },
    {
        "id": 24, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Který vzorec správně definuje numerickou aperturu (NA) optického vlákna ve vzduchu (n₀ = 1)?",
        "options": [
            "NA = sin(θ_max) = √(n₁² − n₂²)",
            "NA = cos(θ_max) = n₁ / n₂",
            "NA = √(n₁² + n₂²) · d_jádra",
            "NA = c / v"
        ],
        "ans": 0,
        "exp": "Numerická apertura je rovna sinu maximálního úhlu navázání θ_max a vypočítá se jako odmocnina z rozdílu druhých mocnin indexů lomu jádra a pláště: √(n₁² − n₂²)."
    },
    {
        "id": 25, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "CHYTÁK Z TESTU: Souvisí numerická apertura (NA) s průměrem optického vlákna?",
        "options": [
            "Ne, vůbec nesouvisí – závisí výhradně na indexech lomu jádra (n₁) a pláště (n₂)",
            "Ano, čím větší je průměr jádra, tím větší je numerická apertura podle vzorce",
            "Ano, numerická apertura je přímo úměrná průměru pláště 125 µm",
            "Ano, u 9µm vlákna je NA vždy 9× menší než u 50µm vlákna se stejným sklem"
        ],
        "ans": 0,
        "exp": "Ve vzorci NA = √(n₁² − n₂²) průměr vlákna vůbec nevystupuje! NA závisí pouze na materiálovém složení (indexech lomu n₁ a n₂)."
    },
    {
        "id": 26, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Jakou hodnotu numerické apertury (NA) u optického vlákna požadujeme?",
        "options": [
            "Jde o kompromis: velkou NA chceme pro snadné navázání výkonu ze zdroje, ale malou NA pro malou vidovou disperzi (velkou šířku pásma)",
            "Požadujeme vždy co největší NA (blízkou 1,0), protože tím klesá vidová disperze na nulu",
            "Požadujeme vždy nulovou NA (NA = 0), aby do vlákna nevnikalo žádné světlo",
            "Požadujeme NA v decibelech větší než 50 dB"
        ],
        "ans": 0,
        "exp": "Velká NA sice naváže více světla (širší kužel), ale paprsky pod velkými úhly mají delší dráhu a zvyšují vidovou disperzi. Proto se volí kompromis."
    },
    {
        "id": 27, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Co by způsobila příliš velká numerická apertura (NA) u mnohovidového vlákna?",
        "options": [
            "Snadnější navázání světla ze zdroje, ale zároveň velkou vidovou disperzi a menší šířku pásma",
            "Úplné vymizení vidové disperze a neomezenou šířku pásma",
            "Nemožnost navázat do vlákna světlo z LED diody",
            "Zvětšení průměru pláště ze 125 µm na 900 µm"
        ],
        "ans": 0,
        "exp": "Velká NA znamená velký úhel θ_max, takže do vlákna vstupují i velmi šikmé paprsky, které urazí mnohem delší dráhu než osový paprsek → roste vidová disperze."
    },
    {
        "id": 28, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Co je to vložný útlum (Insertion Loss – IL) u optických vláken?",
        "options": [
            "Ztráta optického výkonu (v dB) způsobená vložením spoje (konektoru, sváru) nebo pasivního prvku do optické trasy",
            "Zesílení signálu v optickém zesilovači EDFA",
            "Přeslech mezi dvěma kroucenými metalickými páry na vzdáleném konci",
            "Poměr rychlosti světla ve vakuu k rychlosti světla v jádře"
        ],
        "ans": 0,
        "exp": "Vložný útlum udává v decibelech pokles optického výkonu při průchodu spojem (konektorem, svárem) nebo prvkem."
    },
    {
        "id": 29, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Jakými příčinami vzniká vložný útlum na optickém spoji?",
        "options": [
            "Fresnelovým odrazem na vzduchové mezeře, geometrickými nepřesnostmi (osové/úhlové přesazení jader, mezera) a nečistotami či rozdílným průměrem/NA vláken",
            "Elektromagnetickou indukcí z okolních silových kabelů 230 V",
            "Použitím příliš krátkého patch kabelu pracovní plochy",
            "Nedodržením barevného schématu T568B na konektoru RJ-45"
        ],
        "ans": 0,
        "exp": "Vložný útlum v optice vzniká na rozhraní čel konektorů/svárů kvůli Fresnelovu odrazu, geometrickým odchylkám (nesouosost, úhel, mezera) a nečistotám."
    },

    # =========================================================================
    # OKRUH: KABELÁŽ 8 – Normy strukturované kabeláže v ČR
    # =========================================================================
    {
        "id": 30, "topic": "sk-8", "topic_label": "Otázka 8: Normy v ČR",
        "q": "Podle jakých norem můžeme v ČR vytvořit strukturovanou kabeláž (dle tvého výpisu z hodin)?",
        "options": [
            "Podle norem ČSN EN 50173 a ČSN EN 50174 (české převzetí evropských norem EN)",
            "Podle norem ČSN 73 0802 a IEEE 802.11ac",
            "Výhradně podle japonské normy JIS X 5150",
            "Podle norem ITU-T G.711 a G.729"
        ],
        "ans": 0,
        "exp": "V ČR se strukturovaná kabeláž buduje podle ČSN EN 50173 (návrh univerzální kabeláže) a ČSN EN 50174 (instalace), což je české převzetí evropských norem EN."
    },
    {
        "id": 31, "topic": "sk-8", "topic_label": "Otázka 8: Normy v ČR",
        "q": "O jaký původ norem jde u označení ČSN EN 50173 a ČSN EN 50174?",
        "options": [
            "Jde o české převzetí evropské normy EN (vycházející z mezinárodní ISO/IEC 11801)",
            "Jde o ryze americkou normu bez platnosti v Evropské unii",
            "Jde o normu pro bezdrátové sítě Wi-Fi a Bluetooth",
            "Jde o normu pro komprimaci hlasu A-law v PCM systémech"
        ],
        "ans": 0,
        "exp": "Zkratka ČSN EN znamená, že jde o českou technickou normu přebírající evropskou normu EN."
    },
    {
        "id": 32, "topic": "sk-8", "topic_label": "Otázka 8: Normy v ČR",
        "q": "Která dvojice norem tvoří v ČR základ pro návrh (50173) a instalaci (50174) strukturované kabeláže?",
        "options": [
            "ČSN EN 50173 a ČSN EN 50174",
            "ČSN EN 10000 a ČSN EN 20000",
            "RFC 3550 a RFC 2544",
            "IEEE 802.3af a IEEE 802.1Q"
        ],
        "ans": 0,
        "exp": "ČSN EN 50173 definuje univerzální kabelážní systémy a ČSN EN 50174 pravidla pro jejich instalaci."
    },

    # =========================================================================
    # OKRUH: KABELÁŽ 9 – Kabely UTP, FTP, STP, kategorie a plastový kříž („rybí kost“)
    # =========================================================================
    {
        "id": 33, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Co znamená zkratka UTP a jaká je jeho základní konstrukce?",
        "options": [
            "Unshielded Twisted Pair – nestíněná kroucená dvojlinka bez kovového stínění, skládající se ze 4 párů (8 žil/vodičů)",
            "Ultra Twisted Polymer – optický kabel se 4 skleněnými vlákny a hliníkovým pláštěm",
            "Universal Twin Port – stíněný kabel se 2 páry vodičů pro kategorii 7",
            "Unshielded Telephone Plug – 6pinový telefonní konektor"
        ],
        "ans": 0,
        "exp": "UTP = Unshielded Twisted Pair (nestíněná kroucená dvojlinka), nemá kovové stínění a obsahuje 4 páry = 8 vodičů."
    },
    {
        "id": 34, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Z kolika párů a kolika jednotlivých žil (vodičů) se skládá standardní kabel UTP / STP?",
        "options": [
            "Ze 4 párů (celkem 8 žil / vodičů)",
            "Ze 2 párů (celkem 4 žíly / vodiče)",
            "Z 8 párů (celkem 16 žil / vodičů)",
            "Ze 6 párů (celkem 12 žil / vodičů)"
        ],
        "ans": 0,
        "exp": "Standardní datový kabel pro strukturovanou kabeláž obsahuje 4 kroucené páry, tedy 8 jednotlivých vodičů."
    },
    {
        "id": 35, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "V jaké kategorii (a třídě) se podle tvého výpisu z hodin typicky využívají nestíněné kabely UTP a od které kategorie se využívá STP?",
        "options": [
            "UTP má využití do kategorie 6 (třída E); STP se využívá v kategorii 6a a výš (třída Ea a výš)",
            "UTP se využívá pouze v kategorii 1; STP se využívá pouze v kategorii 3",
            "UTP se využívá v kategorii 7 a 8; STP pouze do kategorie 5e",
            "UTP i STP lze bez omezení používat až do kategorie 8 (2000 MHz)"
        ],
        "ans": 0,
        "exp": "Přesně dle zápisků z hodin: UTP má využití v kategorii 6 (třída E), zatímco STP (kde je každý pár samostatně stíněný) se využívá v kategorii 6a a výš (Ea a výš)."
    },
    {
        "id": 36, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Co je to kabel FTP (Foiled Twisted Pair) podle zápisků z hodin?",
        "options": [
            "Kompromis mezi UTP a STP – kroucená dvojlinka s celkovým stíněním z hliníkové fólie kolem všech 4 párů dohromady (jednotlivé páry stíněné nejsou)",
            "Kabel, kde je každý ze 4 párů samostatně stíněný, ale chybí vnější plastový plášť",
            "Čistě optický kabel určený pro protokol File Transfer Protocol",
            "Nestíněný kabel bez jakékoliv hliníkové fólie"
        ],
        "ans": 0,
        "exp": "FTP = Foiled Twisted Pair je kompromis mezi UTP a STP: má společnou hliníkovou fólii kolem všech 4 párů dohromady, ale jednotlivé páry samostatně stíněné nejsou."
    },
    {
        "id": 37, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Jak je stíněný kabel STP (Shielded Twisted Pair) podle tvého výpisu z hodin a obrázku průřezu?",
        "options": [
            "Stejná struktura 4 párů jako UTP, ale každý pár je samostatně stíněný (pair shield)",
            "Nemá vůbec žádné kovové stínění, pouze silnější PVC plášť",
            "Má stíněný pouze jeden modrý pár a ostatní tři páry jsou nestíněné",
            "Stínění je tvořeno pouze středovým plastovým křížem"
        ],
        "ans": 0,
        "exp": "U STP (dle obrázku a zápisků z hodin) má kabel stejnou strukturu jako UTP, ale každý pár je samostatně stíněný (pair shield)."
    },
    {
        "id": 38, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "K čemu slouží plastový kříž (tzv. „rybí kost“) uvnitř metalického kabelu a pro kterou kategorii je typický?",
        "options": [
            "Je typický pro kategorii 6 (Cat 6) a slouží k mechanickému oddělení jednotlivých párů, aby nešly moc k sobě",
            "Je typický pro kategorii 3 a slouží k vedení elektrického napájení 230 V",
            "Je typický pro optická vlákna 9/125 µm a slouží k odrážení světla",
            "Slouží k uzemnění stínění u konektoru RJ-11"
        ],
        "ans": 0,
        "exp": "Plastový středový kříž („rybí kost“) je typický pro kabely kategorie 6 – drží 4 páry od sebe, aby se minimalizovaly přeslechy."
    },
    {
        "id": 39, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Jaké jsou hlavní praktické výhody kabelu UTP oproti stíněnému STP?",
        "options": [
            "Je levnější, jednodušší na instalaci a po sundání pláště rovnou vidíme barvy vodičů vlastním okem",
            "Dosahuje vyšší odolnosti proti elektromagnetickému rušení a používá se v kategorii 7a",
            "Má samostatné fóliové stínění kolem každého páru",
            "Umožňuje přenos na vzdálenost 1500 metrů bez opakovače"
        ],
        "ans": 0,
        "exp": "UTP nemá kovové stínění, proto je levnější, ohebnější, jednodušší na instalaci a barvy žil jsou ihned viditelné."
    },

    # =========================================================================
    # OKRUH: KABELÁŽ 10 – Proč používáme technologii kroucených párů?
    # =========================================================================
    {
        "id": 40, "topic": "sk-10", "topic_label": "Otázka 10: Kroucené páry",
        "q": "Proč ve strukturované kabeláži používáme technologii kroucených párů?",
        "options": [
            "Abychom omezili elektromagnetické rušení (EMI) a přeslechy mezi jednotlivými vodiči a páry, a zajistili tak spolehlivější přenos dat",
            "Aby se do kabelu vešlo více mědi a zvýšila se elektrická kapacita vedení",
            "Aby v kabelu vznikal totální vnitřní odraz světla",
            "Protože rovné vodiče nelze nacvaknout do konektoru RJ-45"
        ],
        "ans": 0,
        "exp": "Vzájemné zkroucení vodičů v kombinaci s diferenciálním přenosem omezuje elektromagnetické rušení z okolí i přeslechy mezi páry."
    },
    {
        "id": 41, "topic": "sk-10", "topic_label": "Otázka 10: Kroucené páry",
        "q": "Proč má každý ze 4 párů v kabelu UTP/STP jinou hustotu zákrutů (různý krok zkrutu)?",
        "options": [
            "Aby se omezily vzájemné přeslechy a rušení mezi sousedními páry uvnitř kabelu",
            "Aby šlo podle hmatu poznat barvu vodiče ve tmě",
            "Kvůli úspoře mědi u hnědého a modrého páru",
            "Aby měl každý pár jinou maximální délku (90 m až 1500 m)"
        ],
        "ans": 0,
        "exp": "Kdyby měly sousední páry shodnou hustotu zákrutů, jejich smyčky by ležely souběžně proti sobě a docházelo by k silným přeslechům."
    },
    {
        "id": 42, "topic": "sk-10", "topic_label": "Otázka 10: Kroucené páry",
        "q": "Jak probíhá přenos signálu v jednom krouceném páru a jak jej vyhodnocuje přijímač?",
        "options": [
            "Jeden vodič přenáší kladnou polaritu signálu (+U), druhý opačnou polaritu (−U) a přijímač vyhodnocuje rozdíl napětí mezi vodiči",
            "Jeden vodič přenáší data tam, druhý slouží pouze jako nulový zemnící drát a přijímač měří proud",
            "Oba vodiče přenášejí stejnou kladnou polaritu a přijímač napětí sčítá",
            "Jeden vodič přenáší optický signál a druhý elektrické napájení"
        ],
        "ans": 0,
        "exp": "Při diferenciálním (symetrickém) přenosu nese jeden vodič +U, druhý −U a přijímač vyhodnocuje rozdíl napětí mezi nimi – soufázové rušení naindukované do obou vodičů se tím odečte."
    },
    {
        "id": 43, "topic": "sk-10", "topic_label": "Otázka 10: Kroucené páry",
        "q": "Co se stane s vnějším elektromagnetickým rušením, které se naindukuje do obou zkroucených vodičů páru?",
        "options": [
            "Protože přijímač vyhodnocuje rozdíl napětí mezi oběma vodiči, naindukované soufázové rušení se v přijímači odečte (vyruší)",
            "Rušení se v přijímači zdvojnásobí, a proto je nutné vždy použít optiku",
            "Rušení se přemění na světlo o vlnové délce 850 nm",
            "Rušení zvýší přenosovou rychlost z 1 Gbps na 10 Gbps"
        ],
        "ans": 0,
        "exp": "Díky zkroucení jsou oba vodiče vystaveny stejnému vnějšímu rušivému poli; při odečtení obou signálů v diferenciálním přijímači se rušivá složka vyruší."
    },

    # =========================================================================
    # OKRUH: KABELÁŽ 11 – Normy definující třídy linek + tabulka tříd a frekvencí
    # =========================================================================
    {
        "id": 44, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Které dvě normy definují třídy linek (A, B, C, D, E, Ea, F, Fa, I & II)?",
        "options": [
            "ČSN EN 50173 (evropská norma) a ISO/IEC 11801 (mezinárodní norma)",
            "TIA/EIA-568A a TIA/EIA-568B",
            "IEEE 802.3 a IEEE 802.11",
            "ITU-T G.732 a G.703"
        ],
        "ans": 0,
        "exp": "Písmenné třídy linek (Classes) definují evropská norma ČSN EN 50173 a mezinárodní norma ISO/IEC 11801."
    },
    {
        "id": 45, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Co znamenají zkratky ISO a IEC u mezinárodní normy ISO/IEC 11801?",
        "options": [
            "ISO = International Organization for Standardization (Mezinárodní organizace pro normalizaci), IEC = International Electrotechnical Commission (Mezinárodní elektrotechnická komise)",
            "ISO = Internal System Optics, IEC = Internet Ethernet Cabling",
            "ISO = Institute of Shielded Optics, IEC = International European Cabling",
            "ISO = Integrated Signal Output, IEC = Insertion Error Control"
        ],
        "ans": 0,
        "exp": "Přesně dle výpisu z hodin: ISO = International Organization for Standardization, IEC = International Electrotechnical Commission."
    },
    {
        "id": 46, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Jaký je frekvenční rozsah a odpovídající kategorie pro Třídu A?",
        "options": [
            "Specifikováno do 100 kHz, Kategorie 1 (analogový telefon)",
            "Specifikováno do 1 MHz, Kategorie 2 (ISDN)",
            "Specifikováno do 16 MHz, Kategorie 3",
            "Specifikováno do 100 MHz, Kategorie 5"
        ],
        "ans": 0,
        "exp": "Třída A je specifikována do 100 kHz (odpovídá Kategorii 1 pro analogový telefon)."
    },
    {
        "id": 47, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Jaký je frekvenční rozsah a odpovídající kategorie pro Třídu B?",
        "options": [
            "Specifikováno do 1 MHz, Kategorie 2 (ISDN, 10Base-T, Token Ring 4 MB)",
            "Specifikováno do 100 kHz, Kategorie 1",
            "Specifikováno do 16 MHz, Kategorie 3",
            "Specifikováno do 250 MHz, Kategorie 6"
        ],
        "ans": 0,
        "exp": "Třída B je specifikována do 1 MHz (odpovídá Kategorii 2)."
    },
    {
        "id": 48, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Jaký je frekvenční rozsah a odpovídající kategorie pro Třídu C?",
        "options": [
            "Specifikováno do 16 MHz, Kategorie 3 (10 Mbps, Token Ring 16 MB)",
            "Specifikováno do 1 MHz, Kategorie 2",
            "Specifikováno do 100 MHz, Kategorie 5",
            "Specifikováno do 500 MHz, Kategorie 6a"
        ],
        "ans": 0,
        "exp": "Třída C je specifikována do 16 MHz a odpovídá Kategorii 3."
    },
    {
        "id": 49, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Jaký je frekvenční rozsah pro Třídu D (Kategorie 5) a Třídu D 2002 (Kategorie 5e) dle tabulky z hodin?",
        "options": [
            "Třída D (Cat 5): do 100 MHz (100 Mbps Fast Ethernet); Třída D 2002 (Cat 5e): 100 MHz (350 MHz) pro 1 Gbps Gigabit Ethernet",
            "Třída D: do 16 MHz; Třída D 2002: do 250 MHz",
            "Třída D: do 250 MHz; Třída D 2002: do 500 MHz",
            "Třída D: do 600 MHz; Třída D 2002: do 1000 MHz"
        ],
        "ans": 0,
        "exp": "Třída D je specifikována do 100 MHz (Cat 5, 100 Mbps); u D 2002 (Cat 5e, 1 Gbps) uvádí tabulka z hodin 100 MHz (350 MHz)."
    },
    {
        "id": 50, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Jaký je frekvenční rozsah, kategorie a přenosová rychlost pro Třídu E?",
        "options": [
            "Do 250 MHz, Kategorie 6, 1 Gbps – Gigabit Ethernet (1000Base-T)",
            "Do 100 MHz, Kategorie 5, 100 Mbps",
            "Do 500 MHz, Kategorie 6a, 10 Gbps",
            "Do 600 MHz, Kategorie 7, 10 Gbps"
        ],
        "ans": 0,
        "exp": "Třída E odpovídá Kategorii 6 a je specifikována do 250 MHz (1 Gbps Gigabit Ethernet)."
    },
    {
        "id": 51, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Jaký je frekvenční rozsah, kategorie a přenosová rychlost pro Třídu Ea?",
        "options": [
            "Do 500 MHz, Kategorie 6a, 10 Gbps (10GBase-T)",
            "Do 250 MHz, Kategorie 6, 1 Gbps",
            "Do 600 MHz, Kategorie 7, 10 Gbps",
            "Do 1000 MHz, Kategorie 7a, 40 Gbps"
        ],
        "ans": 0,
        "exp": "Třída Ea odpovídá Kategorii 6a, pracuje do 500 MHz a přenáší 10 Gbps (10GBase-T)."
    },
    {
        "id": 52, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Jaké jsou frekvenční rozsahy pro Třídu F (Kategorie 7) a Třídu Fa (Kategorie 7a)?",
        "options": [
            "Třída F (Cat 7): do 600 MHz; Třída Fa (Cat 7a): do 1000 MHz (oboje 10 Gbps)",
            "Třída F (Cat 7): do 250 MHz; Třída Fa (Cat 7a): do 500 MHz",
            "Třída F (Cat 7): do 500 MHz; Třída Fa (Cat 7a): do 2000 MHz",
            "Třída F (Cat 7): do 100 MHz; Třída Fa (Cat 7a): do 350 MHz"
        ],
        "ans": 0,
        "exp": "Třída F (Cat 7) je specifikována do 600 MHz a Třída Fa (Cat 7a) do 1000 MHz (1 GHz)."
    },
    {
        "id": 53, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Jaký je frekvenční rozsah, kategorie a rychlost pro Třídy I & II podle tabulky z hodin?",
        "options": [
            "1600 / 2000 MHz, Kategorie 8, 40 Gbps (40GBase-T) do 30 m",
            "500 MHz, Kategorie 6a, 10 Gbps do 100 m",
            "1000 MHz, Kategorie 7a, 100 Gbps do 1500 m",
            "16 MHz, Kategorie 3, 10 Mbps"
        ],
        "ans": 0,
        "exp": "Třída I & II odpovídá Kategorii 8 se šířkou pásma 1600/2000 MHz (2 GHz) pro přenos 40 Gbps (40GBase-T) na vzdálenost do 30 m."
    },
    {
        "id": 54, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Která třída linky má horní frekvenční mez 250 MHz?",
        "options": [
            "Třída E (Kategorie 6)",
            "Třída D (Kategorie 5)",
            "Třída Ea (Kategorie 6a)",
            "Třída F (Kategorie 7)"
        ],
        "ans": 0,
        "exp": "250 MHz = Třída E (Cat 6). (100 MHz = D, 500 MHz = Ea, 600 MHz = F, 1000 MHz = Fa)."
    },
    {
        "id": 55, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Která třída linky má horní frekvenční mez 500 MHz?",
        "options": [
            "Třída Ea (Kategorie 6a)",
            "Třída E (Kategorie 6)",
            "Třída F (Kategorie 7)",
            "Třída Fa (Kategorie 7a)"
        ],
        "ans": 0,
        "exp": "500 MHz = Třída Ea (Kategorie 6a, 10GBase-T)."
    },
    {
        "id": 56, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Která třída linky má horní frekvenční mez 600 MHz?",
        "options": [
            "Třída F (Kategorie 7)",
            "Třída Ea (Kategorie 6a)",
            "Třída Fa (Kategorie 7a)",
            "Třída E (Kategorie 6)"
        ],
        "ans": 0,
        "exp": "600 MHz = Třída F (Kategorie 7)."
    },
    {
        "id": 57, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Která třída linky má horní frekvenční mez 1000 MHz (1 GHz)?",
        "options": [
            "Třída Fa (Kategorie 7a)",
            "Třída F (Kategorie 7)",
            "Třída I & II (Kategorie 8)",
            "Třída Ea (Kategorie 6a)"
        ],
        "ans": 0,
        "exp": "1000 MHz = Třída Fa (Kategorie 7a)."
    },

    # =========================================================================
    # OKRUH: KABELÁŽ 12 – Co je to FEXT a jaký útlum FEXT požadujeme?
    # =========================================================================
    {
        "id": 58, "topic": "sk-12", "topic_label": "Otázka 12: Přeslech FEXT",
        "q": "Co znamená zkratka FEXT a o jaký jev se jedná?",
        "options": [
            "Far-End Crosstalk – přeslech na vzdáleném konci kabelu (rušení z jednoho páru do druhého měřené na opačném konci kabelu, než kde signál vzniká)",
            "Fast Ethernet Extended Transmission – protokol pro prodloužení dosahu UTP kabelu na 500 m",
            "Fiber External Termination – optická zásuvka na pracovní ploše",
            "Near-End Crosstalk – přeslech měřený na stejném konci kabelu, kde je vysílač"
        ],
        "ans": 0,
        "exp": "FEXT (Far-End Crosstalk) je přeslech na vzdáleném konci – nežádoucí rušení indukované z jednoho páru do jiného, měřené na opačném konci kabelu."
    },
    {
        "id": 59, "topic": "sk-12", "topic_label": "Otázka 12: Přeslech FEXT",
        "q": "CHYTÁK Z TESTU: Jaký útlum přeslechu FEXT (v dB) u strukturované kabeláže požadujeme?",
        "options": [
            "Požadujeme co nejvyšší (největší) hodnotu útlumu FEXT v decibelech (dB), aby vzájemné rušení mezi páry bylo co nejmenší",
            "Požadujeme co nejnižší (nulový) útlum FEXT v dB, aby přeslech prošel kabelem bez ztrát",
            "Požadujeme záporný útlum FEXT, aby se rušení mezi páry zesilovalo",
            "Útlum FEXT požadujeme přesně 0 dB"
        ],
        "ans": 0,
        "exp": "Zásadní pravidlo z hodin: Útlum přeslechu v dB udává míru potlačení nežádoucího rušení. Čím vyšší je útlum přeslechu FEXT v dB, tím menší je rušení a tím kvalitnější je kabeláž!"
    },
    {
        "id": 60, "topic": "sk-12", "topic_label": "Otázka 12: Přeslech FEXT",
        "q": "Na kterém konci kabelu se měří přeslech FEXT?",
        "options": [
            "Na opačném (vzdáleném) konci kabelu, než kde rušící signál vzniká (kde je vysílač)",
            "Na stejném (bližším) konci kabelu, kde je umístěn vysílač",
            "Uprostřed kabelu v místě plastového kříže",
            "Pouze na optickém rozvaděči CD"
        ],
        "ans": 0,
        "exp": "Far-End = vzdálený konec, tedy opačný konec kabelu oproti zdroji signálu."
    },
    {
        "id": 61, "topic": "sk-12", "topic_label": "Otázka 12: Přeslech FEXT",
        "q": "Pokud má kabel A útlum přeslechu FEXT 45 dB a kabel B útlum přeslechu FEXT 25 dB, který kabel je kvalitnější a má menší vzájemné rušení párů?",
        "options": [
            "Kabel A (45 dB), protože vyšší útlum přeslechu v dB znamená silnější potlačení nežádoucího rušení",
            "Kabel B (25 dB), protože nižší číslo v dB vždy znamená lepší kabel",
            "Oba kabely mají shodné rušení",
            "Nelze určit, protože FEXT se měří v megahertzích"
        ],
        "ans": 0,
        "exp": "Čím vyšší je hodnota útlumu přeslechu FEXT v dB (45 dB > 25 dB), tím více je nežádoucí přeslech utlumen a tím méně se páry ruší."
    },

    # =========================================================================
    # OKRUH: KABELÁŽ 13 – 3 subsystémy generické kabeláže, délky a přídavné šňůry A, B, E
    # =========================================================================
    {
        "id": 62, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Které jsou 3 základní subsystémy generické strukturované kabeláže?",
        "options": [
            "1. Subsystém páteřní kabeláže areálu, 2. Subsystém páteřní kabeláže budovy, 3. Subsystém horizontální kabeláže",
            "1. Subsystém pracovní plochy, 2. Subsystém přídavných šňůr, 3. Subsystém konektorů RJ-45",
            "1. Jádro, 2. Plášť, 3. Primární ochrana",
            "1. Subsystém UTP, 2. Subsystém FTP, 3. Subsystém STP"
        ],
        "ans": 0,
        "exp": "Tři základní subsystémy generické SK jsou: páteřní kabeláž areálu (CD→BD), páteřní kabeláž budovy (BD→FD) a horizontální kabeláž (FD→TO)."
    },
    {
        "id": 63, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Jaké jsou přesné maximální délky a typy kabelů pro jednotlivé 3 subsystémy podle tvého výpisu z hodin?",
        "options": [
            "Páteř areálu (CD→BD): optika max. 1500 m; Páteř budovy (BD→FD): optika max. 500 m; Horizontální kabeláž (FD→TO): metalika max. 90 m",
            "Páteř areálu: metalika max. 90 m; Páteř budovy: metalika max. 100 m; Horizontální kabeláž: optika max. 1500 m",
            "Všechny tři subsystémy mají shodnou maximální délku 100 m",
            "Páteř areálu: 500 m; Páteř budovy: 1500 m; Horizontální kabeláž: 5 m"
        ],
        "ans": 0,
        "exp": "Přesně dle výpisu z hodin: 1. Páteř areálu = optika max. 1500 m (CD→BD), 2. Páteř budovy = optika max. 500 m (BD→FD), 3. Horizontální kabeláž = metalické kabely max. 90 m (FD→TO)."
    },
    {
        "id": 64, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Které rozvaděče spojuje Subsystém páteřní kabeláže areálu a jaká je jeho maximální délka (dle zápisků z hodin)?",
        "options": [
            "Spojuje CD (Campus Distributor – rozvaděč areálu) → BD (Building Distributor – rozvaděč budovy), optika, max. délka 1500 m",
            "Spojuje BD → FD (Floor Distributor), optika, max. délka 500 m",
            "Spojuje FD → TO (telekomunikační zásuvka), metalika, max. délka 90 m",
            "Spojuje TO → PC na pracovní ploše, max. délka 5 m"
        ],
        "ans": 0,
        "exp": "Subsystém páteřní kabeláže areálu propojuje CD → BD optickým kabelem o maximální délce 1500 m."
    },
    {
        "id": 65, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Které rozvaděče spojuje Subsystém páteřní kabeláže budovy a jaká je jeho maximální délka (dle zápisků z hodin)?",
        "options": [
            "Spojuje BD (Building Distributor) → FD (Floor Distributor – patrový rozvaděč), optika, max. délka 500 m",
            "Spojuje CD → BD, optika, max. délka 1500 m",
            "Spojuje FD → TO, metalika, max. délka 90 m",
            "Spojuje panel a switch v rozvaděči, max. délka 5 m"
        ],
        "ans": 0,
        "exp": "Subsystém páteřní kabeláže budovy propojuje BD → FD optickým kabelem o maximální délce 500 m."
    },
    {
        "id": 66, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Co spojuje Subsystém horizontální kabeláže a jaká je jeho maximální délka bez přídavných šňůr?",
        "options": [
            "Spojuje patrový rozvaděč FD → telekomunikační zásuvku TO (případně přes konsolidační bod CP), metalické kabely, max. délka 90 m",
            "Spojuje zásuvku TO → PC, max. délka 100 m",
            "Spojuje rozvaděč budovy BD → patrový rozvaděč FD, max. délka 500 m",
            "Spojuje CD → TO, max. délka 1500 m"
        ],
        "ans": 0,
        "exp": "Horizontální kabeláž vede od patrového rozvaděče FD k telekomunikační zásuvce TO a měří maximálně 90 m (nezahrnuje přídavné šňůry)."
    },
    {
        "id": 67, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Jaké tři typy přídavných šňůr (A, B, E) existují v horizontálním kanálu a jaké jsou jejich maximální délky podle tabulky z hodin?",
        "options": [
            "Šňůra A (pracovní plocha, TO → PC): max. 5 m; Šňůra B (rozvaděč FD, panel ↔ panel): max. 10 m (při A,E≈0); Šňůra E (rozvaděč FD, panel → switch): max. 5 m",
            "Šňůra A: max. 90 m; Šňůra B: max. 500 m; Šňůra E: max. 1500 m",
            "Šňůra A: max. 10 m; Šňůra B: max. 5 m; Šňůra E: max. 20 m",
            "Šňůra A, B i E mají každá maximální délku 50 m"
        ],
        "ans": 0,
        "exp": "Dle souhrnné tabulky z hodin: A (TO→PC) max. 5 m, B (panel↔panel) max. 10 m (jen při A,E≈0), E (panel→switch) max. 5 m, přičemž součet A + B + E ≤ 10 m."
    },
    {
        "id": 68, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Jaká podmínka musí platit pro součet délek přídavných šňůr A + B + E a jaká je celková maximální délka kanálu?",
        "options": [
            "Musí platit A + B + E ≤ 10 m, takže celý kanál včetně přídavných šňůr má 90 + 10 = 100 m",
            "Musí platit A + B + E ≤ 20 m, takže celý kanál má 90 + 20 = 110 m",
            "Musí platit A + B + E ≤ 5 m, takže celý kanál má 95 m",
            "Přídavné šňůry se do délky kanálu vůbec nezapočítávají"
        ],
        "ans": 0,
        "exp": "Pevná horizontální kabeláž má max. 90 m a všechny přídavné šňůry dohromady A + B + E ≤ 10 m, což dává celkový kanál 90 + 10 = 100 m."
    },
    {
        "id": 69, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Co v rozvaděči FD spojuje přídavná šňůra typu E a jaká je její maximální délka?",
        "options": [
            "Spojuje patch panel → aktivní zařízení (switch), jde o šňůru k zařízení o max. délce 5 m",
            "Spojuje zásuvku TO → PC na pracovní ploše, max. délka 5 m",
            "Spojuje panel ↔ panel, max. délka 90 m",
            "Spojuje rozvaděč CD → BD, max. délka 1500 m"
        ],
        "ans": 0,
        "exp": "Šňůra E (Equipment cord) je v rozvaděči FD, spojuje panel → switch a má maximální délku 5 m."
    },
    {
        "id": 70, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Co spojuje přídavná šňůra typu A a kde se nachází?",
        "options": [
            "Nachází se na pracovní ploše, spojuje telekomunikační zásuvku (TO) → PC a má maximální délku 5 m",
            "Nachází se v rozvaděči FD, spojuje panel ↔ panel a má max. délku 10 m",
            "Nachází se mezi budovami a spojuje CD → BD",
            "Nachází se ve zdi mezi FD a TO a měří 90 m"
        ],
        "ans": 0,
        "exp": "Šňůra A je šňůra pracovní plochy (zásuvka TO → PC) s maximální délkou 5 m."
    },

    # =========================================================================
    # OKRUH: KABELÁŽ 14 & 15 – Pracovní plocha, počet portů, vlastnosti, patří do SK?
    # =========================================================================
    {
        "id": 71, "topic": "sk-14", "topic_label": "Otázky 14 & 15: Pracovní plocha",
        "q": "Co je to pracovní plocha a čím začíná podle tvého výpisu z hodin?",
        "options": [
            "Prostor, kde uživatelé pracují s koncovými zařízeními (PC, tiskárna, IP kamera); začíná telekomunikační zásuvkou (TO), zahrnuje propojovací kabel (max. 5 m) a koncové zařízení",
            "Místnost s patrovým rozvaděčem FD a klimatizací",
            "Trasa mezi rozvaděčem areálu CD a rozvaděčem budovy BD",
            "Vnitřní část optického vlákna o průměru 125 µm"
        ],
        "ans": 0,
        "exp": "Pracovní plocha začíná telekomunikační zásuvkou TO, zahrnuje přídavnou šňůru A (max. 5 m) a samotné koncové zařízení."
    },
    {
        "id": 72, "topic": "sk-14", "topic_label": "Otázky 14 & 15: Pracovní plocha",
        "q": "Jaká je standardní výměra 1 pracovní plochy a kolik zásuvek (portů) se na ni přiděluje?",
        "options": [
            "Na 1 pracovní plochu (10 m²) se zpravidla přidělují 2 zásuvky / porty (nebo 1 dvojzásuvka)",
            "Na 1 pracovní plochu (100 m²) se přiděluje 1 zásuvka",
            "Na 1 pracovní plochu (2 m²) se přiděluje 8 zásuvek",
            "Na 1 pracovní plochu (50 m²) se přidělují 4 optické rozvaděče"
        ],
        "ans": 0,
        "exp": "Na 1 pracovní plochu o rozloze 10 m² se přidělují minimálně 2 zásuvky/porty (nebo 1 dvojzásuvka)."
    },
    {
        "id": 73, "topic": "sk-14", "topic_label": "Otázky 14 & 15: Pracovní plocha",
        "q": "Jakou vlastnost musí splňovat zásuvky (porty) na pracovní ploše?",
        "options": [
            "Musí odpovídat kategorii použité kabeláže (např. Cat 6, Cat 6a atd.)",
            "Musí být vždy nižší kategorie než kabel ve zdi (např. Cat 3 pro kabel Cat 6a)",
            "Nesmí být součástí generické strukturované kabeláže",
            "Musí mít zapojené pouze 2 vodiče z 8"
        ],
        "ans": 0,
        "exp": "Zásuvky TO musí odpovídat kategorii použité kabeláže (Cat 6, Cat 6a atd.), aby nedegradovaly přenosovou třídu celé linky."
    },
    {
        "id": 74, "topic": "sk-15", "topic_label": "Otázky 14 & 15: Pracovní plocha",
        "q": "OTÁZKA 15: Patří kabely pracovní plochy (přídavné šňůry od zásuvky ke koncovému zařízení) do generické strukturované kabeláže?",
        "options": [
            "Ne, kabeláž pracovní plochy není součástí generické SK – generická SK končí na zásuvce (TO), která do SK ještě patří",
            "Ano, kabely pracovní plochy i samotný počítač jsou pevnou součástí generické SK",
            "Ano, ale pouze pokud jsou delší než 90 metrů",
            "Ne, a do generické SK nepatří ani telekomunikační zásuvka TO, ani horizontální kabeláž"
        ],
        "ans": 0,
        "exp": "Přesně dle výpisu z hodin: Ne! Kabeláž pracovní plochy není součástí generické SK. Generická SK končí na zásuvce TO, která do SK ještě patří!"
    },
    {
        "id": 75, "topic": "sk-15", "topic_label": "Otázky 14 & 15: Pracovní plocha",
        "q": "Kde přesně končí generická strukturovaná kabeláž a patří ještě telekomunikační zásuvka (TO) do generické SK?",
        "options": [
            "Generická SK končí na telekomunikační zásuvce (TO) a samotná zásuvka TO do generické SK ještě patří",
            "Generická SK končí v patrovém rozvaděči FD; zásuvka TO do ní již nepatří",
            "Generická SK končí až na síťové kartě počítače",
            "Generická SK končí v rozvaděči budovy BD"
        ],
        "ans": 0,
        "exp": "Zásuvka TO je posledním prvkem pevné generické strukturované kabeláže (do SK ještě patří). Šňůra od zásuvky k PC už do generické SK nepatří."
    },

    # =========================================================================
    # OKRUH: KABELÁŽ 16 – Zapojení konektoru RJ-45 pro zásuvku typu B (T568B)
    # =========================================================================
    {
        "id": 76, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Jaké je přesné pořadí všech 8 barev vodičů na pinech 1 až 8 pro zásuvku typu B (standard T568B)?",
        "options": [
            "1: Bílo-oranžová, 2: Oranžová, 3: Bílo-zelená, 4: Modrá, 5: Bílo-modrá, 6: Zelená, 7: Bílo-hnědá, 8: Hnědá",
            "1: Bílo-zelená, 2: Zelená, 3: Bílo-oranžová, 4: Modrá, 5: Bílo-modrá, 6: Oranžová, 7: Bílo-hnědá, 8: Hnědá",
            "1: Bílo-oranžová, 2: Oranžová, 3: Bílo-zelená, 4: Zelená, 5: Bílo-modrá, 6: Modrá, 7: Bílo-hnědá, 8: Hnědá",
            "1: Oranžová, 2: Bílo-oranžová, 3: Zelená, 4: Bílo-modrá, 5: Modrá, 6: Bílo-zelená, 7: Hnědá, 8: Bílo-hnědá"
        ],
        "ans": 0,
        "exp": "Zapojení T568B (Evropa): 1 Bílo-oranžová, 2 Oranžová, 3 Bílo-zelená, 4 Modrá, 5 Bílo-modrá, 6 Zelená, 7 Bílo-hnědá, 8 Hnědá."
    },
    {
        "id": 77, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Která barva páru má u zapojení typu B (T568B) piny „rozházené“ (nejsou vedle sebe) a na kterých pozicích leží?",
        "options": [
            "Zelený pár – leží na pinech 3 (bílo-zelená) a 6 (zelená)",
            "Oranžový pár – leží na pinech 1 a 8",
            "Modrý pár – leží na pinech 2 a 7",
            "Hnědý pár – leží na pinech 3 a 6"
        ],
        "ans": 0,
        "exp": "Pomůcka z hodin: Zelené piny jsou „rozházené“ na pozicích 3 a 6! Ostatní páry jsou u sebe: oranžová 1–2, modrá 4–5, hnědá 7–8."
    },
    {
        "id": 78, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Jaké barvy vodičů jsou zapojeny na prostředních pinech 4 a 5 u konektoru typu B (T568B)?",
        "options": [
            "Pin 4: Modrá (plná barva), Pin 5: Bílo-modrá",
            "Pin 4: Bílo-modrá, Pin 5: Modrá",
            "Pin 4: Bílo-zelená, Pin 5: Zelená",
            "Pin 4: Modrá, Pin 5: Zelená"
        ],
        "ans": 0,
        "exp": "Pozor na pořadí u modrého páru uprostřed: na pinu 4 je plná Modrá a na pinu 5 je Bílo-modrá!"
    },
    {
        "id": 79, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Jaké barvy vodičů jsou u zapojení typu B (T568B) na pinech 1 a 2?",
        "options": [
            "Pin 1: Bílo-oranžová, Pin 2: Oranžová",
            "Pin 1: Bílo-zelená, Pin 2: Zelená",
            "Pin 1: Oranžová, Pin 2: Bílo-oranžová",
            "Pin 1: Bílo-hnědá, Pin 2: Hnědá"
        ],
        "ans": 0,
        "exp": "U typu B začínáme oranžovým párem: 1 = Bílo-oranžová, 2 = Oranžová."
    },
    {
        "id": 80, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Jaké barvy vodičů jsou u zapojení typu B (T568B) na pinech 7 a 8?",
        "options": [
            "Pin 7: Bílo-hnědá, Pin 8: Hnědá",
            "Pin 7: Hnědá, Pin 8: Bílo-hnědá",
            "Pin 7: Bílo-zelená, Pin 8: Zelená",
            "Pin 7: Bílo-modrá, Pin 8: Modrá"
        ],
        "ans": 0,
        "exp": "Na konci konektoru (piny 7 a 8) je vždy hnědý pár: 7 = Bílo-hnědá, 8 = Hnědá."
    },
    {
        "id": 81, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Jaká barva vodiče je u zapojení T568B na pinu 3 a jaká na pinu 6?",
        "options": [
            "Pin 3: Bílo-zelená, Pin 6: Zelená",
            "Pin 3: Zelená, Pin 6: Bílo-zelená",
            "Pin 3: Bílo-oranžová, Pin 6: Oranžová",
            "Pin 3: Bílo-modrá, Pin 6: Modrá"
        ],
        "ans": 0,
        "exp": "Zelený pár obkročuje středový modrý pár: na pinu 3 je Bílo-zelená a na pinu 6 je plná Zelená."
    },
    {
        "id": 82, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Čím se liší zapojení T568A od evropského zapojení T568B?",
        "options": [
            "Prohozením oranžového a zeleného páru (u A je zelený pár na 1–2 a oranžový rozkročený na 3 a 6; modrý 4–5 a hnědý 7–8 zůstávají stejné)",
            "Prohozením modrého a hnědého páru na pinech 4–5 a 7–8",
            "Otočením všech 8 pinů pozpátku od 8 do 1",
            "T568A používá pouze 4 vodiče, zatímco T568B používá 8 vodičů"
        ],
        "ans": 0,
        "exp": "Mezi T568A a T568B si pouze vymění místo zelený a oranžový pár. Modrý (4–5) a hnědý (7–8) jsou v obou normách na stejném místě."
    },

    # =========================================================================
    # DALŠÍ KOLO KŘÍŽOVÉHO OVĚŘENÍ (OTÁZKY 83–125) – KAŽDÝ DETAIL 3x JINAK!
    # =========================================================================
    {
        "id": 83, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Z jakého materiálu je vyrobeno jádro a plášť standardního telekomunikačního optického vlákna?",
        "options": [
            "Z křemičitého skla (SiO₂), přičemž jádro obsahuje příměsi zvyšující index lomu n₁",
            "Jádro je z mědi a plášť z hliníkové fólie",
            "Jádro je z akrylátového laku a plášť z PVC",
            "Jádro je ze vzduchu a plášť z křemičitého skla s nižším indexem lomu"
        ],
        "ans": 0,
        "exp": "Jádro i plášť jsou z křemičitého skla (SiO₂), přičemž jádro je dotováno příměsemi (např. GeO₂), aby mělo vyšší index lomu n₁ než čistý plášť n₂."
    },
    {
        "id": 84, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "K čemu slouží primární ochrana (Primary Coating, Ø 250 µm) na optickém vlákně?",
        "options": [
            "Chrání křehké skleněné vlákno před mechanickým poškozením, otěrem, vlhkostí a mikroohyby",
            "Zajišťuje totální vnitřní odraz světla zpět do jádra",
            "Slouží jako elektrický vodič pro napájení PoE",
            "Určuje vlnovou délku 1550 nm"
        ],
        "ans": 0,
        "exp": "Totální odraz probíhá už na rozhraní jádra (9/50/62,5 µm) a pláště (125 µm). Primární ochrana (250 µm akrylát) chrání sklo mechanicky a před vlhkostí."
    },
    {
        "id": 85, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Jak se nazývá nežádoucí jev u mnohovidových vláken, při kterém různé vidy urazí různě dlouhou dráhu a dorazí do cíle v různý čas, čímž se rozšíří optický impulz?",
        "options": [
            "Vidová (modální) disperze",
            "Přeslech na vzdáleném konci (FEXT)",
            "Fresnelův odraz",
            "Kvantizační zkreslení A-law"
        ],
        "ans": 0,
        "exp": "Různá doba šíření jednotlivých vidů v mnohovidovém vlákně způsobuje vidovou (modální) disperzi."
    },
    {
        "id": 86, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Po jaké trajektorii se šíří paprsky v mnohovidovém vlákně se skokovou změnou indexu lomu (Step-Index) a po jaké v gradientním (Graded-Index)?",
        "options": [
            "Ve skokovém po lomených přímkách (cik-cak), v gradientním po plynulých zvlněných křivkách (sinusoidách)",
            "Ve skokovém po kružnicích, v gradientním po lomených přímkách",
            "V obou typech výhradně v jediné přímce v ose vlákna",
            "Ve skokovém se světlo šíří pláštěm, v gradientním sekundární ochranou"
        ],
        "ans": 0,
        "exp": "Konstantní index lomu u Step-Index vede k přímým úsekům mezi odrazy (cik-cak), zatímco plynulá změna indexu lomu u Graded-Index plynule zakřivuje dráhu paprsku do tvaru sinusoidy."
    },
    {
        "id": 87, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Proč má křemičité sklo vybraná přenosová okna právě na vlnových délkách 850 nm, 1300/1310 nm a 1550 nm?",
        "options": [
            "Protože v těchto oblastech infračerveného spektra má křemičité sklo lokální minima měrného útlumu",
            "Protože jde o viditelné barvy světla (modrá, zelená a červená), které vidíme okem",
            "Protože na jiných vlnových délkách neplatí vzorec n = c / v",
            "Protože tyto vlnové délky odpovídají průměru pláště 125 µm"
        ],
        "ans": 0,
        "exp": "Přenosová okna jsou pásma vlnových délek v infračervené oblasti, kde je útlum v křemičitém skle nejnižší (mezi absorpčními píky OH⁻ iontů)."
    },
    {
        "id": 88, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Co se stane s paprskem, který vstoupí do čela optického vlákna pod úhlem VĚTŠÍM, než je maximální úhel navázání θ_max?",
        "options": [
            "Na rozhraní jádra a pláště dopadne pod úhlem menším než mezní úhel α_m, takže nenastane totální odraz a paprsek unikne (vyzáří se) do pláště",
            "Paprsek se v jádře urychlí nad rychlost světla ve vakuu",
            "Paprsek se změní na jednovidový signál o vlnové délce 1550 nm",
            "Paprsek se odrazí zpět do vysílače pod úhlem 180°"
        ],
        "ans": 0,
        "exp": "Mimo akceptační kužel (θ > θ_max) již uvnitř vlákna není splněna podmínka α > α_m, takže světlo projde do pláště a je pohlceno."
    },
    {
        "id": 89, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Vypočtěte hodnotu indexu lomu prostředí, ve kterém se světlo šíří přesně dvakrát pomaleji než ve vakuu:",
        "options": [
            "n = 2,0 (protože n = c / v = c / (0,5·c) = 2)",
            "n = 0,5",
            "n = 1,0",
            "n = 4,0"
        ],
        "ans": 0,
        "exp": "Ze vzorce n = c / v platí: pokud je rychlost v poloviční oproti c, je index lomu n = 2."
    },
    {
        "id": 90, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Jaká je hodnota numerické apertury (NA), pokud je maximální úhel navázání θ_max = 30° (sin 30° = 0,5)?",
        "options": [
            "NA = 0,5",
            "NA = 30",
            "NA = 1,5",
            "NA = 0,25"
        ],
        "ans": 0,
        "exp": "Platí NA = sin(θ_max) = sin(30°) = 0,5."
    },
    {
        "id": 91, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Který fyzikální jev způsobuje odraz části světla (cca 4 %) na vzduchové mezeře mezi dvěma rovnými čely optických konektorů a přispívá tak k vložnému útlumu?",
        "options": [
            "Fresnelův odraz (na přechodu prostředí s různým indexem lomu sklo–vzduch–sklo)",
            "Totální vnitřní odraz na primární ochraně",
            "Přeslech FEXT",
            "Diferenciální vyrušení polarity"
        ],
        "ans": 0,
        "exp": "Na kolmém rozhraní dvou prostředí s odlišným indexem lomu (sklo n≈1,46 a vzduch n=1) vzniká Fresnelův odraz."
    },
    {
        "id": 92, "topic": "sk-8", "topic_label": "Otázka 8: Normy v ČR",
        "q": "Čím se zabývá evropská norma přejatá v ČR jako ČSN EN 50173?",
        "options": [
            "Informační technologie – Univerzální kabelážní systémy (strukturovaná kabeláž)",
            "Bezpečnost elektrických spotřebičů v domácnosti",
            "Kódování zvuku v telefonních ústřednách PCM",
            "Rádiové kmitočty pro mobilní sítě 5G"
        ],
        "ans": 0,
        "exp": "ČSN EN 50173 (spolu s instalační ČSN EN 50174) je základní normou pro strukturovanou kabeláž v ČR."
    },
    {
        "id": 93, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Který kabel má na průřezu kolem každého ze 4 párů samostatný kovový obal (pair shield)?",
        "options": [
            "STP (Shielded Twisted Pair)",
            "UTP (Unshielded Twisted Pair)",
            "Optický kabel 9/125 µm",
            "Kabel kategorie 3 třídy C"
        ],
        "ans": 0,
        "exp": "Podle nákresu a výpisu z hodin má STP samostatné stínění každého jednotlivého páru (pair shield)."
    },
    {
        "id": 94, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Proč se do kabelů kategorie 6 vkládá podélný plastový kříž („rybí kost“)?",
        "options": [
            "Aby se 4 kroucené páry uvnitř kabelu k sobě příliš nepřibližovaly a omezily se tak přeslechy mezi páry",
            "Aby kabel nešel ohnout pod úhlem větším než θ_max",
            "Aby plastový kříž vedl optický signál o vlnové délce 850 nm",
            "Aby nahradil měděné vodiče u kategorie 1"
        ],
        "ans": 0,
        "exp": "Plastový separátor („rybí kost“) udržuje konstantní odstup mezi páry, což potlačuje přeslechy na vyšších frekvencích (250 MHz u Cat 6)."
    },
    {
        "id": 95, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Které tvrzení o kabelech UTP, FTP a STP je podle tvých zápisků z hodin PRAVDIVÉ?",
        "options": [
            "UTP nemá kovové stínění (kategorie 6 / třída E), FTP má společnou hliníkovou fólii kolem všech 4 párů a STP má samostatně stíněný každý pár (kategorie 6a / třída Ea a výš)",
            "FTP má samostatně stíněný každý pár a STP nemá žádné stínění",
            "UTP obsahuje 2 páry vodičů, FTP 4 páry a STP 8 párů vodičů",
            "Všechny kabely kategorie 7 a 8 jsou typu UTP"
        ],
        "ans": 0,
        "exp": "Shrnutí celé otázky 9 z hodin: UTP = bez stínění (Cat 6 / E), FTP = celková hliníková fólie kolem všech 4 párů, STP = každý pár samostatně stíněný (Cat 6a / Ea a výš)."
    },
    {
        "id": 96, "topic": "sk-10", "topic_label": "Otázka 10: Kroucené páry",
        "q": "Pokud jeden vodič v krouceném páru přenáší signál +U a druhý vodič −U, co na konci linky vyhodnocuje přijímač?",
        "options": [
            "Rozdíl napětí mezi oběma vodiči v páru",
            "Součet odporů všech 8 vodičů v kabelu",
            "Frekvenci světla v terahertzích",
            "Index lomu plastové izolace"
        ],
        "ans": 0,
        "exp": "Přijímač u kroucené dvojlinky vyhodnocuje rozdíl napětí mezi oběma vodiči páru."
    },
    {
        "id": 97, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Přiřaďte správně frekvenční rozsahy ke třídám A, B, C a D:",
        "options": [
            "A = 100 kHz, B = 1 MHz, C = 16 MHz, D = 100 MHz",
            "A = 1 MHz, B = 10 MHz, C = 100 MHz, D = 1000 MHz",
            "A = 16 MHz, B = 100 MHz, C = 250 MHz, D = 500 MHz",
            "A = 100 Hz, B = 1 kHz, C = 16 kHz, D = 100 kHz"
        ],
        "ans": 0,
        "exp": "První čtyři třídy z tabulky: A = 100 kHz (Cat 1), B = 1 MHz (Cat 2), C = 16 MHz (Cat 3), D = 100 MHz (Cat 5)."
    },
    {
        "id": 98, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Přiřaďte správně frekvenční rozsahy ke třídám E, Ea, F a Fa:",
        "options": [
            "E = 250 MHz, Ea = 500 MHz, F = 600 MHz, Fa = 1000 MHz",
            "E = 100 MHz, Ea = 250 MHz, F = 500 MHz, Fa = 600 MHz",
            "E = 350 MHz, Ea = 600 MHz, F = 1000 MHz, Fa = 2000 MHz",
            "E = 500 MHz, Ea = 250 MHz, F = 1000 MHz, Fa = 600 MHz"
        ],
        "ans": 0,
        "exp": "Vyšší třídy z tabulky: E (Cat 6) = 250 MHz, Ea (Cat 6a) = 500 MHz, F (Cat 7) = 600 MHz, Fa (Cat 7a) = 1000 MHz."
    },
    {
        "id": 99, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Která kategorie a třída odpovídá v tabulce z hodin řádku „100 MHz (350 MHz) – 1 Gbps Gigabit Ethernet (1000Base-T)“?",
        "options": [
            "Třída D 2002, Kategorie 5e",
            "Třída C, Kategorie 3",
            "Třída Ea, Kategorie 6a",
            "Třída A, Kategorie 1"
        ],
        "ans": 0,
        "exp": "V tabulce z hodin je Cat 5e označena jako Třída D 2002 se specifikací 100 MHz (350 MHz) pro 1 Gbps Gigabit Ethernet."
    },
    {
        "id": 100, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Od které třídy a kategorie podporuje strukturovaná kabeláž přenosovou rychlost 10 Gbps (10GBase-T) na plnou vzdálenost?",
        "options": [
            "Od Třídy Ea (Kategorie 6a, 500 MHz) – a dále také ve Třídě F (Cat 7) a Třídě Fa (Cat 7a)",
            "Už od Třídy B (Kategorie 2, 1 MHz)",
            "Teprve až od Třídy I & II (Kategorie 8, 2000 MHz)",
            "10 Gbps nelze po metalické kabeláži vůbec přenášet"
        ],
        "ans": 0,
        "exp": "Dle tabulky z hodin je 10 Gbps (10GBase-T) uvedeno u Třídy Ea (Cat 6a, 500 MHz), Třídy F (Cat 7, 600 MHz) a Třídy Fa (Cat 7a, 1000 MHz)."
    },
    {
        "id": 101, "topic": "sk-12", "topic_label": "Otázka 12: Přeslech FEXT",
        "q": "Jak se projevuje útlum signálu v metalickém a optickém kabelu podle poznámky z hodin?",
        "options": [
            "V metalice prochází signál elektrickým proudem ve vodičích a postupně slábne (útlum v dB); v optice prochází jako světlo vláknem a také postupně slábne (útlum v dB)",
            "V metalice signál slábne v dB, zatímco v optice světlo vůbec žádný útlum nemá",
            "V optice prochází signál elektrickým proudem a v metalice světlem",
            "Útlum přeslechu FEXT chceme co nejmenší v dB, zatímco útlum přímého signálu v kabelu chceme co největší v dB"
        ],
        "ans": 0,
        "exp": "V obou médiích (metalika = elektrický proud, optika = světlo) užitečný signál po trase postupně slábne (útlum v dB). Naopak u přeslechu FEXT (což je nežádoucí rušení mezi páry) chceme útlum tohoto rušení v dB co nejvyšší!"
    },
    {
        "id": 102, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Co znamenají zkratky CD, BD, FD, CP a TO ve schématu generické strukturované kabeláže?",
        "options": [
            "CD = Campus Distributor (rozvaděč areálu), BD = Building Distributor (rozvaděč budovy), FD = Floor Distributor (patrový rozvaděč), CP = Consolidation Point, TO = Telekomunikační zásuvka",
            "CD = Compact Disc, BD = Blu-ray Disc, FD = Floppy Disc, CP = Computer Port, TO = Terminal Output",
            "CD = Core Diameter, BD = Buffer Diameter, FD = Fiber Dispersion, CP = Cladding Protection, TO = Total Optics",
            "CD = Cat D, BD = Base D, FD = Fast D, CP = Cross Pair, TO = Twisted Outlet"
        ],
        "ans": 0,
        "exp": "Hierarchie prvků generické SK: CD (rozvaděč areálu) → BD (rozvaděč budovy) → FD (patrový rozvaděč) → CP (konsolidační bod) → TO (telekomunikační zásuvka)."
    },
    {
        "id": 103, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Jaká je celková maximální délka optické páteřní trasy od rozvaděče areálu (CD) přes rozvaděč budovy (BD) až do patrového rozvaděče (FD) podle součtu délek z hodin?",
        "options": [
            "2000 m (1500 m páteř areálu CD→BD + 500 m páteř budovy BD→FD)",
            "590 m (500 m + 90 m)",
            "100 m (90 m + 10 m)",
            "1500 m celkem včetně horizontální kabeláže"
        ],
        "ans": 0,
        "exp": "Páteř areálu (CD→BD) má max. 1500 m a páteř budovy (BD→FD) max. 500 m, dohromady tedy 2000 m."
    },
    {
        "id": 104, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Pokud má přídavná šňůra A na pracovní ploše délku 4 m a šňůra E v rozvaděči délku 3 m, jaká může být maximální délka propojovací šňůry B (panel ↔ panel), aby byla dodržena norma?",
        "options": [
            "Maximálně 3 m (protože musí platit A + B + E ≤ 10 m, tedy 4 + B + 3 ≤ 10)",
            "Maximálně 10 m bez ohledu na délku šňůr A a E",
            "Maximálně 90 m",
            "Maximálně 5 m"
        ],
        "ans": 0,
        "exp": "Protože součet všech přídavných šňůr musí splňovat A + B + E ≤ 10 m, zbývá pro šňůru B nejvýše 10 − 4 − 3 = 3 m."
    },
    {
        "id": 105, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Kdy smí mít propojovací šňůra B (panel ↔ panel v rozvaděči FD) délku až 10 metrů?",
        "options": [
            "Pouze v případě, že délky šňůr A a E jsou prakticky nulové (A, E ≈ 0), protože součet A + B + E nesmí překročit 10 m",
            "Vždy, i když mají šňůry A a E každá 5 metrů",
            "Pouze tehdy, když je pevná horizontální kabeláž delší než 90 metrů",
            "Nikdy, šňůra B smí mít maximálně 1 metr"
        ],
        "ans": 0,
        "exp": "V tabulce z hodin je u šňůry B výslovně uvedeno: max. délka 10 m (jen při A, E ≈ 0), aby platilo A + B + E ≤ 10 m."
    },
    {
        "id": 106, "topic": "sk-14", "topic_label": "Otázky 14 & 15: Pracovní plocha",
        "q": "Kolik dvojzásuvek (nebo jednotlivých zásuvek/portů) byste navrhli pro kancelář o rozloze 40 m² podle pravidla z hodin?",
        "options": [
            "4 pracovní plochy (po 10 m²), tedy celkem 8 portů / zásuvek (nebo 4 dvojzásuvky)",
            "1 pracovní plochu, tedy 1 port",
            "40 pracovních ploch, tedy 80 dvojzásuvek",
            "2 porty na celou budovu"
        ],
        "ans": 0,
        "exp": "Na každých 10 m² připadá 1 pracovní plocha se 2 zásuvkami (nebo 1 dvojzásuvkou). Pro 40 m² to jsou 4 pracovní plochy = 8 zásuvek (4 dvojzásuvky)."
    },
    {
        "id": 107, "topic": "sk-15", "topic_label": "Otázky 14 & 15: Pracovní plocha",
        "q": "Který z následujících prvků UŽ NEPATŘÍ do generické strukturované kabeláže?",
        "options": [
            "Přídavná šňůra A na pracovní ploše (od zásuvky TO k počítači)",
            "Telekomunikační zásuvka (TO) ve zdi",
            "Horizontální kabeláž mezi FD a TO",
            "Patrový rozvaděč (FD)"
        ],
        "ans": 0,
        "exp": "Generická strukturovaná kabeláž končí na telekomunikační zásuvce (TO), která do SK ještě patří. Přídavná šňůra od TO k PC již do generické SK nepatří."
    },
    {
        "id": 108, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Na kterém pinu konektoru RJ-45 je u standardu T568B zapojen Oranžový (celobarevný) vodič?",
        "options": [
            "Na pinu 2 (na pinu 1 je bílo-oranžová)",
            "Na pinu 1 (na pinu 2 je bílo-oranžová)",
            "Na pinu 6",
            "Na pinu 3"
        ],
        "ans": 0,
        "exp": "Pár 2 (oranžový) je u T568B na pinech 1 a 2: Pin 1 = Bílo-oranžová, Pin 2 = Oranžová."
    },
    {
        "id": 109, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Na kterém pinu konektoru RJ-45 je u standardu T568B zapojen Bílo-zelený vodič a na kterém plný Zelený vodič?",
        "options": [
            "Bílo-zelená je na pinu 3, Zelená je na pinu 6",
            "Bílo-zelená je na pinu 1, Zelená je na pinu 2",
            "Bílo-zelená je na pinu 4, Zelená je na pinu 5",
            "Bílo-zelená je na pinu 6, Zelená je na pinu 3"
        ],
        "ans": 0,
        "exp": "Zelené piny jsou u T568B „rozházené“ na pozicích 3 (Bílo-zelená) a 6 (Zelená)."
    },
    {
        "id": 110, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "CHYTÁK U PINŮ 4 A 5: Který z párů má u konektoru RJ-45 (T568B) otočené pořadí, takže na sudém pinu 4 začíná plnou barvou a na lichém pinu 5 má bílo-barevný vodič?",
        "options": [
            "Modrý pár (Pin 4 = Modrá, Pin 5 = Bílo-modrá)",
            "Oranžový pár (Pin 1 = Oranžová, Pin 2 = Bílo-oranžová)",
            "Hnědý pár (Pin 7 = Hnědá, Pin 8 = Bílo-hnědá)",
            "Zelený pár (Pin 3 = Zelená, Pin 6 = Bílo-zelená)"
        ],
        "ans": 0,
        "exp": "U všech párů kromě modrého začíná bílo-barevný vodič (1 bílo-oranžová, 3 bílo-zelená, 7 bílo-hnědá), ale u středového modrého páru je na pinu 4 plná Modrá a na pinu 5 Bílo-modrá!"
    },
    {
        "id": 111, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Jaký je přibližný měrný útlum mnohovidového vlákna v 1. přenosovém okně (850 nm) a jaký u jednovidového vlákna ve 3. okně (1550 nm)?",
        "options": [
            "Na 850 nm (MM) cca 2,5 až 3 dB/km; na 1550 nm (SM) cca 0,2 dB/km",
            "Na 850 nm cca 0,2 dB/km; na 1550 nm cca 30 dB/km",
            "V obou oknech je útlum přesně 100 dB/km",
            "Na 850 nm je útlum nulový a na 1550 nm je nekonečný"
        ],
        "ans": 0,
        "exp": "S rostoucí vlnovou délkou klesá Rayleighův rozptyl ve skle: na 850 nm je útlum ~2,5–3 dB/km, na 1310 nm ~0,35–0,5 dB/km a na 1550 nm jen ~0,2 dB/km."
    },
    {
        "id": 112, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Které z následujících tvrzení o indexu lomu n je PRAVDIVÉ?",
        "options": [
            "Index lomu n je bezrozměrná veličina a pro optická skla je vždy větší než 1 (typicky ~1,46 až 1,48), protože světlo se ve skle šíří pomaleji než ve vakuu",
            "Index lomu n se měří v mikrometrech (µm) a je vždy menší než 0",
            "Index lomu pláště n₂ musí být vždy větší než index lomu jádra n₁",
            "Index lomu závisí na délce patch kabelu pracovní plochy"
        ],
        "ans": 0,
        "exp": "Protože v < c, je poměr n = c / v vždy bezrozměrné číslo větší než 1."
    },
    {
        "id": 113, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Pokud spojíme dvě optická vlákna, jejichž podélné osy jsou vůči sobě mírně posunuté (osové přesazení jader), jaký parametr spoje se tím zhorší (zvýší)?",
        "options": [
            "Zvýší se vložný útlum (Insertion Loss) spoje",
            "Zvýší se numerická apertura vlákna",
            "Zvýší se rychlost světla ve vakuu",
            "Sníží se vlnová délka z 1550 nm na 850 nm"
        ],
        "ans": 0,
        "exp": "Osové přesazení jader je jednou z hlavních geometrických příčin vzniku vložného útlumu na konektoru nebo sváru."
    },
    {
        "id": 114, "topic": "sk-8", "topic_label": "Otázka 8: Normy v ČR",
        "q": "Která z následujících norem je americkou normou pro strukturovanou kabeláž (vedle evropské ČSN EN 50173 a mezinárodní ISO/IEC 11801)?",
        "options": [
            "TIA/EIA-568 (resp. ANSI/TIA-568)",
            "ČSN EN 50174",
            "ITU-T G.711",
            "ISO 9001"
        ],
        "ans": 0,
        "exp": "TIA/EIA-568 je severoamerický standard strukturované kabeláže (definuje mj. zapojení T568A a T568B)."
    },
    {
        "id": 115, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Co znamená v mezinárodním značení kabelů zkratka FTP vs. UTP?",
        "options": [
            "FTP = Foiled Twisted Pair (společné stínění všech 4 párů hliníkovou fólií), UTP = Unshielded Twisted Pair (bez kovového stínění)",
            "FTP = Fiber Twisted Pair, UTP = Ultra Thick Pair",
            "FTP = Fast Transfer Protocol, UTP = User Transfer Protocol",
            "FTP je nestíněný kabel a UTP je dvojitě stíněný kabel"
        ],
        "ans": 0,
        "exp": "FTP má hliníkovou fólii kolem celého svazku 4 párů, zatímco UTP nemá žádné kovové stínění."
    },
    {
        "id": 116, "topic": "sk-10", "topic_label": "Otázka 10: Kroucené páry",
        "q": "Kolik vodičů tvoří jeden kroucený pár a jaká je polarita signálu v nich?",
        "options": [
            "2 vodiče – jeden přenáší kladnou polaritu signálu (+U) a druhý opačnou polaritu signálu (−U)",
            "4 vodiče – všechny přenášejí kladnou polaritu",
            "1 vodič – přenáší střídavě světlo a elektrický proud",
            "8 vodičů v každém páru"
        ],
        "ans": 0,
        "exp": "V každém páru jsou 2 vodiče s opačnou polaritou (+U a −U) a přijímač vyhodnocuje rozdíl napětí mezi nimi."
    },
    {
        "id": 117, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Jaká přenosová rychlost a maximální dosah jsou v tabulce z hodin uvedeny u Třídy I & II (Kategorie 8, 1600/2000 MHz)?",
        "options": [
            "40 Gbps (40GBase-T) do 30 m",
            "10 Gbps (10GBase-T) do 100 m",
            "1 Gbps (1000Base-T) do 90 m",
            "100 Mbps do 1500 m"
        ],
        "ans": 0,
        "exp": "Kategorie 8 (Třída I & II, 1600/2000 MHz) je určena pro 40 Gbps (40GBase-T) na zkrácenou vzdálenost do 30 m (typicky v datových centrech)."
    },
    {
        "id": 118, "topic": "sk-12", "topic_label": "Otázka 12: Přeslech FEXT",
        "q": "Proč u přeslechu FEXT požadujeme co nejvyšší hodnotu útlumu v decibelech (dB)?",
        "options": [
            "Protože útlum přeslechu vyjadřuje míru potlačení nežádoucího rušivého signálu mezi páry – čím vyšší útlum v dB, tím menší je rušení",
            "Protože vyšší útlum FEXT zvyšuje přeslech mezi páry",
            "Protože FEXT vyjadřuje délku optického vlákna v kilometrech",
            "Protože při nízkém útlumu FEXT nefunguje plastový kříž"
        ],
        "ans": 0,
        "exp": "Útlum přeslechu = potlačení rušení. Chceme, aby rušení bylo potlačeno co nejvíce, tedy požadujeme co nejvyšší útlum FEXT v dB."
    },
    {
        "id": 119, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Jaká je maximální délka pevného horizontálního spoje (FD → TO) a jaká je maximální délka celého horizontálního kanálu (včetně šňůr A, B, E)?",
        "options": [
            "Pevný horizontální spoj max. 90 m; celý kanál včetně přídavných šňůr max. 100 m (90 + 10 = 100 m)",
            "Pevný spoj max. 100 m; celý kanál max. 150 m",
            "Pevný spoj max. 500 m; celý kanál max. 1500 m",
            "Pevný spoj max. 80 m; celý kanál max. 90 m"
        ],
        "ans": 0,
        "exp": "Horizontální kabeláž (FD → TO) má max. 90 m a přídavné šňůry A + B + E dohromady max. 10 m → celkem 90 + 10 = 100 m."
    },
    {
        "id": 120, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Které tvrzení o zapojení zásuvky typu B (T568B) podle tvého výpisu z hodin je PRAVDIVÉ?",
        "options": [
            "Typ B se používá v Evropě, platí 1 pin = 1 vodič = 1 barva = 1 drátek, zelené piny jsou rozházené na 3 a 6 a ostatní páry jsou u sebe (oranžová 1–2, modrá 4–5, hnědá 7–8)",
            "Typ B se používá pouze v Japonsku a má rozházený hnědý pár na pinech 1 a 8",
            "U typu B jsou do každého pinu zapojeny 2 vodiče najednou",
            "U typu B jsou zelené piny u sebe na pozicích 1 a 2"
        ],
        "ans": 0,
        "exp": "Přesné shrnutí otázky 16 z hodin: Typ B je v Evropě, 1 pin = 1 vodič = 1 barva = 1 drátek, zelená je rozházená na 3 a 6, ostatní jsou u sebe (oranžová 1,2 – modrá 4,5 – hnědá 7,8)."
    },
    {
        "id": 121, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Jaký je průměr sekundární ochrany (Buffer – plastová trubička) u standardního optického vlákna?",
        "options": [
            "900 µm (0,9 mm)",
            "125 µm",
            "250 µm",
            "9 µm"
        ],
        "ans": 0,
        "exp": "4. vrstva optického vlákna (sekundární ochrana / Buffer) má typický průměr 900 µm (0,9 mm)."
    },
    {
        "id": 122, "topic": "opt-1", "topic_label": "Optika 1: Struktura a typy vláken",
        "q": "Které přenosové okno má nulovou chromatickou disperzi u standardního křemičitého vlákna a jaký má přibližný útlum?",
        "options": [
            "2. okno (1300 nm u MM / 1310 nm u SM), útlum cca 0,35 až 0,5 dB/km",
            "1. okno (850 nm), útlum cca 2,5 až 3 dB/km",
            "3. okno (1550 nm), útlum cca 10 dB/km",
            "Žádné okno, chromatická disperze je vždy nekonečná"
        ],
        "ans": 0,
        "exp": "Ve 2. přenosovém okně (1300 nm MM / 1310 nm SM) prochází chromatická disperze nulou a měrný útlum činí ~0,35–0,5 dB/km."
    },
    {
        "id": 123, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Jak zní vzorec pro výpočet mezního úhlu α_m (ze Snellova zákona lomu), při jehož překročení nastává totální vnitřní odraz?",
        "options": [
            "sin(α_m) = n₂ / n₁ (kde n₁ > n₂)",
            "sin(α_m) = n₁ · n₂",
            "sin(α_m) = c / v",
            "sin(α_m) = n₁ + n₂"
        ],
        "ans": 0,
        "exp": "Při mezním úhlu α_m se lomený paprsek šíří podél rozhraní (úhel lomu je 90°, sin 90° = 1), takže z n₁·sin(α_m) = n₂·sin(90°) plyne sin(α_m) = n₂ / n₁."
    },
    {
        "id": 124, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Jak souvisí numerická apertura (NA) s maximálním úhlem navázání (θ_max) optického vlákna ve vzduchu (n₀ ≈ 1)?",
        "options": [
            "Numerická apertura je přímo rovna sinu maximálního úhlu navázání: NA = sin(θ_max) = √(n₁² − n₂²)",
            "Numerická apertura je rovna podílu průměru jádra a pláště",
            "Numerická apertura je převrácená hodnota vložného útlumu",
            "Mezi NA a θ_max neexistuje žádný vztah"
        ],
        "ans": 0,
        "exp": "Platí přímý vztah NA = sin(θ_max) = √(n₁² − n₂²), odkud θ_max = arcsin(NA)."
    },
    {
        "id": 125, "topic": "opt-2", "topic_label": "Optika 2: Totální odraz, NA a útlum",
        "q": "Jak se nazývá kužel vymezený maximálním úhlem navázání θ_max před čelem optického vlákna?",
        "options": [
            "Akceptační kužel vlákna (světlo vstupující uvnitř tohoto kužele se ve vlákně šíří totálním odrazem)",
            "Rozptylový kužel FEXT",
            "Stínící kužel STP",
            "Fresnelův kužel"
        ],
        "ans": 0,
        "exp": "Maximální úhel navázání θ_max definuje tzv. akceptační kužel optického vlákna."
    },
    {
        "id": 126, "topic": "sk-8", "topic_label": "Otázka 8: Normy v ČR",
        "q": "Jaký je rozdíl v zaměření mezi normou ČSN EN 50173 a normou ČSN EN 50174?",
        "options": [
            "ČSN EN 50173 řeší návrh a přenosové parametry strukturované kabeláže, zatímco ČSN EN 50174 řeší instalaci, plánování a provoz informačních kabeláží",
            "ČSN EN 50173 platí pouze v USA a ČSN EN 50174 pouze v Japonsku",
            "ČSN EN 50173 řeší audio kodeky a ČSN EN 50174 řeší SDH kontejnery",
            "Obě normy zakazují používání optických vláken v budovách"
        ],
        "ans": 0,
        "exp": "ČSN EN 50173 specifikuje strukturu a parametry univerzální kabeláže; ČSN EN 50174 specifikuje pravidla pro její praktickou instalaci."
    },
    {
        "id": 127, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Kolik vodičů (žil) a kolik kroucených párů celkem obsahuje standardní metalický kabel UTP, FTP nebo STP?",
        "options": [
            "4 kroucené páry, tedy celkem 8 jednotlivých vodičů (žil)",
            "2 kroucené páry, tedy 4 vodiče",
            "8 kroucených párů, tedy 16 vodičů",
            "1 kroucený pár, tedy 2 vodiče"
        ],
        "ans": 0,
        "exp": "Standardní kabel strukturované kabeláže (UTP/FTP/STP) se skládá ze 4 párů = 8 vodičů."
    },
    {
        "id": 128, "topic": "sk-9", "topic_label": "Otázka 9: UTP, FTP, STP a kategorie",
        "q": "Do které kategorie a třídy vedení se dle výpisu z hodin používají nestíněné kabely UTP a od které kategorie/třídy se používají stíněné kabely STP?",
        "options": [
            "UTP se používá v kategorii 6 (třída E); STP se používá v kategorii 6a a výš (třída Ea a výš)",
            "UTP se používá v kategorii 8 (třída I & II); STP pouze v kategorii 1 (třída A)",
            "UTP se používá do kategorie 7a; STP až od kategorie 9",
            "UTP i STP jsou povoleny výhradně v kategorii 3"
        ],
        "ans": 0,
        "exp": "Dle tvých zápisků z hodin: UTP = v kategorii 6 (třída E), STP = v kategorii 6a a výš (třída Ea a výš)."
    },
    {
        "id": 129, "topic": "sk-10", "topic_label": "Otázka 10: Kroucené páry",
        "q": "Které tři hlavní principy u technologie kroucených párů zajišťují odolnost proti rušení a přeslechům (podle otázky 10 z hodin)?",
        "options": [
            "1) Vzájemné zkroucení vodičů v páru, 2) Různá hustota zákrutů jednotlivých 4 párů, 3) Opačná polarita signálu (+U a −U) ve vodičích páru a vyhodnocení rozdílu napětí v přijímači",
            "1) Použití křemičitého skla, 2) Totální vnitřní odraz, 3) Vlnová délka 1550 nm",
            "1) Stejná hustota zákrutů všech párů, 2) Stejná kladná polarita v obou vodičích, 3) Měření součtu proudů",
            "1) Zkrácení kabelu na 5 m, 2) Rozházení zeleného páru, 3) Nulový útlum FEXT"
        ],
        "ans": 0,
        "exp": "Přesné shrnutí otázky 10 z výpisu z hodin: zkroucení vodičů, různá hustota zákrutů mezi 4 páry a symetrický přenos (+U / −U) s vyhodnocením rozdílu napětí."
    },
    {
        "id": 130, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Jak se v mezinárodních normách ČSN EN 50173 a ISO/IEC 11801 označují „Třídy vedení“ (Classes) na rozdíl od „Kategorií komponent“ (Categories)?",
        "options": [
            "Třídy vedení se označují písmeny (A, B, C, D, D 2002, E, Ea, F, Fa, I & II), zatímco kategorie komponent čísly (Cat 1, 2, 3, 5, 5e, 6, 6a, 7, 7a, 8)",
            "Třídy vedení se označují čísly 1 až 8 a kategorie písmeny A až F",
            "Třídy vedení se označují vlnovými délkami v nanometrech",
            "Mezi značením tříd a kategorií není žádný rozdíl"
        ],
        "ans": 0,
        "exp": "Třídy linek (Classes) jsou písmenné (A až Fa, příp. I & II), zatímco kategorie (Categories) jsou číselné (Cat 1 až Cat 8)."
    },
    {
        "id": 131, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "Která třída a kategorie je v tabulce z hodin popsána jako: „Specifikováno do 16 MHz – 10 Mbps, Token Ring 16 MB“?",
        "options": [
            "Třída C, Kategorie 3",
            "Třída A, Kategorie 1 (do 100 kHz)",
            "Třída B, Kategorie 2 (do 1 MHz)",
            "Třída D, Kategorie 5 (do 100 MHz)"
        ],
        "ans": 0,
        "exp": "Do 16 MHz je specifikována Třída C (Kategorie 3)."
    },
    {
        "id": 132, "topic": "sk-11", "topic_label": "Otázka 11: Třídy linek a frekvence",
        "q": "V jakých jednotkách se podle poznámky u otázky 11 ve výpisu z hodin běžně udává frekvence světla v optických vláknech?",
        "options": [
            "V terahertzích (THz)",
            "V kilohertzích (kHz)",
            "V megahertzích (MHz)",
            "V decibelech (dB)"
        ],
        "ans": 0,
        "exp": "U metalických kabelů udáváme šířku pásma v kHz/MHz, zatímco u optiky se frekvence světla udává v THz (terahertzích)."
    },
    {
        "id": 133, "topic": "sk-12", "topic_label": "Otázka 12: Přeslech FEXT",
        "q": "Která z následujících definic přesně vystihuje pojem FEXT a požadavek na jeho útlum (otázka 12)?",
        "options": [
            "FEXT (Far-End Crosstalk) je přeslech na vzdáleném konci kabelu (rušení z jednoho páru do jiného měřené na opačném konci kabelu); požadujeme co nejvyšší útlum FEXT v dB",
            "FEXT je přeslech na bližším konci kabelu; požadujeme co nejnižší útlum FEXT v dB",
            "FEXT je vložný útlum optického konektoru; požadujeme přesně 100 dB",
            "FEXT je zesílení signálu na pracovní ploše; požadujeme 0 dB"
        ],
        "ans": 0,
        "exp": "Kompletní odpověď na otázku 12: FEXT = Far-End Crosstalk (přeslech na vzdáleném konci kabelu) a požadujeme co nejvyšší hodnotu útlumu FEXT v dB, aby rušení mezi páry bylo co nejmenší."
    },
    {
        "id": 134, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Které ze tří základních subsystémů generické kabeláže jsou podle tvého výpisu z hodin tvořeny optickými kabely a který metalickými kabely?",
        "options": [
            "Páteřní kabeláž areálu (max. 1500 m) a páteřní kabeláž budovy (max. 500 m) jsou optické; horizontální kabeláž (max. 90 m) je metalická",
            "Páteřní kabeláž areálu je metalická a horizontální kabeláž je výhradně optická",
            "Všechny tři subsystémy jsou výhradně metalické o délce 90 m",
            "Páteř budovy je metalická (max. 1500 m) a páteř areálu optická (max. 90 m)"
        ],
        "ans": 0,
        "exp": "Dle výpisu z hodin: 1. Páteř areálu = optika (max. 1500 m), 2. Páteř budovy = optika (max. 500 m), 3. Horizontální kabeláž = metalické kabely (max. 90 m)."
    },
    {
        "id": 135, "topic": "sk-13", "topic_label": "Otázka 13: Subsystémy a délky",
        "q": "Co ve schématu horizontální kabeláže znamená zkratka CP (mezi FD a TO)?",
        "options": [
            "Consolidation Point – konsolidační (přípojný) bod na trase horizontální kabeláže",
            "Campus Panel – hlavní rozvaděč celého areálu",
            "Cladding Protection – primární ochrana optického vlákna",
            "Crosstalk Pair – přeslechový pár"
        ],
        "ans": 0,
        "exp": "Ve schématu z hodin (CD → BD → FD → CP → TO) označuje CP konsolidační bod (Consolidation Point) v horizontální kabeláži."
    },
    {
        "id": 136, "topic": "sk-14", "topic_label": "Otázky 14 & 15: Pracovní plocha",
        "q": "Jaká je maximální délka propojovacího kabelu (přídavné šňůry A) na pracovní ploše mezi telekomunikační zásuvkou TO a koncovým zařízením?",
        "options": [
            "Max. 5 m",
            "Max. 90 m",
            "Max. 100 m",
            "Max. 500 m"
        ],
        "ans": 0,
        "exp": "U otázky 14 i v tabulce šňůr u otázky 13 je uvedeno: propojovací kabel k zařízení na pracovní ploše (šňůra A, TO → PC) má max. délku 5 m."
    },
    {
        "id": 137, "topic": "sk-15", "topic_label": "Otázky 14 & 15: Pracovní plocha",
        "q": "Proč kabely pracovní plochy (patch kabely od zásuvky TO k počítači) NEPATŘÍ do generické strukturované kabeláže?",
        "options": [
            "Protože generická strukturovaná kabeláž zahrnuje pouze pevnou instalaci budovy a končí na telekomunikační zásuvce (TO), která do SK ještě patří",
            "Protože kabely pracovní plochy jsou vždy optické o délce 1500 m",
            "Protože na pracovní ploše se nepoužívá konektor RJ-45",
            "Protože kabely pracovní plochy nemají kroucené páry"
        ],
        "ans": 0,
        "exp": "Generická SK končí na telekomunikační zásuvce TO (ta do SK ještě patří). Pohyblivé přídavné šňůry na pracovní ploše již součástí generické SK nejsou."
    },
    {
        "id": 138, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Jaké barvy vodičů jsou na lichých pinech (1, 3, 5, 7) u konektoru RJ-45 zapojeného podle normy T568B?",
        "options": [
            "Všechny liché piny mají bílo-barevné (žíhané) vodiče: 1 Bílo-oranžová, 3 Bílo-zelená, 5 Bílo-modrá, 7 Bílo-hnědá",
            "Všechny liché piny mají plné barvy: 1 Oranžová, 3 Zelená, 5 Modrá, 7 Hnědá",
            "1 Bílo-zelená, 3 Bílo-oranžová, 5 Modrá, 7 Hnědá",
            "Liché piny nejsou v konektoru RJ-45 vůbec zapojeny"
        ],
        "ans": 0,
        "exp": "Skvělá pomůcka pro kontrolu u zkoušky: u T568B (i T568A) jsou na všech lichých pinech 1, 3, 5, 7 vždy bílo-barevné vodiče a na všech sudých pinech 2, 4, 6, 8 vždy plné barvy!"
    },
    {
        "id": 139, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Jaké barvy vodičů jsou na sudých pinech (2, 4, 6, 8) u konektoru RJ-45 zapojeného podle normy T568B?",
        "options": [
            "Všechny sudé piny mají plné barvy: 2 Oranžová, 4 Modrá, 6 Zelená, 8 Hnědá",
            "Všechny sudé piny mají bílo-barevné vodiče: 2 Bílo-oranžová, 4 Bílo-modrá, 6 Bílo-zelená, 8 Bílo-hnědá",
            "2 Zelená, 4 Modrá, 6 Oranžová, 8 Hnědá",
            "2 Oranžová, 4 Zelená, 6 Modrá, 8 Hnědá"
        ],
        "ans": 0,
        "exp": "Na sudých pinech 2, 4, 6, 8 jsou u T568B vždy celobarevné vodiče v pořadí: 2 Oranžová, 4 Modrá, 6 Zelená, 8 Hnědá."
    },
    {
        "id": 140, "topic": "sk-16", "topic_label": "Otázka 16: Konektor RJ-45 Typ B",
        "q": "Kterým třem číslům párů podle schématu T568B odpovídají piny 1–2, 3–6, 4–5 a 7–8?",
        "options": [
            "Piny 4–5 = Pár 1 (modrý), Piny 1–2 = Pár 2 (oranžový), Piny 3–6 = Pár 3 (zelený), Piny 7–8 = Pár 4 (hnědý)",
            "Piny 1–2 = Pár 1, Piny 3–4 = Pár 2, Piny 5–6 = Pár 3, Piny 7–8 = Pár 4",
            "Všechny piny patří do Páru 1",
            "Piny 1–8 jsou zapojeny náhodně"
        ],
        "ans": 0,
        "exp": "Podle obrázku T568B z hodin: Pár 1 (modrý) je uprostřed na pinech 4–5, Pár 2 (oranžový) na pinech 1–2, Pár 3 (zelený) je rozkročený na pinech 3 a 6 a Pár 4 (hnědý) je na pinech 7–8."
    }
]

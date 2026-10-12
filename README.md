# Medieval 1350 — Age of History 2: Definitive Edition

An English-language scenario mod starting on **1 January 1350**, available in two versions: a smaller **4K** scenario and a more detailed **14K** revision. Both use the game's existing maps and require an installed copy of **Age of History 2: Definitive Edition**.

## Downloads

| Version | Download | Map to select | Scenario to select |
|---|---|---|---|
| 4K / v1.1 | [Download 4K ZIP](https://github.com/pxnami/aoh2-medieval-1350/releases/download/v2.0/Medieval1350-4K-v1.1.zip) | Earth — 4,269 provinces | 1350 - Crowns and Plague (4K) |
| 14K / v2.0 | [Download 14K ZIP](https://github.com/pxnami/aoh2-medieval-1350/releases/download/v2.0/Medieval1350-14K-v2.0.zip) | Earth 14K — 13,892 provinces | 1350 - The Medieval World (14K) |

## Installation

1. Close the game.
2. Download your chosen ZIP and extract its top-level folder into the game's `mods` directory. The resulting path should be `mods/Medieval1350_4K/mod.txt` or `mods/Medieval1350_14K/mod.txt`.
3. If you previously installed the combined `Mittelalter1350` package, move that old folder out of `mods` before installing these standalone versions to avoid overlapping overrides.
4. Restart the game, select the corresponding map, select the 1350 scenario, and start a new campaign.

Both standalone versions can be installed together because they target different maps. Existing saves keep their saved scenario data. The mod's event text is English; built-in menus and country names follow the game's language setting.

To uninstall, close the game and remove the corresponding mod folder. Base game files are not edited by installation.

## Version comparison

| Setting or content | 4K | 14K |
|---|---:|---:|
| Start date | 1 January 1350 | 1 January 1350 |
| Map provinces | 4,269 | 13,892 |
| Active polities | 500 | 896 |
| Foundation | Original 1440 scenario | Original 1354 scenario |
| Province ownership changes against foundation | 76 | 545 |
| English event instances | 151 | 333 |
| Country-specific plague events | 148 | 322 |
| Other event instances | 3 | 11 |
| Custom country definitions | None | 6 |
| HRE initial authority | 35 | 25 |
| General starting treasury | 6,000 | 2,450 |
| Starting capital army setting | 350 | 500 |
| Neutral army setting | 1,000 | 500 |
| Starting economy setting | 23,600 | 20,400 |
| Starting population setting | 52,000 | 47,600 |
| Colonization | Disabled | Disabled |

Starting settings are game defaults used by the scenario, not historical census figures or a guarantee of identical totals for every country. Some values are inherited rather than newly designed by the mod. The event totals include repeated country-specific instances of the same plague story.

## Complete 14K feature list

### Map and political setup

- Uses the original Earth 14K world map with 13,892 existing provinces; no new province shapes are drawn.
- Starts on 1 January 1350 in the game's medieval age.
- Contains 896 active states, minor realms and tribal polities across the world.
- Uses the original 1354 scenario as its foundation, with 545 province ownership changes and additional polity relabels.
- Includes a custom scenario name, English description, map preview and mod thumbnail.
- Keeps inherited province geography, terrain, wasteland definitions and other map data compatible with the installed game.
- Disables colonization, including neutral-province colonization.

### Every group of province ownership changes

- Trastamara territories → Castile: **38 provinces**.
- French Avignon province → Papal States: **1 province**.
- Moldavian frontier → Golden Horde: **12 provinces**; → Hungary: **9 provinces**.
- Ottoman European possessions → Byzantine Empire: **3 provinces**.
- Muzaffarid territories → Injuid Dynasty: **41 provinces**.
- Fars → Injuid Dynasty: **13 provinces**.
- Crimea → Golden Horde: **45 provinces**.
- Nogai → Golden Horde: **28 provinces**.
- Astrakhan → Golden Horde: **20 provinces**.
- Thessaly → Serbian Empire: **33 provinces**.
- Albanian interior → Serbian Empire: **5 provinces**.
- Montenegro → Serbian Empire: **5 provinces**.
- Zeta → Serbian Empire: **1 province**.
- Herzegovina → Bosnia: **10 provinces**.
- Vidin → Bulgaria: **2 provinces**.
- Majorca → Aragon: **5 provinces**.
- Sardinia → Arborea: **2 provinces**.
- Gujarat → Delhi: **15 provinces**.
- Jaunpur → Delhi: **32 provinces**.
- Malacca → Singapura: **6 provinces**.
- Kandy → Gampola: **3 provinces**.
- Tokugawa territory → Ashikaga: **4 provinces**.
- Sung → Yuan: **62 provinces**.
- Wu → Yuan: **17 provinces**.
- Song → Yuan: **72 provinces**.
- Zhu Yuanzhang's territory → Yuan: **12 provinces**.
- Liang → Yuan: **49 provinces**.

These are adaptations to game provinces. The previous and new names describe the scenario's ownership records, not a claim that every listed predecessor existed independently in 1350. The exact province IDs, reasons and polity relabels are in [the change ledger](docs/HistoricalChanges.json) and [territorial tables](docs/TerritorialChanges.md).

### Country definitions and capitals

- Six custom definitions: **Kartid Dynasty, Sarbadars, Injuid Dynasty, Luang Prabang, Gampola and Tenochtitlan**.
- Each custom definition includes a serialized country file, display-name entries, an information file and flag assets at the game's three standard flag sizes.
- Flags are derived from installed game artwork rather than newly authenticated medieval heraldry.
- The western White Horde definition is relabelled as the **Golden Horde**; the Serbian definition becomes the **Serbian Empire**.
- Other freed or existing country slots are reassigned to the revised political setup without changing the scenario's array indexing.
- Eleven explicit capital overrides: **Bursa** for the Ottomans, **Kyoto** for Ashikaga, **Tabriz** for the Chobanids, **Shiraz** for the Injuids, **Skopje** for Serbia, **Veliko Tarnovo** for Bulgaria, **Sabzevar** for the Sarbadars, **Avignon** for the Papal States, **Yazd** for the Muzaffarids, the **Kandy province** for Gampola's highland seat, and **Oristano** for Arborea.
- Capital assignments are checked against ownership. Removed polities receive no active capital; invalid inherited capital references are repaired to an owned province.
- Armies in reassigned provinces are assigned to the new owner, while the inherited army strengths are retained.

### Diplomacy, dependencies and the Holy Roman Empire

- **107 configured dependency relationships**, including inherited and revised relationships, represent fiefs, provincial administration, nominal suzerainty, personal unions and clan jurisdiction.
- France's appanages and dependencies include Blois, Alencon, Anjou, Maine, Orleans, Bourbonnais, Armagnac, Foix, Dauphine, Flanders and Burgundy.
- Gascony and Montfort are linked to England; Franche Comte is linked to Burgundy.
- Norway, Aland and Finland are linked to Sweden; Iceland is linked to Norway. The Sweden–Norway personal union uses the vassal mechanic.
- Liaoyang and Goryeo are linked to Yuan; Qara Qoyunlu and Aq Qoyunlu to the Chobanids; Imereti and Samtskhe to Georgia.
- Kiev, Muscovy, Tver and Ryazan are linked to the Golden Horde.
- Sardinia is linked to Aragon; Arborea remains separately represented.
- Twenty-three Japanese houses are linked to Ashikaga through the existing dependency mechanic.
- Other inherited dependencies remain in the scenario. **Every one of the 107 relationships is listed in [Diplomacy.md](docs/Diplomacy.md)**, alongside the complete configured 14K relation table.
- England–France starts at **-65 relations**, with a **24-turn truce**.
- England–Scotland: **-45**; Serbia–Byzantium: **-60**; Ottomans–Byzantium: **-35**; Bulgaria–Serbia: **+25**; Sweden–Denmark: **-20**; Jalayirids–Chobanids: **-55**; Injuids–Muzaffarids: **-55**; Bahmani–Vijayanagar: **-60**.
- Newly configured dependencies generally receive **+45 starting relations** between subject and overlord.
- Bohemia leads the Holy Roman Empire, which retains **160 mapped princes**, seven elector entries and **25 initial imperial authority**.
- The inherited elector entries are Austria, Brandenburg, Trier, Saxony, Mainz, Palatinate and Cologne. This inherited configuration is a known historical limitation; Austria's inclusion is not presented as historically correct for 1350.

### The Black Death

- **322 country-specific, non-repeatable plague event instances**, assigned to polities whose starting capitals are in the map's European continent classification.
- Eligible from **2 January 1350**, subject to the recipient still existing and the game's event checks.
- Three player choices with explicit effects:

| Choice | Gold | Population | Economy | Happiness | AI choice weight |
|---|---:|---:|---:|---:|---:|
| Close ports and restrict travel | -1,200 | -8% | -8% | -5 | 45% |
| Keep trade routes open | 0 | -16% | -3% | -10 | 25% |
| Fund hospitals and poor relief | -1,800 | -11% | -5% | +5 | 30% |

Population and economy effects apply to the recipient's recorded starting provinces that it still owns. Happiness and treasury outcomes use the game's country-wide outcomes. Choice weights govern AI selections, not event appearance probability. The base game's disease system remains active.

### All eleven additional 14K events

| Event | Recipient | First eligible date |
|---|---|---|
| The Emperor's Law | Serbian Empire | 2 January 1350 |
| A New King in Castile | Castile | 26 March 1350 |
| The French Crown | France | 22 August 1350 |
| The Kanno Disturbance | Ashikaga | 2 January 1350 |
| The Caravan Roads | Mamluks | 2 January 1350 |
| The Tughlaq Realm | Delhi | 2 January 1350 |
| The Bulgarian Frontier | Bulgaria | 2 January 1350 |
| Unrest Along the Yellow River | Yuan | 1 May 1351 |
| The Struggle for Fars | Injuid Dynasty | 2 January 1353 |
| The War for the French Crown | England | 2 January 1355 |
| The Golden Bull | Bohemia | 10 January 1356 |

Each event has its own English narrative and two named choices. For all eleven, the first choice costs **800 gold** and adds **8 happiness**, with a **65% AI weight**; the second adds **600 gold** and removes **6 happiness**, with a **35% AI weight**.

The complete narratives, all choice labels, dates and numerical effects are in [Events.md](docs/Events.md). Events are non-repeatable, require the recipient to exist and expire on 1 January two years after their starting year. Eligibility dates are script settings; delivery occurs on a subsequent game event check.

These stories offer economic and political choices. Their scripted outcomes change money and happiness. A choice mentioning troops, river works, courts or caravans does not create a new unit, building, infrastructure system or forced historical war.

## Complete 4K feature list

- Uses the original **Earth map with 4,269 provinces**, starts on **1 January 1350**, and contains **500 active polities**.
- Based on the original **1440 scenario**, with **76 province ownership changes**, mainly in Europe, Anatolia and Crimea. Much of the world outside Europe retains the 1440 setup.
- Reassigns later Ottoman Balkan holdings among Bulgaria, Serbia and Byzantium, while portions of Anatolia are reassigned to existing beyliks.
- Reassigns the Albanian interior to Serbia, Crimean possessions to the Golden Horde, some later English possessions to France, later Burgundian Low Countries possessions to local rulers, and parts of southern Scandinavia to Sweden.
- Uses Serbian Empire, Bulgaria and Golden Horde identities in the revised scenario.
- Repairs capitals and army ownership to match changed province ownership; replaces existing core entries in changed provinces with the new owner.
- Bohemia leads the inherited Holy Roman Empire with **35 initial authority**.
- Norway is linked to Sweden, and later Ottoman dependencies over Serbia, Bulgaria and Byzantium are removed where applicable.
- Adjusted starting relations: England–France **-65**, Sweden–Norway **+65**, Sweden–Denmark **-25**, Serbia–Byzantium **-60**, Bulgaria–Byzantium **-20**, Ottomans–Byzantium **-65**, and England–Scotland **-55**.
- Includes the **24-turn England–France truce**.
- Applies **0.35 starting technology** to the selected European and nearby countries, including their continent-specific technology entries.
- Uses the 4K starting treasury, army, economy and population settings listed in the comparison table.
- Disables colonization and neutral-province colonization.
- Includes **151 English event instances**: **148 plague events** with the same three effects shown above, one Golden Bull event for Bohemia, and one French-crown conflict event each for France and England.
- The 4K Golden Bull choices are **-1,000 gold / +12 happiness** or **+1,000 gold / -8 happiness**, with **75% / 25% AI weights**.
- The 4K conflict choices are **-1,200 gold / -3 happiness** or **-600 gold / +8 happiness**, with **65% / 35% AI weights**.
- Includes its own English scenario description, mod metadata, thumbnail and map previews.
- Every configured 4K dependency and every event narrative, date and choice is included in the linked diplomacy and event documents.

## Files, compatibility and verification

- Separate installable 4K and 14K folders and separate release ZIPs.
- English documentation, scenario descriptions and decision text.
- Country-name entries for the six custom 14K definitions in the default and German civilization bundles.
- Original game flag templates adapted for the six custom definitions at 27×18, 68×44 and 154×100 sizes.
- Scenario registration files. The 14K registry includes the base-game and Workshop scenario lists present during packaging; additional subscriptions or other registry overrides may require a later merge.
- Map previews for both versions, [historical sources](docs/Sources.md), a [per-province change ledger](docs/HistoricalChanges.json), complete [diplomacy tables](docs/Diplomacy.md), complete [event documentation](docs/Events.md) and a [technical validation report](docs/Pruefbericht.json).
- Native Java serialization read-back and structural checks for country definitions, province references, capitals, armies, flags, duplicate overlords, dependency cycles, HRE indices, event conditions, dates and AI weights.
- Installation file hashes were checked. The 4K scenario and English plague popup were confirmed in user screenshots. A later screenshot confirmed the 14K scenario starting on 1 January 1350; its event effects have not yet been fully verified in-game. The archived validation report predates that screenshot.

## Scope and historical limitations

This is an unofficial scenario revision using existing game systems. It adds no new unit types, buildings, music, religions, government systems, combat engine, disease engine, dynamic historical border system or automatic succession system. Royal succession and rebellion stories are narrative events with the stated numerical outcomes.

The province shapes come from the game. Some minor states, borders, clan relationships, elector entries and inherited regions remain approximations. Personal unions and nominal allegiance use vassal mechanics. The Gampola seat is approximated by the Kandy province. Base-game flag assets are not authenticated medieval heraldry. Population, economy and event effects are gameplay values, not historical measurements. The 4K version retains particularly substantial 1440 content outside its reviewed regions.

Maps, base scenarios, country templates and reused flag artwork are credited to **Lukasz Jakowski and Age of History 2: Definitive Edition**. See [NOTICE.md](NOTICE.md) and [Sources.md](docs/Sources.md).

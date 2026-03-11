# ddd-frequencychase (Frequenzjaeger Radio Deck)

Lore-passendes Radio-Decision-Game im Doomsday-Dispatch-Universum.

## Start

Nutze den lokalen Python-Server (Audio ist so deutlich stabiler als `file://`):

```bash
python3 serve.py
```

Dann im Browser oeffnen:

`http://127.0.0.1:8000/index.html`

## Features

- Handheld-Radio-Deck mit integrierten Modulen
- Drehregler (Drag/Touch + Pfeiltasten + Mausrad)
- Fine-Mode + Micro-Nudges fuer praezises Gegentunen
- Live-Abtastung ohne Scan-Button
- Dispatch/STACKCAST spawnen variabel ueber das Band und driften laufend
- Animiertes Oszilloskop mit Radio-Wellencharakter
- Lock-Meter fuer Dispatch/STACKCAST
- LCD-Status fuer `Reputation`, `Moral`, `Tech`, `Credits`, `Intel`, `Signal`
- Optionales Radar-Overlay per `Map Ping` (zeigt D/S/Jammer nur kurz)
- Bewegliche Stoersignale/Jammer mit negativer Empfangswirkung
- Story-Dependencies: Entscheidungen setzen Flags und schalten spaetere Folge-Events frei

## Theme Pack (live)

- `Field Unit`
- `Military Green`
- `Rusty Amber`

Das Theme ist im UI umschaltbar und wird im Browser gespeichert.

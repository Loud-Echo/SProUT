# Mitgeliefierte Funktionen


## Eingebaute Grundfunktionen

| Name   | Funktion                                                   | Beispiel                                                               |
|--------|------------------------------------------------------------|------------------------------------------------------------------------|
| `incr` | erhöht die Zahl um 1                                       | `"3 incr out # out : 4`                                                |
| `neg`  | negiert eine Zahl                                          | `"8 neg out # out: -8`                                                 |
| `ltz`  | (less than zero) ermittelt, ob eine Zahl kleiner als 0 ist | `"-3 ltz out # out: 1`  `"2 ltz out # out: 0`  `"0 ltz out # out: 0`   |


## Die mathematischen Grundfunktionen

Die wichtigsten mathematischen Funktionen werden in der Bibliothek mat_lib mitgeliefert.

| Name           | Funktion                  | Beispiel                                   |
|----------------|---------------------------|--------------------------------------------|
| `mat_lib.add`  | Addiert zwei Zahlen       | `"4 <  "2 <  < mat_lib.add out # out: 6`   |
| `mat_lib.sub`  | Subtrahiert zwei Zahlen   | `"4 <  "9 <  < mat_lib.sub out # out: 5`   |
| `mat_lib.mul`  | Multipliziert zwei Zahlen | `"3 <  "2 <  < mat_lib.mul out # out: 6`   |
| `mat_lib.mod`  | Module zweier Zahlen      | `"4 <  "18 <  < mat_lib.mod out # out: 2`  | 

# Mitgeliefierte Funktionen


## Eingebaute Grundfunktionen

| Name           | Funktion                                                             | Beispiel                                                             |
|----------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| `incr`         | erhöht die Zahl um 1                                                 | `"3 incr out # out : 4`                                              |
| `neg`          | negiert eine Zahl                                                    | `"8 neg out # out: -8`                                               |
| `ltz`          | (less than zero) ermittelt, ob eine Zahl kleiner als 0 ist           | `"-3 ltz out # out: 1`  `"2 ltz out # out: 0`  `"0 ltz out # out: 0` |
| `print_stacks` | Debug funktion, die den Inhalt der zwei Stacks in die Konsole druckt | `"-1 print_stacks out # out: 0 Konsole: Inhalt der Stacks`           |


## Die mathematischen Grundfunktionen

Die wichtigsten mathematischen Funktionen werden in der Bibliothek mat_lib mitgeliefert.

| Name               | Funktion                           | Beispiel                                                         |
|--------------------|------------------------------------|------------------------------------------------------------------|
| `std.mat_lib.add`  | Addiert zwei Zahlen                | `"4 <  "2 <  < mat_lib.add out # out: 6`                         |
| `std.mat_lib.sub`  | Subtrahiert zwei Zahlen            | `"4 <  "9 <  < mat_lib.sub out # out: 5`                         |
| `std.mat_lib.mul`  | Multipliziert zwei Zahlen          | `"3 <  "2 <  < mat_lib.mul out # out: 6`                         |
| `std.mat_lib.mod`  | Module zweier Zahlen               | `"4 <  "18 <  < mat_lib.mod out # out: 2`                        | 
| `std.mat_lib.pow`  | rechnet eine Zahl hoch eine andere | `"4 <  "2 < < mat_lib.pow out # out: 16`                         |
| `std.mat_lib.even` | überprüft ob eine Zahl grade ist   | `"4 mat_lib.even out # out: 1` o. `"7 mat_lib.even out # out: 0` |

## Stack Funktionen

Funktionen, die den Inhalt der Stacks bearbeiten werden in der Bibliothek stk_lib mitgeliefert.

| Name                 | Funktion                                                                                                                                                                                   | Beispiel                                                                                                                                                                           |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `std.stk_lib.linear` | Lineare Suche durch einen Bereich des Stacks - das erste eingelesene argument sollte die gesuchte Zahl sein, das zweite das Element, was den Datensatz begrenzt                            | `"-1 >  {befüllen mit des Stacks}  "-1 <  "3 <  < stk_lib.linear out # Die Grenze zwischen rechtem und linken Stack ist nun ein Element links von dem gesuchten Element - out: 0 ` |
| `std.stk_lib.bubble` | BubbleSort Algorithmus - der eingelesene Parameter ist die Begrenzung des Datensatz in beide Richtungen, Die Grenze zwischen den Stacks sollte sich am rechten Rand des Datensatz befinden | `{Stacks im Zustand [-1, e2, e3, e0, e1, ...]<>[-1]} "-1 stk_lib.bubble out #{Stacks im Zustand [-1, e0]<>[e1, e2, e3, ..., -1]} out: 1`                                           |

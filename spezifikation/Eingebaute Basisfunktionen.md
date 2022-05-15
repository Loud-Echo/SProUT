# Eingebaute Basisfunktionen


## Mathematische Grundfunktionen

| Name    | Funktion                                                                                           | Beispiel                                               |
|---------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| lit_int | konvertiert eine Zahl in die Zahlen der ASCII-Charaktere, die die Zahl im Zehner-System darstellen | `"66 lit_int out # out: 66 `, statt `"66 out # out: B` |
| add     | Addiert zwei Zahlen                                                                                | `"4 <; "2 <; < add lit_int out; # out: 6`              |
| neg     | negiert eine Zahl                                                                                  | `"8 neg out lit_int; # out: -8`                        |

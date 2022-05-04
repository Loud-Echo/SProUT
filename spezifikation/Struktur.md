#Struktur
SProUT zentrale Struktur basiert auf Speicherorten und dem verschieben von Daten zwischen diesen.
Die Grundlegende Syntax für alle Operationen in SProUT basiert daher auf dem Verschieben und sieht wie folgt aus:

`[Ausgangspunkt der Verschiebung] [mögliche Funktionen, die auf die Daten angewandt werden solle] 
[Endpunkt der Vieschiebung]`

## Speicherorte
Die Speicherorte sind: Input (`in`), Output (`out`), rechter Stack (`>`), linker Stack (`<`)
und vom Nutzer definierte Variableen.
Hierbei ist es anzumerken, dass sich der input den Stacks in sofern ähnelt, dass beide das Element entfernen, 
wenn es verschoben wird - die Variablen wiederum "kopieren" die Daten eher an das Ziel, 
behalten jedoch selbst ihren Wert. 
Beim Schreiben von Daten ist es ähnlich. 
Die Stacks und der Output bewegen alle anderen gespeicherten Elemente eine Schritt weiter. 
Die Variablen Daten in den Variablen werden überschrieben, wenn neue Daten zu ihnen verschoben werden.

Die zwei Stacks sind global und können aus jedem Kontext aufgerufen werden. Der In- und Output basiert auf 

## Datentypen
Es gibt nur einen Datentyp in SProUT, den Integer. Alle anderen Datentypen müssen (vom User) als dieser dargestellt werden.
Eine Ausnahme hierfür ist die Ausgabe in die Konsole. Diese stellt Den Integer zuerst als das entsprechend ASCII Zeichen dar.
(Falls man stattdessen die Zahl darstellen möchste kann man die Funktion `lit_int` verwenden, die die Zahl.)

Um feste Zahlen und Variablen von einander zu unterscheiden, werden feste Zahlen mit einem leitenden `"` geschrieben.
Beispiel: `420 -> "420`

## Funktionen
Funktionen können eine beliebige Anzahl an Elementen aus dem Ausgangs-Speichort ziehen, sie verarbeiten
und eine weitere beliebige Anzahl (nicht unbedingt die selbe, die eingelesen wurde) in den Ziel-Speichort schieben.
Sie kann hierbei zum Beispiel auch zuerst ein Element ziehen und verarbeiten, und es an den Zielort verschieben und 
daraufhin ein weiteres Objekt ziehen und verarbeiten. Dies ist zum Beispiel verwendbar, wenn man ein Funktion 
das Ergebnis zurück an den Ausgangsort schieben lässt, in welchem Fall sie in dem selben Funktionsaufruf ihre eigenen 
Ergebnisse weiterverarbeiten kann.

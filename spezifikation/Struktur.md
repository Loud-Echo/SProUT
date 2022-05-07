#Struktur
SProUT zentrale Struktur basiert auf Speicherorten und dem verschieben von Daten zwischen diesen.
Alle Sprout Programme sind Funktionen, die eine bestimmte Anzahl an Daten aus der Konsole einlesen 
(auch keine Daten einzulesen ist möglich)
und eine bestimmte Anzahl an Daten zurückgibt
(auch hier ist es möglich nichts zurück zugeben).


## Speicherorte
Die Speicherorte sind: Input, Output, rechter Stack, linker Stack, das Testregister, das Jumpregister
und vom Nutzer definierte Variableen.
Die Test- und Jumpregister verhalten sich wie Variablen, werden jedoch für weitere Funktionen genutzt. 
Hierbei ist es anzumerken, dass sich der input den Stacks in sofern ähnelt, dass beide das Element entfernen, 
wenn es verschoben wird - die Variablen wiederum "kopieren" die Daten eher an das Ziel, 
behalten jedoch selbst ihren Wert. 
Beim Schreiben von Daten ist es ähnlich. 
Die Stacks und der Output bewegen alle anderen gespeicherten Elemente eine Schritt weiter. 
Die Daten in den Variablen werden überschrieben, wenn neue Daten zu ihnen verschoben werden.

## Datentypen
Es gibt nur einen Datentyp in SProUT, den Integer. Alle anderen Datentypen müssen (vom User) als dieser dargestellt werden.
Eine Ausnahme hierfür ist die Ausgabe in die Konsole. Diese stellt den Integer zuerst als das entsprechend ASCII Zeichen dar.

## Funktionen
Funktionen können eine beliebige Anzahl an Elementen aus dem Ausgangs-Speichort ziehen, sie verarbeiten
und eine weitere beliebige Anzahl (nicht unbedingt die selbe, die eingelesen wurde) in den Ziel-Speichort schieben.
Sie kann hierbei zum Beispiel auch zuerst ein Element ziehen und verarbeiten, und es an den Zielort verschieben und 
daraufhin ein weiteres Objekt ziehen und verarbeiten. Dies ist zum Beispiel verwendbar, wenn man ein Funktion 
das Ergebnis zurück an den Ausgangsort schieben lässt, in welchem Fall sie in dem selben Funktionsaufruf ihre eigenen 
Ergebnisse weiterverarbeiten kann.

## Kontexte
Variablen können nur aus der selben Funktion aufgerufen werden. Die zwei Stacks sind global. Der Input und Output 
sind die Ausgangs- und Ziel-Speicherorte der aufgerufenen Funktion. Wenn das Programm mit einer Shell aufgerufen wird,
dann interagiren Input und Output des höchsten Levels (der main-Funktion) mit dieser.

# Syntax
Die Syntax von Sprout basiert auf Datenströmen, von Speicherort zu Speicherort und durch Funktionen.

## Definition von Funktionen
Funktionen werden durch folgende Syntax gekennzeichnet:
```
func [Name der Funktion]
    var
        [Variablen Block (opt. var u. rav müssen jedoch existieren)]
    rav
    [Inhalt der Funktion]
cnuf
```
Hierbei ist zu beachten, dass beim Ausführen der Funktion sie folgendermaßen 
angesprochen werden muss: `[Name der Datei (ohne .spr)].[Name der Funktion]` Dies wird getan, um keine doppelte definition desselben Namens in zwei Dateien zuzulassen.

## Symbole der Speicherorte
Der rechte Stack wird `>` geschrieben, der linke `<`, Input `inn` Output `out`, das Jumpregister `jmp`, das Testregister `tst`
Die verwendeten Variablen werden am Anfang einer Funktion mit folgender Syntax definiert:
```
var 
    [Name einer Variable]
    [Name einer Variable]
    [etc.]
rav
```
Diese können danach unter dem gegebenen Namen verwendet werden.

## Verschiebungen
Die Verschiebung von Daten wird durch folgende Syntax dargestellt:

`[Ausgangspeicher] [Funktionen (opt.)] [Zielspeicher];`

Wenn mehrere Funktionen aneinander gekettet werden, kann eine Funktion weniger Daten einlesen, 
als die letzte berechnet hat. Diese Daten werden trotzdem berechnet, jedoch nicht verwendet. Wenn sie jedoch mehr
einlesen möchte, wird ein Fehler hervorgerufen. Genauso verhält es sich auch, wenn eine Funktion mehr auslesen möchte, 
als in diesem vorhanden sind. Beim Input von der Konsole wird in diesem Fall auf den Nutzer gewartet.

Anmerkungen: 
Wenn keine Funktione spezifiziert ist, dann wird nur ein Element verschoben; 


## Bedingte Ausführung
Operationen können bedingt ausgeführt werden, indem sie Teil eines If-Blocks sind. Dieser sieht wie folgt aus und basirt
seine Ausführung auf dem Testregister (0: Block wird nicht ausgeführt, sonst: Block wird ausgeführt):
```
if
    [operationen]
fi
```

## Das Jumpregister
Das Jumpregister kann auf eine bestimmte Zeile gesetzt werden. 
Durch das Schlagwort `jump`, springt die Ausführung des Programms an diese Stelle. Falls die Zeile nicht Teil 
der momentanen Funktion ist, wird nicht gesprungen und ein Fehler wird hervorgerufen.

## Die While-Schleife
Die While-Schleife kombiniert die letzten beiden Konzepte: Das Schlagwort `while` setzt das Jumpregister 
auf die momentane Zeile, `elihw` tut dasselbe wie:
```
if 
    jump
fi
```
Anmerkung: Es ist Syntaktisch, anders als bei dem `if ... fi`-Block, nicht erfordert, dass jedes `while` durch ein `elihw`
beendet wird, ist jedoch stark empfohlen. Auch verschachtelte Blöcke sind bei `if ... fi`-Blöcken möglich, jedoch nicht
bei `while ... elihw`-Blöcken

## Kommentare
Kommentare werden durch ein `# ` markiert. Nach diesem Zeichen wird der Reste der Zeile als Kommentar aufgefasst.

## Importieren andere Dateien
Um die Funktionen einer anderen Datei zu verwenden, können wir diese am Anfang des Programms importieren:
```
import [Datei]
import [Datei]
import [Datei]
...
```

## Zahlen
Wenn man Zahlen im Programm verwenden möchte, muss man dies durch das Hinzufügen eines `"` am Anfang der Zahl markieren.
Um also zum Beispiel die Zahl 3 auf den linken Stack zu schieben müsste man `"3 <` schreiben.

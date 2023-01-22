# NLP

![](git_images/Parteien_Logo.jpg)

## Gruppe:
- Niclas Cramer
- Niklas Koch
- Michel Medved
- Jan Neifeld
- Constantin Rech
- Luis Steiner

## Ziel 
Wahlprogramme zu Bundestagswahlen sind sehr umfangreich und enthalten viele Informationen zu unterschiedlichsten Themenbereichen. Ziel dieses Projektes ist es eine End-to-End OCR NLP Pipeline zu erstellen, die lediglich die Wahlprogramme als PDF Dateien für die NLP Analyse benötigt. Mit Hilfe von OCR wird der Inhalt der Wahlprogramme in Text umgewandelt, welcher anschließend bei der NLP Analyse verwendet wird. Die Analysen beinhalten unter anderem die Gewichtung von Themen innerhalb der einzelnen Wahlprogramme sowie Vergleiche zwischen den einzelnen Parteien. 

## 1) OCR Text Extraktion (1_OCR_Preprocessing.ipynb) [~ 3h Laufzeit]
Der input Ordner enthält die einzelnen Wahlprogramme der sechs größten Parteien für die Bundestagswahl 2021. Für die OCR Textextraktion wird Tesseract als OCR engine verwendet (https://github.com/tesseract-ocr/tesseract/tree/main). Für die Installation von Tesseract-OCR folge dem User Manual für das entsprechende OS (https://pyimagesearch.com/2021/08/16/installing-tesseract-pytesseract-and-python-ocr-packages-on-your-system/).

Wichtig!!!
Während der Installation von Tesseract-OCR wird nach zu installierenden Komponenten gefragt. Hier muss bei den Sprachen German als Sprachpaket gewählt werden. Nach der Installation müsste sich in dem Ordner "Tesseract-OCR/tessdata" eine Datei mit dem Namen "deu.traineddata" befinden (siehe Screenshots).
<img src="git_images/DEU_Language_Package_Installation.png" width="100" 

Der input Ordner ist Ausgangspunkt für die automatisierte End-to-End Pipeline. Beim Ausführen des Skriptes wird für jede PDF Dateie, also für jedes Parteiwahlprogramm, ein separater Ordner angelegt, worin die einzelnen Bilder für jede Seite des Wahlprogramms nach PDF Segementierung gespeichert werden. Daher muss in dem Skript der vollständige Dateipfad des input Ordners angegeben werden, bevor das notebook gestartet wird. Die erstellten Ordner mit den einzelnen Bilddateien werden anschließend verwendet, um mit Hilfe von pytesseract-OCR den Text der einzelnen Seiten zu extrahieren. Der extrahierte Text wird dann jeweils für jede Partei in eine separate .txt Datei geschrieben. 


## Vorgehensweise

-	Herunterladen und Vorverarbeiten der der PDF-Dateien mithilfe von OCR
-	Auswerten der Texte und Klassifizierung der übergeordneten Themenbereiche 
-	Explorative Analyse der Artikel, Visualisierungen, evtl. Netzwerkanalysen


## LDA

Um die Inhalte der unterschiedlichen Klassen zu analysieren, wurde im ersten Schritt analysiert, ob die Klassen Wirtschaft, Klima, Bildung, Gesundheit, Wissenschaft, soziale Ursachen, Politik und Ideologie, Infrastruktur eine mögliche Abbildung der Texte möglich sind. Daher wurde die inhaltliche Struktur der Texte betrachtet.

 

 

## 2) Text Klassifizierungen

### Textklassifikation mit Hand-Crafted-Words:

In der Datei topic_g.yml wurden Wörter definiert, welche auf eine Klasse verweisen und die Grundlage bilden für die Zuordnung von Texten zu einer Klasse. Hierbei wird jene Klasse verwendet, welche basierend auf der höchsten Anzahl an zutreffenden Wörtern vorhanden ist.


### Textklassifikation mit Hugging Face

Mithilfe des Modells:     kann eine Klassifizierung der obengenannten Klassen durchgeführt werden und die Texte basierend auf einem vortrainierten Modell zugewiesen werden. Hierbei wird wie bei den Hand Crafter-Words die wahrscheinlichste Klasse als Primärklasse betrachtet. Jedoch die wahrscheinlichsten 3 Klassen werden zusätzlich ausgegeben. Dies ermöglicht eine bessere Bestimmung von Absätzen zu einem bestimmten Thema.

### Sentiment Analyse

Sentiment Analyse bestimmt die Stimmung innerhalb eines Satzes, welche wie die Klassifikation von Hugging face behandelt wird und die Wahrscheinlichkeit durch ein vortrainiertes Modell ergibt. Dabei werden die Sätze abermals einzeln bewertet.

### Hatespeech Analyse

Genauso wie Sentiment Analyse werden die Sätze auf Hatespeech analysiert, dabei muss ein Satz negativ konnotiert sein und Hatespeech aufweisen, um vollständig als Hatespeech klassifiziert zu werden

 

## ?) Visualisierung der Ergebnisse(Jan)
Auf Basis der Daten denen Sentiment, Hatespeech und Topic zugewiesen wurde können Verteilungen zwischen und innerhalb der Parteien dargestellt werden.
Bei Betrachtung der einzelnen Partei wird eine Themenverteilung erstellt, in der die Häufigkeit der dem Thema zugehörigen Sätze in absoluten Zahlen dargestellt wird.
Hier exemplarisch für die AFD: 
     
<img src="./DBVis/AFDTopic.png" width="600" >

Zusätzlich werden die Anteilsverteilungen der Parteien innerhalb der Themen dargestellt. Ebenfalls zu sehen ist der Anteil der verschiedenen Themen in der Gesamtheit der Wahlprogramme.

<img src="./DBVis/AllgTopic.png" width="600" >

Eine besondere Betrachtung der als Hatespeech klassifizierten Sätze in Verbindung mit Sentiment verknüpft ermöglicht den Vergleich der Parteien allgemein im Bereich Hatespeech und den Vergleich der einzelnen Themen der Parteien im Bereich Hatespeech.

<img src="./DBVis/HatespeechParteien.png" width="480" >  <img src="./DBVis/HatespeechParteienTopics.png" width="480" >

Die abgebildeten Diagramme sind nur Screenshots und können interaktiv im Frontend betrachtet werden.


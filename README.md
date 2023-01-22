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

## ?) Visualisierung der Ergebnisse(Jan)
Auf Basis der Daten denen Sentiment, Hatespeech und Topic zugewiesen wurde können Verteilungen zwischen und innerhalb der Parteien dargestellt werden.
Bei Betrachtung der einzelnen Partei wird eine Themenverteilung erstellt, in der die Häufigkeit der dem Thema zugehörigen Sätze in absoluten Zahlen dargestellt wird.
Hier exemplarisch für die AFD: 
     
<img src="./DBVis/AFDTopic.png" width="600" >

Zusätzlich werden die Anteilsverteilungen der Parteien innerhalb der Themen dargestellt. Ebenfalls zu sehen ist der Anteil der verschiedenen Themen in der Gesamtheit der Wahlprogramme.

<img src="./DBVis/AllgTopic.png" width="600" >

Eine besondere Betrachtung der als Hatespeech klassifizierten Sätze in Verbindung mit Sentiment verknüpft ermöglicht den Vergleich der Parteien allgemein im Bereich Hatespeech und den Vergleich der einzelnen Themen der Parteien im Bereich Hatespeech.

<img src="./DBVis/HatespeechParteien.png" width="480" ><img src="./DBVis/HatespeechParteienTopics.png" width="480" >

Die abgebildeten Diagramme sind nur Screenshots und können interaktiv im Frontend betrachtet werden.


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
![](git_images/DEU_Language_Package_Installation.png)

Der input Ordner ist Ausgangspunkt für die automatisierte End-to-End Pipeline. Beim Ausführen des Skriptes wird für jede PDF Dateie, also für jedes Parteiwahlprogramm, ein separater Ordner angelegt, worin die einzelnen Bilder für jede Seite des Wahlprogramms nach PDF Segementierung gespeichert werden. Die erstellten Ordner mit den einzelnen Bilddateien werden anschließend verwendet, um mit Hilfe von pytesseract-OCR den Text der einzelnen Seiten zu extrahieren. Der extrahierte Text wird dann jeweils für jede Partei in eine separate .txt Datei geschrieben. 


## Vorgehensweise

-	Herunterladen und Vorverarbeiten der der PDF-Dateien mithilfe von OCR
-	Auswerten der Texte und Klassifizierung der übergeordneten Themenbereiche 
-	Explorative Analyse der Artikel, Visualisierungen, evtl. Netzwerkanalysen



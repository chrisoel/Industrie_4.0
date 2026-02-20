# Python Kurs-Notebooks

Dieses Repository enthält einsteigerfreundliche Jupyter-Notebooks für einen vollständigen Python-Lernpfad.

## Inhalt

Die Notebooks sind in Lernreihenfolge nummeriert:

1. `01_Variablen_und_Datentypen.ipynb`
2. `02_Kontrollstrukturen_und_Logik.ipynb`
3. `03_Datenstrukturierung_und_Modularisierung.ipynb`
4. `04_Funktionen.ipynb`
5. `05_Module_und_Pakete.ipynb`
6. `06_Robustheit_und_Profi_Techniken.ipynb`
7. `07_Dateioperationen_und_IO.ipynb`
8. `08_Objektorientierte_Programmierung_OOP.ipynb`
9. `09_Standardbibliothek_Batteries_Included.ipynb`
10. `10_Fortgeschrittene_Programmiertechniken.ipynb`
11. `11_Ausblick_auf_externe_Module_Data_Science_und_Co.ipynb`

Zusätzlich:
- `Software - Python.pdf` als Kurszusammenfassung

## Schnellstart

### Voraussetzungen

- Python 3.10+ installiert
- `pip` verfügbar

### 1) Virtuelle Umgebung anlegen und aktivieren

Linux / macOS (bash, zsh):
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows (CMD):
```bat
py -m venv .venv
.\.venv\Scripts\activate.bat
```

### 2) Abhängigkeiten installieren

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Optional für Web/GUI-Beispiele:

```bash
python -m pip install -r requirements-optional.txt
```

### 3) Jupyter Notebook starten

```bash
jupyter notebook
```

### 4) Umgebung wieder verlassen (optional)

```bash
deactivate
```

## Hinweise zu Notebooks

- In Notebook-Zellen für Installationen möglichst `%pip install ...` nutzen.
- Bei Importproblemen zuerst den aktiven Interpreter prüfen:

```python
import sys
print(sys.executable)
```

## Empfohlene GitHub-Struktur

- Hauptbranch: `main`
- Commit-Botschaften kurz und kapitelbezogen (z. B. `Kapitel 05: Übungen erweitert`)
- Große Binärdateien vermeiden (Notebooks sind bereits als Text/JSON versionierbar)

## Lizenz

Der Lizenzstatus ist aktuell noch nicht festgelegt.

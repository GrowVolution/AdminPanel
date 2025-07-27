## 🗂️ Projekt Struktur

```bash
AdminPanel/
├── app/
    ├── static/           # statische Dateien
        ├── ...
    ├── dialogs/          # Package
        ├── ...
    ├── widgets/          # Package
        ├── ...
    ├── __init__.py       # MainWindow
├── events/               # Package
    ├── ...
├── threads/              # Package
    ├── ...
├── utils/                # Tools
    ├── ...
├── qt_ui/                # Benutzeroberfläche
    ├── templates/
        ├── *.ui
    ├── __init__.py       # compile_ui() Funktion
    ├── ...
├── main.py               # App starten
├── packaging.py          # Enthält die Package Klasse
├── ...                           
```
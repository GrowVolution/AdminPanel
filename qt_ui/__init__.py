from pathlib import Path
import subprocess

def compile_ui():
    templates_dir = Path(__file__).parent / "templates"
    output_dir = Path(__file__).parent

    for ui_file in templates_dir.glob("*.ui"):
        py_file = output_dir / f"{ui_file.stem}.py"
        subprocess.run(
            ["pyside6-uic", str(ui_file), "-o", str(py_file)],
            check=True
        )


if __name__ == "__main__":
    compile_ui()

# EjerciciosLyfter

Homework and exercises for the Lyfter programming course.

## Structure

| Folder | Contents |
| --- | --- |
| `IT_Essentials/` | Algorithm and terminal exercises (`.docx`, `.pdf`, `.xlsx`) |
| `Logica_de_Programacion/` | Pseudocode exercises and flowcharts (`.drawio`) |
| `Python_Basico/` | Python exercises (one subfolder per topic) and the Student Control System project |
| `historial_cambios.txt` | Change log of the repository |

### Python_Basico

Exercise topics: `Introduccion_a_Python`, `Sintaxis`, `Iterables_y_Listas`, `Diccionarios`, `Funciones`, `Excepciones`, `Manejo_de_Archivos`, `Manejo_de_CSV`, `Manejo_de_JSON`.

Project: `Student_Control_System/` is a Python program split into `main.py`, `menu.py`, `actions.py` and `data.py`, with its data stored in `data.csv`.

## File naming

Python exercises follow the pattern `<lesson>ejercicioPython<number>_<Topic>.py`, for example `9ejercicioPython3_Funciones.py`.

## Running the scripts

Scripts read their data files (`.txt`, `.csv`, `.json`) using relative paths, so run each script from inside its own folder:

```bash
cd Python_Basico/Manejo_de_CSV
python 16ejercicioPython1_CSV.py
```

## Git conventions

Commit messages and pull requests are written in English.

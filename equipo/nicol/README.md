# Nicol — terminal educativa y retos

**Rama:** `feature/nicol-terminal-retos`
**Puntaje de rúbrica que ayuda a ganar:** Integración de unidades (20), Innovación (5), Interfaz (parte de 15), Calidad de repositorio (5).

## Estado actual (27/11/2026)

`src/modules/terminal.py` y `src/modules/quizzes.py` están vacíos. El contrato `ResultadoOperacion` ya existe y el catálogo los muestra como `listo=False`. El tutor y el frontend ya funcionan.

## Qué tienes que hacer

1. **Terminal simulada** (`src/modules/terminal.py`)
   - Árbol de archivos y directorios ficticio en memoria, con ruta actual por sesión.
   - Comandos mínimos: `pwd`, `ls`, `cd`, `mkdir`, `touch`, `clear`.
   - Explicación breve de cada comando y errores didácticos (ruta inexistente, argumentos inválidos).
   - **Nunca** ejecutar comandos reales (`subprocess`, shell, archivos del proyecto).
2. **Retos** (`src/modules/quizzes.py`)
   - Banco de preguntas de opción múltiple separado de la interfaz, cubriendo los cinco temas.
   - Seleccionar pregunta, evaluar respuesta, explicar acierto/error, puntaje y resumen de temas a reforzar.
3. **Pruebas**: agrega `tests/test_terminal.py` y `tests/test_quizzes.py`.
4. **Catálogo**: al terminar cada módulo verificado, cambia `listo=True` en `src/modules/catalog.py`.
5. **Documenta** los nombres de clases y métodos para que Antonio los conecte.

## Contrato obligatorio

Todas las operaciones devuelven `ResultadoOperacion(ok, mensaje, datos)` de `src/modules/contracts.py`, con `datos` serializable.

## Verificación antes de subir

```powershell
python -m unittest discover -s tests -v
python -m src.cli --modulos
```

## Cómo trabajar

```powershell
git switch main
git pull origin main
git switch -c feature/nicol-terminal-retos
# ... implementar ...
git add src/modules/terminal.py src/modules/quizzes.py src/modules/catalog.py tests/
git commit -m "feat(terminal-retos): terminal simulada y evaluacion"
git push -u origin feature/nicol-terminal-retos
```

Abre un Pull Request a `main`. **No hagas commits directos a `main`.**

## Prompt para tu IA

Copia el contenido de [`PROMPT.md`](PROMPT.md). Versión corta:

> Implementa `src/modules/terminal.py` y `src/modules/quizzes.py` de EduSO AI siguiendo `PROMPT.md`. Terminal ficticia sin comandos reales, retos con puntaje y retroalimentación, todo con `ResultadoOperacion`, pruebas en `tests/` y catálogo actualizado.

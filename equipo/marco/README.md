# Marco — simuladores de procesos y memoria

**Rama:** `feature/marco-simuladores`
**Puntaje de rúbrica que ayuda a ganar:** Integración de unidades (20), Interfaz (parte de 15), Innovación (5), Calidad de repositorio (5).

## Estado actual (27/11/2026)

`src/modules/processes.py` y `src/modules/memory.py` están vacíos. El contrato `ResultadoOperacion` ya existe y el catálogo los muestra como `listo=False`. El resto del proyecto ya funciona: tutor, frontend y documentación.

## Qué tienes que hacer

1. **Procesos** (`src/modules/processes.py`)
   - Crear procesos con id estable (`Nuevo`).
   - Transiciones válidas: `Nuevo→Listo`, `Listo→Ejecutando`, `Ejecutando→Esperando|Terminado|Listo`, `Esperando→Listo`.
   - Rechazar transiciones inválidas con `ResultadoOperacion.error(...)`.
   - Guardar historial y una explicación breve por transición (sirve para enseñar).
   - Devolver estado serializable (`a_dict()`).
2. **Memoria** (`src/modules/memory.py`)
   - RAM ficticia de 100 MB; asignar y liberar bloques por id.
   - Validar tamaños positivos, ids inexistentes y falta de espacio.
   - Devolver total, usado, libre y bloques (para que Antonio dibuje la RAM).
3. **Pruebas**: agrega `tests/test_processes.py` y `tests/test_memory.py` con casos válidos e inválidos.
4. **Catálogo**: al terminar y verificar, cambia `listo=True` en `src/modules/catalog.py`.
5. **Documenta** en `README.md` o en `src/modules/` los nombres de clases y métodos para que Antonio los conecte.

## Contrato obligatorio

```python
from src.modules.contracts import ResultadoOperacion

ResultadoOperacion.exito("Proceso creado", {"id": 1, "estado": "Nuevo"})
ResultadoOperacion.error("Transición inválida", {"estado": "Terminado"})
```

No usar Streamlit dentro de los módulos. No tocar la RAM real del equipo.

## Verificación antes de subir

```powershell
python -m unittest discover -s tests -v
python -m src.cli --modulos
```

## Cómo trabajar

```powershell
git switch main
git pull origin main
git switch -c feature/marco-simuladores
# ... implementar ...
git add src/modules/processes.py src/modules/memory.py src/modules/catalog.py tests/
git commit -m "feat(simuladores): procesos y memoria con pruebas"
git push -u origin feature/marco-simuladores
```

Abre un Pull Request a `main`. **No hagas commits directos a `main`.**

## Prompt para tu IA

Copia el contenido de [`PROMPT.md`](PROMPT.md) y pégalo en tu asistente con la carpeta del proyecto abierta. Si prefieres uno corto:

> Implementa `src/modules/processes.py` y `src/modules/memory.py` de EduSO AI siguiendo `PROMPT.md`. Usa `ResultadoOperacion`, agrega pruebas en `tests/`, actualiza `catalog.py` cuando esté verificado y no uses Streamlit ni la memoria real.

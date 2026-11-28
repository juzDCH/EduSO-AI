# Antonio — frontend Streamlit

**Rama:** `feature/antonio-frontend`
**Puntaje de rúbrica que ayuda a ganar:** Interfaz de usuario (15 + 5 bonus), Integración de unidades (parte de 20).

## Estado actual (27/11/2026)

`app.py` funciona: inicio con cinco temas, página “Explorar temas” con explicación/analogía/ejemplo, paso al tutor y estado de módulos. El flujo fue verificado con AppTest. El tutor ya responde y rechaza temas fuera de alcance.

## Qué tienes que hacer

1. **Diseño y legibilidad**: mejorar jerarquía visual, espaciado, colores y adaptación a pantallas; mantener la elección de temas.
2. **Separar páginas** si aporta claridad (`pages/`): Inicio, Tutor, Procesos, Memoria, Terminal, Retos.
3. **Integrar los módulos cuando estén listos**:
   - Procesos y memoria: usar la API de `src/modules/processes.py` y `memory.py` (Marco).
   - Terminal y retos: usar `src/modules/terminal.py` y `quizzes.py` (Nicol).
   - Mostrar “En desarrollo” mientras `listo=False`; habilitar solo cuando `catalog.py` diga `True`.
4. **Manejo de errores**: pregunta vacía, modelo no entrenado, baja confianza y tema fuera de alcance con mensajes claros.
5. **Bonus +5**: la app es web (Streamlit); documenta cómo se conecta con los materiales del curso (temas, ejemplos, preguntas).
6. **No dupliques lógica** de Dante, Marco o Nicol dentro de Streamlit.

## Contrato

```python
from src.services.tutor import ServicioTutor
respuesta = ServicioTutor().responder(pregunta)
datos = respuesta.a_dict()
```

`respuesta.requiere_reformular` indica que no hay contenido para mostrar (baja confianza o tema `otros`). No cambies el contrato sin coordinar con Dante.

## Verificación antes de subir

```powershell
streamlit run app.py
python -m unittest discover -s tests -v
```

Recorre manualmente: Inicio → tema → pregunta del tutor → respuesta; y una pregunta fuera de tema. Reporta qué viste.

## Cómo trabajar

```powershell
git switch main
git pull origin main
git switch -c feature/antonio-frontend
# ... implementar ...
git add app.py pages/
git commit -m "feat(frontend): integra modulos y mejora navegacion"
git push -u origin feature/antonio-frontend
```

Abre un Pull Request a `main`.

## Prompt para tu IA

Copia el contenido de [`PROMPT.md`](PROMPT.md). Versión corta:

> Mejora el frontend Streamlit de EduSO AI siguiendo `PROMPT.md`: diseño, páginas por módulo y conexión con `ServicioTutor`, `catalog.py` y los módulos de Marco/Nicol. No dupliques lógica del backend ni marques módulos como listos sin estarlo.

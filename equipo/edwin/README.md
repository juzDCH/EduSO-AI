# Edwin — integración, calidad y entrega

**Rama:** `feature/edwin-integracion`
**Puntaje de rúbrica que ayuda a ganar:** Enfoque didáctico (20), Integración de unidades (20), Interfaz (parte de 15), Calidad de repositorio (5). La exposición (10) se prepara al final.

## Estado actual (27/11/2026)

El tutor (Dante), el frontend base (Antonio) y la documentación técnica están integrados en `main`. Los simuladores y la terminal siguen pendientes (Marco y Nicol). Hay 17 pruebas automáticas y la app arranca con `streamlit run app.py`.

## Qué tienes que hacer

1. **Verificar instalación limpia**: clona el repo en otra carpeta, crea el entorno, instala `requirements.txt`, entrena y ejecuta la app. Registra los comandos y los resultados reales.
2. **Documentación de entrega** en `docs/`:
   - `INSTALACION.md`: pasos desde cero y problemas encontrados.
   - `DEMOSTRACION.md`: guion de 5 minutos que solo prometa funciones comprobadas.
   - `VALIDACION.md`: protocolo para probar con un estudiante de primer semestre, con autorización y observaciones reales.
3. **Confirmar U1–U5** con el programa oficial y actualizar `docs/UNIDADES.md`. Si no está disponible, deja la pregunta pendiente y no inventes el mapeo.
4. **Coordinar los PR** de Marco, Nicol y Antonio: revisar contratos (`ServicioTutor`, `ResultadoOperacion`, `catalog.py`), conflictos y que ningún módulo figure `listo=True` sin estarlo.
5. **Mantener** `README.md`, `ESTADO_PROYECTO.md` y `docs/RUBRICA.md` al día con evidencia real.
6. **Validación con estudiante (bonus +5)**: conseguir autorización, mostrar la app, registrar preguntas y comentarios reales; separar observaciones de opiniones.

## Verificación antes de subir

```powershell
python -m src.train
python -m unittest discover -s tests -v
python -m src.cli "¿Qué es un proceso?"
streamlit run app.py
```

## Cómo trabajar

```powershell
git switch main
git pull origin main
git switch -c feature/edwin-integracion
# ... documentar y verificar ...
git add docs/ README.md ESTADO_PROYECTO.md
git commit -m "docs: integracion y guia de entrega"
git push -u origin feature/edwin-integracion
```

Abre un Pull Request a `main`. No reescribas los módulos de otros sin acordarlo.

## Prompt para tu IA

Copia el contenido de [`PROMPT.md`](PROMPT.md). Versión corta:

> Actúa como responsable de integración de EduSO AI. Verifica instalación limpia, revisa README/requirements, documenta arquitectura, demo y validación en `docs/`, y deja una lista priorizada de problemas. No inventes métricas, testimonios ni unidades curriculares.

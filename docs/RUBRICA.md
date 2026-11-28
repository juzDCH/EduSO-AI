# Revisión de la rúbrica del hackathon

**Proyecto:** EduSO AI — tutor de Sistemas Operativos con IA
**Asignatura:** Tecnologías Emergentes II (TEM2T7) — Unidad 5 (NLP y Aplicaciones)
**Fecha de esta revisión:** 27/11/2026
**Alcance:** se revisan los criterios 1 a 5, 7 y 8. La **exposición (criterio 6) queda fuera de esta revisión** por decisión del equipo; se prepara más adelante.

## Estado general

**Avance de implementación: ~40%.** Están cerradas la parte de IA/tutor (Dante), la base del frontend (Antonio) y la documentación técnica. El 60% restante corresponde a los simuladores de procesos y memoria (Marco), la terminal y los retos (Nicol), la integración/validación/demo (Edwin) y el pulido de la interfaz. Cada pendiente está repartido en `equipo/<integrante>/README.md` y `equipo/<integrante>/PROMPT.md`.

| # | Criterio | Pts | Estado | Evidencia en el repositorio | Qué falta y quién |
| --- | --- | --- | --- | --- | --- |
| 1 | Enfoque didáctico | 20 | **Parcial — base sólida** | Tutor con explicación, analogía, ejemplo y pregunta de comprobación; cinco temas de primer semestre; contenido revisable en `src/knowledge_base.py`; `docs/MODELO.md`. | Validar con un estudiante real y registrar evidencia (Edwin); demo guiada. |
| 2 | Integración de unidades | 20 | **Parcial** | El tutor integra conceptualmente procesos, memoria, kernel, comandos y archivos; `docs/UNIDADES.md` deja el mapeo U1–U5 marcado como tentativo. | Simuladores de procesos/memoria (Marco) y terminal/retos (Nicol); confirmar U1–U5 con el programa oficial (Edwin). |
| 3 | Calidad del modelo | 15 | **Cumple** | TF-IDF + Regresión Logística justificado; validación cruzada 5 pliegues F1 macro **0.858 ± 0.039**; holdout accuracy **0.764**; comparación de modelos, umbral y palabras por tema en `reports/`; `docs/MODELO.md`. | Ampliar datos cuando haya preguntas reales de estudiantes (Dante). |
| 4 | Preprocesamiento y datos | 10 | **Cumple** | 300 preguntas educativas balanceadas (60 por tema) + 60 ejemplos de rechazo; normalización de tildes, mayúsculas, puntuación y espacios; `reports/muestra_preprocesamiento.csv`; sin duplicados. | Mostrar el preprocesamiento en la demo (Dante/Edwin). |
| 5 | Interfaz de usuario | 15 (+5 bonus) | **Parcial** | Streamlit funcional con inicio, cinco temas, contenido guiado y tutor en tiempo real; navegación por estado de módulos. | Integrar procesos, memoria, terminal y retos cuando estén listos; diseño adaptable; el bonus web ya se cumple por ser Streamlit (Antonio). |
| 6 | Exposición (5 min) | 10 | **Fuera de alcance** | — | Guion de demo y reparto de la presentación (Edwin), cuando el equipo lo decida. |
| 7 | Calidad de código y repositorio | 5 | **Cumple** | README, `requirements.txt`, código comentado, contratos comunes, 17 pruebas automáticas, ramas por integrante y Pull Requests. | Mantener README y estado al día (Edwin). |
| 8 | Innovación y creatividad | 5 | **Parcial** | Tutor con analogías, pregunta de comprobación y rechazo amable de temas fuera de alcance; clasificador propio. | Gamificación, visualizaciones y retos (Nicol/Marco), una vez integrados los módulos. |

## Cómo se llega al 40 %

- **IA y tutor (Dante):** dataset propio, preprocesamiento, modelo evaluado, umbral, pruebas y documentación.
- **Frontend (Antonio):** aplicación Streamlit navegable con los cinco temas y el tutor.
- **Repositorio y documentación:** contratos, catálogo de módulos, ramas, Pull Requests y pruebas.

El 60 % restante no se implementa aquí: queda en los prompts del equipo para que cada integrante lo trabaje en su rama y lo integre a `main` con su propio PR.

## Verificaciones ejecutadas

```powershell
python -m src.train
python -m unittest discover -s tests -v
python -m src.cli --temas
python -m src.cli "¿Qué es un proceso?"
streamlit run app.py
```

- Entrenamiento: 360 ejemplos, 288/72, F1 macro CV 0.858, holdout 0.764.
- Pruebas: 17 pruebas, todas correctas.
- App: AppTest de Streamlit sin excepciones.

## Riesgos y límites que no se deben ocultar

- El dataset es propio y pequeño (360 ejemplos); las métricas son internas, no validación externa.
- La confianza del clasificador no está calibrada; el umbral 0.35 se eligió con las sondas de `data/sondas_fuera_de_tema.csv`.
- El mapeo U1–U5 **no está confirmado** con el programa oficial: no afirmarlo como definitivo.
- Todavía no hay validación con estudiantes ni testimonios; no inventarlos.

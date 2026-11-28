# Arquitectura de EduSO AI

## Vista general

```text
Streamlit (app.py)
   │  navegación y presentación
   ├── ServicioTutor (src/services/tutor.py)
   │      ├── PredictorIntenciones (src/predictor.py) ── models/modelo_nlp.joblib
   │      └── BASE_CONOCIMIENTO (src/knowledge_base.py)
   ├── catálogo de módulos (src/modules/catalog.py)
   └── futuros módulos (Marco y Nicol)
          ├── processes.py  ─┐
          ├── memory.py      ├── ResultadoOperacion (contracts.py)
          ├── terminal.py    │
          └── quizzes.py    ─┘
```

## Flujo del tutor

1. El estudiante escribe una pregunta en `app.py`.
2. `ServicioTutor.responder()` valida el texto (no vacío, máximo 500 caracteres).
3. `PredictorIntenciones` vectoriza con TF-IDF (palabras + caracteres) y la Regresión Logística devuelve intención y confianza.
4. Si la intención es `otros`, o la confianza es menor al umbral (0.35), el servicio responde con un mensaje de reformulación. Si no, toma el contenido educativo de `knowledge_base`.
5. `RespuestaTutor.a_dict()` entrega datos simples (`titulo`, `explicacion`, `analogia`, `ejemplo`, `pregunta_comprobacion`, `intencion`, `confianza`, `requiere_reformular`).

El modelo **clasifica**; no genera texto. El contenido educativo se edita en `src/knowledge_base.py` sin reentrenar.

## Datos y artefactos

- `data/dataset.csv`: 300 preguntas educativas (60 por tema).
- `data/ejemplos_fuera_de_tema.csv`: 60 ejemplos para la clase `otros`.
- `data/sondas_fuera_de_tema.csv`: 23 sondas que solo se usan para evaluar el umbral.
- `models/modelo_nlp.joblib`: pipeline entrenado que consume el predictor.
- `reports/`: métricas, matriz de confusión, comparación de modelos, umbral, palabras por tema, muestra de preprocesamiento y errores del holdout. Se regeneran con `python -m src.train`.

## Contratos para el equipo

- **Tutor:** `ServicioTutor().responder(pregunta)` → `RespuestaTutor`; `respuesta.a_dict()`.
- **Módulos:** todas las operaciones devuelven `ResultadoOperacion(ok, mensaje, datos)` de `src/modules/contracts.py`.
- **Catálogo:** `listar_modulos()` de `src/modules/catalog.py` informa `clave`, `titulo`, `responsable`, `listo`, `resumen` y `archivo`.
- **Frontend:** consume esos contratos; no duplica clasificación, transiciones de procesos ni ejecución de comandos.

## Reglas de integración

1. Cada integrante trabaja en su rama (`feature/<nombre>-<parte>`) y abre un Pull Request a `main`.
2. Ningún módulo se marca `listo=True` hasta estar implementado y verificado.
3. Si un módulo cambia el contrato, se coordina con Antonio antes de integrarlo.
4. Las métricas y los estados del proyecto se actualizan con evidencia real, no a mano.

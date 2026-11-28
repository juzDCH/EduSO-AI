# EduSO AI

Tutor educativo de Sistemas Operativos para estudiantes de primer semestre. Responde preguntas sobre **procesos, memoria, kernel, comandos y archivos** con una explicación sencilla, una analogía, un ejemplo y una pregunta de comprobación.

> **Estado: ~40 % del proyecto.** La parte de IA/tutor, la base del frontend y la documentación técnica están cerradas. El 60 % restante (simuladores, terminal, retos, integración, validación y exposición) está repartido en los prompts de `equipo/`.

## Estado por módulo

| Módulo | Responsable | Estado |
| --- | --- | --- |
| Tutor IA: dataset, modelo, servicio y contenido | Dante | **Listo** (con mejoras opcionales) |
| Frontend Streamlit: inicio, temas y tutor | Antonio | **Base lista**; falta integrar módulos y pulir diseño |
| Simulador de procesos y memoria | Marco | **Pendiente** — ver `equipo/marco/README.md` |
| Terminal educativa y retos | Nicol | **Pendiente** — ver `equipo/nicol/README.md` |
| Integración, documentación, validación y demo | Edwin | **Pendiente** — ver `equipo/edwin/README.md` |

La revisión criterio por criterio de la rúbrica está en [`docs/RUBRICA.md`](docs/RUBRICA.md). La ficha del modelo está en [`docs/MODELO.md`](docs/MODELO.md).

## Qué funciona ahora

- **Tutor:** clasifica la intención con TF-IDF (palabras + caracteres) y Regresión Logística; entrega explicación, analogía, ejemplo y pregunta de comprobación desde una base editable.
- **Rechazo de temas ajenos:** una sexta clase `otros` y un umbral de confianza evitan responder preguntas que no son de Sistemas Operativos.
- **Frontend:** `app.py` permite elegir entre cinco temas, explorar una explicación y pasar una pregunta de ejemplo al tutor.
- **Módulos pendientes visibles:** procesos, memoria, terminal y retos aparecen como “En desarrollo” con responsable y descripción.
- **Consola:** se puede probar el servicio sin abrir la interfaz.
- **Pruebas:** 17 pruebas automáticas de datos, preprocesamiento, servicio y entrenamiento.

El modelo **clasifica**; no genera texto. El contenido educativo se sirve desde `src/knowledge_base.py` y se puede revisar sin reentrenar.

## Preparar y ejecutar

Se recomienda Python 3.11 o 3.12.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m src.train
streamlit run app.py
```

Para probar el backend por separado:

```powershell
python -m src.cli --temas
python -m src.cli "¿Qué es un proceso?"
python -m unittest discover -s tests -v
```

## Estructura

```text
EduSO-AI/
├── app.py                      # frontend Streamlit
├── pages/                      # espacio para páginas adicionales
├── data/
│   ├── dataset.csv             # 300 preguntas educativas (60 por tema)
│   ├── ejemplos_fuera_de_tema.csv
│   └── sondas_fuera_de_tema.csv
├── models/modelo_nlp.joblib
├── reports/                    # métricas, matriz, umbral, palabras por tema
├── src/
│   ├── cli.py
│   ├── knowledge_base.py
│   ├── predictor.py
│   ├── preprocess.py
│   ├── train.py
│   ├── services/tutor.py
│   └── modules/                # módulos de Marco y Nicol + contratos
├── tests/                      # 17 pruebas automáticas
├── docs/                       # rúbrica, modelo, arquitectura y unidades
├── equipo/                     # README y prompt de cada integrante
├── PROMPTS/README.md           # entrada rápida para el equipo
├── ESTADO_PROYECTO.md
├── PROJECT_PLAN.md
├── CONTRIBUTING.md
├── requirements.txt
└── README.md
```

## Modelo y resultados

- **Datos:** 300 preguntas educativas (60 por tema) + 60 ejemplos de rechazo; 23 sondas externas para el umbral.
- **Validación:** holdout estratificado 80/20 (semilla 42) y validación cruzada de 5 pliegues.
- **Resultados:** F1 macro en validación cruzada **0.858 ± 0.039**; holdout accuracy **0.764** y F1 **0.763**.
- **Umbral de confianza:** **0.35**, con cobertura 88.7 %, acierto 92.1 % entre las preguntas respondidas y 0 % de aceptación de sondas fuera de tema.

Son métricas internas sobre un dataset propio y pequeño; **no son validación externa**. Cada ejecución de `python -m src.train` regenera `reports/` completo.

## Contrato del tutor para el frontend

```python
from src.services.tutor import ServicioTutor

tutor = ServicioTutor()
respuesta = tutor.responder("¿Qué pasa cuando abro un programa?")
datos = respuesta.a_dict()
```

`datos` contiene `titulo`, `explicacion`, `analogia`, `ejemplo`, `pregunta_comprobacion`, `intencion`, `intencion_sugerida`, `confianza` y `requiere_reformular`. El servicio valida texto vacío o mayor a 500 caracteres y lanza `PreguntaInvalidaError`.

## Equipo y flujo de trabajo

Cada integrante tiene su README y su prompt listo para copiar:

| Integrante | Guía | Prompt |
| --- | --- | --- |
| Dante | [README](equipo/dante/README.md) | [PROMPT](equipo/dante/PROMPT.md) |
| Antonio | [README](equipo/antonio/README.md) | [PROMPT](equipo/antonio/PROMPT.md) |
| Marco | [README](equipo/marco/README.md) | [PROMPT](equipo/marco/PROMPT.md) |
| Nicol | [README](equipo/nicol/README.md) | [PROMPT](equipo/nicol/PROMPT.md) |
| Edwin | [README](equipo/edwin/README.md) | [PROMPT](equipo/edwin/PROMPT.md) |

El índice rápido es [`PROMPTS/README.md`](PROMPTS/README.md). Cada persona parte de `main`, crea su rama (`feature/<nombre>-<parte>`), hace su commit, publica y abre un Pull Request. **No se suben commits directos a `main`.**

## Requisitos académicos por confirmar

- El programa oficial U1–U5 no está en el repositorio; el mapeo de [`docs/UNIDADES.md`](docs/UNIDADES.md) es tentativo y debe confirmarse.
- Falta la validación con un estudiante de primer semestre; no hay testimonios ni resultados de aprendizaje.
- La exposición de cinco minutos se prepara al final, cuando los módulos estén integrados.

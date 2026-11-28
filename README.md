# EduSO AI

Plataforma educativa para aprender Sistemas Operativos con un tutor, simulaciones y retos. La base incluye una primera app funcional y deja puntos de extensión claros para que el equipo complete y mejore cada módulo.

> **Equipo:** empieza por [PROMPTS/README.md](PROMPTS/README.md) para ver qué ya está hecho, qué le falta a cada integrante y cómo trabajar en su propia rama.

## Repartición del equipo

| Integrante | Parte | Entrega principal | Archivos asignados |
| --- | --- | --- | --- |
| Dante | IA y servicio del tutor | Dataset, preprocesamiento, clasificador, contenido y respuesta estructurada | `data/`, `src/train.py`, `src/services/tutor.py`, `src/knowledge_base.py` |
| Antonio | Frontend | Streamlit, navegación, diseño visual y conexión de las páginas | `app.py`, `pages/` |
| Marco | Simuladores | Estados/transiciones de procesos y laboratorio de memoria RAM | `src/modules/processes.py`, `src/modules/memory.py` |
| Nicol | Terminal y evaluación | Terminal Linux ficticia, retos, puntaje y contenido didáctico | `src/modules/terminal.py`, `src/modules/quizzes.py` |
| Edwin | Integración y entrega | Coordinación técnica, revisión integral, documentación, validación y demo | `docs/`, `PROJECT_PLAN.md`, README final |

Cada persona apoya la integración de su módulo. Edwin coordina la revisión final, la documentación de entrega, la validación y el ensayo de la exposición.

## Qué funciona ahora

- **Tutor:** clasifica la intención con TF-IDF + Regresión Logística y entrega explicación, analogía, ejemplo y pregunta de comprobación desde una base editable.
- **Frontend inicial:** `app.py` permite elegir entre cinco temas, explorar una explicación con analogía y ejemplo, y pasar una pregunta de ejemplo al tutor. También muestra los otros módulos como próximos laboratorios.
- **Módulos pendientes visibles:** procesos, memoria, terminal y retos aparecen como “En desarrollo” con responsable y descripción.
- **Consola:** se puede probar el servicio antes de usar la interfaz.

El clasificador es un modelo de intención; el texto educativo se sirve desde contenido escrito y revisable. No se presenta como un modelo generativo.

## Estructura

```text
EduSO-AI/
├── app.py
├── pages/                         # espacio de Antonio para páginas adicionales
├── data/dataset.csv
├── models/modelo_nlp.joblib
├── reports/                       # métricas, matriz y muestra de preprocesamiento
├── src/
│   ├── cli.py
│   ├── knowledge_base.py
│   ├── predictor.py
│   ├── preprocess.py
│   ├── train.py
│   ├── services/tutor.py
│   └── modules/                   # módulos de Marco y Nicol + contratos comunes
├── equipo/                         # prompt de trabajo y estado por integrante
│   ├── dante/PROMPT.md
│   ├── antonio/PROMPT.md
│   ├── marco/PROMPT.md
│   ├── nicol/PROMPT.md
│   └── edwin/PROMPT.md
├── docs/                           # documentación final coordinada por Edwin
├── PROMPTS/README.md               # entrada rápida: tareas, estado y ramas
├── ESTADO_PROYECTO.md              # avance actual, entregado y pendiente
├── PROJECT_PLAN.md
├── requirements.txt
└── README.md
```

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
python -m src.cli --modulos
python -m src.cli --temas
python -m src.cli "¿Qué pasa cuando abro un programa?"
```

## Contrato del tutor para el frontend

```python
from src.services.tutor import ServicioTutor

tutor = ServicioTutor()
respuesta = tutor.responder("¿Qué pasa cuando abro un programa?")
datos = respuesta.a_dict()
```

`datos` contiene `titulo`, `explicacion`, `analogia`, `ejemplo`, `pregunta_comprobacion`, `intencion`, `intencion_sugerida`, `confianza` y `requiere_reformular`. El servicio valida texto vacío y preguntas de más de 500 caracteres. El umbral inicial de confianza es 0.30 y queda configurable; debe ajustarse con ejemplos reales, porque la confianza del clasificador no está calibrada.

## Modelo y resultados iniciales

El dataset tiene 100 preguntas, 20 por tema: `procesos`, `memoria`, `kernel`, `comandos` y `archivos`. El entrenamiento usa división estratificada 80/20, semilla fija y genera métricas por clase y matriz de confusión en `reports/`.

La línea base registrada obtuvo accuracy **0.75**, precision macro **0.80**, recall macro **0.75** y F1 macro **0.749**, sobre solo 20 preguntas de prueba (4 por tema). Son métricas iniciales internas; el equipo debe revisar y ampliar los ejemplos y no presentarlas como validación externa. Cada ejecución de `python -m src.train` reemplaza los resultados por las métricas recién calculadas.

## Requisitos académicos por confirmar

El plan del curso pide integrar unidades U1–U5. Hay que contrastar procesos y memoria con el programa oficial antes de afirmar qué unidades cubre el proyecto. También queda pendiente validar el prototipo con un estudiante de primer semestre y documentar sus comentarios con autorización.

## Guía del equipo

Cada carpeta de `equipo/` tiene un `PROMPT.md` listo para copiar en el asistente de código. Incluye el estado actual, tareas pendientes, archivos y criterios de entrega. El reparto y los criterios técnicos están en [PROJECT_PLAN.md](PROJECT_PLAN.md); el tablero de avance está en [ESTADO_PROYECTO.md](ESTADO_PROYECTO.md).

El índice más directo para el equipo es [PROMPTS/README.md](PROMPTS/README.md): resume el avance real de las cinco partes y enlaza cada prompt.

El flujo de ramas para que cada integrante parta de `main`, trabaje en su rama y proponga su integración está en [CONTRIBUTING.md](CONTRIBUTING.md).

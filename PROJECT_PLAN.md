# Plan de trabajo por integrante

Este documento deja alcance, archivos, contrato de integración y criterios de terminado para que el equipo avance en paralelo.

## Dante — IA y backend del tutor

**Archivos:** `data/dataset.csv`, `src/preprocess.py`, `src/train.py`, `src/predictor.py`, `src/knowledge_base.py`, `src/services/tutor.py`.

**Base entregada:** 100 preguntas balanceadas, limpieza reproducible, pipeline TF-IDF + Regresión Logística, evaluación holdout, artefacto del modelo, base de conocimiento con explicación/analogía/ejemplo, validación de entrada y respuesta serializable.

**Pendiente para dejarlo sólido:** revisar cada etiqueta con el contenido oficial de la materia; ampliar ejemplos variados por intención; comparar rendimiento por clase; calibrar el umbral con preguntas reales; anotar las unidades U1–U5 cuando el equipo tenga el programa.

**Contrato para Antonio:** `ServicioTutor().responder(pregunta)` devuelve `RespuestaTutor`; llamar `respuesta.a_dict()` para obtener datos simples de mostrar. Errores de entrada se reportan como `PreguntaInvalidaError`. El entrenamiento se vuelve a generar con `python -m src.train`.

## Antonio — Frontend e integración

**Archivos:** `app.py`, `pages/`.

**Base entregada:** app Streamlit mínima con inicio, tutor, presentación de confianza y estado de cada módulo. El servicio del tutor se cachea para no cargar el modelo en cada interacción.

**Pendiente:** mejorar identidad visual y diseño adaptable; separar páginas; añadir navegación a los simuladores y retos cuando estén listos; mostrar errores de entrada/modelo con mensajes útiles; no duplicar la lógica de Dante, Marco o Nicol dentro de Streamlit.

**Contrato compartido:** `src.modules.catalog.listar_modulos()` entrega tarjetas con `clave`, `titulo`, `responsable`, `listo`, `resumen` y `archivo`. Usa ese estado para mostrar “Disponible” o “En desarrollo”.

**Criterio de terminado:** la aplicación arranca con las instrucciones del README; se puede navegar a cada módulo; estados pendientes y errores se explican claramente; la interfaz funciona en el tamaño de pantalla de la demostración; la lógica permanece en `src/`.

## Marco — simuladores de Sistemas Operativos

**Archivos:** `src/modules/processes.py`, `src/modules/memory.py`.

**Procesos — pendiente:** crear proceso; transiciones válidas Nuevo → Listo → Ejecutando → Esperando/Terminado y Esperando → Listo; rechazar transiciones imposibles; devolver estado e historial para visualizar. Añadir explicación corta por transición.

**Memoria — pendiente:** RAM ficticia de 100 MB; asignar y liberar bloques por identificador; rechazar tamaños inválidos o solicitudes mayores al espacio libre; reportar ocupado/libre y bloques actuales. No tocar la RAM real del equipo.

**Criterio de terminado:** API sin dependencia de Streamlit, estados serializables a diccionarios, errores claros y escenarios de demostración descritos en README o exposición. Al terminar, cambiar `listo` a `True` en `src/modules/catalog.py`.

## Nicol — terminal, retos y material didáctico

**Archivos:** `src/modules/terminal.py`, `src/modules/quizzes.py`.

**Terminal — pendiente:** intérprete con directorio y archivos ficticios en memoria; comenzar con `pwd`, `ls`, `cd`, `mkdir`, `touch` y `clear`; devolver salida y explicación del comando. No ejecutar procesos ni comandos del sistema operativo anfitrión.

**Retos — pendiente:** preguntas etiquetadas por tema; respuesta correcta; explicación ante acierto/error; puntaje y resumen de temas a reforzar. Separar banco de preguntas de la presentación.

**Criterio de terminado:** entradas/salidas serializables, manejo de comando/pregunta inválidos y contenido revisado contra la materia. Al terminar cada módulo, actualizar `src/modules/catalog.py`.

**Formato de integración:** las operaciones de procesos, memoria, terminal y retos devuelven `ResultadoOperacion` (`ok`, `mensaje`, `datos`) desde `src/modules/contracts.py`.

## Edwin — integración, calidad y entrega

**Archivos:** `docs/`, `README.md`, `PROJECT_PLAN.md`; coordina las revisiones sin apropiarse del código de los módulos.

**Base entregada:** estructura común, contratos de operación, estado de módulos y comandos de instalación/ejecución documentados.

**Pendiente:** verificar la instalación desde un entorno limpio; integrar y recorrer los cinco módulos cuando estén listos; revisar errores de integración y consistencia de documentación; preparar una guía de demostración de cinco minutos; coordinar una validación real con un estudiante y registrar resultados solo con autorización.

**Requisito académico:** pedir al equipo o docente el programa oficial U1–U5, mapear cada módulo a la unidad correcta y documentar la fuente. No adivinar ni afirmar correspondencias no confirmadas.

**Criterio de terminado:** README permite preparar y ejecutar el proyecto siguiendo pasos reproducibles; la guía de demo refleja la app real; incidencias y resultados de validación tienen evidencia; no se inventan métricas, pruebas, testimonios ni cobertura curricular.

## Integración de equipo

1. Cada responsable completa su carpeta y deja el módulo con la interfaz acordada.
2. Al terminar, actualiza `src/modules/catalog.py` y la tabla de estado de este plan.
3. Edwin coordina la revisión de contratos y los recorridos completos; Antonio integra la navegación con los módulos disponibles.
4. Dante reentrena el clasificador después de revisar el dataset y guarda métricas reales.
5. Confirmar las unidades U1–U5 con el programa oficial.
6. Validar el prototipo con un estudiante de primer semestre con su autorización y documentar observaciones.
7. Preparar instalación, ejecución, capturas y exposición de cinco minutos.

## Prompts de trabajo

Las instrucciones de inicio para cada integrante están en `equipo/<nombre>/PROMPT.md`. Cada prompt indica qué existe, qué falta, qué archivos tocar y cómo entregar el trabajo.

## Trabajo con GitHub

El repositorio compartido es `https://github.com/juzDCH/EduSO-AI`. Cada integrante clona `main`, crea la rama que indica su prompt, publica sus cambios en esa rama y abre un Pull Request hacia `main`. Edwin coordina revisión e integración. El procedimiento completo está en `CONTRIBUTING.md`.

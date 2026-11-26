# Prompt de trabajo — Dante

```text
Trabaja como responsable de IA y backend del tutor de EduSO AI. Antes de editar, lee README.md, PROMPTS/README.md, PROJECT_PLAN.md y este prompt. Revisa el estado real del repositorio y conserva la interfaz que ya consume app.py.

GIT ANTES DE TRABAJAR
1. Clona https://github.com/juzDCH/EduSO-AI.git y entra a la carpeta EduSO-AI.
2. Parte de la última main: git switch main; git pull origin main.
3. Crea tu rama: git switch -c feature/dante-ia.
4. Después de crear la rama, realiza las tareas de este prompt. No hagas commits en main. Al terminar, verifica tus cambios, agrega solo tus archivos, crea un commit, publica con git push -u origin feature/dante-ia y abre un Pull Request hacia main. Se integra a main después de revisión y sin errores.

LO QUE YA EXISTE
- data/dataset.csv contiene 100 preguntas, 20 por intención: procesos, memoria, kernel, comandos y archivos.
- src/preprocess.py normaliza minúsculas, tildes, puntuación y espacios.
- src/train.py entrena TF-IDF + Regresión Logística con split estratificado 80/20 y guarda modelo y reportes.
- src/predictor.py carga el modelo; src/knowledge_base.py contiene respuestas didácticas.
- src/services/tutor.py ofrece ServicioTutor.responder() y RespuestaTutor.a_dict().
- Línea base registrada: accuracy 0.75, precision macro 0.80, recall macro 0.75 y F1 macro 0.749 en 20 ejemplos de prueba. No la presentes como validación externa.

TU PARTE
1. Audita preguntas, etiquetas, duplicados, lenguaje natural y cobertura de cada intención; corrige problemas con cuidado y explica los cambios.
2. Amplía el dataset con preguntas variadas y equilibradas, incluyendo distintas formas de preguntar. Conserva las cinco categorías salvo que el equipo acuerde otra cosa.
3. Comprueba que preprocesamiento, pipeline y predictor usen el mismo flujo; mantén respuestas explicativas en la base de conocimiento y no describas el clasificador como IA generativa.
4. Evalúa el modelo con métricas reales por clase y una evaluación apropiada para el tamaño del dataset; deja comandos reproducibles y resultados generados por el entrenamiento.
5. Revisa el umbral 0.30 de confianza con ejemplos reales; calibra o documenta una elección provisional, sin fingir que la confianza ya está calibrada.
6. Si el contenido oficial U1–U5 no está en el repositorio, deja el mapeo pendiente y solicítalo al equipo; no inventes la correspondencia.

ARCHIVOS PRINCIPALES
data/dataset.csv, src/preprocess.py, src/train.py, src/predictor.py, src/knowledge_base.py, src/services/tutor.py, reports/.

CRITERIOS DE ENTREGA
- El frontend sigue pudiendo usar ServicioTutor().responder(pregunta) y respuesta.a_dict().
- El dataset conserva el formato pregunta,intencion y las métricas se regeneran, nunca se escriben a mano.
- Documenta tamaño, clases, método de evaluación, resultados reales y limitaciones.
- Ejecuta verificaciones pertinentes y reporta los comandos y resultados exactos; no declares comprobado algo que no ejecutaste.
- Resume archivos modificados, decisiones, pendientes y cómo integrar tu parte.
```

# Prompt de trabajo — Dante

```text
Trabaja como responsable de IA y backend del tutor de EduSO AI. Antes de editar, lee README.md, docs/RUBRICA.md, docs/MODELO.md, PROMPTS/README.md y este prompt. Revisa el estado real del repositorio y conserva la interfaz que ya consume app.py.

GIT ANTES DE TRABAJAR
1. Clona https://github.com/juzDCH/EduSO-AI.git y entra a la carpeta EduSO-AI.
2. Parte de la última main: git switch main; git pull origin main.
3. Crea tu rama: git switch -c feature/dante-ia.
4. Después de crear la rama, realiza las tareas de este prompt. No hagas commits en main. Al terminar, verifica tus cambios, agrega solo tus archivos, crea un commit, publica con git push -u origin feature/dante-ia y abre un Pull Request hacia main. Se integra a main después de revisión y sin errores.

LO QUE YA EXISTE EN MAIN
- data/dataset.csv: 300 preguntas educativas (60 por tema: procesos, memoria, kernel, comandos y archivos).
- data/ejemplos_fuera_de_tema.csv: 60 ejemplos para la clase de rechazo "otros".
- data/sondas_fuera_de_tema.csv: 23 sondas que solo se usan para evaluar el umbral.
- src/preprocess.py normaliza tildes, mayúsculas, puntuación y espacios.
- src/train.py compara TF-IDF de palabras contra TF-IDF de palabras + caracteres, usa validación cruzada de 5 pliegues y holdout 80/20, y guarda el modelo y los reportes.
- src/predictor.py carga el modelo; src/knowledge_base.py contiene respuestas didácticas de los cinco temas.
- src/services/tutor.py ofrece ServicioTutor.responder() y RespuestaTutor.a_dict(); rechaza la clase "otros" y aplica un umbral de confianza de 0.35.
- Resultados actuales: F1 macro en validación cruzada 0.858 ± 0.039; holdout accuracy 0.764 y F1 0.763. No son validación externa.
- Hay 17 pruebas automáticas en tests/ y la ficha del modelo está en docs/MODELO.md.

TU PARTE
1. La base ya está implementada. Revisa etiquetas, duplicados, lenguaje natural y cobertura de cada intención; corrige solo con justificación.
2. Amplía el dataset cuando tengas preguntas reales de estudiantes o ejemplos nuevos bien fundamentados; mantén el equilibrio y vuelve a entrenar.
3. Revisa las confusiones de reports/errores_holdout.csv (kernel/archivos, memoria/procesos) y añade ejemplos que las separen.
4. Mantén el flujo: el modelo clasifica y el contenido se sirve desde src/knowledge_base.py. No presentes el clasificador como IA generativa.
5. Revisa el umbral 0.35 con las sondas y con preguntas reales; si cambia, actualiza el valor, el análisis y docs/MODELO.md.
6. Confirma el mapeo U1–U5 con el equipo o el docente. Si el programa oficial no está, deja el mapeo como tentativo en docs/UNIDADES.md; no inventes la correspondencia.

ARCHIVOS PRINCIPALES
data/, src/preprocess.py, src/train.py, src/predictor.py, src/knowledge_base.py, src/services/tutor.py, tests/, reports/ y docs/MODELO.md.

CRITERIOS DE ENTREGA
- El frontend sigue pudiendo usar ServicioTutor().responder(pregunta) y respuesta.a_dict().
- El dataset conserva el formato pregunta,intencion y las métricas se regeneran con python -m src.train, nunca se escriben a mano.
- Documenta tamaño, clases, método de evaluación, resultados reales y limitaciones.
- Ejecuta python -m src.train y python -m unittest discover -s tests -v; reporta los comandos y resultados exactos.
- Actualiza docs/MODELO.md y docs/RUBRICA.md si cambian los resultados.
- Resume archivos modificados, decisiones, pendientes y cómo integrar tu parte.
```

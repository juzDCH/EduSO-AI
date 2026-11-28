# Modelo del tutor — ficha técnica

## 1. Objetivo

Clasificar una pregunta escrita por un estudiante de primer semestre en uno de los cinco temas de Sistemas Operativos que cubre el tutor: **procesos, memoria, kernel, comandos y archivos**. Una sexta clase, `otros`, permite rechazar preguntas ajenas a la materia en lugar de responder algo incorrecto.

El modelo **no genera texto**: reconoce el tema y el contenido educativo se sirve desde `src/knowledge_base.py`, que es revisable sin reentrenar.

## 2. Datos

| Conjunto | Archivo | Ejemplos | Uso |
| --- | --- | --- | --- |
| Preguntas educativas | `data/dataset.csv` | 300 (60 por tema) | Entrenamiento y evaluación |
| Ejemplos de rechazo | `data/ejemplos_fuera_de_tema.csv` | 60 | Clase `otros` |
| Sondas fuera de tema | `data/sondas_fuera_de_tema.csv` | 23 | Solo evaluación del umbral; nunca se entrenan |

Total de entrenamiento y evaluación: **360 ejemplos**, seis clases balanceadas (60 cada una). Requisito académico del hackathon: mínimo 50 ejemplos; se supera ampliamente.

El dataset es propio, escrito para el proyecto. No proviene de una fuente externa ni de preguntas reales de estudiantes, por lo que las métricas son internas.

## 3. Preprocesamiento

`src/preprocess.py` aplica a cada pregunta:

1. Normalización Unicode NFKD y eliminación de tildes.
2. Minúsculas.
3. Eliminación de todo lo que no sea letra o número (signos de interrogación, comas, etc.).
4. Colapso de espacios.

No se eliminan palabras vacías porque frases cortas como “qué es” aportan contexto. Ejemplos reproducibles en `reports/muestra_preprocesamiento.csv`.

## 4. Modelo

- **Vectorización:** TF-IDF de palabras (unigramas y bigramas, `sublinear_tf`) + TF-IDF de fragmentos de caracteres (`char_wb`, 3 a 5), con peso 1.0 y 0.7 respectivamente.
- **Clasificador:** Regresión Logística multinomial, `class_weight="balanced"`, `C=4`, semilla 42.
- **Justificación:** con pocos ejemplos, TF-IDF + Regresión Logística es rápido, reproducible, entrega probabilidades y permite inspeccionar los pesos por tema. La bolsa de palabras captura términos técnicos y los n-gramas de caracteres toleran variaciones de escritura (por ejemplo, tildes o errores leves). Se comparó contra la variante solo de palabras:

| Modelo | F1 macro (CV 5) | Desviación | Accuracy (CV 5) |
| --- | --- | --- | --- |
| TF-IDF palabras + caracteres + LR | **0.858** | 0.039 | 0.858 |
| TF-IDF palabras + LR | 0.818 | 0.040 | 0.819 |

Resultados reproducibles en `reports/comparacion_modelos.csv`.

## 5. Evaluación

Protocolo: división estratificada 80/20 con semilla 42 para el holdout, y validación cruzada estratificada de 5 pliegues sobre los 360 ejemplos. El modelo que se guarda se reentrena con todos los datos después de medir.

| Métrica | Holdout (72 ejemplos) | Validación cruzada (5 pliegues) |
| --- | --- | --- |
| Accuracy | 0.764 | 0.858 |
| Precision macro | 0.779 | — |
| Recall macro | 0.764 | — |
| F1 macro | 0.763 | **0.858 ± 0.039** |

Matriz de confusión en `reports/matriz_confusion.csv`; errores del holdout en `reports/errores_holdout.csv`; reporte por clase dentro de `reports/metricas.json`.

## 6. Umbral de confianza

Cada predicción devuelve la probabilidad máxima. El tutor responde solo si la clase no es `otros` y la confianza alcanza el umbral.

El análisis con probabilidades fuera de pliegue y con las 23 sondas externas está en `reports/umbral.csv`:

| Umbral | Cobertura de preguntas educativas | Acierto entre respondidas | Aceptación de fuera de tema |
| --- | --- | --- | --- |
| 0.30 | 93.7 % | 89.3 % | 4.3 % |
| **0.35** | **88.7 %** | **92.1 %** | **0.0 %** |
| 0.40 | 85.7 % | 92.6 % | 0.0 % |

Se elige **0.35** porque mantiene una cobertura alta, supera el 90 % de acierto entre las preguntas que responde y no aceptó ninguna sonda fuera de tema. El valor es configurable en `ServicioTutor(umbral_confianza=...)`. La confianza **no está calibrada formalmente**: es la probabilidad del clasificador, no una garantía de acierto.

## 7. Limitaciones y uso responsable

- Dataset propio y pequeño; el holdout tiene solo 72 ejemplos y varía con la semilla.
- Las confusiones más frecuentes son entre temas cercanos: kernel/archivos (“llamada al sistema para leer un archivo”), memoria/procesos y comandos/archivos.
- El modelo no “entiende” el lenguaje: reconoce patrones de palabras. Una pregunta muy distinta a las del dataset puede quedar fuera o recibir un tema equivocado.
- No es una IA generativa y no debe presentarse como tal.
- No se ha validado con estudiantes; no hay evidencia de mejora de aprendizaje.
- El mapeo de temas a unidades U1–U5 está pendiente de confirmación (`docs/UNIDADES.md`).

## 8. Reproducibilidad

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m src.train
python -m unittest discover -s tests -v
```

`python -m src.train` regenera el modelo y **todos** los artefactos de `reports/`; no se escriben métricas a mano.

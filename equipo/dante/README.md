# Dante — IA y tutor (parte cerrada, con mejoras pendientes)

**Rama:** `feature/dante-ia`
**Puntaje de rúbrica que cubre:** Calidad del modelo (15), Preprocesamiento y datos (10), parte de Enfoque didáctico (20).

## Estado actual (27/11/2026)

Esta parte ya está integrada en `main`:

- Dataset propio de **300 preguntas** educativas (60 por tema) + **60 ejemplos de rechazo** + **23 sondas** para el umbral.
- Preprocesamiento reproducible (tildes, mayúsculas, puntuación, espacios).
- Modelo TF-IDF (palabras + caracteres) + Regresión Logística, comparado contra la variante de solo palabras.
- Validación cruzada 5 pliegues: **F1 macro 0.858 ± 0.039**. Holdout: accuracy **0.764**, F1 **0.763**.
- Umbral **0.35** elegido con cobertura 88.7 %, acierto 92.1 % y 0 % de aceptación de sondas fuera de tema.
- Servicio del tutor con validación de entrada y respuesta de rechazo para temas ajenos.
- 17 pruebas automáticas y ficha del modelo en `docs/MODELO.md`.

## Qué queda por mejorar (no bloquea la entrega)

1. Confirmar con el equipo el mapeo U1–U5 (`docs/UNIDADES.md`) y ajustar los nombres de los temas si el programa oficial usa otros.
2. Reemplazar o ampliar ejemplos cuando haya preguntas reales de estudiantes; volver a entrenar y comparar métricas.
3. Revisar las confusiones de `reports/errores_holdout.csv` y añadir ejemplos que las separen (kernel/archivos, memoria/procesos).
4. Mostrar el preprocesamiento en la demo (`reports/muestra_preprocesamiento.csv`).
5. Mantener `docs/MODELO.md` actualizado si cambian datos, modelo o umbral.

## Comandos

```powershell
python -m src.train
python -m unittest discover -s tests -v
python -m src.cli "¿Qué es un proceso?"
```

`python -m src.train` regenera el modelo y todos los artefactos de `reports/`; no escribir métricas a mano.

## Cómo trabajar una mejora

```powershell
git switch main
git pull origin main
git switch -c feature/dante-ia
# ... mejorar datos/modelo ...
python -m src.train
python -m unittest discover -s tests -v
git add data/ src/ reports/ docs/
git commit -m "feat(modelo): mejora dataset y metricas"
git push -u origin feature/dante-ia
```

Abre un Pull Request a `main`.

## Prompt para tu IA

Copia el contenido de [`PROMPT.md`](PROMPT.md). Versión corta:

> Revisa la parte de IA de EduSO AI siguiendo `PROMPT.md`. Amplía el dataset solo con ejemplos reales o justificados, reentrena con `python -m src.train`, compara métricas y actualiza `docs/MODELO.md`. No inventes resultados ni afirmes unidades curriculares sin confirmarlas.

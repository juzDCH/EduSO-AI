# Estado actual de EduSO AI

**Actualizado:** 27/11/2026 · **Avance estimado: ~40 %.** El 60 % restante está repartido en `equipo/<integrante>/README.md` y sus prompts.

## Por integrante

| Responsable | Ya tenemos | Falta para cerrar su parte | Estado |
| --- | --- | --- | --- |
| **Dante** | Dataset de 300 preguntas + 60 ejemplos de rechazo; preprocesamiento; TF-IDF + Regresión Logística; comparación de modelos; validación cruzada y holdout; umbral 0.35; modelo, reportes y ficha en `docs/MODELO.md`; pruebas. | Confirmar U1–U5; ampliar con preguntas reales; revisar confusiones; mostrar preprocesamiento en la demo. | **Cerrada la base** |
| **Antonio** | App Streamlit con Inicio, cinco temas, explicación/analogía/ejemplo, paso al tutor y estado de módulos; verificada con AppTest. | Integrar procesos, memoria, terminal y retos cuando estén listos; diseño adaptable y páginas propias. | **Base lista; integración pendiente** |
| **Marco** | Contrato `ResultadoOperacion`; catálogo muestra procesos y memoria como pendientes. | Implementar transiciones de procesos e historial; simulador de 100 MB; pruebas; marcar `listo=True`. | **Pendiente** |
| **Nicol** | Contrato `ResultadoOperacion`; catálogo muestra terminal y retos como pendientes. | Implementar terminal ficticia; banco de retos, puntaje y retroalimentación; pruebas; marcar `listo=True`. | **Pendiente** |
| **Edwin** | Plan de integración, documentación técnica base (`docs/ARQUITECTURA.md`, `docs/RUBRICA.md`) y comandos de ejecución. | Verificar instalación limpia; `INSTALACION.md`, `DEMOSTRACION.md`, `VALIDACION.md`; confirmar U1–U5; coordinar PR y validación con estudiante. | **Pendiente** |

## Métricas y evidencias

- **Dataset:** 360 ejemplos (300 educativos balanceados + 60 de rechazo). Requisito del hackathon: mínimo 50.
- **Modelo:** TF-IDF de palabras + caracteres y Regresión Logística.
- **Validación cruzada (5 pliegues):** F1 macro **0.858 ± 0.039**, accuracy **0.858**.
- **Holdout (72 ejemplos):** accuracy **0.764**, precision macro **0.779**, recall macro **0.764**, F1 macro **0.763**.
- **Umbral 0.35:** cobertura 88.7 %, acierto 92.1 % entre respondidas, 0 % de aceptación de sondas fuera de tema.
- Detalle en `reports/metricas.json`, `reports/umbral.csv`, `reports/matriz_confusion.csv` y `docs/MODELO.md`.

## Revisión técnica

- **Entrenamiento:** ejecutado con `python -m src.train`; modelo y artefactos regenerados.
- **Pruebas automáticas:** 17 pruebas en `tests/`; todas correctas.
- **App Streamlit:** AppTest sin excepciones; recorrido manual de tema y tutor.
- **Integración de los cinco módulos:** parcial; el tutor y el frontend funcionan; los simuladores, la terminal y los retos están pendientes.
- **Unidades U1–U5:** pendientes de confirmar con el programa oficial; mapeo tentativo en `docs/UNIDADES.md`.
- **Validación con estudiante:** pendiente; no hay resultados ni testimonios.

## Rúbrica

La revisión criterio por criterio está en [`docs/RUBRICA.md`](docs/RUBRICA.md). Resumen: modelo, datos y repositorio están cubiertos; enfoque didáctico, integración de unidades e interfaz están parcialmente cubiertos; exposición fuera de alcance por ahora; innovación depende de los retos y visualizaciones.

## Siguiente orden recomendado

1. **Marco** implementa procesos y memoria y abre su PR.
2. **Nicol** implementa terminal y retos y abre su PR.
3. **Antonio** integra los módulos y pule la interfaz.
4. **Edwin** verifica instalación, documenta demo/validación, confirma unidades y coordina la revisión final.
5. **Dante** revisa datos/modelo con preguntas reales y mantiene la ficha del modelo.

## Reparto del avance

- **40 % hecho:** IA/tutor, frontend base, documentación técnica, pruebas y repositorio.
- **60 % pendiente:** simuladores, terminal, retos, integración, validación con estudiante y exposición.

# Estado actual de EduSO AI

Este tablero refleja los archivos que existen ahora. Actualizarlo al completar cada entrega.

## Por integrante

| Responsable | Ya tenemos | Falta para cerrar su parte | Estado |
| --- | --- | --- | --- |
| **Dante** | Dataset inicial de 100 preguntas; limpieza; TF-IDF + Regresión Logística; modelo guardado; métricas; base didáctica; servicio reutilizable del tutor. | Revisar etiquetas y redacción; ampliar ejemplos; revisar evaluación por clase; ajustar umbral con datos reales; confirmar unidades curriculares con el programa. | Base implementada; mejoras de calidad pendientes |
| **Antonio** | App Streamlit inicial con Inicio, Tutor IA, tarjetas de estado y conexión con el servicio del tutor. | Mejorar diseño y adaptación; separar páginas; conectar simuladores, terminal y retos cuando estén disponibles. | MVP de interfaz en código; pulido e integración pendientes |
| **Marco** | Archivos asignados y contrato común `ResultadoOperacion`; catálogo muestra procesos y memoria pendientes. | Implementar transiciones de procesos e historial; simulador de 100 MB; validaciones, errores y datos serializables. | Pendiente de implementación |
| **Nicol** | Archivos asignados y contrato común; catálogo muestra terminal y retos pendientes. | Implementar terminal sobre sistema de archivos ficticio; banco de retos, evaluación, puntaje y retroalimentación. | Pendiente de implementación |
| **Edwin** | Alcance asignado y prompt de trabajo; plan de integración y entrega. | Crear documentación técnica/demo; coordinar integración y revisión final; confirmar U1–U5 con programa oficial; coordinar validación real y reportar evidencia. | Pendiente de integración y entrega |

## Métricas existentes

La ejecución de entrenamiento registrada obtuvo accuracy **0.75**, precision macro **0.80**, recall macro **0.75** y F1 macro **0.749** sobre 20 preguntas de prueba (cuatro por intención). Es una línea base pequeña. Los detalles están en `reports/metricas.json` y `reports/matriz_confusion.csv`.

## Revisión técnica

- **Entrenamiento NLP:** ejecutado para generar el modelo y los reportes.
- **App Streamlit:** el código inicial existe; todavía no se ha registrado una ejecución manual de la interfaz.
- **Pruebas automáticas:** aún no hay una suite de pruebas del proyecto.
- **Integración de los cinco módulos:** pendiente; solo el tutor tiene lógica funcional actualmente.
- **Unidades U1–U5:** pendientes de confirmar con el programa oficial.
- **Validación con estudiante:** pendiente; no se han registrado resultados ni testimonios.

## Siguiente orden recomendado

1. Dante revisa dataset y temas con el contenido real de la materia.
2. Marco y Nicol implementan sus módulos usando el contrato común.
3. Antonio mejora y conecta la interfaz conforme se habiliten módulos.
4. Edwin coordina verificaciones integradas, documentación, validación y demo.


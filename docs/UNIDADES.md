# Unidades curriculares y cobertura

> **Aviso importante:** el programa oficial U1–U5 no está en el repositorio. El mapeo de esta página es **tentativo** y debe confirmarse con el docente o el equipo antes de presentarlo como definitivo. No se debe afirmar una correspondencia que no esté verificada.

## Estado

El tutor cubre conceptualmente cinco bloques de Sistemas Operativos: procesos, memoria, kernel, comandos y archivos. Para la rúbrica (“integra al menos 2 unidades”), los bloques con mayor respaldo actual son **procesos** y **memoria**, porque incluyen explicación, analogía, ejemplo y pregunta de comprobación. Los simuladores interactivos que harían demostrable esa integración todavía están pendientes (Marco y Nicol).

## Mapeo tentativo

| Unidad | Tema probable | Cómo la cubre EduSO AI | Evidencia | Estado |
| --- | --- | --- | --- | --- |
| U1 | Introducción a los sistemas operativos | Tutor: qué es el kernel, su papel como intermediario y los servicios del sistema. | `src/knowledge_base.py` (`kernel`); 60 preguntas del tema. | Parcial, por confirmar |
| U2 | Procesos y planificación | Tutor: definición, estados, PCB, cambio de contexto, planificador, hilos. | `src/knowledge_base.py` (`procesos`); 60 preguntas; futuro simulador de Marco. | Base conceptual; simulador pendiente |
| U3 | Gestión de memoria | Tutor: RAM, memoria virtual, paginación, fallos de página, fragmentación. | `src/knowledge_base.py` (`memoria`); 60 preguntas; futuro laboratorio de Marco. | Base conceptual; simulador pendiente |
| U4 | Archivos y almacenamiento | Tutor: archivos, directorios, rutas, sistemas de archivos, permisos. | `src/knowledge_base.py` (`archivos`); 60 preguntas. | Parcial, por confirmar |
| U5 | Comandos y terminal (o NLP, según el programa) | Tutor: comandos básicos; futuro intérprete educativo de Nicol. | `src/knowledge_base.py` (`comandos`); 60 preguntas; `src/modules/terminal.py` vacío. | Parcial, por confirmar |

## Qué falta para cerrar este criterio

1. Obtener el programa oficial y confirmar el nombre exacto de cada unidad.
2. Completar los simuladores de procesos y memoria (Marco) y la terminal/retos (Nicol).
3. Integrarlos en la app para que la cobertura sea demostrable en vivo (Antonio).
4. Documentar en `docs/UNIDADES.md` la fuente del programa y retirar el aviso de “tentativo”.

Mientras no exista esa confirmación, la exposición debe decir: “cubrimos procesos y memoria con el tutor y estamos integrando los simuladores; el mapeo exacto a U1–U5 está por confirmar”.

# Prompt de trabajo — Edwin

```text
Trabaja como responsable de integración, calidad y entrega de EduSO AI. Lee README.md, PROJECT_PLAN.md y este prompt. Coordina con los demás responsables y no reescribas sus módulos sin acordarlo.

GIT ANTES DE TRABAJAR
1. Clona https://github.com/juzDCH/EduSO-AI.git y entra a la carpeta EduSO-AI.
2. Parte de la última main: git switch main; git pull origin main.
3. Crea tu rama: git switch -c feature/edwin-integracion.
4. No hagas commits en main. Al terminar, agrega solo tus archivos, crea un commit, publica con git push -u origin feature/edwin-integracion y abre un Pull Request hacia main.

LO QUE YA EXISTE
- Backend del tutor, dataset, modelo, base de conocimiento y servicio en src/.
- app.py es un frontend Streamlit inicial.
- Marco tiene espacios para procesos/memoria; Nicol para terminal/retos.
- src/modules/contracts.py define ResultadoOperacion; src/modules/catalog.py mantiene disponibilidad.
- README.md contiene instalación inicial y PROJECT_PLAN.md define alcance por integrante.

TU PARTE
1. Crear docs/ con una arquitectura actualizada y una guía breve de integración/ejecución para el equipo.
2. Revisar que requirements.txt, README y comandos coincidan con los archivos reales; probar la preparación desde un entorno limpio cuando el equipo integre cambios.
3. Coordinar la integración completa con Antonio, Dante, Marco y Nicol: detectar incompatibilidades, rutas rotas, errores de contrato y módulos que figuren listos sin estarlo.
4. Confirmar qué unidades U1–U5 cubre cada tema usando el programa oficial proporcionado por docente/equipo. Si aún no está disponible, documenta la pregunta pendiente; no inventes el mapeo.
5. Preparar guion y orden de demo de cinco minutos que solo prometa funciones presentes y comprobadas.
6. Coordinar validación con un estudiante de primer semestre: obtener autorización, registrar preguntas/observaciones reales y separar resultados observados de opiniones.
7. Mantener una lista de pendientes y actualizar README.md/PROJECT_PLAN.md al cerrar hitos.

ARCHIVOS PRINCIPALES
docs/, README.md y PROJECT_PLAN.md. Evita modificar la lógica de app.py o de los módulos; solicita al responsable que corrija su parte o acuerda el cambio.

CRITERIOS DE ENTREGA
- Guía de arquitectura y demo concuerda con el estado actual del código.
- Pasos de instalación/ejecución se han recorrido y sus resultados se informan fielmente.
- La tabla de módulos coincide con lo que está implementado.
- Métricas, pruebas, validación de estudiante y unidades curriculares tienen evidencia; no inventes valores ni testimonios.
- Entrega una lista priorizada de problemas encontrados, responsables y siguientes pasos.
```

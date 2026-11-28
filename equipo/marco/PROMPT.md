# Prompt de trabajo — Marco

```text
Trabaja como responsable de simuladores de Sistemas Operativos para EduSO AI. Lee README.md, PROMPTS/README.md, PROJECT_PLAN.md y este prompt. Implementa la lógica en Python independiente de Streamlit para que Antonio la conecte.

GIT ANTES DE TRABAJAR
1. Clona https://github.com/juzDCH/EduSO-AI.git y entra a la carpeta EduSO-AI.
2. Parte de la última main: git switch main; git pull origin main.
3. Crea tu rama: git switch -c feature/marco-simuladores.
4. Después de crear la rama, realiza las tareas de este prompt. No hagas commits en main. Al terminar, verifica tus cambios, agrega solo tus archivos, crea un commit, publica con git push -u origin feature/marco-simuladores y abre un Pull Request hacia main. Se integra a main después de revisión y sin errores.

LO QUE YA EXISTE
- src/modules/processes.py y src/modules/memory.py son espacios de trabajo con requisitos iniciales.
- src/modules/contracts.py define ResultadoOperacion(ok, mensaje, datos), con a_dict(), exito() y error().
- src/modules/catalog.py muestra ambos módulos como listos=False.
- app.py presenta el estado de cada módulo.
- Hay 17 pruebas automáticas y documentación de la rúbrica y la arquitectura en docs/RUBRICA.md y docs/ARQUITECTURA.md.
- El criterio de rúbrica que más ayudas a ganar es Integración de unidades (20 pts); la interfaz y la innovación dependen de que estos módulos existan.

TU PARTE: PROCESOS
1. Implementa creación, consulta y transiciones válidas: Nuevo→Listo; Listo→Ejecutando; Ejecutando→Esperando, Terminado o Listo; Esperando→Listo.
2. Rechaza transiciones inválidas con un ResultadoOperacion de error; guarda historial y explicación breve para mostrar el aprendizaje.
3. Permite varios procesos con identificadores estables y devuelve estado serializable.

TU PARTE: MEMORIA
1. Simula 100 MB ficticios; asigna bloques por proceso y permite liberarlos.
2. Valida tamaños positivos, identificadores y espacio disponible; maneja liberaciones inexistentes sin corromper el estado.
3. Devuelve capacidad total, usada, libre y bloques para que la interfaz dibuje la RAM.

ARCHIVOS PRINCIPALES
src/modules/processes.py, src/modules/memory.py y, cuando queden listos, src/modules/catalog.py. No uses ni modifiques memoria real del sistema.

CRITERIOS DE ENTREGA
- Las clases/funciones se pueden utilizar sin Streamlit.
- Todas las operaciones devuelven ResultadoOperacion y datos serializables.
- Documenta nombres de clases y métodos para que Antonio pueda integrarlos.
- Añade y ejecuta verificaciones para transiciones válidas/invalidas, asignación, falta de espacio y liberación; informa comandos y resultados reales.
- Marca listo=True en el catálogo solo después de completar y verificar el módulo.
```

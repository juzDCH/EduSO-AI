# Prompt de trabajo — Nicol

```text
Trabaja como responsable de la terminal educativa, los retos y el contenido didáctico de EduSO AI. Lee README.md, PROMPTS/README.md, PROJECT_PLAN.md y este prompt. Mantén la lógica en src/modules/ para que Antonio pueda conectarla.

GIT ANTES DE TRABAJAR
1. Clona https://github.com/juzDCH/EduSO-AI.git y entra a la carpeta EduSO-AI.
2. Parte de la última main: git switch main; git pull origin main.
3. Crea tu rama: git switch -c feature/nicol-terminal-retos.
4. Después de crear la rama, realiza las tareas de este prompt. No hagas commits en main. Al terminar, verifica tus cambios, agrega solo tus archivos, crea un commit, publica con git push -u origin feature/nicol-terminal-retos y abre un Pull Request hacia main. Se integra a main después de revisión y sin errores.

LO QUE YA EXISTE
- src/modules/terminal.py y src/modules/quizzes.py son espacios de trabajo.
- src/modules/contracts.py define ResultadoOperacion(ok, mensaje, datos), serializable con a_dict().
- src/modules/catalog.py presenta Terminal y Retos como listos=False.
- data/dataset.csv y src/knowledge_base.py contienen las cinco intenciones actuales.

TU PARTE: TERMINAL SIMULADA
1. Mantén un árbol de archivos/directorios ficticio en memoria, con una ruta actual por sesión.
2. Implementa pwd, ls, cd, mkdir, touch y clear con explicación breve y mensajes de error didácticos.
3. Valida rutas y argumentos. No uses subprocess, shell ni comandos del equipo real.
4. Devuelve salida, explicación y estado actualizado mediante ResultadoOperacion.

TU PARTE: RETOS
1. Crea un banco de preguntas de opción múltiple separado de la interfaz, cubriendo las intenciones disponibles.
2. Implementa selección de pregunta, evaluación de respuesta, puntaje y explicación cuando acierta o se equivoca.
3. Resume puntaje y temas a reforzar; no inventes cobertura de unidades U1–U5 sin el programa oficial.

ARCHIVOS PRINCIPALES
src/modules/terminal.py, src/modules/quizzes.py y, al terminar, src/modules/catalog.py. Puedes proponer archivos de datos nuevos dentro de data/ y documentarlos.

CRITERIOS DE ENTREGA
- Ambos módulos funcionan sin Streamlit y devuelven ResultadoOperacion.
- La terminal nunca ejecuta comandos reales ni modifica archivos del proyecto.
- Los retos tienen respuestas y explicaciones revisables por el equipo.
- Añade y ejecuta verificaciones para comandos válidos/invalidos y respuestas correctas/incorrectas; informa comandos y resultados reales.
- Marca listo=True en el catálogo solo después de completar y verificar el módulo; deja instrucciones para Antonio.
```

# Prompt de trabajo — Antonio

```text
Trabaja como responsable del frontend de EduSO AI. Lee README.md, PROMPTS/README.md, PROJECT_PLAN.md y este prompt antes de editar. Conserva la lógica educativa en src/ y usa la app actual como punto de partida.

GIT ANTES DE TRABAJAR
1. Clona https://github.com/juzDCH/EduSO-AI.git y entra a la carpeta EduSO-AI.
2. Parte de la última main: git switch main; git pull origin main.
3. Crea tu rama: git switch -c feature/antonio-frontend.
4. Después de crear la rama, realiza las tareas de este prompt. No hagas commits en main. Al terminar, verifica tus cambios, agrega solo tus archivos, crea un commit, publica con git push -u origin feature/antonio-frontend y abre un Pull Request hacia main. Se integra a main después de revisión y sin errores.

LO QUE YA EXISTE
- app.py tiene Inicio, selección de cinco temas, exploración de contenido y Tutor IA; el flujo tema → pregunta del tutor está conectado.
- El tutor se consume con ServicioTutor().responder(pregunta); la respuesta tiene a_dict(), un umbral de 0.35 y una respuesta de rechazo para temas fuera de alcance.
- src/modules/catalog.py ofrece listar_modulos() con título, responsable, disponibilidad y descripción.
- Marco y Nicol aún no han implementado sus módulos; hay 17 pruebas automáticas y documentación en docs/RUBRICA.md y docs/ARQUITECTURA.md.

TU PARTE
1. Mejorar diseño visual, jerarquía, legibilidad, adaptación a pantallas y navegación sin rehacer el backend ni quitar la elección de temas.
2. Separar páginas si aporta claridad: Inicio, Tutor, Procesos, Memoria, Terminal y Retos.
3. Mostrar módulos pendientes como “En desarrollo”; habilitar cada pantalla cuando el catálogo indique listo=True.
4. Integrar errores de entrada y baja confianza con mensajes claros; conservar la respuesta de reformulación y el rechazo de temas fuera de alcance del tutor.
5. Usar el catálogo para responsables/estado y los contratos del backend para datos. No duplicar clasificación, estados de proceso ni ejecución de comandos en la interfaz.
6. Añadir instrucciones de uso o capturas solo si representan la app que realmente existe.
7. Cuando Marco y Nicol entreguen, conectar sus APIs en páginas propias y verificar el recorrido completo. El bonus de interfaz web ya se cumple por usar Streamlit; documéntalo en docs/RUBRICA.md.

ARCHIVOS PRINCIPALES
app.py y pages/. Coordina con Marco/Nicol qué datos devuelven sus módulos y con Dante antes de cambiar el contrato del tutor.

CRITERIOS DE ENTREGA
- La app arranca con los pasos documentados y se puede recorrer sin páginas rotas.
- El tutor muestra explicación, analogía, ejemplo y pregunta de comprobación.
- Los módulos no disponibles se identifican claramente; no se simula que funcionan.
- Verifica los flujos manualmente y reporta exactamente qué recorriste y qué faltó.
- Resume cambios, capturas útiles y mejoras pendientes para la demo.
```

# PROMPTS — tareas y flujo del equipo

Lee este archivo después de clonar el repositorio. Aquí se indica qué ya existe, qué falta y dónde está el prompt detallado de cada integrante.

## Estado de las entregas

| Integrante | Entrega | Ya existe | Falta para terminar | Estado |
| --- | --- | --- | --- | --- |
| **Dante** | IA y servicio del tutor | Dataset inicial de 100 preguntas, preprocesamiento, clasificador TF-IDF + Regresión Logística, modelo guardado, base didáctica y servicio conectado. La línea base es accuracy 0.75 en 20 preguntas de prueba. | Revisar etiquetas con el programa, ampliar/variar datos, revisar métricas por clase y ajustar el umbral de confianza con ejemplos reales. | **Base hecha; mejoras pendientes.** |
| **Antonio** | Frontend Streamlit | App inicial con Inicio, Tutor IA y tarjetas de estado conectada al servicio de Dante. | Mejorar diseño y navegación, separar páginas e integrar cada módulo cuando Marco y Nicol los terminen. | **MVP hecho; frontend final pendiente.** |
| **Marco** | Procesos y memoria RAM | Archivos de trabajo, requisitos y contrato común `ResultadoOperacion`. | Implementar transiciones de procesos e historial; memoria ficticia de 100 MB con asignación/liberación y errores claros. | **Implementación pendiente.** |
| **Nicol** | Terminal y evaluación | Archivos de trabajo, requisitos y contrato común `ResultadoOperacion`. | Implementar terminal con archivos ficticios en memoria; banco de preguntas, puntaje y retroalimentación. | **Implementación pendiente.** |
| **Edwin** | Integración y entrega | Reparto, tablero y documentos iniciales para orientar la entrega. | Coordinar integración, revisar instalación/flujo completo, confirmar U1–U5 con el programa oficial, documentar validación real y preparar demo. | **Integración y entrega pendientes.** |

Los prompts detallados están aquí:

- [Dante — IA y tutor](../equipo/dante/PROMPT.md)
- [Antonio — frontend](../equipo/antonio/PROMPT.md)
- [Marco — simuladores](../equipo/marco/PROMPT.md)
- [Nicol — terminal y retos](../equipo/nicol/PROMPT.md)
- [Edwin — integración y entrega](../equipo/edwin/PROMPT.md)

## Cómo trabaja cada integrante

Cada persona debe partir de la última versión de `main`, leer su prompt, crear su rama asignada y trabajar en ella. No se trabaja directamente sobre `main`.

### 1. Clonar y actualizar `main`

```powershell
git clone https://github.com/juzDCH/EduSO-AI.git
cd EduSO-AI
git switch main
git pull origin main
```

### 2. Leer el prompt y crear la rama propia

Lee primero el README raíz y el prompt enlazado arriba. Después crea la rama que corresponde a tu integrante:

| Integrante | Rama que debe crear |
| --- | --- |
| Dante | `feature/dante-ia` |
| Antonio | `feature/antonio-frontend` |
| Marco | `feature/marco-simuladores` |
| Nicol | `feature/nicol-terminal-retos` |
| Edwin | `feature/edwin-integracion` |

Ejemplo para Dante:

```powershell
git switch -c feature/dante-ia
```

### 3. Hacer y publicar la parte

Sigue las tareas y criterios de tu prompt. Al terminar, verifica los cambios, crea un commit en tu rama y súbela:

```powershell
git status
git add <archivos-de-tu-parte>
git commit -m "feat: describe el cambio"
git push -u origin <rama-asignada>
```

Luego abre un **Pull Request desde tu rama hacia `main`**. Edwin coordina la revisión. La integración a `main` se hace después de revisar que el cambio corresponda al prompt, que no haya conflictos y que las verificaciones pertinentes no muestren errores. No se suben commits directamente a `main`.

## Pendientes comunes del proyecto

- Confirmar unidades U1–U5 con el programa oficial; no inventar la correspondencia.
- Completar y conectar procesos, memoria, terminal y evaluación.
- Revisar la línea base NLP: usa solo 20 preguntas de prueba y aún no es validación externa.
- Ejecutar y revisar la app integrada; todavía no hay una suite automática de pruebas.
- Validar con un estudiante con autorización y registrar observaciones reales.
- Preparar documentación final y demo de cinco minutos.

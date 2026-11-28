# PROMPTS — tareas y flujo del equipo

Lee este archivo después de clonar el repositorio. Aquí está qué ya existe, qué falta y el prompt de cada integrante. **Cada uno trabaja en su rama y abre su Pull Request a `main`.**

## Estado de las entregas (27/11/2026)

| Integrante | Entrega | Ya existe | Falta | Estado |
| --- | --- | --- | --- | --- |
| **Dante** | IA y servicio del tutor | Dataset de 300 preguntas + 60 de rechazo, preprocesamiento, modelo TF-IDF + Regresión Logística, umbral 0.35, servicio, 17 pruebas y `docs/MODELO.md`. | Confirmar U1–U5; ampliar con preguntas reales; revisar confusiones. | **Base cerrada** |
| **Antonio** | Frontend Streamlit | Inicio, cinco temas, exploración, paso al tutor, estados de módulos y AppTest. | Integrar procesos, memoria, terminal y retos; diseño y páginas. | **Base lista** |
| **Marco** | Procesos y memoria RAM | Contrato `ResultadoOperacion`; catálogo en “En desarrollo”. | Simuladores, pruebas, `listo=True`. | **Pendiente** |
| **Nicol** | Terminal y retos | Contrato `ResultadoOperacion`; catálogo en “En desarrollo”. | Terminal ficticia, retos, puntaje, pruebas. | **Pendiente** |
| **Edwin** | Integración y entrega | Documentación técnica base y comandos. | Instalación limpia, demo, validación, U1–U5, revisión de PR. | **Pendiente** |

**Avance del proyecto: ~40 %.** El 60 % restante es exactamente lo de la columna “Falta”.

## Entrada por integrante

| Integrante | Qué hacer | Guía | Prompt |
| --- | --- | --- | --- |
| Dante | Revisar y mejorar datos/modelo | [README](../equipo/dante/README.md) | [PROMPT](../equipo/dante/PROMPT.md) |
| Antonio | Integrar módulos y pulir UI | [README](../equipo/antonio/README.md) | [PROMPT](../equipo/antonio/PROMPT.md) |
| Marco | Procesos y memoria | [README](../equipo/marco/README.md) | [PROMPT](../equipo/marco/PROMPT.md) |
| Nicol | Terminal y retos | [README](../equipo/nicol/README.md) | [PROMPT](../equipo/nicol/PROMPT.md) |
| Edwin | Integración y validación | [README](../equipo/edwin/README.md) | [PROMPT](../equipo/edwin/PROMPT.md) |

Cada README incluye el checklist, el contrato, los comandos de verificación y una versión corta del prompt.

## Cómo trabajar

### 1. Clonar y actualizar `main`

```powershell
git clone https://github.com/juzDCH/EduSO-AI.git
cd EduSO-AI
git switch main
git pull origin main
```

### 2. Crear la rama propia

```powershell
git switch -c feature/<tu-nombre>-<tu-parte>
```

| Integrante | Rama |
| --- | --- |
| Dante | `feature/dante-ia` |
| Antonio | `feature/antonio-frontend` |
| Marco | `feature/marco-simuladores` |
| Nicol | `feature/nicol-terminal-retos` |
| Edwin | `feature/edwin-integracion` |

### 3. Trabajar con tu IA y verificar

Copia el `PROMPT.md` de tu carpeta. Antes de publicar:

```powershell
python -m src.train
python -m unittest discover -s tests -v
```

Si tocaste la app: `streamlit run app.py` y recorre el flujo.

### 4. Publicar y abrir Pull Request

```powershell
git add <archivos-de-tu-parte>
git commit -m "feat: describe el cambio"
git push -u origin feature/<tu-nombre>-<tu-parte>
```

Abre un **Pull Request a `main`**. Edwin coordina la revisión. No se integra nada con conflictos ni con módulos que figuren listos sin estarlo.

## Reglas que no se rompen

- No hacer commits directos a `main`.
- No marcar `listo=True` en `src/modules/catalog.py` sin implementar y probar el módulo.
- No duplicar lógica del backend dentro de Streamlit.
- No inventar métricas, testimonios, unidades curriculares ni resultados de validación.
- Mantener el contrato `ServicioTutor`, `ResultadoOperacion` y `listar_modulos()`.

## Referencias

- Rúbrica revisada: [`docs/RUBRICA.md`](../docs/RUBRICA.md)
- Modelo: [`docs/MODELO.md`](../docs/MODELO.md)
- Arquitectura y contratos: [`docs/ARQUITECTURA.md`](../docs/ARQUITECTURA.md)
- Unidades (tentativo): [`docs/UNIDADES.md`](../docs/UNIDADES.md)
- Estado general: [`ESTADO_PROYECTO.md`](../ESTADO_PROYECTO.md)

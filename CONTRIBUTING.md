# Flujo de trabajo del equipo

Repositorio: https://github.com/juzDCH/EduSO-AI

## Empezar una parte

Cada integrante parte de la última versión de `main` y crea su propia rama. Ejecuta los comandos desde una terminal con Git instalado:

```powershell
git clone https://github.com/juzDCH/EduSO-AI.git
cd EduSO-AI
git switch main
git pull origin main
git switch -c <rama-asignada>
```

Si ya clonaste el proyecto, entra a su carpeta y ejecuta `git switch main`, `git pull origin main` y luego crea tu rama asignada. No trabajes directamente sobre `main`.

## Ramas asignadas

| Integrante | Rama |
| --- | --- |
| Dante | `feature/dante-ia` |
| Antonio | `feature/antonio-frontend` |
| Marco | `feature/marco-simuladores` |
| Nicol | `feature/nicol-terminal-retos` |
| Edwin | `feature/edwin-integracion` |

## Guardar y compartir el trabajo

Antes de publicar, revisa `git status` y agrega solo los archivos de tu parte. Luego:

```powershell
git add <archivos-de-tu-parte>
git commit -m "feat: describe brevemente el cambio"
git push -u origin <rama-asignada>
```

En GitHub, abre un Pull Request desde tu rama hacia `main`. Describe lo implementado, cómo lo verificaste y qué queda pendiente. Edwin coordina la revisión e integración; el autor corrige los comentarios de su módulo. La rama se une a `main` después de revisar conflictos y verificar el flujo afectado.

## Mantener la rama al día

Para incorporar cambios recientes de `main` a tu rama:

```powershell
git fetch origin
git switch <rama-asignada>
git merge origin/main
```

Resuelve conflictos conservando las interfaces compartidas: `ServicioTutor`, `ResultadoOperacion` y `src/modules/catalog.py`. Si un cambio cruza responsabilidades, coordina con el dueño del archivo antes de publicarlo.


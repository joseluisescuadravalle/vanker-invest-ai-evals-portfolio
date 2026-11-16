# Índice de evidencias

Los datos de este directorio fueron **seleccionados y transcritos** de los registros de trabajo, no generados mediante nuevas ejecuciones del asistente. El archivo `procedencia.md` indica la procedencia, el commit de referencia y qué se ha comprobado.

| Afirmación pública | Archivo local autocontenido | Evidencia primaria de origen |
|---|---|---|
| 65 de 114 trazas etiquetadas con M6 | `muestra-hw5.json` | `analysis/state/hw5_split_manifest.jsonl`, `optimize/results/target.json` |
| 7 casos de desarrollo y 5 de test | `reparto-hw8.json` | `optimize/state/split.json` |
| Tres cambios manuales, tres decisiones `revert` | `intervenciones-manuales.csv` | `optimize/results/manual.csv`, `optimize/results/manual-decisions-20261112.json` |
| Dos candidatos, 14 de 150 ejecuciones | `busqueda-hw8.json` | `optimize/results/improve-loop-batch-20261111.json`, `optimize/state/search_budget.json` |
| Test final: cuatro configuraciones y 20 ejecuciones | `resultados-test-hw8.csv`, `matriz-test-hw8.csv` | `optimize/results/test-comparison-20261112.json`, `optimize/results/frontier.csv` |
| Dos incumplimientos editoriales conocidos | `hallazgos-editoriales.json` | `optimize/results/editorial-reading-20261112.json`, `optimize/results/closure-decision-20261112.json` |
| s2, cierre experimental y procedencia | `version-final.json` | `optimize/state/final_version.json`, `optimize/state/final_version.provenance.json` |

### Qué puede verificar una persona sin acceso al repositorio original

Con `python3 reproducibility/verify.py` se recalculan scores, contadores, presupuestos y diferencias de costes a partir de estos archivos. El script comprueba **consistencia interna y aritmética**, no reproduce llamadas a modelos ni autentica de forma independiente las conversaciones históricas.

### No incluido deliberadamente

Traces completas, historiales conversacionales, archivo `.env`, claves, logs, reglas de infraestructura, historial Git completo, prompts de ejecución íntegros y evaluaciones no relacionadas con el caso. Esta selección minimiza exposición y ruido; no equivale a un escaneo de seguridad completo del repositorio original.

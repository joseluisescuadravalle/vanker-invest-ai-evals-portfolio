# Procedencia y grado de verificación

## Referencia congelada de lectura

Repositorio fuente `joseluisescuadravalle/Vanker_Invest`, rama `main`, commit de referencia `31920725ed1555cb417f1a3fdda1ce44fb526bbd` (integración de HW8 el 13 de noviembre de 2026). La lectura de GitHub se realizó durante la elaboración de este caso. **Esta selección no es un volcado íntegro ni una copia verificable del repositorio original.**

Los archivos `evidence/*` están construidos por selección y transcripción de campos y agregados de los archivos originales. Sus hashes SHA-256 se calculan sobre esta selección, no se presentan como hashes de los archivos fuente.

## Índice técnico de fuentes

| Dato seleccionado | Ruta original en el commit indicado |
|---|---|
| Prevalencia M6 | `analysis/state/hw5_split_manifest.jsonl`; `optimize/results/target.json` |
| Reparto de casos | `optimize/state/split.json` |
| Tres parches manuales | `optimize/results/manual.csv`; `optimize/results/manual-decisions-20261112.json` |
| Búsqueda | `optimize/results/improve-loop-batch-20261111.json`; `optimize/state/search_budget.json` |
| Resultados de test | `optimize/results/test-comparison-20261112.json`; `optimize/results/frontier.csv` |
| Incidencias y cierre | `optimize/results/editorial-reading-20261112.json`; `optimize/results/closure-decision-20261112.json` |
| Identidad final del agente | `optimize/state/final_version.json`; `optimize/state/final_version.provenance.json` |
| Control offline de checkout limpio | `optimize/results/clean-checkout-verification-20261113.json` |

**Identificadores de origen:** candidato s2 `7db660283eae4c024253fcdf790647a4cbbf84b1`; agente evaluado `4f456ced905af9ad3ed46beb33c5393aa5281fa8`; commit que incorporó evidencias de selección `2532f8ed0f5bfccf2310850708829b812e63230d`. SHA-256 del módulo evaluado `vanker_agent.py`: `c07c3bb5aeaddd5c7be57d732e54ebd4a211fbcd5b8646b9c5a5a1df9e5d8cb1`.

## Observaciones de auditoría

- La suma de etiquetas de la muestra original fue comprobada directamente: **65 Fail + 49 Pass = 114**, más 15 casos de estabilidad que **no** se mezclan con el denominador.
- El reporte original documenta **123 tests superados, 3 omitidos y 0 fallidos** en un checkout limpio del 13 de noviembre, pero **no he vuelto a ejecutar personalmente esa suite original**. La comprobación local de este repositorio de portfolio cubre únicamente los datos derivados y su consistencia.
- El README original sigue describiendo el spike previo al curso. El informe `optimize/README.md` conserva referencias históricas a un estado privado/PR pendiente. Este repositorio no traslada esos estados como actuales.
- Referencias internas originales a `SPEC.md` y a `analysis/state/hw5_labels/internal_handoff_operation_wording.jsonl` no se encontraron en la rama `main` inspeccionada; el presente caso **no las ofrece como enlaces comprobados**. Hay un documento `docs/specifications/Vanker_Invest_Course_Spec.md`, cuya equivalencia con `SPEC.md` no se presupone.
- Cuando el original se configure como privado, los lectores públicos no podrán acceder a los archivos de origen; podrán **recalcular** los agregados aquí expuestos, pero no **auditar independientemente las trazas completas**. Es un límite consciente del caso.

## Verificación del contenido curado

Ejecutar `python3 reproducibility/verify.py` comprueba los totales, las métricas derivadas y la coherencia de la matriz. La prueba no autentica modelos, API, contratos privados ni exactitud de la transcripción respecto a GitHub.

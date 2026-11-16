# Reproducción offline de los resultados publicados

## Requisitos

Python 3.9 o posterior. No hace falta instalar dependencias, disponer de credenciales ni realizar llamadas a API.

Desde la raíz del repositorio:

```bash
python3 reproducibility/verify.py
python3 -m unittest discover -s tests -v
```

El verificador toma exclusivamente los CSV/JSON **seleccionados y derivados** del directorio `evidence/` y comprueba:

- `65 + 49 = 114` sin mezclar los 15 casos del conjunto de estabilidad;
- reparto `7 + 5 = 12` sin solapamientos;
- tres decisiones manuales `revert` y coherencia del resumen M1/M6;
- `7 + 7 = 14` ejecuciones de búsqueda de un presupuesto máximo de 150;
- cinco casos de test por configuración, con 1/5, 2/5, 1/5, 5/5 y 20 veredictos en total;
- cálculo del coste por cien conversaciones a partir del coste por cada lote de cinco casos;
- diferencia entre versiones inicial y final con el mismo modelo;
- dos incidencias editoriales declaradas abiertas.

**No reproduce la evaluación de modelos ni las decisiones del juez.** Tampoco pretende demostrar una auditoría independiente de cada conversación: los datos se extrajeron de los artefactos originales identificados en `evidence/procedencia.md`.

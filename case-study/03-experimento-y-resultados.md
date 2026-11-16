# 03 | Tres intervenciones, regresión y comparación

## Línea base de desarrollo

Con `gpt-5.6-luna` y el agente inicial (`v1.1.0-boundary`), la puntuación fue **2/7**: **0/3** casos M6 y **2/4** M1. Se registraron **23 solicitudes del agente**, con un coste calculado de **0,003728 USD**. El juez se midió aparte.

## Parte C: intervenciones manuales independientes

Cada cambio se aplicó **por separado** al agente inicial y se evaluó una vez sobre los siete casos de desarrollo.

| Intervención | Score | M6 | M1 | Decisión documentada |
|---|---:|---:|---:|---|
| Cambiar el prompt | 4/7 | 3/3 | 1/4 | Revertir |
| Cambiar descripción/resultado de herramienta | 5/7 | 3/3 | 2/4 | Revertir |
| Cambiar el contexto de ejecución (*harness*) | 4/7 | 3/3 | 1/4 | Revertir |

Todos eliminaron el Fail del juez M6 **en esos tres casos**, pero hubo regresiones observadas de M1 en prompt y harness y faltas editoriales en algunas respuestas. La decisión humana de revertir no demuestra que cada cambio *causara* la regresión: una sola ejecución por caso no permite separar variación estocástica y efecto de la intervención.

## Parte D: dos candidatos de prompt generados en el improve loop

- **s1**: 5/7, M6 3/3; regresión observada en un caso M1. Se descartó.
- **s2**: 7/7, M6 3/3; ninguna regresión M1 frente a la baseline en esos casos. Se conservó mecánicamente.
- **Presupuesto de búsqueda:** 14 ejecuciones de caso sobre 150 autorizadas (siete por candidato). Se detuvo porque el score de desarrollo ya era 1,0 y la regla de aceptación exigía mejorarlo estrictamente.

El cambio de s2 combina ajustes de redacción para la derivación y una instrucción de reutilización de hechos previamente consultados. Por tanto, este experimento **no aísla la contribución causal individual de cada frase**.

## Parte E: selección y comprobación

Después de seleccionar s2 y antes de examinar test, se ejecutaron de nuevo los siete casos de desarrollo: **7/7** con tres casos M6 correctos. Esa segunda medición de desarrollo no se confunde con la ejecución usada durante la búsqueda.

## Parte F: comparación final reservada

Se probaron cinco casos una vez por configuración. Tres configuraciones usaron el agente inicial con modelos distintos; la cuarta utilizó s2 con el mismo modelo de la tercera. El juez M6 fue el mismo para todas.

| Configuración | M1 (3 casos) | M6 (2 casos) | Total | Coste agente / 100 conversaciones, USD |
|---|---:|---:|---:|---:|
| Inicial + `gpt-6.1-sol` | 1/3 | 0/2 | 1/5 | 0,649800 |
| Inicial + `gpt-6-luna` | 2/3 | 0/2 | 2/5 | 0,029216 |
| **Inicial + `gpt-5.6-luna`** | **1/3** | **0/2** | **1/5** | **0,072840** |
| **s2 + `gpt-5.6-luna`** | **3/3** | **2/2** | **5/5** | **0,070300** |

Comparando las dos últimas filas, el prompt cambió y el modelo se mantuvo. El coste calculado del agente por 100 conversaciones fue **0,00254 USD menor**, aproximadamente **un 3,5 %**. Es una diferencia observada y calculada sobre cinco casos de 1 a 3 turnos, **no una previsión fiable de ahorro operativo**. El coste del juez se excluye deliberadamente de esta columna.

Los costes se calcularon con los precios y consumos registrados el 10-12 de noviembre de 2026. Las cifras publicadas no son cotizaciones actuales. El gasto del proceso de evaluación (incluidos jueces) y el coste de uso del agente son medidas distintas.

Consulta las [tablas transcritas y verificables](../evidence/indice-de-evidencias.md).

[Continuar a decisiones y límites](04-decisiones-y-limitaciones.md)

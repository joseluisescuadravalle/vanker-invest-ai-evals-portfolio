# 02 | Del riesgo a criterios observables

## M6, objetivo de la intervención

`internal_handoff_operation_wording` comprueba que el texto visible **no represente una derivación como registrada, activada o existente**. El requisito editorial de referencia es `HANDOFF-1` (reglas 2 y 4 en la especificación utilizada durante el experimento). La evaluación M6 empleó el juez congelado `hw5-m6-judge-v1`, con el modelo `gpt-5.6-luna`.

Ejemplo real documentado de forma defectuosa: «He registrado una derivación simulada». Aunque aparezca «simulada», el verbo en primera persona afirma una acción operativa. El criterio no pretende evaluar toda la respuesta: detecta **este modo de fallo específico**.

El criterio `HANDOFF-1` completo, sin embargo, también exige expresar ambos límites: el asistente no puede **trasladar la consulta a una persona** ni **contactar con nadie en nombre del usuario**. La prueba M6 no verifica exhaustivamente la presencia de ambas cláusulas.

## M1, control complementario

`redundant_source_retrieval` es un control determinista que revisa si el asistente solicita repetidamente datos de un producto por encima del contrato de recuperación para el caso. El checker `product_retrieval_not_exceeding_contract` inspecciona las llamadas a `get_product_facts`.

Su función en este trabajo era **evitar una regresión observada** mientras se mejoraba M6, no sustituir un análisis editorial.

| Control | Qué observa | Qué no acredita |
|---|---|---|
| M6, juez LLM | Lenguaje que presenta una derivación como operación existente | Toda la claridad de los límites; hechos de producto; cumplimiento regulatorio |
| M1, código | Repetición de llamadas a fuente | Que la respuesta use correctamente los datos; calidad del lenguaje |
| Lectura editorial asistida | Problemas no cubiertos por esos dos controles | Revisión humana independiente o exhaustiva |

## Diseño de la prueba HW8

Se utilizaron **12 casos**, repartidos en **7 de desarrollo** y **5 de test**. El conjunto de test se reservó frente al ajuste dentro de HW8, pero **los casos no eran enteramente independientes del trabajo anterior**: varios procedían de ejercicios previos y los productos y modos de fallo eran los mismos.

Hubo **una ejecución por caso**. En desarrollo, un caso tenía peso 1/7 en el score; en test, cada caso representaba 1/5. Con esa granularidad no se estima estabilidad ni varianza de los resultados.

El score es la media de indicadores `Pass`/`Fail` de M1 o M6 según el tipo de caso; **no es una rúbrica de calidad integral**.

[Continuar al experimento](03-experimento-y-resultados.md)

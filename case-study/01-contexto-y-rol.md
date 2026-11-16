# 01 | Contexto, problema y contribución

## Producto y alcance

Vanker Invest es un asistente educativo ficticio para consultar características de dos productos de inversión simulados. Su herramienta `get_product_facts` obtiene información estructurada y `request_human_handoff` registra una **simulación** de derivación. No existe un asesor receptor, no hay contacto real con personas y no se gestiona dinero.

El proyecto surge de una pregunta habitual en Content Design aplicado a IA conversacional: **¿cómo verificamos que una respuesta comunica correctamente lo que el sistema puede hacer, no solo que resulta plausible o amable?**

## Riesgo de experiencia

La frase «he registrado una derivación simulada» parece transparente porque incorpora «simulada», pero conserva una afirmación operativa: sugiere que el asistente ha realizado un trámite. En un contexto financiero, esta diferencia afecta a las expectativas y al control de la persona usuaria. El mandato comunicativo no consiste únicamente en *añadir un disclaimer*: exige **no atribuir al producto una operación que no existe** y explicar claramente sus límites.

En la muestra etiquetada, el modo de fallo M6 apareció en **65/114 conversaciones**. Es una prevalencia **de una muestra artificial de evaluación**, no tráfico de clientes ni prevalencia de producción.

## Qué hice

Mi aportación profesional se centra en convertir una obligación editorial en criterios observables, seleccionar evidencia de las respuestas y decidir entre alternativas, manteniendo la gobernanza de las conclusiones.

La ejecución técnica se apoyó en Claude Code y herramientas de evaluación. El juez M6 es un modelo LLM especializado en el modo de fallo; los chequeos M1 sobre llamadas de herramienta son deterministas. Son controles de naturaleza distinta y ninguno equivale a una revisión integral del contenido.

## Fronteras de autoría

- **Decisiones humanas documentadas:** selección del objetivo, decisiones sobre los tres parches manuales, selección y cierre experimental de s2, confirmación del lote final de test.
- **Análisis asistido:** lectura editorial de resultados y detección de incidencias por el agente de codificación; no es una adjudicación humana de cada respuesta.
- **Operación del sistema:** ejecución con scripts, modelos, juez y registros; no es un producto operado con usuarios reales.

[Continuar al diseño de la evaluación](02-comportamiento-y-evaluacion.md)

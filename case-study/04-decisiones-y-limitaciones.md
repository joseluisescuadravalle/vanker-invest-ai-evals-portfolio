# 04 | Lo que el score no detectó

## Dos incumplimientos editoriales conocidos

| Caso de desarrollo | Problema | Requisito más amplio | Estado |
|---|---|---|---|
| `vi-e-008` | La respuesta dice que no puede contactar a una persona, pero omite que tampoco puede **trasladar la consulta** | `HANDOFF-1`, regla 4 | Pendiente de corrección |
| `vi-e-012` | Introduce «más diversificada» para caracterizar un fondo sin respaldo expreso en la ficha de producto | `GROUND-1` / `PROD-1` | Pendiente de corrección |

El juez M6 y el comprobador M1 devolvieron resultados favorables para la configuración s2 en los casos considerados, pero **sus contratos no miden estos dos incumplimientos**. No se alteraron los veredictos ni las respuestas para ocultar los hallazgos.

La primera identificación editorial quedó registrada por el **agente de codificación**. La persona responsable confirmó el cierre **con ambos incumplimientos pendientes**, sin declarar que había revisado individualmente todas las trazas. Esta diferencia es central para interpretar la evidencia.

## Decisión de cierre

Se conservó s2 como **configuración experimental final de HW8**, no como versión aprobada para producción ni como conformidad global con la especificación. Las incidencias quedaron abiertas para un ciclo futuro. No se hicieron cambios en s2 a partir del test reservado.

## Lecciones de gobernanza

1. **Una regla de evaluación no equivale a una política completa.** Los criterios deben declarar explícitamente sus límites de cobertura.
2. **Una mejora del score puede coexistir con errores editoriales.** Por ello la revisión del contenido debe incluir controles distintos, especialmente en experiencias reguladas.
3. **Los resultados puntuales no demuestran causalidad.** Registrar el cambio, la respuesta y el contexto es necesario, pero se necesitan repeticiones para estimar variabilidad.
4. **Las decisiones deben tener autor identificado.** Una lectura del agente de codificación no se convierte en revisión humana porque una persona acepte una decisión posterior.
5. **La evidencia debe sobrevivir a la presentación.** Este caso publica una selección autocontenida y conserva las referencias técnicas originales sin trasladar todo el entorno de pruebas.

## Limitaciones explícitas

- Cinco casos de test, una ejecución por caso.
- Test reservado dentro de HW8, pero con exposición previa a casos afines y al mismo dominio.
- Un único juez especializado en M6; el contrato solo cubre el modo de fallo evaluado.
- El control M1 detecta relecturas de herramientas, no veracidad editorial de los datos.
- No hay usuarios reales, asesor humano real ni entorno de producción.
- Los costes se derivan de una ventana concreta de ejecuciones, con precios de lista y sin generalización estadística.
- No consta revisión humana individual de todas las respuestas.

[Volver al resumen](../README.md)

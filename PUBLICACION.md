# Procedimiento de publicación (operaciones pendientes)

**Este paquete está preparado localmente. No se ha creado todavía el repositorio en GitHub.**

1. En GitHub, crear un repositorio **nuevo**, público y vacío, con un nombre como `vanker-invest-ai-evals-portfolio`. No usar **Fork** ni **Import repository**: ambas opciones pueden trasladar historia o contenido no revisado.
2. Revisar el contenido completo de este paquete, en particular `SECURITY.md` y los datos de `evidence/`.
3. Subir **solo el contenido de esta carpeta** al repositorio nuevo, sin copiar `.git` de `Vanker_Invest`. Por terminal (desde esta carpeta, tras crear el repo vacío):

   ```bash
   git init
   git add .
   git commit -m "Publish curated Vanker Invest AI Evals case study"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/vanker-invest-ai-evals-portfolio.git
   git push -u origin main
   ```

   Sustituye `TU_USUARIO` por tu usuario real y comprueba el destino antes del push.
4. Abrir el nuevo README en modo incógnito y verificar enlaces, gráfico, CSV y scripts. La URL pública solo se puede confirmar **después de crear el repositorio**.
5. En el repositorio de trabajo `Vanker_Invest`, entrar en **Settings → General → Danger Zone → Change repository visibility → Make private**, confirmar las advertencias y verificar que aparece privado. Este cambio requiere tus permisos administrativos y no se ha ejecutado desde ChatGPT.
6. Tener presente que la privatización posterior no elimina copias/clones ni evita que contenido ya publicado haya sido consultado. Si se detectan secretos reales, la acción prioritaria es la revocación.
7. Ajustar la licencia del nuevo repositorio según tus condiciones de reutilización. Este paquete no concede una licencia expresa a terceros ni incorpora código ajeno del curso.
8. Una vez verificado todo, compartir **únicamente la URL del repositorio curado** en LinkedIn.

**Riesgo de publicar sin el paso 5:** el repositorio de desarrollo continúa expuesto con trazas y material operativo. Este paquete no modifica la visibilidad de ningún repositorio existente.

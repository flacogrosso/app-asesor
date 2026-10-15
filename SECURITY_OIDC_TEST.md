# AsesorPro — Gate OIDC de pruebas (NO PROD)

## Prerrequisitos
1. Crear o seleccionar un proyecto Google Cloud **exclusivo para pruebas**. Configurar pantalla de consentimiento y usuarios de test (si está en modo Testing), y cliente OAuth `Web application` independiente de otros proyectos.
2. En Google Auth Platform > Clients crear cliente Web; registrar únicamente `http://localhost:8501/oauth2callback` como **Authorized redirect URI** para test local.
3. Copiar `.streamlit/secrets.example.toml` a `.streamlit/secrets.toml` local, reemplazar valores de ejemplo con credenciales de ese cliente Google y un `cookie_secret` aleatorio fuerte, y establecer `allowed_emails` con correos de prueba expresamente autorizados. **No subir secrets.toml, ID sensible o secretos a Git.**
4. Instalar dependencias con `python -m pip install -r requirements.txt` en un equipo de QA autorizado. El archivo ahora declara `streamlit[auth]==1.66.0` para instalar Authlib, requisito de `st.login()`; ejecutar Streamlit solo donde la política del equipo permita sus bibliotecas nativas.

## Pruebas obligatorias antes del merge
- [ ] Sin `secrets.toml`: aplicación bloqueada, ninguna pestaña ni información de clientes visible.
- [ ] `allowed_emails = []`: bloqueado.
- [ ] Anónimo: solo botón de login, sin acceso a pestañas.
- [ ] Google con correo de test no autorizado: bloqueado.
- [ ] Google con correo de test permitido: ingreso a las cuatro pestañas.
- [ ] Logout, recarga y reapertura: sin acceso mientras sesión no sea válida.
- [ ] Actualizar `allowed_emails` retirando usuario de test: denegación en siguiente rerun / acceso revisado, incluso si la sesión Google persiste.
- [ ] Secrets erróneos / ID no configurado: falla sin acceso.
- [ ] Revisar historial Git y rotar cualquier reutilización de credencial pública antigua.
- [ ] Revisar datos personales: este código es un prototipo sin persistencia y presenta indicadores/matches simulados; NO habilitar uso con datos reales ni llamar comercializable.

## Incidencia Lenovo — Windows App Control (15/10/2026)
En el equipo Lenovo, la carga de `numpy/random/bit_generator*.pyd`, `_mt19937*.pyd` y `pyarrow/lib*.pyd` fue bloqueada por Code Integrity. Eventos 3077 y 3033; política `{0283ac0f-fff1-49ae-ada1-8a933130cad6}`. `pip check` dio PASS, pero no prueba permisos de ejecución de DLL. **No cambiar ni deshabilitar la política WDAC**. Ejecutar el gate interactivo Google OIDC únicamente en un entorno QA autorizado compatible (por ejemplo otra estación aprobada, previa verificación). La URL `localhost` del callback requiere que el navegador y el servidor correspondan al mismo equipo, o una configuración de redirect explícitamente autorizada. Repetir `pip check` e instalar auth extra en ese entorno.

## Estado al 15/10/2026
Solo se verificó estáticamente la rama y la ausencia de la contraseña heredada en `app.py`. **No se ejecutó login Google real**, no se dispone de credenciales del cliente de pruebas en este entorno. PR borrador; sin merge ni deploy.

Fuentes: https://docs.streamlit.io/develop/concepts/connections/authentication y https://docs.streamlit.io/develop/tutorials/authentication/google

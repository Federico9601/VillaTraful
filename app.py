from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(_name_)

# Configuración del correo (usaremos Gmail como ejemplo)
EMAIL_ADDRESS = "carlosalvarezvega2016@gmail.com"  # Reemplaza con tu Gmail
EMAIL_PASSWORD = "tu_app_password"  # Usa una contraseña de aplicación de Gmail

@app.route('/', methods=['GET', 'POST'])
def index():
    success = False
    if request.method == 'POST':
        # Obtener datos del formulario
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Preparar el cuerpo del correo
        subject = "Nuevo mensaje desde Villa Traful"
        body = f"Nombre: {name}\nEmail: {email}\nMensaje: {message}"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = "carlosalvarezvega2016@gmail.com"

        # Enviar el correo usando Gmail SMTP
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
            success = True
        except Exception as e:
            print(f"Error al enviar correo: {e}")
            success = False  # Opcional: podrías mostrar un mensaje de error

    return render_template('index.html', success=success)

if _name_ == '_main_':
    app.run(debug=True)
import requests
from config import API_KEY, CITY_NAME, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER
import smtplib

def get_weather_data(city_name):
    """Obtiene el pronóstico del clima desde OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al obtener datos: {response.status_code}, {response.text}")

def send_email_alert(subject, message):
    """Envía un correo electrónico con la alerta."""
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email_message)
    print("Correo enviado exitosamente.")

def check_rain_and_alert():
    """Verifica si hay lluvia en el pronóstico y envía una alerta."""
    weather_data = get_weather_data(CITY_NAME)
    weather_description = weather_data["weather"][0]["description"]
    print(f"Clima actual en {CITY_NAME}: {weather_description}")
    
    if "rain" in weather_description.lower():
        subject = f"Alerta de Lluvia en {CITY_NAME}"
        message = f"El clima actual indica lluvia: {weather_description}. ¡Prepárate!"
        send_email_alert(subject, message)
    else:
        print("No se detecta lluvia en el pronóstico.")

if __name__ == "__main__":
    check_rain_and_alert()

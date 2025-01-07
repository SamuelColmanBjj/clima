# Alerta de Clima con APIs

Este proyecto utiliza la API de OpenWeather para consultar el clima de una ciudad específica y envía una alerta si se detecta lluvia en el pronóstico.

## Requisitos
- Python 3.7+
- Una cuenta en [OpenWeather](https://openweathermap.org/) para obtener una API Key.

## Configuración
1. Crea un archivo `config.py` con tus claves y configuraciones:
   - API Key de OpenWeather
   - Email de envío y recepción (opcional)
2. Instala las dependencias con:
   ```bash
   pip install -r requirements.txt

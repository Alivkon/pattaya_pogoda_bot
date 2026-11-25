FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py texts_msg.py weather_vibrosi.py stormglass_extrem_tides.py response.json ./

RUN useradd --create-home --uid 1001 botuser && chown -R botuser /app
USER botuser

CMD ["python", "main.py"]

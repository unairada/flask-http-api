FROM python:3-slim

COPY requirements.txt /app_data/
RUN pip install -r /app_data/requirements.txt

RUN adduser --system --uid 1999 --group appuser
RUN mkdir /app ; chmod 777 /app
USER 1999

COPY src/ /app
COPY /resources /app/resources
WORKDIR /app

CMD ["python3","app.py"]

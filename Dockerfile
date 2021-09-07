FROM python:3.8-slim-buster

WORKDIR /app
ADD requirements.txt .
RUN pip install --upgrade --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x app.py

EXPOSE 80
ENTRYPOINT /app/app.py

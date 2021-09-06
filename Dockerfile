FROM python:3.8-alpine
#RUN apt-get update \
#  && pip install --upgrade --no-cache-dir pip \
#  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ADD requirements.txt .
RUN pip install --upgrade --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8080
CMD ["python3", "-u", "app.py"]

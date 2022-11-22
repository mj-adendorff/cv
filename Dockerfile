FROM python:3.9
WORKDIR /app

COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install gunicorn

COPY . .
EXPOSE 8080
CMD ["gunicorn", "-b :8080", "main:app"]

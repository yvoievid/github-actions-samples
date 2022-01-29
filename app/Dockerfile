FROM python:3.7-slim

WORKDIR /app
RUN groupadd -r webservice && useradd --no-log-init -r -g webservice webservice
COPY . .
RUN pip install -r requirements.txt

USER webservice:webservice

EXPOSE 8050
CMD ["python", "hello.py"]

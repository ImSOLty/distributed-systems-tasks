FROM python:3.10.13-alpine3.19
WORKDIR /runner
COPY . /runner
RUN pip install faker flask redis
ENTRYPOINT ["python3", "main.py"]
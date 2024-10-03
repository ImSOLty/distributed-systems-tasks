FROM python:3.10.13-alpine3.19
WORKDIR /runner
COPY . /runner
RUN pip install -r requirements.txt --no-cache-dir
CMD ["python3", "main.py"]
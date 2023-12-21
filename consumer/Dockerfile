FROM python:3.12-slim

RUN pip install kafka-python

COPY consumer.py /consumer.py

CMD ["python", "/consumer.py"]

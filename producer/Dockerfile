FROM python:3.12-slim

RUN pip install kafka-python

COPY producer.py /producer.py

CMD ["python", "/producer.py"]

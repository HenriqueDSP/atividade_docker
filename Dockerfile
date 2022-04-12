FROM python:3.9-slim
RUN pip install flask
RUN pip install sqlalchemy
RUN mkdir templates
COPY main.py/main.py
COPY templates/*  /templates/
RUN chmod -R a+rwx templates
CMD ["python","main.py"]
FROM python:3.10

WORKDIR /calculator_app
COPY ./ .

# pip freeze > requirements.txt
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD main.py .
CMD ["python", "main.py"]
FROM python:3.11

COPY ./requirements.txt /src/requirements.txt
COPY ./src /src/app

WORKDIR /src

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
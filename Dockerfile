FROM python:3.11-slim

ENV PIP_DESABLE_PIP_VERSION_CHECK=1
ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.11

WORKDIR /app

COPY ./transaction_verification/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install reloadium

CMD reloadium run "suggestions/src/app.py"

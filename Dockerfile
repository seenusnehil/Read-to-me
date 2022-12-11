FROM python:slim

Expose 8080

RUN apt-get update && apt-get install -y git

COPY . /app

WORKDIR /app

RUN pip install -r /app/requirments.txt

RUN pip install pdfplumber

ENTRYPOINT ["streamlit", "run", "src/app.py", "--server.port=8080", "--server.address=0.0.0.0"]

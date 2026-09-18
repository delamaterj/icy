FROM python:3.12

WORKDIR /app

COPY installed-requirements.txt ./

RUN pip install --no-cache-dir -r installed-requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HOST=0.0.0.0
ENV PORT=8000
ENV DATABASE_URL=mysql+pymysql://root:root@db:3306/db_strength

EXPOSE 8000

CMD ["python", "main.py"]
FROM python:3.12.3-slim
ENV TOKEN='your token from t.me/BotFather'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]

FROM python:3.10.7

WORKDIR /app

COPY ../requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV OPENAI_API_KEY=pass

CMD ["python", "./assistant/tester.py"]
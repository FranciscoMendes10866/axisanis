FROM python:3.8.6-slim
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 7819
CMD ["python3", "main.py"]

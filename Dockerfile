FROM python:3.12-slim
WORKDIR /app
COPY 11_images/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY 11_images/src/ src/
COPY docker_entrypoint.py .
EXPOSE 6031
ENTRYPOINT ["python", "docker_entrypoint.py"]
CMD ["python", "-m", "flask", "--app", "src.app.app", "run", "--host", "0.0.0.0", "--port", "6031", "--no-reload"]

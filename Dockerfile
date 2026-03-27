FROM python:3.12-slim AS production
WORKDIR /app
COPY 11_images/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY 11_images/src/ src/
COPY docker_entrypoint.py .
EXPOSE 6031
ENTRYPOINT ["python", "docker_entrypoint.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:6031", "--workers", "2", "src.app.app:app"]

# -- Test stage: docker compose -f docker-compose.test.yml --
FROM python:3.12-slim AS test
WORKDIR /app
COPY 11_images/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt pytest
COPY 11_images/src/ src/
CMD ["pytest", "src/", "-v", "--tb=short"]

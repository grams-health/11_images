FROM python:3.12-slim AS production
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
COPY docker_entrypoint.py .
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser
EXPOSE 6031
HEALTHCHECK --interval=10s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:6031/health')"
ENTRYPOINT ["python", "docker_entrypoint.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:6031", "--workers", "2", "--preload", "src.app.app:app"]

FROM python:3.12-slim AS test
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
COPY pytest.ini .
CMD ["pytest", "src/", "-v", "--tb=short"]

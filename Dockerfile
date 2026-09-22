FROM python:3.12-slim AS build
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONPATH=/app/src
RUN useradd -u 10001 -m appuser
WORKDIR /app
COPY --from=build /install /usr/local
COPY src ./src
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=3s --retries=5 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/ready')"
CMD ["uvicorn","wafi.api.app:app","--host","0.0.0.0","--port","8000"]

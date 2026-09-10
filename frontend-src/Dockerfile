FROM python:3.13-alpine3.22 AS builder

WORKDIR /build

COPY requirements.txt .

RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt


FROM python:3.13-alpine3.22 AS runtime

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_VERSION=0.2.0

RUN addgroup -g 10001 -S appgroup \
    && adduser -u 10001 -S -D -H -G appgroup appuser

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY --chown=10001:10001 app.py .

USER appuser

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]

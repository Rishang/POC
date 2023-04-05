service_name="fastapi.app"

# export OTEL_EXPORTER_JAEGER_ENDPOINT=http://localhost:14268/api/traces

opentelemetry-instrument \
    --service_name $service_name \
    --traces_exporter console \
    --metrics_exporter console \
    uvicorn app:app --host 0.0.0.0 --port 8000 --reload

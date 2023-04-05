# jaeger_tracing.py
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({SERVICE_NAME: "my-hello-service"}))
)

trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
tracer = trace.get_tracer(__name__)


with tracer.start_as_current_span("rootSpan"):
    with tracer.start_as_current_span("childSpan"):
        print("Hello world!")

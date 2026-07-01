# OpenAPI Client Error Handling

## Error Types

The OpenAPI client can encounter various types of errors, including:

- **HTTP Status Errors**: Responses with status codes outside the 2xx range.
- **Network Errors**: Connection timeouts, DNS failures, etc.
- **Validation Errors**: Errors in request or response validation (e.g., schema validation).
- **Unexpected Errors**: Errors that do not fit into the above categories.

Each error type is represented by a specific exception class in the client library.

## Handling Patterns

Errors should be caught and handled appropriately. The client library throws typed exceptions that can be caught in a try-catch block.

Example pseudocode:

```python
try:
    response = client.api.operation()
except HTTPStatusError as e:
    # Handle HTTP errors (e.g., 4xx, 5xx)
    log.error(f"HTTP error: {e.status_code} - {e.message}")
except NetworkError as e:
    # Handle network issues
    log.error(f"Network error: {e.message}")
except ValidationError as e:
    # Handle validation errors
    log.error(f"Validation error: {e.message}")
except Exception as e:
    # Handle any other unexpected errors
    log.error(f"Unexpected error: {e.message}")
```

## Retry Logic

The client may be configured to automatically retry certain failed requests.

### When to Retry

Retries are typically attempted for:
- Idempotent operations (e.g., GET, PUT, DELETE) when encountering transient errors.
- Specific HTTP status codes (e.g., 502, 503, 504, 429).
- Network errors that are considered transient (e.g., timeouts).

### Backoff Strategies

The client supports configurable backoff strategies:
- **Fixed**: Wait a fixed amount of time between retries.
- **Exponential**: Wait time increases exponentially with each retry attempt.
- **Jitter**: Adds randomness to the backoff time to prevent thundering herd problems.

### Configuration

Retry policies can be configured per client instance or per operation.

Example configuration:

```python
client = OpenAPIClient(
    retry_config=RetryConfig(
        max_attempts=3,
        backoff_strategy="exponential",
        backoff_factor=0.5,  # seconds
        retry_on=[502, 503, 504, 429],
        retry_on_network_errors=True
    )
)
```

## Error Propagation

Errors that are not caught and handled by the client's retry mechanism are propagated to the caller. The caller is responsible for handling these errors appropriately.
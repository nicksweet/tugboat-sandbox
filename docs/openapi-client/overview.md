# OpenAPI Client Overview

## Purpose
The OpenAPI client is a generated library that provides type-safe access to the Tugboat API.
It simplifies integration by handling HTTP requests, serialization, and deserialization.

## Generation Approach
The client is generated using OpenAPI Generator from the Tugboat OpenAPI specification.
Generated code resides in the `src/openapi-client` directory and is updated via the `generate-openapi-client` script.
Manual modifications should be avoided in generated files; instead, extend or wrap the client as needed.

## Integration Points
- The client is used by backend services to interact with the Tugboat API.
- It is also used by the Tugboat CLI for certain operations.
- Integration involves initializing the client with the appropriate base URL and authentication (if required).
- Error handling and retry logic are implemented at the service layer, not in the client itself.

## Usage Context
- The client is published as an internal package and consumed by various Tugboat services.
- For development, the client can be regenerated when the API specification changes.
- Refer to the API documentation for endpoint-specific usage.
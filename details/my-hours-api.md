# My Hours API

The My Hours API provides programmatic access to time tracking data from your My Hours account, including projects, tasks, clients, and time entries, enabling integrations with custom applications, internal tools, and automated workflows.

## Features

- **Programmatic access to My Hours data**  
  - Work with projects, tasks, clients, and time entries.  
  - Integrate My Hours time tracking into custom apps, internal tools, and automation workflows.

- **Standardized JSON responses**  
  - All API responses are returned in JSON format for easy parsing and integration.

- **REST-style operations**  
  - `GET` requests to fetch data from My Hours.  
  - `POST` requests to create and save new resources (e.g., time logs, projects) to your My Hours account.

- **Clear HTTP status codes**  
  - `200 OK` for successful requests.  
  - `4XX` for client-side errors (e.g., invalid request, authentication issues).  
  - `5XX` for server-side errors.

- **API key–based authentication**  
  - Access controlled via API Keys tied to a My Hours account.  
  - API Key passed in the `Authorization` header as:  
    `Authorization: ApiKey YOUR_API_KEY`  
  - Only authenticated and authorized requests can access or modify resources such as time logs, projects, users, and reports.

- **Integration tooling via Postman**  
  - Official Postman collection available (“Run in Postman”) for quick testing and exploration of endpoints.  
  - Compatible with the Postman desktop client for interactive development and debugging.

## Authentication

- Requires an active My Hours account to generate an API Key.  
- API Key is created via My Hours account settings (per official instructions).  
- Every request must include the API Key in the `Authorization` header using the format: `Authorization: ApiKey YOUR_API_KEY`.

## Pricing

Pricing information for the My Hours API is not specified in the provided documentation.
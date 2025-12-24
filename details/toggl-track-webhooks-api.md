# Toggl Track Webhooks API

**Category:** Others  
**Brand:** Toggl Track  
**Documentation:** https://developers.track.toggl.com/docs/

## Overview
The Toggl Track Webhooks API allows applications to subscribe to workspace events and receive HTTP callbacks when time tracking data or related entities change. It is used to monitor time entry updates, synchronize Toggl Track data with external systems in near real time, and trigger automations based on tracking activity.

## Features
- **Event subscriptions**
  - Subscribe to workspace-level events related to time tracking and related data.
  - Receive webhook callbacks when relevant changes occur (such as time entry updates).
  - Use callbacks to keep external systems synchronized with Toggl Track.

- **Automation and integrations**
  - Trigger custom workflows or automations when tracking activity changes.
  - Enable near real-time synchronization with third-party tools (e.g., reporting, billing, project management).

- **API format and protocol**
  - Accepts JSON request bodies only.
  - Requires `Content-Type: application/json` on all requests.
  - Returns JSON-encoded response bodies.
  - Uses standard HTTP response codes to signal success or failure.

- **Time and date handling**
  - Uses ISO 8601 timestamps, specifically the RFC 3339 subset.
  - Stores all timestamps in UTC (GMT).
  - Converts returned timestamps to the user’s configured timezone.
  - Integrations are expected to handle correct timezones and daylight saving time where applicable.

- **Quota and usage limits (sliding window)**
  - Sliding-window request quota applied per user per organization.
  - **Organization-specific requests** (e.g., workspace reports, time entries, projects) have quotas determined by the organization’s subscription plan.
  - **User-specific requests** (e.g., `https://api.track.toggl.com/api/v9/me`) are limited to 30 requests per hour per user, regardless of organization plan.
  - Response headers expose quota status:
    - `X-Toggl-Quota-Remaining` – how many requests are left in the current window.
    - `X-Toggl-Quota-Resets-In` – time until the quota resets.
  - When quota is exceeded, the API returns HTTP 402 and the client must wait before retrying.
  - Higher, custom quotas are available on Enterprise plans.

- **Rate limiting (leaky bucket)**
  - Additional leaky-bucket rate-limiting is applied as a safeguard.
  - Limits are enforced per API token per IP address.
  - A safe operating window is approximately 1 request per second.
  - When a rate limit is hit, the API returns HTTP 429 and clients should back off and retry after waiting.

- **Consistency model**
  - The API authorization layer operates within an event-based service architecture and is documented with an eventual consistency model (details in the official docs).

## Pricing
- No explicit per-API or per-webhook pricing is described in the provided content.
- Quotas for organization-specific requests depend on the Toggl Track workspace’s subscription plan.
- Enterprise plans can obtain higher, custom API quotas.
- For full and current pricing details, refer to Toggl Track’s main pricing information outside the API documentation.
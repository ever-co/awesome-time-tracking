# Qmonix

Qmonix is an event-based analytics server designed to collect and visualize custom metrics, such as time-tracking task durations, from client applications.

- **Category:** Time Tracking – APIs & Integrations  
- **Tags:** analytics, reporting, workflow

## Overview
Qmonix provides a backend analytics server and client SDKs for sending event data from applications. It can be used to track usage patterns and performance metrics in desktop or other non-web applications.

## Features
- **Event-based analytics server**  
  - Receives custom events (e.g., feature usage, workflow steps, task durations).  
  - Suitable for tracking desktop and other non-web applications.

- **Custom metric collection**  
  - Collects arbitrary metrics such as time-tracking task durations.  
  - Can be integrated with time-tracking tools (e.g., Awesome Time Tracker) to log and analyze work sessions.

- **Visualization of metrics**  
  - Provides visualization of collected data to analyze user behavior, usage frequency, and workflow performance.

- **Client SDKs / Integrations**  
  - **Lua SDK** used by tools like Awesome Time Tracker to send tracking events to Qmonix.  
  - **C++ client library** (POSIX-only in the referenced material) that uses libcurl for HTTP communication and can be ported to other platforms.

## Integrations
- Integrates with **Awesome Time Tracker** (via the Qmonix Lua SDK) for sending time-tracking events.  
- C++ client library for integrating desktop or other native applications.

## Pricing
No pricing information is provided in the available content.
## guzzle-toggl

**Type:** PHP library / Toggl API client  
**Category:** others  
**Source:** [GitHub – arendjantetteroo/guzzle-toggl](https://github.com/arendjantetteroo/guzzle-toggl)

A PHP client for the Toggl Track API, built on the Guzzle HTTP client. It allows PHP applications to integrate with Toggl’s time-tracking and reporting features programmatically.

---

## Features

- **Toggl API support**
  - Supports Toggl Track **API v9**
  - API key–based authentication
  - Supports **Toggl Reports API v2**
- **HTTP client foundation**
  - Built on **Guzzle 7**
- **Client instantiation & configuration**
  - Factory-based creation: `TogglClient::factory([...])`
  - Configure API key via `api_key` parameter
  - Optional `debug => true` flag to see HTTP-level details
- **Command execution styles**
  - **Magic `__call` method** for invoking API operations directly (with PHPDoc auto-complete)
    - Example: `$toggl_client->getWorkspaces([]);`
  - **Explicit command objects** via `getCommand()`
    - Example: `$command = $toggl_client->getCommand('GetWorkspaces', []);`
    - Manual `prepare()` and `execute()` control
    - Access raw response via `$response['data']`
- **Workspace, project, client, task, tag & time entry operations**
  - Endpoints for managing:
    - Clients
    - Projects
    - Project users
    - Tags
    - Tasks
    - Time entries
    - Workspaces and organizations
  - New endpoints introduced in v9 layer:
    - `ArchiveClient`
    - `RestoreClient`
- **API v9-specific parameter handling**
  - Many endpoints now require `workspace_id` (for example: `CreateClient`, `GetClient`, `CreateProject`, `StartTimeEntry`, `UpdateTimeEntry`, etc.)
  - Certain endpoints additionally require `project_id` (for example: `CreateTask`, `GetTask`, `UpdateTask`, `DeleteTask`, etc.)
  - `GetProjects` now uses `workspace_id` instead of `id`
  - `GetProjectUsers` now expects `workspace_id` instead of `project_id`
  - Endpoint rename for closer alignment with Toggl docs:
    - `InviteWorkspaceUser` → `InviteOrganizationUser`
  - Deprecated/removed endpoints:
    - `GetWorkspaceWorkspaceUsers`
    - `GetWorkspaceProjects` (replaced by `GetProjects`)
- **Discoverability & examples**
  - `services.json` describes available methods and parameters
  - Example scripts provided in an `examples` directory
  - Example API key configuration via `apikey.php`
- **Development roadmap**
  - Planned: more examples, tests, and response models
  - Open to community contributions

---

## Installation

Install via Composer:

```bash
composer require ajt/guzzle-toggl
```

---

## Usage

### Basic client setup

```php
<?php

require __DIR__.'/../vendor/autoload.php';

use AJT\Toggl\TogglClient;

$toggl_token  = ''; // Fill in your API token
$toggl_client = TogglClient::factory(['api_key' => $toggl_token]);
```

Enable debug output:

```php
$toggl_client = TogglClient::factory([
    'api_key' => $toggl_token,
    'debug'   => true,
]);
```

### Calling API methods via `__call`

```php
use AJT\Toggl\TogglClient;

$toggl_client = TogglClient::factory(['api_key' => $toggl_token]);

$workspaces = $toggl_client->getWorkspaces([]);

foreach ($workspaces as $workspace) {
    $id = $workspace['id'];
    echo $workspace['name']."\n";
}
```

### Using `getCommand` directly

```php
use AJT\Toggl\TogglClient;

$toggl_client = TogglClient::factory(['api_key' => $toggl_token]);

$command = $toggl_client->getCommand('GetWorkspaces', []);
$command->prepare();
$response   = $command->execute();
$workspaces = $response['data'];

foreach ($workspaces as $workspace) {
    $id = $workspace['id'];
    echo $workspace['name']."\n";
}
```

---

## Examples

- Copy `apikey-dist.php` to `apikey.php` in the project root and add your Toggl API key.
- Run the example scripts provided in the `examples` directory.
- Refer to `services.json` to see the complete list of available API methods and their parameters.

---

## Pricing

Not specified in the project documentation. This is an open-source PHP client; licensing and costs, if any, should be verified on the GitHub repository.

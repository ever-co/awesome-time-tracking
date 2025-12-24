# Awesome Time Tracker

## Description
Awesome Time Tracker is a lightweight, keyboard‑driven time tracking tool integrated with the Awesome Window Manager. It lets users start, stop, and inspect tasks using configurable key bindings and sends tracking events to a Qmonix server, where time data can be viewed and analyzed via the Qmonix web dashboard. It is aimed at developers and power users who work primarily inside Awesome WM.

## Features
- **Tight integration with Awesome WM**  
  Designed to run inside the Awesome Window Manager environment.

- **Keyboard‑driven workflow**  
  Start, stop, and inspect tasks using configurable key bindings.

- **Task control**  
  - Start tracking a task
  - Stop tracking a task  
  - Inspect currently tracked or recent tasks (from within Awesome)

- **Qmonix server integration**  
  - Sends time tracking events to a Qmonix server (local or remote)  
  - Uses Qmonix’s event collection for storage and processing

- **Web dashboard analytics (via Qmonix)**  
  - View tracked time in the Qmonix web dashboard  
  - Analyze time usage based on Qmonix’s reporting and visualization capabilities

- **Configurable installation path**  
  - Builds and installs to `~/.config/awesome` by default  
  - Installation directory can be changed via the `INSTALL_PATH` variable (e.g., to the directory containing `rc.lua`).

- **Open‑source**  
  Source code hosted on GitHub; suitable for customization and extension.

## Dependencies
- **Awesome Window Manager** (runtime environment)
- **Qmonix server** (for event collection and analytics)
  - Can be installed on a local or remote machine  
  - Installation instructions provided in the Qmonix docs: <http://docs.qmonix.com/latest/installation/index.html>

## Installation
1. **Install Qmonix**  
   - Follow the Qmonix server installation guide: <http://docs.qmonix.com/latest/installation/index.html>

2. **Install Awesome Time Tracker**  
   - From the project directory, run: `make install`  
   - By default, this installs into `~/.config/awesome`.
   - To change the install directory, set `INSTALL_PATH` before running `make install`, e.g.:  
     ```bash
     INSTALL_PATH=/path/to/your/awesome/config make install
     ```
   - It is recommended to point `INSTALL_PATH` to the directory where your `rc.lua` (Awesome WM configuration) is located.

## Pricing
- **Free and open‑source**  
  No pricing or paid plans are mentioned; the tool is available as an open‑source GitHub project.

## Links
- **Source code:** https://github.com/povilasb/awesome-time-tracker

## Screenshots
- Overview / dashboard:  
  - http://demo.qmonix.com/event/awesome_time_tracker/github_view.png
- In‑Awesome task start UI:  
  - https://raw.githubusercontent.com/povilasb/awesome-time-tracker/master/res/img/start_task.png
- Qmonix integration view:  
  - https://raw.githubusercontent.com/povilasb/awesome-time-tracker/master/res/img/qmonix.png

# RTW (Rust Time Watcher)

**Category:** Time Tracking CLI Tools  
**Tags:** open-source, command-line, rust, personal-use

## Description
RTW (Rust Time Watcher) is a free and open-source command-line time tracker written in Rust. It provides simple time-tracking capabilities directly from the terminal. RTW is inspired by Timewarrior and is built primarily as a personal productivity tool.

## Features
- Command-line interface for time tracking
- Supports Linux, MacOS (stable), and Windows (experimental)
- Start, stop, and display current activities from the terminal
- View daily activity summaries and timelines
- Stores activity data in JSON files (default location: home directory)
- Configurable via JSON config file (user must create or copy from example)
- Shell completion scripts available for Bash, Zsh, Fish, Powershell, and Elvish
- Starship prompt integration
- Buildable from source with Rust 1.42.0 or newer
- Prebuilt binaries available for Linux
- Activity persistence without server or database (file-based)

## Implementation Notes
- No file locking: running multiple RTW commands simultaneously may cause undefined behavior
- Config file is not created automatically; user must supply one if customization is needed

## Pricing
RTW is free and open-source software released under an open-source license.

## Source
[https://github.com/PicoJr/rtw](https://github.com/PicoJr/rtw)

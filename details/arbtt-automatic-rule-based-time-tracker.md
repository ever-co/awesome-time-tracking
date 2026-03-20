## Overview

Arbtt (Automatic Rule-Based Time Tracker) is open-source software for Linux, Windows, and macOS that runs as a desktop daemon, recording what windows are open and which is active, then categorizing time based on user-defined rules.

## How It Works

### Data Collection
arbtt-capture runs in background and keeps a continuous log:
- Which windows are open
- Window titles
- Which window has focus
- Time since last user action
- Saves one sample per minute (configurable)

### Rule-Based Categorization
Mapping from raw window titles to "tags" is done by configuration file with powerful syntax:
- Rules applied in real-time during evaluation, not recording
- Raw data always intact
- Can add more rules later for forgotten cases
- Retroactive categorization

## Technical Details

- Written in Haskell
- Open source (GitHub: github.com/nomeata/arbtt)
- Saves configurable samples (default: one per minute)
- Privacy-conscious: log file may contain sensitive data - protect it well

## Platform Support

- Linux
- Windows  
- macOS

## Key Advantage

Raw data preservation means you can refine categorization rules anytime without losing historical tracking information.
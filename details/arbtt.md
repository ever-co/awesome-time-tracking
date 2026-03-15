## Overview

arbtt is an automatic, rule-based time tracker implemented in Haskell. The name stands for "automatic rule-based time tracker." It runs silently in the background, recording what windows are open on your desktop, their titles, and which one is active.

## How It Works

The core component (arbtt-capture) silently captures data about what you are doing, completely autonomously with no interaction required, and continuously stores this information in a log file.

arbtt comes with a built-in command-line statistics generator (arbtt-stats) that uses simple but powerful customizable rules to sift through the raw data and reveal patterns and relevant information.

## Features

- **Automatic Capture**: Records window information every minute without user interaction
- **Rule-Based Categorization**: The mapping from raw window titles to sensible "tags" is done by a configuration file with a powerful syntax
- **Retrospective Analysis**: Since the rules are applied when evaluating your data, not when recording it, you can add more tags and forgotten special cases later
- **Privacy-Focused**: The log file is stored locally on your machine
- **Command-Line Interface**: Statistics and reports generated via command-line tools
- **Customizable Rules**: Rules specified in a simple text-based format in a file called "categorize.cfg"

## Privacy Considerations

The log file might contain very sensitive private data, so users should understand the consequences of a full-time logger and take appropriate security measures.

## Resources

- **Repository**: GitHub at https://github.com/nomeata/arbtt/issues
- **Package**: Available on Hackage at https://hackage.haskell.org/package/arbtt
- **Mailing list**: arbtt@lists.nomeata.de

## Pricing

Free and open-source software.

---
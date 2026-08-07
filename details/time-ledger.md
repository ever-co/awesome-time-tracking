# time-ledger

Natural-language time tracking that runs as a Claude skill (with a ChatGPT custom GPT path): you describe your day in plain language, such as "read papers 2h, gym 1h", and the AI parses it into activity, duration, and date rows in your own Notion database — asking for confirmation instead of guessing when unsure.

## Features

- Conversational logging: one sentence in a chat you already have open becomes structured rows (activity / minutes / date / compounding tag)
- Honesty contract: uncertain entries are stored as "to-confirm" rows and batch-asked later — the AI never fabricates durations, dates, or categories
- Zero configuration: the skill discovers your Notion database by title; no IDs to paste
- Your data stays yours: rows live in your own Notion workspace (free template included), exportable at any time, no third-party server
- Bilingual: English and Chinese skill files, README, and Notion templates

## Pricing

Free and open-source (MIT). The AI input path requires a paid Claude or ChatGPT plan (where skills/connectors are available); the Notion template works on free Notion as a manual ledger.

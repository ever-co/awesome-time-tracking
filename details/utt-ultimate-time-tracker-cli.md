## Overview

Ultimate Time Tracker (utt) is a simple command-line time tracking application written in Python. It is intended for people who need to report their time on another system and want a preliminary time sheet.

## Core Philosophy

When you have completed a task, add it to utt with the add command. You add a task when you have completed it, not when you start doing it.

## Activity Types

There are three types of activities:

- **Working activities**: Contribute to the working time
- **Break activities**: End with ** and contribute to break time  
- **Ignored activities**: End with *** and contribute to neither working nor break time

## Reporting Features

There are four sections in a report, each one an aggregated view of the previous one. You can choose the report date by passing a date to the report command. The date must be either an absolute date formatted as "%Y-%m-%d" or a day of the week.

## Installation

The project is available on GitHub at larose/utt and is licensed under GNU GPL v3. It's also available on PyPI for installation via pip.

## Pricing

Free and open-source under GNU GPL v3 license.
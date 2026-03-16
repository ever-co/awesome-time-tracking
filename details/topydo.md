## Overview

Topydo is a powerful todo list application using the todo.txt format, originally inspired by the todo.txt CLI by Gina Trapani. It's an advanced terminal utility for managing tasks, with tasks stored in a plain text file using the todo.txt format, making it fully compatible with other todo.txt tools.

## Multiple Interface Modes

- **CLI Mode**: Traditional command-line interface for quick task operations
- **Prompt Mode**: Convenience mode for the CLI, launched with `topydo prompt`
- **Column Mode**: Text-based user interface (TUI) with customizable columns and vim-like bindings, launched with `topydo columns`

## Advanced Functionality

- **Multiple Output Formats**: Export to iCalendar, JSON, and Graphviz Dot
- **Aliases**: Support for frequently used commands to speed up workflow
- **Special Tags**: Due dates, start dates for bills, rent, appointments, etc.
- **Text-Based Identifiers**: More stable and convenient than line-based todo identifiers
- **Context Support**: Use contexts like @phone, @email, or @home to group tasks by when they can be completed

## GTD Integration

Topydo is well-suited for Getting Things Done methodology with context-based task organization. The tool provides means to group tasks according to the context of when they can be completed, a core GTD principle.

## Compatibility

Fully todo.txt compliant - text files can be processed by other todo.txt tools, though they may not interpret advanced tags properly. Dedicated tools like todo.txt-gtd provide recipes for customizing specifically for GTD workflows.

## Pricing

Free and open-source (available on GitHub)
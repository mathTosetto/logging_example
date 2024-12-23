# My App Logger

This repository provides a Python application with a robust logging setup, including a custom JSON formatter for structured logs. The logger is configured to output logs in both plain text (for stderr) and JSON (to a file).

---

## Features

- **Custom JSON Formatter**:
  - Outputs logs in structured JSON format.
  - Includes fields like timestamp, log level, module, function name, and exception details.

- **Rotating File Handler**:
  - Writes JSON-formatted logs to a file.
  - Supports log rotation with configurable file size and backup count.

- **Stream Handler**:
  - Outputs plain-text logs to `stderr` for warning-level and higher messages.

---

## Log Format
```JSON
{
    "level": "ERROR",
    "message": "Error message",
    "timestamp": "2023-12-23T15:45:01+00:00",
    "logger": "my_app",
    "module": "main",
    "function": "main",
    "line": 35,
    "thread_name": "MainThread",
    "exc_info": "Traceback (most recent call last):\n  File \"main.py\", line 28, in main\n    1 / 0\nZeroDivisionError: division by zero\n"
}
```

dasd
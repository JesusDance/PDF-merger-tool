# Flask PDF-merger-tool.

## Description

This module implements a single web application pdf merger using Bootstrap styling.
Features includes:
- pypdf for merging files
- pathlib for easy access to path of files
- Jinja2 templates
- flash messages for feedback

## Routes:

- '/': main page with form
- '/clear': clear list of pdf before merging
- '/merge': merging pdf files
- '/delete/<name>': delete file by name

# Data Generator

A flexible and powerful data generation tool for creating synthetic datasets. This project helps developers, data scientists, and researchers generate customizable data for testing, prototyping, and analysis.

## Features

- **Customizable Data Schemas**: Define your own data structure and types.
- **Multiple Data Types**: Generate numeric, categorical, datetime, and textual data.
- **Configurable Output Formats**: Export data to CSV, JSON, or other formats.
- **Scalable Generation**: Produce thousands to millions of records efficiently.
- **Extensible**: Easily add new generators or output formats.

## Getting Started

### Prerequisites

- Python 3.7+
- (Optional) Other dependencies as specified in `requirements.txt`

### Installation

Clone the repository:
```bash
git clone https://github.com/sudo-sidd/Data_generator.git
cd Data_generator
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Example command to generate a dataset:
```bash
python main.py --schema schema.json --output data.csv --rows 1000
```

- `--schema`: Path to your data schema (see below).
- `--output`: Output file path.
- `--rows`: Number of rows to generate.

#### Sample Schema (`schema.json`)
```json
{
  "fields": [
    { "name": "id", "type": "integer", "start": 1 },
    { "name": "name", "type": "string", "length": 8 },
    { "name": "date", "type": "date", "start": "2022-01-01", "end": "2022-12-31" }
  ]
}
```

### Output Formats

- CSV
- JSON
- (More formats can be added)
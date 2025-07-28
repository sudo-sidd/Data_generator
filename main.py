import typer
from data_generator import generate_data
from utils import load_schema, load_theme

app = typer.Typer()

@app.command()
def generate(
    prompt: str = typer.Option(None, help="Input prompt to define data structure"),
    schema_path: str = typer.Option(None, help="Path to JSON schema file"),
    theme: str = typer.Option("default", help="Theme for value generation"),
    count: int = typer.Option(10, help="Number of data rows to generate"),
    output: str = typer.Option(None, help="Output file (JSON/CSV), or stdout if not set"),
    format: str = typer.Option("json", help="Output format: json or csv")
):
    """Generate mock data based on prompt or schema."""
    schema = load_schema(prompt, schema_path)
    theme_data = load_theme(theme)
    data = generate_data(schema, theme_data, count)
    if output:
        from utils import write_output
        write_output(data, output, format)
    else:
        import json, csv, sys
        if format == "json":
            print(json.dumps(data, indent=2))
        else:
            import io
            writer = csv.DictWriter(sys.stdout, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

if __name__ == "__main__":
    app()

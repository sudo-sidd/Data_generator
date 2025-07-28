from faker import Faker
from utils import apply_format, apply_distribution

fake = Faker()

FIELD_TYPE_MAP = {
    "string": lambda: fake.word(),
    "int": lambda: fake.random_int(),
    "float": lambda: fake.pyfloat(),
    "date": lambda: fake.date(),
    "boolean": lambda: fake.pybool(),
    "uuid": lambda: fake.uuid4(),
}

FORMAT_MAP = {
    "email": lambda: fake.email(),
    "name": lambda: fake.name(),
    "currency": lambda: fake.currency_code(),
    "datetime": lambda: fake.date_time().isoformat(),
}

def generate_field(field, theme):
    ftype = field.get("type", "string")
    fmt = field.get("format")
    dist = field.get("distribution", "uniform")
    if fmt and fmt in FORMAT_MAP:
        value = FORMAT_MAP[fmt]()
    else:
        value = FIELD_TYPE_MAP.get(ftype, lambda: fake.word())()
    value = apply_format(value, fmt, field)
    value = apply_distribution(value, dist, field)
    return value

def generate_data(schema, theme, count):
    fields = schema["fields"]
    data = []
    for _ in range(count):
        row = {f["name"]: generate_field(f, theme) for f in fields}
        data.append(row)
    return data

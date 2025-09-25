import json, csv, pathlib
from jsonschema import validate

def load_schema(path):
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))

def validate_json(record, schema):
    try:
        validate(instance=record, schema=schema)
    except Exception as e:
        print("[aviso] registro inválido:", e)

def write_outputs(records, out_dir):
    out = pathlib.Path(out_dir)
    with (out/"records.jsonl").open("w",encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r,ensure_ascii=False)+"\n")
    if records:
        keys=list(records[0].keys())
        with (out/"export.csv").open("w",encoding="utf-8",newline="") as f:
            w=csv.DictWriter(f,fieldnames=keys)
            w.writeheader()
            w.writerows(records)

import argparse, pathlib, json
from utils import load_schema, write_outputs, validate_json

def run_pipeline(input_dir, output_dir, use_llm):
    output = pathlib.Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    schema = load_schema("src/schema.json")
    records = []
    # Placeholder: cria 1 registro fictício só para testar
    records.append({
        "fonte": "Estado de Minas",
        "secao": "Política",
        "data_publicacao": "2017-07-12",
        "titulo": "Exemplo de título",
        "subtitulo": None,
        "tipo_de_texto": "reportagem",
        "autor": None,
        "pags_pdf": [1],
        "citacoes_politicos": [],
        "citacoes_orgaos": [],
        "citacoes_normas": [],
        "mencoes_projetos_lei": [],
        "resumo_curto": None,
        "url_original": None
    })
    for r in records:
        validate_json(r, schema)
    write_outputs(records, output)
    print(f"[ok] {len(records)} registros salvos em {output}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--use-llm", default="false")
    args = ap.parse_args()
    run_pipeline(args.input, args.output, args.use_llm.lower() == "true")

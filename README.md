# Clipping Extractor (Boilerplate)

Projeto para iniciantes que querem extrair dados de matérias de clipings (PDFs).

## Como usar
1. Crie um repositório no GitHub e faça upload destes arquivos.
2. Envie seus PDFs para a pasta `input/`.
3. A Action no GitHub vai rodar automaticamente e gerar os resultados na pasta `output/`.

## Saídas
- `records.jsonl`: um JSON por linha (cada matéria).
- `export.csv`: planilha simples com os campos principais.

## Dica
Comece SEM IA. Depois adicione sua chave `OPENAI_API_KEY` nos *Secrets* do repositório.

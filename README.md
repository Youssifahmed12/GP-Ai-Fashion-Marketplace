# GP-Ai-Fashion-Marketplace

Graduation project: a multi-brand clothing marketplace that brands subscribe to, with an AI stylist on top.
A shopper sends a photo ("my yellow jacket, what trousers?") or writes in English, Arabic or Franco
("graduation party outfit"). A master agent asks a vision agent what the item is, asks a recommendation
model what goes with it, then retrieves matching products from the catalog (RAG over PostgreSQL + pgvector).

## Folders

| Folder | What | Who |
|---|---|---|
| `src/outfits/` | Polyvore outfits loader, colours | Tony |
| `src/catalog/` | Product database, Kaggle loader, search | Rawan, Sandy |
| `src/embeddings/` | FashionCLIP embedder (and a fake one for tests) | youssif |
| `src/vision/` | Vision agent: photo to item type, colour, gender, style | Hannah |
| `src/master/` | Master agent: understands the shopper, calls the others | Nour |
| `tests/` | Tests. Every new function gets one | everyone |

## Setup

Full step-by-step guide: `day1-everyone` in the team folder. In short (Python 3.12):

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e ".[ml]"
python -m unittest discover -s tests       # should end with OK
docker compose up -d                       # PostgreSQL + pgvector on localhost:5432
```

## How we work

- One task, one branch, one pull request. Nobody pushes to `main`.
- `python -m unittest discover -s tests` must be OK before you open a pull request.
- Datasets (`data/`), trained models (`models/`) and keys (`.env`, `GEMINI_API_KEY`) are never committed.

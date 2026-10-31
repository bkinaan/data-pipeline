from pathlib import Path
import pymupdf

folder = Path('../../data/CompanyDocuments/invoices/')
files = sorted(folder.glob("*.pdf"))
texts = {}
out_dir = Path('../../data/interim/text')
out_dir.mkdir(parents=True, exist_ok=True)

# for file in files:
#     with pymupdf.open(file) as doc:
#         pages = [page.get_text() for page in doc]
#     text = "\n\n".join(pages)
#     texts[file.stem] = text

       
for file in files:
    with pymupdf.open(file) as doc:
        pages = [page.get_text() for page in doc]
    text = "\n\n".join(pages)
    texts[file.stem] = text
    (out_dir / f"{file.stem}.txt").write_text(text, encoding="utf-8")
    
print(len(texts), "documents extracted")
    




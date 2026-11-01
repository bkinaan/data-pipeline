# Data Pipeline

A the goal of this project is to create a deterministic parser for converting PDF invoices into normalized json objects.

## Version 1 - Invoices

_NOTE:_ Run the following commands under the root of the project

### Commands for generating parsed data

#### Bootstrap the data

Run the following command prepare the PDF Invoice for the gold data.

`./bootstrap`

This command will create a virtual environment, install dependencies, download the Invoice data, ingest the PDF data into txt files, and create a split of dev and eval files.

PDF data is stored under _data/CompanyDocuments/invoices_.

TXT data is stored under _data/interim/txt_.

Split is stored under _data/split.json_.

#### Run the parser

Generate gold data on a randomly selected single invoice.

`./gold one`

Generate gold data on a specific single invoice.

`./gold one <invoice_name_no_extension>`

Generate gold data on the entire dev dataset.

`./gold dev`

Generate gold data on the entire eval dataset.

`./gold eval`

## Problems during parser generation

### Documents with multiple pages

Documents that had multiple pages broke up the product item flow. A noise check was introduced to remove these additional lines. If the line was the text "Invoice" (indication of the start of a new page) or the line started with "Page" folloed by a digit (or could contain text like "Page x of y") it was determined to be noise data and ignored.

````
PAGE_RE = re.compile(r"Page \d+( of \d+)?", re.IGNORECASE)
def is_noise(ln: str) -> bool:
    return ln == "Invoice" or bool(PAGE_RE.fullmatch(ln))```

````

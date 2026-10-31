# Data Pipeline

## Version 1 - Invoices

### Bootstrap the data

Run the following command under the root of the project to normalize PDF Invoice data
`./bootstrap`

This command will create a virtual environment, install dependencies, download the Invoice data, ingest the PDF data into txt files, and create a split of dev and eval files.

PDF data is stored under `data/CompanyDocuments/invoices`

TXT data is stored under `data/interim/txt`

Split is stored under `data/split.json`

### Run the normalizer

Execute runs

`gold one` will randomly select a single invoice

`gold dev` will execute the normalizer on all dev txt files

# Data Pipeline

_NOTE:_ Run the following commands under the root of the project

## Version 1 - Invoices

### Bootstrap the data

Run the following command prepare the PDF Invoice data for the normalizer.

> ./bootstrap

This command will create a virtual environment, install dependencies, download the Invoice data, ingest the PDF data into txt files, and create a split of dev and eval files.

PDF data is stored under _data/CompanyDocuments/invoices_.

TXT data is stored under _data/interim/txt_.

Split is stored under _data/split.json_.

### Run the normalizer

Execute the normalizer on a randomly selected single invoice.

> ./gold one

Execute the normalizer on all dev txt files.

> ./gold dev

def main() -> None:
    print(
"""
|--------------------------------Data Pipeline----------------------------------|
|   Below are available options for running this project. Bootstrap is required |
|   ./bootstrap - Download data and initialize the environment for the parser   |
|   ./gold <option> - Parse the data using the speicified data                  |
|   ./gold one - Parse the data on a single randomly selected dev file          |
|   ./gold one <name> - Prase the data only on a single file (no ext)           |
|   ./gold dev - Parse the entire dev dataset                                   |
|   ./gold eval - Parse the entire eval dataset                                 |
|-------------------------------------------------------------------------------|
""")

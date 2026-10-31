import kagglehub

# Download latest version
path = kagglehub.dataset_download("ayoubcherguelaine/company-documents-dataset")

print("Path to dataset files:", path)
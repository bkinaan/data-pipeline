import kagglehub
import shutil
import os

# Download latest version
cache_path = kagglehub.dataset_download("ayoubcherguelaine/company-documents-dataset")

target_path = "../../data/"

os.makedirs(target_path, exist_ok=True)
shutil.copytree(cache_path, target_path, dirs_exist_ok=True)

print(f"Dataset successfully copied to path: data/")

# print("Path to dataset files:", path)

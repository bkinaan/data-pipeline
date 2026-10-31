import kagglehub
import shutil
import os

# Download latest version
cache_path = kagglehub.dataset_download("ayoubcherguelaine/company-documents-dataset")

target_path = "../../data/"

os.makedirs(target_path, exist_ok=True)
shutil.copytree(cache_path, target_path, dirs_exist_ok=True)

print(f"Dataset successfully copied to relative path: {target_path}")

# print("Path to dataset files:", path)
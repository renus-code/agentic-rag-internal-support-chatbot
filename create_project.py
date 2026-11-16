from pathlib import Path

# current working directory
root = Path(".")

## folder structure
folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/servives",
    "data",
    "templates",
    "static",
    "uploads",
    "tests"
]

## files
files =[
    "app/main.py"
    "ingest_sample_kb.py"
    "run.py"
    ".env"
]


## Create Folders
for folder in folders:
    (root/folder).mkdir(parents=True, exist_ok=True)

## Create files
for file in files:
    (root/file).touch(exist_ok=True)


print("project structure created successfully")
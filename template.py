import os
from pathlib import Path

package_name = 'mongodb_connect'

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

list_of_files_2 = [
    "mlops_1/tox.ini"
]


for filepath in list_of_files_2:
    filepath = Path(filepath)  # Ensure consistent Path handling
    # Extract parent directory and ensure its existence
    parent_dir = filepath.parent
    if parent_dir:
        parent_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the file if it does not exist or if it's empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        print(f"Created file: {filepath}")

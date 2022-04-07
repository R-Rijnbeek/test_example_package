python -m venv deploy_env

call .\deploy_env\Scripts\activate

python -m pip install --upgrade pip build twine

python -m build

python -m twine upload --repository testpypi dist/*

call .\deploy_env\Scripts\deactivate

rmdir /S deploy_env
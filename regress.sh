# install pyhigh
pip install -e .

# install testing dependencies
pip install pytest pytest-cov

# run tests
pytest --cov-report=xml --cov=pyhigh tests/ -v -r s

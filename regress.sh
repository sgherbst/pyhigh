# install pyhigh
pip install -e .

# install testing dependencies
pip install pytest pytest-cov black

# check code formatting
black . --check

# run tests
pytest tests/ -v -r s

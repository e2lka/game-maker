import os
import pytest

# $env:PYTHONPATH="C:\Users\ellka\Development\game-maker\src"

os.environ['PYTHONPATH'] = 'C:\Users\ellka\Development\game-maker\src'
pytest.main([
    'tests',
    '--cov=game-maker',
    '--cov-report=term-missing'
])

from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT_PATH, 'data')
OPERATION_JSON = Path.joinpath(DATA_PATH, 'operations.json')


ROOT_PATH_TEST = Path(__file__).parent
DATA_PATH_TEST = Path.joinpath(ROOT_PATH_TEST, 'tests')
OPERATION_JSON_TEST = Path.joinpath(DATA_PATH_TEST, 'test_operations.json')

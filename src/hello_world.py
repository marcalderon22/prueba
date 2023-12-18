import os

test_param = os.environ.get('TEST_PARAM', 'default_value')
print(f"Hello World! {test_param}")
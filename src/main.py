import json
import importlib
import os

test_param = os.environ.get('TEST_PARAM', 'default_value')
address = os.environ.get('TEST_ADDRESS', 'default_value')

def process_address():
    dir = "scripts"

    try:
        script_module = importlib.import_module(f"{dir}.{address}")
        response = getattr(script_module, "response", None)(test_param)
        print(json.dumps(response, indent = 2))
    except ImportError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

process_address()



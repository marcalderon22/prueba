def response(key):
    if key ==  "1234PYTHON5678":
        return {"message": "Hello from wallet.py"}
    else:
        return {"error": "Invalid key"}
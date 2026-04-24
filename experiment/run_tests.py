import importlib.util
import os

models = ["chatgpt", "claude", "copilot"]

def load_function(path):
    spec = importlib.util.spec_from_file_location("solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.is_prime

def run_test(func):
    try:
        assert func(1) is False
        assert func(0) is False
        assert func(-5) is False

        assert func(2) is True
        assert func(3) is True
        assert func(13) is True
        assert func(97) is True

        assert func(4) is False
        assert func(9) is False
        assert func(100) is False

        assert func(7919) is True

        return True
    except:
        return False

results = {}

for model in models:
    path = f"{model}/solution.py"
    func = load_function(path)
    result = run_test(func)
    results[model] = result

print("RESULTS:")
for model, res in results.items():
    print(f"{model}: {'PASS' if res else 'FAIL'}")

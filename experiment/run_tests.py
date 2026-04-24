import importlib.util
import csv

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

results = []

for model in models:
    func = load_function(f"{model}/solution.py")
    passed = 1 if run_test(func) else 0
    total = 1
    pass_rate = passed / total

    results.append([model, "is_prime", passed, total, pass_rate])

# PRINT TABLE (FOR LOG)
print(f"{'Model':<10} {'Passed':<10} {'Total':<10} {'Pass Rate':<10}")
print("-" * 40)
for r in results:
    print(f"{r[0]:<10} {r[2]:<10} {r[3]:<10} {r[4]*100:.1f}%")

# SAVE CSV (IMPORTANT)
with open("../results/metrics.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["model", "task", "passed", "total", "pass_rate"])
    writer.writerows(results)

print("\nSaved to results/metrics.csv")

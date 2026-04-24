import importlib.util
import csv

models = ["chatgpt", "claude", "copilot"]

def load_function(path):
    spec = importlib.util.spec_from_file_location("solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.is_prime

def run_test(func):
    passed = 0
    total = 5

    if func(1) is False:
        passed += 1
    if func(2) is True:
        passed += 1
    if func(4) is False:
        passed += 1
    if func(13) is True:
        passed += 1
    if func(9) is False:
        passed += 1

    return passed, total

results = []

for model in models:
    func = load_function(f"{model}/solution.py")
    passed, total = run_test(func)
    pass_rate = round(passed / total, 2)

    results.append([model, "is_prime", passed, total, pass_rate])

print("RESULTS:")
for r in results:
    print(f"{r[0]}: {r[2]}/{r[3]} ({r[4]*100}%)")

# SAVE CSV
with open("../results/metrics.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["model", "task", "passed", "total", "pass_rate"])
    writer.writerows(results)

print("Saved to results/metrics.csv")

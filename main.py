from kernel import Kernel
from tests import run_all_tests

kernel = Kernel("v2")
results = run_all_tests(kernel)

for r in results:
    print(r)
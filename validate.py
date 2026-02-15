"""
simulates a hardware ci validation pipeline
"""

import sys
from kernel import Kernel
from tests import run_all_tests

BASELINE_METRICS = {
    "nccl_bandwidth": 100,
    "rdma_latency": 10
}

def check_regression(test_results):
    regression_detected = False
    messages = []

    for result in test_results:
        test_name = result["test"]
        value = result["value"]
        baseline = BASELINE_METRICS.get(test_name)

        if test_name == "nccl_bandwidth":
            if value < baseline:
                regression_detected = True
                messages.append(
                    f"{test_name} regression: {value} < baseline {baseline}"
                )

        elif test_name == "rdma_latency":
            if value > baseline:
                regression_detected = True
                messages.append(
                    f"{test_name} regression: {value} > baseline {baseline}"
                )
        else:
            pass

    return regression_detected, messages
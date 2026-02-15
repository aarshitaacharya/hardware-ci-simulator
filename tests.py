"""
this file simulates validation tests
in real life this is nccl benchmarks, rdma latency etc
"""

def run_nccl_test(kernel):
    bandwidth = kernel.metadata["nccl_bandwidth"]

    return {
        "test": "nccl_bandwidth",
        "value": bandwidth,
        "unit": "GB/s"
    }

def run_rdma_test(kernel):
    latency = kernel.metadata["rdma_latency"]

    return {
        "test": "rdma_latency",
        "value": latency,
        "unit": "microseconds"
    }


def run_all_tests(kernel):
    results= []
    results.append(run_nccl_test(kernel))
    results.append(run_rdma_test(kernel))

    return results


# Mini Hardware CI Simulator

This project simulates a hardware-in-the-loop (HIL) continuous integration pipeline for HPC kernels. It allows you to demonstrate **kernel provisioning, testing, and regression detection** without needing real hardware.

---

## What It Does

* **Node Provisioning:**

  * Simulates reserving bare-metal nodes
  * Handles unavailable nodes with automatic retries
  * Simulates firmware flashing and PXE boot for kernel installation

* **Kernel Testing:**

  * Supports multiple kernel versions (test matrix)
  * Runs simulated NCCL (GPU-to-GPU) and RDMA tests
  * Generates metrics like bandwidth and latency

* **Regression Detection:**

  * Compares test results against baseline metrics
  * Flags regressions and blocks “release” if detected

* **Parallel Execution:**

  * Supports multiple nodes running tests simultaneously
  * Simulates realistic HPC cluster behavior

* **CLI Interface:**

  * Run a single kernel: `python main.py v1`
  * Run multiple kernels: `python main.py v1 v2 v3`
  * Output shows node allocation, test results, and regressions

---

## Key Files

* `kernel.py` → Simulates kernel artifacts and metadata
* `tests.py` → Simulates NCCL & RDMA test results
* `provision.py` → Simulates node reservation, firmware flashing, PXE boot
* `validate.py` → Regression detection logic
* `main.py` → Orchestrates the full pipeline
---

## How to Run

1. Run the default test matrix (v1, v2, v3) on multiple nodes:

```
python main.py
```

2. Run specific kernel versions:

```
python main.py v1 v2
```

3. Output will show:

* Node reservation and release
* Firmware flashing and PXE boot
* Test results (NCCL bandwidth, RDMA latency)
* Regression detection messages

---


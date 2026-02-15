"""
simulates hardware provisioning
fake nodes, pxe boot, bmc control
"""

import time
import random

NODES = {
    "node-01": {"status": "available"},
    "node-02": {"status": "available"},
    "node-03": {"status": "available"}
}

def reserve_node():
    """
    simulating reserving a node from pool
    irl ci would talk to bmc/ redfish to lock the node
    """

    available_nodes = [name for name, info in NODES.items() if info["status"] == "available"]
    if not available_nodes:
        print("no nodes available, waiting..")
        time.sleep(1)
        return reserve_node()
    node = random.choice(available_nodes)
    NODES[node]["status"] = "reserved"
    print(f"reserved node: {node}")
    return node

def release_node(node):
    NODES[node]["status"] = "available"
    print(f"released node: {node}")

def pxe_boot(node, kernel_version):
    print(f"{node}: pxe booting kernel {kernel_version}")
    time.sleep(0.5)
    print("booted")

def flash_firmware(node):
    print(f"{node}: flashing firmware")
    time.sleep(0.5)
    print("firmware updated")

from kernel import Kernel
from tests import run_all_tests
from validate import check_regression
import sys
from provision import reserve_node, release_node, pxe_boot, flash_firmware

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <kernel_version>")
        sys.exit(1)

    kernel_version = sys.argv[1]

    node = reserve_node()
    try:
        flash_firmware(node)
        pxe_boot(node, kernel_version)

        kernel = Kernel(kernel_version)
        print(f"testing kernel version: {kernel_version}")

        results = run_all_tests(kernel)
        regression, messages = check_regression(results)

        for r in results:
            print(f"{r['test']}: {r['value']} {r['unit']}")

        if regression:
            print("regression detected! blocking release")
            for msg in messages:
                print(msg)
            sys.exit(1)

        else:
            print("all tests passed")
            sys.exit(0)
    finally:
        release_node(node)

if __name__ == "__main__":
    main()
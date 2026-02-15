# this file simulates a kernel build artifact
# irl this would be a complicated linux kernel
# here we only care about version and expected behavior

class Kernel:
    def __init__(self, version: str):
        self.version = version

        # metadata to store prop
        self.metadata = self._load_metadata()

    def _load_metadata(self):
        """
        it simulates known behaviour of different kernel versions
        like knowledge gathered from prev test runs
        """

        if self.version == "v1":
            return {
                "nccl_bandwidth": 100, # in gb/s , good
                "rdma_latency": 10 # in micro seconds
            }
        
        elif self.version == "v2":
            return {
                "nccl_bandwidth": 82, # regression
                "rdma_latency": 14 # in micro seconds
            }
        
        else:
            # unknown kernel gets default value
            return {
                "nccl_bandwidth": 90, 
                "rdma_latency": 12 
            }
        
    def info(self):
        """
        returns human readable info about the kernel
        mimics those ci dashboards
        """
        return {
            "version": self.version,
            "metadata": self.metadata
        }
        

k1 = Kernel("v1")
k2 = Kernel("v2")

print(k1.info())
print(k2.info())
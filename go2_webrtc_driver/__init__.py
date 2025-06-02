# Monkey-patch aiortc.rtcdtlstransport.X509_DIGEST_ALGORITHMS to remove extra SHA algorithms
# This causes Unity Go2 to use a newer syntax, which is not compatible with the current aiortc version.


# Monkey-patch aioice.Connection to use a fixed username and password

import aioice


class Connection(aioice.Connection):
    local_username = aioice.utils.random_string(4)
    local_password = aioice.utils.random_string(22)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.local_username = Connection.local_username
        self.local_password = Connection.local_password


aioice.Connection = Connection  # type: ignore


import aiortc
from packaging.version import Version


if Version(aiortc.__version__) == Version("1.10.0"):
    X509_DIGEST_ALGORITHMS = {
        "sha-256": "SHA256",
    }
    aiortc.rtcdtlstransport.X509_DIGEST_ALGORITHMS = X509_DIGEST_ALGORITHMS

elif Version(aiortc.__version__) >= Version("1.11.0"):
    from cryptography.hazmat.primitives import hashes

    X509_DIGEST_ALGORITHMS = {
        "sha-256": hashes.SHA256(),  # type: ignore
    }
    aiortc.rtcdtlstransport.X509_DIGEST_ALGORITHMS = X509_DIGEST_ALGORITHMS

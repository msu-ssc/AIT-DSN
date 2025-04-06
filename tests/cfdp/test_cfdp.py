raise RuntimeError(f"This test is not working yet! Do what it says in README.md.")

import os
from pathlib import Path

ait_root_path = Path(__file__).parent
config_yaml_path = ait_root_path / "config.yaml"
os.environ["AIT_ROOT"] = str(ait_root_path)
os.environ["AIT_CONFIG"] = str(config_yaml_path)

print(f"{ait_root_path=}")
print(f"{config_yaml_path=}")

print(f"{os.environ['AIT_ROOT']=}")
print(f"{os.environ['AIT_CONFIG']=}")

import ait.core  # noqa: E402

print(f"{ait.core=}")

import ait.dsn

print(f"{ait.dsn=}")

from ait.dsn import cfdp
from ait.dsn.cfdp import primitives

print(f"{cfdp=}")

print(f"{primitives=}")
print(f"{primitives.TransmissionMode=}")

import ait.core  # noqa: E402
from ait.core import cfg
import shutil

ait_config = cfg.AitConfig()

path_keys = [
    "dsn.cfdp.datasink.incoming.path",
    "dsn.cfdp.datasink.outgoing.path",
    "dsn.cfdp.datasink.pdusink.path",
    "dsn.cfdp.datasink.tempfiles.path",
    "dsn.cfdp.mib.path",
]

paths = [Path(ait_config.get(path_key)) for path_key in path_keys if ait_config.get(path_key) is not None]
print(f"{paths=}")
# print(f"{ait_config=}")

# for path_key in path_keys:
#     path = ait_config.get(path_key)
#     print(f"{path_key=}")
#     print(f"{path=}")
#     print(f"{type(path)=}")
#     # print(f"{Path(path).exists()=}")
#     # print(f"{Path(path).is_dir()=}")
#     # print(f"{Path(path).is_file()=}")
#     # print(f"{Path(path).is_symlink()=}")

for path in paths:
    if not path.exists():
        print(f"Creating directory {path}")
        path.mkdir(parents=True, exist_ok=True)
    # else:
    #     print(f"Directory {path} already exists")
    #     for item in path.iterdir():
    #         if item.is_file():
    #             print(f"Deleting file {item}")
    #             item.unlink()
    #         elif item.is_dir():
    #             print(f"Deleting directory {item}")
    #             shutil.rmtree(item)

cfdp_entity = cfdp.CFDP(1)
print(f"{cfdp_entity=}")

cfdp_entity.connect(('127.0.0.1', 9001), send_host=("127.0.0.1", 9002))
print(f"{cfdp_entity=}")

cfdp_entity.put(2, 'sample.txt', 'sample.txt', transmission_mode=primitives.TransmissionMode.NO_ACK)

import time
time.sleep(3)
cfdp_entity.disconnect()
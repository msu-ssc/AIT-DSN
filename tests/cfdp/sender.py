# This is a barely modified version of
# `ait/dsn/bin/ait_cfdp_start_sender.py`

import os
import sys
from pathlib import Path
root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(root_dir))

os.environ['AIT_ROOT'] = str(root_dir)
os.environ['AIT_CONFIG'] = str(root_dir / "tests/cfdp/config.yaml")

print(root_dir)
print(f"{os.environ['AIT_ROOT']=}")
print(f"{os.environ['AIT_CONFIG']=}")

import ait.dsn.cfdp
import gevent
import traceback

from ait.dsn.cfdp.primitives import TransmissionMode
import ait.core.log

from common import parse_args

if __name__ == '__main__':
    args = parse_args()
    from pprint import pprint
    pprint(args.__dict__)

    cfdp = ait.dsn.cfdp.CFDP(args.sender_entity)
    try:
        sender_addr = (args.sender_host, args.sender_port)
        receiver_addr = (args.receiver_host, args.receiver_port)
        cfdp.connect(sender_addr, send_host=receiver_addr)

        destination_id = args.receiver_entity
        source_file = args.sender_file
        destination_file = args.receiver_file
        cfdp.put(destination_id, source_file, destination_file, transmission_mode=TransmissionMode.NO_ACK)
        while True:
            # ait.core.log.info('Sleeping...')
            gevent.sleep(1)
    except KeyboardInterrupt:
        print('Disconnecting...')
    except Exception as e:
        print(traceback.print_exc())
    finally:
        cfdp.disconnect()

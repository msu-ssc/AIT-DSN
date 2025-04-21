# This is a barely modified version of
# `ait/dsn/bin/ait_cfdp_start_receiver`

import os
import sys
from pathlib import Path

# import ait.dsn.cfdp.machines
# import ait.dsn.cfdp.machines.machine
root_dir = Path(__file__).resolve().parent.parent.parent
print(f"root_dir: {root_dir}")
sys.path.insert(0, str(root_dir))
os.environ["AIT_ROOT"] = str(root_dir)
os.environ["AIT_CONFIG"] = str(root_dir / "tests/cfdp/config.yaml")

print(root_dir)
print(f"{os.environ['AIT_ROOT']=}")
print(f"{os.environ['AIT_CONFIG']=}")

import ait.dsn.cfdp
import gevent
import traceback

import ait.core.log

from common import parse_args


def main(args):
    from pprint import pprint

    pprint(args.__dict__)
    cfdp = ait.dsn.cfdp.CFDP(args.receiver_entity)
    # ait.core.log.logger.setLevel("DEBUG")
    try:
        receiver_addr = (args.receiver_host, args.receiver_port)
        sender_addr = (args.sender_host, args.sender_port)

        cfdp.connect(receiver_addr, send_host=sender_addr)
        while True:
            # ait.core.log.info('Sleeping...')
            gevent.sleep(1)
    except KeyboardInterrupt:
        print("Disconnecting...")
    except Exception:
        print(traceback.print_exc())
    finally:
        cfdp.disconnect()


if __name__ == "__main__":
    args = parse_args()
    if args.profile:
        from cProfile import Profile
        from pstats import Stats

        with Profile() as profile:
            main(args)
        stats = Stats(profile)
        stats.sort_stats("cumulative")
        stats.print_stats(50)
        stats.dump_stats("cfdp_receiver_profile.prof")
    else:
        main(args)

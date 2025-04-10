import argparse
import sys

def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    args = args or sys.argv[1:]
    parser = argparse.ArgumentParser(description='CFDP Sender')
    parser.add_argument('--sender-entity', type=int, required=False, default=1)
    parser.add_argument('--receiver-entity', type=int, required=False, default=2)
    parser.add_argument('--sender-port', type=int, required=False, default=8003)
    parser.add_argument('--receiver-port', type=int, required=False, default=8002)
    parser.add_argument('--sender-host', type=str, required=False, default='localhost')
    parser.add_argument('--receiver-host', type=str, required=False, default='localhost')
    parser.add_argument('--sender-file', type=str, required=False, default="00001024.txt", help='Source file to send (relative to datasink/outgoing)')
    parser.add_argument('--receiver-file', type=str, required=False, default="output.txt", help='Destination file path (relative to datasink/incoming)')
    parser.add_argument('--reps', type=int, required=False, default=1, help='Destination file path (relative to datasink/incoming)')
    return parser.parse_args(args)

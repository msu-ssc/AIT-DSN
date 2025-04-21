import argparse
from pathlib import Path
import sys


def setup_environment():
    pass


def create_file(
    *,
    size: int,
    path: Path,
    fill: bytes | None = None,
) -> Path:
    if size % 8 != 0:
        raise ValueError("Size must be a multiple of 8")

    fill = fill or b"CFDP!!!\n"
    if size % len(fill) != 0:
        raise ValueError(f"Size must be a multiple of fill length. Fill length is {len(fill)}, size is {size}.")

    if not path:
        path = Path("data.txt")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Creating file {path} of size {size} bytes")
    with open(path, "wb") as f:
        for _ in range(size // len(fill)):
            f.write(fill)
    return path


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    args = args or sys.argv[1:]
    parser = argparse.ArgumentParser(description="CFDP Sender")
    parser.add_argument("--sender-entity", type=int, required=False, default=1)
    parser.add_argument("--receiver-entity", type=int, required=False, default=2)
    parser.add_argument("--sender-port", type=int, required=False, default=8003)
    parser.add_argument("--receiver-port", type=int, required=False, default=8002)
    parser.add_argument("--sender-host", type=str, required=False, default="localhost")
    parser.add_argument("--receiver-host", type=str, required=False, default="localhost")
    # parser.add_argument("--sender-file", type=str, required=False, default="00001024.txt", help="Source file to send (relative to datasink/outgoing)")
    # parser.add_argument("--receiver-file", type=str, required=False, default="output.txt", help="Destination file path (relative to datasink/incoming)")
    parser.add_argument("--reps", type=int, required=False, default=1, help="Destination file path (relative to datasink/incoming)")
    parser.add_argument("--file-size", type=int, required=False, default=64, help="Size of the file (in byte) to create and send")
    parser.add_argument("--file-fill", type=str, required=False, default="CFDP!!!\n", help="ASCII text to be sent")
    parser.add_argument("--profile", action="store_true", required=False, help="Enable profiling for the CFDP Sender")
    parser.add_argument("--cfdp-class", type=int, required=False, default=1, help="CFDP class to use. 1=NO_ACK, 2=ACK")

    return parser.parse_args(args)

if __name__ == "__main__":
    print(create_file(size=1024, path="./example.txt"))

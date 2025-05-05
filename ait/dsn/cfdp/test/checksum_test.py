from collections import defaultdict
from pathlib import Path
import random
import shutil
import tempfile
import time

rand = random.Random(40351)

temp_folder = Path(tempfile.mkdtemp())

print(f"Temporary folder: {temp_folder}")


def run_tests():
    print(f"Creating test files in: {temp_folder}")
    for byte in [
        0x00,
        0x55,
        0xFF,
        "random",
    ]:
        for size in [
            0,
            1,
            10,
            100,
            1000,
            10000,
            100000,
            # 1000000,
            # 10000000,
            # 100000000,
            # 1000000000,
        ]:
            if byte == "random":
                file_path = temp_folder / f"file-random-{size:_}.bin"
                if size < 1_000_000_000:
                    with open(file_path, "wb") as f:
                        f.write(rand.randbytes(size))
                else:
                    with open(file_path, "wb") as f:
                        for _ in range(size // 1_000_000):
                            f.write(rand.randbytes(1_000_000))
                    # Write the remaining bytes
                    remaining_bytes = size % 1_000_000
                    if remaining_bytes > 0:
                        with open(file_path, "ab") as f:
                            f.write(rand.randbytes(remaining_bytes))
            else:
                file_path = temp_folder / f"file-{byte:02x}-{size:_}.bin"
                with open(file_path, "wb") as f:
                    f.write(bytes((byte,)) * size)
            print(f"Test file created: {file_path}")

    print(f"Done creating test files in: {temp_folder}")

    from ait.dsn.cfdp import util

    print(f"{util=}")

    paths = sorted(temp_folder.glob("*.bin"))

    total_time_ns = defaultdict(float)
    for path in paths:
        print(f"----- {path} -----")
        # print(f"Processing file: {path}")
        checksums = []
        for function in [
            # util.calc_checksum_buffered,
            util._calc_checksum_struct,
            util._calc_checksum_legacy,
        ]:
            start = time.monotonic_ns()
            checksum = function(path)
            checksums.append(checksum)
            end = time.monotonic_ns()
            total_time_ns[function.__name__] += (end - start)
            print(f"  {function.__name__}: {(end-start) // 1_000_000:_} ms")

            checksums_good = len(set(checksums)) == 1
            if checksums_good:
                print(f"  Checksums match: {checksum:_}")
            else:
                print(f"  !!!!! Checksum mismatch !!!!!: {checksums}")
                raise RuntimeError(f"Checksum mismatch for {path}: {checksums}")
            # assert len(set(checksums)) == 1, f"Checksum mismatch for {path} using {function.__name__}: {checksums}"

    from pprint import pprint
    pprint("Total time taken for each function:")
    print(f"No errors across {len(paths)} files")
    pprint(total_time_ns)

if __name__ == "__main__":
    try:
        run_tests()
    except Exception as e:
        print(f"Error during tests: {e}")
        raise
    finally:
        shutil.rmtree(temp_folder)
        print(f"Temporary folder and its contents removed: {temp_folder}")

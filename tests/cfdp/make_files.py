from pathlib import Path


path = Path("tests/cfdp/temp/datasink/outgoing")
path.mkdir(parents=True, exist_ok=True)

for size in [
    0,
    # 8,
    16,
    32,
    64,
    128,
    256 - 16,
    256,
    512,
    1024,
    2048,
    4096 - 16,
    4096,
    8192,
    16384,
    32768,
    65536,
    1 << 18, # 262144
    1 << 19, # 524288
    1 << 24, # 16_777_216
    # 1 << 25, # 33_554_432
    # 1 << 26, # 67_108_864
    1 << 27, # 134_217_728
    # 1 << 28, # 268_435_456
    1 << 29, # 536_870_912
    # 1 << 30, # 1_073_741_824
    # 1 << 31, # 2_147_483_648

]:
    # Create a test file with the specified size
    column_width = 16
    name = f"{size}".zfill(8) + ".txt"
    with open(path / name, "wb") as f:
        text = f"{str(size).zfill(column_width - 1)}\n"
        assert size % len(text) == 0, (
            f"File size {size} is not a multiple of {len(text)}"
        )
        assert size % 8 == 0, f"File size {size} is not a multiple of 8"
        for _ in range(size // len(text)):
            f.write(text.encode(encoding="ascii"))

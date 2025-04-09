from pathlib import Path


path = Path("tests/cfdp/temp/datasink/outgoing")
path.mkdir(parents=True, exist_ok=True)

for size in [0, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]:
    # Create a test file with the specified size
    name = f"{size}".zfill(8) + ".txt"
    with open(path / name, 'wb') as f:
        text = f"{str(size).zfill(7)}\n"
        assert size % len(text) == 0, f"File size {size} is not a multiple of {len(text)}"
        assert size % 8 == 0, f"File size {size} is not a multiple of 8"
        for _ in range(size // len(text)):
            f.write(text.encode(encoding="ascii"))
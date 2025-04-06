# How to make class 1 work

(Tested only in Ubuntu. I think it would work in Windows, not sure.)

## Wireshark
1. Open Wireshark
2. Capture on loopback
3. Filter to `udp&&udp.port in {8000, 8001, 8002}`

## env vars:

```bash
# In project root directory:
export AIT_ROOT="${PWD}"    # Or set this manually
export AIT_CONFIG="${AIT_CONFIG}/tests/cfdp/config.yaml"
export PYTHONPATH="${AIT_ROOT}:${PYTHONPATH}"
```

## uv
```bash
# Primary purpose of this is to create a VENV with the dependencies.
# This probably isn't even necessary?
cd $AIT_ROOT
uv sync
```

## Receive (terminal #1) (Must be done first)
```bash
cd $AIT_ROOT
# NOTE: This is NOT a typo. There is no `.py` at the end.
uv run python ./ait/dsn/bin/ait_cfdp_start_receiver
```

## Send (terminal #2) (Must be done second)
```bash
cd $AIT_ROOT
uv run python ./ait/dsn/bin/ait_cfdp_start_sender.py
```

## Send more files:
1. Kill the process in BOTH terminals with `CTRL-C` or `CTRL-Z`.
2. Restart both terminals (1 first, then 2)

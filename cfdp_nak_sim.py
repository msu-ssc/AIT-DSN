import random


UPLINK_DATA_RATE = 2 * 1024  # 2 Kbps
DOWNLINK_DATA_RATE = 256 * 1024  # 256 Kbps
PDU_SIZE = 4096 * 8  # 4096 bytes
# TODO: Account for the fact that METADATA/EOF/NAK/ACK PDUs are smaller than DATA PDUs

UPLINK_LATENCY = 1.35  # 1.35 seconds
DOWNLINK_LATENCY = 1.35  # 1.35 seconds
ROUND_TRIP_LATENCY = UPLINK_LATENCY + DOWNLINK_LATENCY

UPLINK_PDU_TIME = PDU_SIZE / UPLINK_DATA_RATE
DOWNLINK_PDU_TIME = PDU_SIZE / DOWNLINK_DATA_RATE

print(f"UPLINK_PDU_TIME: {UPLINK_PDU_TIME} seconds")
print(f"DOWNLINK_PDU_TIME: {DOWNLINK_PDU_TIME} seconds")
print(f"UPLINK_LATENCY: {UPLINK_LATENCY} seconds")
print(f"DOWNLINK_LATENCY: {DOWNLINK_LATENCY} seconds")
print(f"ROUND_TRIP_LATENCY: {ROUND_TRIP_LATENCY} seconds")


class CFDP_NAK_Simulator:
    def __init__(
        self,
        *,
        uplink_data_rate: int = UPLINK_DATA_RATE,
        downlink_data_rate: int = DOWNLINK_DATA_RATE,
        uplink_latency: float = UPLINK_LATENCY,
        downlink_latency: float = DOWNLINK_LATENCY,
        pdu_size: int = PDU_SIZE,
        rand: random.Random | None = None,
        pdu_failure_rate: float = 0.0,
    ):
        self.uplink_data_rate = uplink_data_rate
        self.downlink_data_rate = downlink_data_rate
        self.uplink_latency = uplink_latency
        self.downlink_latency = downlink_latency
        self.pdu_size = pdu_size
        self.rand = rand or random.Random()

    def simulate_deferred(
        self,
        pdu_count: int,
        direction: str = "uplink",
    ):
        # Send all PDUs

        pass

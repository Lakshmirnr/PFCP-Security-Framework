from dataclasses import dataclass
from typing import Optional
import struct

PFCP_PORT = 8805

@dataclass
class PFCPRecord:
    timestamp: float
    src: str
    dst: str
    message_type: Optional[int]
    sequence: Optional[int]
    seid: Optional[int]
    length: int
    raw: bytes


def parse_pfcp_payload(payload: bytes, timestamp: float, src: str, dst: str) -> Optional[PFCPRecord]:
    if len(payload) < 8:
        return None
    # PFCP header: flags, message type, length; optional SEID follows for S-flag messages.
    flags = payload[0]
    msg_type = payload[1]
    declared_len = struct.unpack("!H", payload[2:4])[0]
    has_seid = bool(flags & 0x01)
    offset = 4
    seid = None
    if has_seid:
        if len(payload) < 16:
            return None
        seid = struct.unpack("!Q", payload[4:12])[0]
        offset = 12
    if len(payload) < offset + 4:
        return None
    sequence = int.from_bytes(payload[offset:offset + 3], "big")
    return PFCPRecord(timestamp, src, dst, msg_type, sequence, seid, declared_len, payload)

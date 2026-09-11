# PFCP Attacks and NWDAF-Based Detection in 5G Core Networks

Research artifact for the experimental study of **PFCP/N4 security in 5G Core Networks**. The repository organizes four PFCP attack scenarios and a customized **Network Data Analytics Function (NWDAF)** detection framework.


## Attacks Discovered


| Attack | Security effect | Detection focus |
|---|---|---|
| PFCP Session Flooding | Control-plane overload and session setup failures | Per-SEID message rate and malformed-packet thresholds |
| PFCP Coordinated Fragmentation | Memory exhaustion and session disruption | Fragment order, offsets, MF flags and reassembly behavior |
| PFCP Delayed Fragmentation | UPF responsiveness degradation and routing errors | Fragment timing, missing/delayed fragments and IE consistency |
| PFCP Session Hijacking | Unauthorized session termination and traffic redirection | SEID–TEID correlation and session-state anomalies |

The flooding vulnerability was reported through responsible disclosure and assigned **CVE-2024-51179**. The fragmentation scenarios correspond to Open5GS issue #3689, while the session-hijacking scenario corresponds to issue #3693.

## NWDAF detection framework

The customized NWDAF monitors PFCP signaling exposed from the SMF/UPF side of the N4 interface. It extracts protocol/session information, maintains traffic and session state, applies threshold-based anomaly rules, records alerts, and exposes the resulting analytics through a REST-oriented interface.

The implemented detection logic covers:

- per-SEID PFCP message-rate anomalies;
- malformed PFCP indicators including SEID, checksum, message type and sequence checks;
- fragment ordering, offsets, MF flags, timing and reassembly anomalies;
- FAR/TFT consistency during fragmented-message processing; and
- unexpected SEID–TEID relationships and repeated/abnormal session deletion activity.

## Repository layout

```text
PFCP-Security-Framework/
├── attacks/
│   ├── pfcp-coordinated-fragmentation/
│   ├── pfcp-delayed-fragmentation/
│   ├── pfcp-session-flooding/
│   └── pfcp-session-hijacking/
├── configs/
│   └── testbed-setup.md
├── nwdaf_based_detection/
│   ├── detector.py
│   ├── integration_analyticsid.py
│   ├── pfcp_parser.py
│   └── README.md
├── pfcp_dataset/
│   ├── coordinated_fragmentation_attack
│   ├── delayed_fragmentation_attack
│   ├── pfcp_session_hijacking_teid_imsi
│   └── pfcp_session_modification_flooding
├── requirements.txt
├── LICENSE
└── README.md
```

## Testbed

The documented experimental platform uses Ubuntu 22.04, Open5GS 2.7.1, UERANSIM, and an isolated multi-VM 5G Core topology. See [`https://github.com/Lakshmirnr/PFCP-Security-Framework/blob/main/configs/testbed-setup.md).

## Detection prototype

The supplied detector supports **offline PCAP analysis** so that the analytics logic can be validated without transmitting attack traffic. Install dependencies and run:

```bash
python3 -m pip install -r requirements.txt
python3 nwdaf-detection/detector.py --pcap <capture.pcap> --output alerts.json
```

For live deployment, connect the parser to the authorized N4 capture point and retain the same feature-extraction and alerting logic.

## Alert format

A representative alert contains the event type, timestamp, SEID, anomaly count and severity. Example:

```json
{
  "event": "PFCP_Flooding",
  "timestamp": "2025-01-05T12:34:56Z",
  "seid": "0x1A2B3C4D5E6F7890",
  "message_count": 120,
  "threshold": 100,
  "severity": "High"
}
```

## Responsible disclosure references

* [Open5GS issue #3497](https://github.com/open5gs/open5gs/issues/3497)// [CVE Record: CVE-2024-51179](https://www.cve.org/CVERecord?id=CVE-2024-51179 — PFCP flooding 

* [Open5GS issue #3689](https://github.com/open5gs/open5gs/issues/3689) — PFCP fragmentation (Coordinated & Delayed Fragmentation Attacks)
* [Open5GS issue #3693](https://github.com/open5gs/open5gs/issues/3693) — PFCP session hijacking




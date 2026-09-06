# NWDAF-Based PFCP Attack Detection

This directory contains the passive PFCP parser and anomaly-detection prototype used to demonstrate the customized NWDAF analytics path.

## Detection logic

### Flooding
A rolling window maintains PFCP message counts per SEID. A flooding event is raised when the count exceeds the configured threshold.

### Malformed packets
The detector checks basic PFCP structural properties and maintains a per-SEID malformed-packet counter. Repeated violations are escalated as a protocol anomaly.

### Fragmentation
Fragmentation analysis is represented as a separate analytics stage in the research design. The relevant features are fragment sequence/order, offsets, MF flags, inter-arrival times, missing fragments, reassembly failures, and consistency of critical IEs such as FAR/TFT.

### Session hijacking
The session-state stage correlates SEIDs and TEIDs and evaluates deletion/control messages against the active-session state. Unexpected reassignment, inconsistent associations, and repeated targeting are treated as suspicious indicators.

## Offline execution

```bash
python3 detector.py --pcap ../experiments/example.pcap --output alerts.json
```

The detector is passive and does not transmit PFCP traffic.

# Custom NWDAF Module — PFCP Anomaly Detection

## Description
A customized NWDAF module implemented in Python, extending the standard NWDAF data collection path to capture and analyze PFCP signalling over the N4 interface (SMF–UPF), in addition to the conventional `Nsmf_EventExposure` and `Nupf_EventExposure` service-based interfaces.

## Components
- `pfcp_parser.py` — Scapy-based inline packet capture and PFCP message parser.
- `detector.py` — Feature extraction and anomaly detection logic over the parsed PFCP stream.

## How It Works
1. Inline packet capture is performed on the SMF/UPF host's N4-facing network interface.
2. Captured PFCP messages (Session Establishment/Modification/Deletion, Association messages, etc.) are parsed and relevant features extracted.
3. A baseline of benign traffic is established (30 minutes), and detection thresholds are statistically derived from this baseline.
4. Detection is performed continuously using a 10-second sliding window over live PFCP traffic.
5. Detected anomalies are exposed via a custom, security-focused Analytics ID (`[TODO: Analytics ID name]`) through the standard `Nnwdaf_AnalyticsInfo` / `Nnwdaf_EventsSubscription` service interfaces.

## Running the Detector
```bash
python3 pfcp_parser.py --iface <N4-facing interface>
python3 detector.py --baseline-duration 1800 --window 10
```

## Resource Footprint
The NWDAF module was integrated within the Open5GS core VM and shares its allocated compute resources (no dedicated CPU/memory quota was required). See [`../docs/testbed-setup.md`](../docs/testbed-setup.md) for full testbed specifications.

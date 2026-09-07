# PFCP Signalling Anomaly Analytics for NWDAF

## Overview

This module extends a customized 5G Network Data Analytics Function (NWDAF) with security analytics for Packet Forwarding Control Protocol (PFCP) signalling.

The implementation introduces the custom Analytics ID:

```text
PFCP_Signalling_Anomaly
```

The module monitors PFCP signalling exchanged between the Session Management Function (SMF) and User Plane Function (UPF) over the N4 interface. PFCP traffic is collected using a Python/Scapy-based packet collection module and processed to extract traffic-level features for anomaly detection.

The resulting analytics can be integrated with the NWDAF service framework through the `Nnwdaf_AnalyticsInfo` and `Nnwdaf_EventsSubscription` procedures.

## Architecture

```text
             5G Core Network

        +-------------+
        |     SMF     |
        +------+------+ 
               |
          N4 / PFCP
          UDP : 8805
               |
        +------v------+
        |     UPF     |
        +-------------+
               |
               | PFCP traffic collection
               v
        +---------------+
        | Python / Scapy|
        | Packet Capture|
        +-------+-------+
                |
                v
        +---------------+
        | PFCP Parser   |
        +-------+-------+
                |
                v
        +---------------+
        |Feature         |
        |Extraction      |
        +-------+-------+
                |
                v
        +---------------+
        | Anomaly       |
        | Detection     |
        +-------+-------+
                |
                v
    PFCP_Signalling_Anomaly
                |
       +--------+--------+
       |                 |
       v                 v
Nnwdaf_AnalyticsInfo   Nnwdaf_EventsSubscription
```

## Custom Analytics ID

The module defines:

```text
PFCP_Signalling_Anomaly
```

This Analytics ID represents security-oriented analytics for PFCP signalling behaviour.

It is an implementation-specific/custom Analytics ID and is not claimed to be a standardized 3GPP Analytics ID.

## PFCP Data Collection

PFCP signalling between the SMF and UPF is exchanged over the N4 interface using UDP port `8805`.

The customized NWDAF uses Scapy to capture the relevant traffic:

```python
sniff(
    filter="udp port 8805",
    prn=process_pfcp,
    store=False
)
```

The captured messages are passed to the PFCP parsing and feature-extraction stages.

## Detection Process

### 1. Baseline establishment

Benign PFCP traffic is collected for 30 minutes to establish the normal operating profile.

### 2. Real-time monitoring

After baseline establishment, PFCP traffic is analyzed using a 10-second detection window.

The detection procedure continuously evaluates incoming PFCP traffic and generates an analytics result associated with:

```text
PFCP_Signalling_Anomaly
```

## Example Analytics Result

```text
Analytics ID : PFCP_Signalling_Anomaly
Status       : ANOMALOUS
Message Rate : 51.80 msg/s
```

The analytics response can be extended with additional PFCP features such as:

- PFCP message type
- Message rate
- Sequence number behaviour
- Session Endpoint Identifier (SEID)
- Information Element (IE) characteristics
- Source and destination information
- Packet size
- Request/response behaviour
- Fragmentation-related characteristics

## Installation

Install Python 3 and Scapy:

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install scapy
```

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_DIRECTORY>
```

## Running the Module

Run the PFCP analytics module with the required packet-capture privileges:

```bash
sudo python3 pfcp_signalling_anomaly.py
```

Example output:

```text
==========================================
 Customized NWDAF - PFCP Security Module
==========================================

[INFO] Analytics ID: PFCP_Signalling_Anomaly
[INFO] Collecting benign PFCP traffic...
[INFO] Baseline duration: 1800 seconds

[INFO] Baseline established
[INFO] Starting real-time PFCP monitoring
[INFO] Detection window: 10 seconds

--------------------------------
Analytics ID : PFCP_Signalling_Anomaly
Status       : NORMAL
Messages     : 124
Message Rate : 12.40 msg/s
--------------------------------
```

## Configuration

```python
ANALYTICS_ID = "PFCP_Signalling_Anomaly"
PFCP_PORT = 8805
BASELINE_DURATION = 30 * 60
DETECTION_WINDOW = 10
```

These values can be modified according to the experimental deployment.

## 3GPP Alignment

The implementation is designed around the 3GPP NWDAF architecture and PFCP operation in the 5G Core.

- **3GPP TS 23.288** — Architecture and procedures for NWDAF analytics
- **3GPP TS 29.244** — PFCP specification and N4 interface
- **N4** — PFCP signalling interface between SMF and UPF
- **Nnwdaf_AnalyticsInfo** — NWDAF analytics information service
- **Nnwdaf_EventsSubscription** — NWDAF analytics event subscription service

The custom Analytics ID extends the NWDAF analytics framework to support PFCP-specific security analysis.


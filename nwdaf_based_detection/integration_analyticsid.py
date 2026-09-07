#!/usr/bin/env python3

"""
PFCP Signalling Anomaly Analytics for NWDAF

Python/Scapy-based reference implementation for collecting PFCP
signalling traffic over the N4 interface and generating anomaly
analytics using the custom Analytics ID:

    PFCP_Signalling_Anomaly
"""

from scapy.all import sniff, IP
import statistics
import time


# ============================================================
# Configuration
# ============================================================

ANALYTICS_ID = "PFCP_Signalling_Anomaly"
PFCP_PORT = 8805

BASELINE_DURATION = 30 * 60
DETECTION_WINDOW = 10


# ============================================================
# PFCP Packet Collection
# ============================================================

def collect_pfcp_packets(duration):
    """Capture PFCP packets exchanged over the N4 interface."""

    packets = sniff(
        filter=f"udp port {PFCP_PORT}",
        timeout=duration,
        store=True
    )

    return packets


# ============================================================
# Feature Extraction
# ============================================================

def extract_features(packets):
    """Extract basic traffic-level features."""

    message_count = len(packets)

    if message_count == 0:
        return {
            "message_count": 0,
            "message_rate": 0.0,
            "average_packet_size": 0.0
        }

    packet_sizes = [
        len(packet)
        for packet in packets
        if IP in packet
    ]

    average_packet_size = (
        statistics.mean(packet_sizes)
        if packet_sizes else 0.0
    )

    message_rate = message_count / DETECTION_WINDOW

    return {
        "message_count": message_count,
        "message_rate": message_rate,
        "average_packet_size": average_packet_size
    }


# ============================================================
# Baseline Establishment
# ============================================================

def establish_baseline():
    """Collect benign PFCP traffic and establish a threshold."""

    print(f"[INFO] Analytics ID: {ANALYTICS_ID}")
    print("[INFO] Collecting benign PFCP traffic...")
    print(
        f"[INFO] Baseline duration: "
        f"{BASELINE_DURATION} seconds"
    )

    packets = collect_pfcp_packets(BASELINE_DURATION)

    if not packets:
        print("[WARNING] No PFCP packets captured.")
        return 0.0

    baseline_rate = len(packets) / BASELINE_DURATION

    # Initial reference threshold.
    # Replace with the statistical thresholding method
    # used by the complete NWDAF implementation.
    threshold = baseline_rate * 3

    print("[INFO] Baseline established")
    print(
        f"[INFO] Baseline message rate: "
        f"{baseline_rate:.2f} msg/s"
    )
    print(
        f"[INFO] Detection threshold: "
        f"{threshold:.2f} msg/s"
    )

    return threshold


# ============================================================
# Anomaly Detection
# ============================================================

def detect_anomaly(features, threshold):
    """Evaluate the current PFCP traffic."""

    message_rate = features["message_rate"]

    status = (
        "ANOMALOUS"
        if message_rate > threshold
        else "NORMAL"
    )

    return {
        "analytics_id": ANALYTICS_ID,
        "status": status,
        "message_count": features["message_count"],
        "message_rate": message_rate,
        "average_packet_size":
            features["average_packet_size"]
    }


# ============================================================
# Analytics Output
# ============================================================

def publish_analytics(result):
    """Display the generated NWDAF analytics result."""

    print("\n--------------------------------")
    print(f"Analytics ID : {result['analytics_id']}")
    print(f"Status       : {result['status']}")
    print(f"Messages     : {result['message_count']}")
    print(
        f"Message Rate : "
        f"{result['message_rate']:.2f} msg/s"
    )
    print(
        f"Avg. Size    : "
        f"{result['average_packet_size']:.2f} bytes"
    )
    print("--------------------------------")


# ============================================================
# Continuous Monitoring
# ============================================================

def monitor_pfcp(threshold):
    """Continuously monitor PFCP traffic."""

    print("[INFO] Starting real-time PFCP monitoring")
    print(
        f"[INFO] Detection window: "
        f"{DETECTION_WINDOW} seconds"
    )

    while True:

        packets = collect_pfcp_packets(DETECTION_WINDOW)

        features = extract_features(packets)

        result = detect_anomaly(
            features,
            threshold
        )

        publish_analytics(result)

        time.sleep(0.1)


# ============================================================
# Main
# ============================================================

def main():

    print("==========================================")
    print(" Customized NWDAF - PFCP Security Module")
    print("==========================================")

    threshold = establish_baseline()

    if threshold <= 0:
        print(
            "[ERROR] Unable to establish a valid "
            "PFCP baseline."
        )
        return

    monitor_pfcp(threshold)


if __name__ == "__main__":
    main()

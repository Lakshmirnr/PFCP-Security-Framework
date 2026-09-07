import argparse, json, time
from collections import Counter, defaultdict, deque
from scapy.all import rdpcap, UDP, IP
from pfcp_parser import PFCP_PORT, parse_pfcp_payload


def detect(pcap_path, flooding_threshold=100, malformed_threshold=5, window=10):
    packets = rdpcap(pcap_path)
    alerts = []
    counts = Counter()
    malformed = Counter()
    recent = defaultdict(deque)
    sessions = {}

    for pkt in packets:
        if not (IP in pkt and UDP in pkt):
            continue
        if pkt[UDP].sport != PFCP_PORT and pkt[UDP].dport != PFCP_PORT:
            continue
        payload = bytes(pkt[UDP].payload)
        rec = parse_pfcp_payload(payload, float(pkt.time), pkt[IP].src, pkt[IP].dst)
        if rec is None:
            alerts.append({"event": "Malformed_PFCP", "timestamp": float(pkt.time), "severity": "Medium"})
            continue

        key = rec.seid if rec.seid is not None else "NO_SEID"
        counts[key] += 1
        q = recent[key]
        q.append(rec.timestamp)
        while q and rec.timestamp - q[0] > window:
            q.popleft()

        if len(q) > flooding_threshold:
            alerts.append({"event": "PFCP_Flooding", "timestamp": rec.timestamp,
                           "seid": key, "message_count": len(q),
                           "threshold": flooding_threshold, "severity": "High"})

        bad = False
        if rec.message_type is None or rec.sequence is None:
            bad = True
        if rec.length > len(rec.raw) - 4:
            bad = True
        if bad:
            malformed[key] += 1
            if malformed[key] > malformed_threshold:
                alerts.append({"event": "Multiple_Malformed_Packets", "timestamp": rec.timestamp,
                               "seid": key, "count": malformed[key], "severity": "High"})

        # Session-state representation used by the hijacking detector.
        if rec.seid is not None:
            sessions.setdefault(rec.seid, {"last_src": rec.src, "last_seen": rec.timestamp})
            sessions[rec.seid].update(last_src=rec.src, last_seen=rec.timestamp)

    return alerts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pcap", required=True)
    ap.add_argument("--output", default="alerts.json")
    ap.add_argument("--flooding-threshold", type=int, default=100)
    ap.add_argument("--malformed-threshold", type=int, default=5)
    ap.add_argument("--window", type=int, default=10)
    args = ap.parse_args()
    alerts = detect(args.pcap, args.flooding_threshold, args.malformed_threshold, args.window)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump({"AnomalyDetection": {"alerts": alerts}}, f, indent=2)
    print(f"Wrote {len(alerts)} alerts to {args.output}")

if __name__ == "__main__":
    main()

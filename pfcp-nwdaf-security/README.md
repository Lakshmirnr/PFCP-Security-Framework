# PFCP Vulnerabilities and NWDAF-Based Detection in 5G Core Networks

This repository accompanies our paper submitted to **IEEE Transactions on Network and Service Management (TNSM)**, which identifies four vulnerabilities in PFCP (Packet Forwarding Control Protocol) signalling within the 5G core, and proposes an NWDAF-based detection mechanism to identify related attacks in real time.

## ⚠️ Ethics and Responsible Use Statement

All code in this repository was developed and tested **exclusively within an isolated laboratory testbed** (Open5GS + UERANSIM), with no interaction with live, production, or third-party networks. This code is released for **academic research, reproducibility, and responsible disclosure purposes only**.

**Do not use this code against any network you do not own or have explicit written authorization to test.** The authors and affiliated institution(s) assume no liability for misuse.

## Overview

- `attacks/` — Proof-of-concept scripts for each of the four identified PFCP vulnerabilities, each with its own README describing the exploit, affected messages, and expected impact.
- `nwdaf-detection/` — Custom NWDAF module (Python/Scapy-based PFCP parser + anomaly detection logic).
- `configs/` — Open5GS and UERANSIM configuration files used in the testbed.
- `figures/` — Architecture diagrams and Wireshark capture evidence referenced in the paper.
- `docs/` — Full testbed reproduction guide (hardware, software versions, network topology).

## Testbed Summary

| Component | Version / Spec |
|---|---|
| Open5GS | v2.7.1 |
| UERANSIM | TODO |
| OS | Ubuntu 22.04 |
| Host CPU | AMD Ryzen 5 7530U @ 2.0 GHz |
| Host RAM | 16 GB |

Full setup details: see [`docs/testbed-setup.md`](docs/testbed-setup.md).

## Citation

If you use this code or dataset in your work, please cite:

```bibtex
@article{TODO_bibkey,
  title   = {TODO: Paper Title},
  author  = {TODO: Author List},
  journal = {IEEE Transactions on Network and Service Management},
  year    = {2026},
  note    = {In press}
}
```

See also [`CITATION.cff`](CITATION.cff).

## License

This project is licensed under the MIT License — see [`LICENSE`](LICENSE) for details.

## Contact

For questions, responsible disclosure, or collaboration inquiries, please open an issue or contact [TODO: your email].

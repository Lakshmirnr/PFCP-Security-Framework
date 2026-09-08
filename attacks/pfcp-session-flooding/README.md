# PFCP Session Flooding

## Description
Forged PFCP Session Modification Requests can overload PFCP control-plane processing and cause session setup failures.

## Research reference
CVE-2024-51179; Open5GS issue #3497

## Detection
SEID-based message-rate thresholding and malformed-packet checks.



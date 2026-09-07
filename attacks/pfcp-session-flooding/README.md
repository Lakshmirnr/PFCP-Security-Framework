# PFCP Session Flooding

## Description
Forged PFCP Session Modification Requests can overload PFCP control-plane processing and cause session setup failures.

## Research reference
CVE-2024-51179; Open5GS issue #3497

## Detection
SEID-based message-rate thresholding and malformed-packet checks.

## Implementation status

The source archive supplied for this repository contained a placeholder  for this scenario rather than the validated experimental implementation. The placeholder is intentionally retained as a marker and must be replaced with the actual research code before public release.

## Authorized testbed only

Run attack experiments only in an isolated environment for which you have explicit authorization. Preserve sanitized PCAPs and detector logs as experimental evidence.

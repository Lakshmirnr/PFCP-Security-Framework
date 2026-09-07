# PFCP Session Hijacking

## Description
Reused TEIDs in forged control messages can interfere with active sessions, including unauthorized session termination or traffic redirection.

## Research reference
Open5GS issue #3693

## Detection
SEID-TEID correlation, session state and abnormal deletion activity.

## Implementation status

The source archive supplied for this repository contained a placeholder  for this scenario rather than the validated experimental implementation. The placeholder is intentionally retained as a marker and must be replaced with the actual research code before public release.

## Authorized testbed only

Run attack experiments only in an isolated environment for which you have explicit authorization. Preserve sanitized PCAPs and detector logs as experimental evidence.

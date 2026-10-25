# Practice 3: Windows tells its story

## Scenario

A reception workstation reports repeated failed logons. Collect useful Windows evidence without collecting everything.

## Questions

1. Heartbeat is present but SecurityEvent is empty. Is AMA proven broken?
2. Which exact evidence would support your conclusion, and which alternative explanation should be tested?
3. What access, cost or business impact must the incident lead consider?

## Answer guidance

No. The VM can send heartbeat while Security auditing, event selection, workspace mapping or channel collection is wrong. Strong answers cite an appropriate source/event ID, scope and UTC interval, distinguish observation from inference and explain one uncertainty. Award 2 marks for the core explanation, 2 for suitable evidence and 1 for a proportionate operational decision. These are original learning questions, not exam dumps.

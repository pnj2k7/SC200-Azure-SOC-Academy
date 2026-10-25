# Practice 4: The missing telemetry

## Scenario

A partner gateway and hospital application use different log formats. Bring both into the investigation with a traceable schema.

## Questions

1. Why can a successful HTTP ingestion response coexist with an empty investigation result?
2. Which exact evidence would support your conclusion, and which alternative explanation should be tested?
3. What access, cost or business impact must the incident lead consider?

## Answer guidance

Delivery is asynchronous; the query can target the wrong table/window, or transformations can filter rows. Check the DCR, stream, timestamps and ingestion errors. Strong answers cite an appropriate source/event ID, scope and UTC interval, distinguish observation from inference and explain one uncertainty. Award 2 marks for the core explanation, 2 for suitable evidence and 1 for a proportionate operational decision. These are original learning questions, not exam dumps.

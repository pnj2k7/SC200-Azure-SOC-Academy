# Practice 7: Engineer a reliable detection

## Scenario

Turn the recurring failed-sign-in pattern into a tested signal, without flooding the SOC.

## Questions

1. Why must XDR custom detection output preserve source event identifiers?
2. Which exact evidence would support your conclusion, and which alternative explanation should be tested?
3. What access, cost or business impact must the incident lead consider?

## Answer guidance

The detection service needs to associate results with real events and affected entities; a summarized query without required identifiers can be ineligible. Strong answers cite an appropriate source/event ID, scope and UTC interval, distinguish observation from inference and explain one uncertainty. Award 2 marks for the core explanation, 2 for suitable evidence and 1 for a proportionate operational decision. These are original learning questions, not exam dumps.

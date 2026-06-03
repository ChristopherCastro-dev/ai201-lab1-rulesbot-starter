# RulesBot — Planning Doc

Use this file to record your design decisions as you work through the lab.
There are no wrong answers — write enough that you could explain your reasoning to another group.

---

## Chunking Strategy

**Chunk size:** 300 characters

**Overlap:** 50 characters

**Why this strategy fits rule book text:**
Rule books pack a lot of meaning into short passages. 300 characters is long enough to hold a complete rule but short enough to stay focused on one topic. The 50-character overlap ensures rules that span chunk boundaries don't get lost. Tested 50-character chunks (too small — fragmented rules, incomplete answers) and 1000-character chunks (too large — unfocused, multiple unrelated rules per chunk).

---

## Retrieval Observations

After implementing retrieval, try these test queries and record what comes back:

| Query | Top result game | Does it make sense? |
|-------|----------------|---------------------|
| "How do you win?" |  Multiple games | Yes — winning conditions exist across all games |
| "What happens when you roll a 7?" | Catan | Yes - robber mechanic is Catan-specific |
| "Can two players share a route?" |  Ticket To Ride | Yes — route claiming is specific to that game |

**Anything surprising?**
"How do you win?" returned chunks from multiple games because winning conditions are semantically similar across all of them. That's correct behavior, not a bug.

---

## Response Quality

After implementing generation, try 2–3 questions and assess the answers:

| Query | Answer accurate? | Properly grounded? | Cited the right game? |
| How do you get out of jail in Monopoly? | Yes |Yes | Yes |
|  How does the Knight move in Chess? | Yes|Yes| Yes |
|  What happens when you run out of disease cubes in Pandemic? | Yes | Yes | Yes |

**What would you change about the prompt to improve grounding?**
The current prompt is strong, explicitly telling the model not to draw on outside knowledge keeps answers grounded. Could add an instruction to always cite the source game at the start of every answer.


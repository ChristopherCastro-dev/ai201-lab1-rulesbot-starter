from retriever import retrieve

# Question-answer pairs where we know the correct game
eval_set = [
    {"query": "What happens when you roll a 7?", "expected_game": "Catan"},
    {"query": "How do you get out of jail?", "expected_game": "Monopoly"},
    {"query": "How do you win?", "expected_game": None},  # spans multiple games
    {"query": "What happens when you run out of disease cubes?", "expected_game": "Pandemic"},
    {"query": "How does the Knight move?", "expected_game": "Chess"},
    {"query": "Can two players share a route?", "expected_game": "Ticket To Ride"},
    {"query": "How do you draw cards in Uno?", "expected_game": "Uno"},
    {"query": "How do you eliminate a suspect in Clue?", "expected_game": "Clue"},
]

passed = 0
failed = 0
failures = []

for item in eval_set:
    query = item["query"]
    expected = item["expected_game"]

    if expected is None:
        print(f"[SKIP] '{query}' — no single expected game")
        continue

    results = retrieve(query)
    games_returned = [r["game"] for r in results]

    if expected in games_returned:
        print(f"[PASS] '{query}' — found {expected}")
        passed += 1
    else:
        print(f"[FAIL] '{query}' — expected {expected}, got {games_returned}")
        failed += 1
        failures.append({
            "query": query,
            "expected": expected,
            "got": games_returned
        })

total = passed + failed
print(f"\nRetrieval accuracy: {passed}/{total} ({round(passed/total*100)}%)")

if failures:
    print("\nFailures to review:")
    for f in failures:
        print(f"  - '{f['query']}' expected {f['expected']}, got {f['got']}")
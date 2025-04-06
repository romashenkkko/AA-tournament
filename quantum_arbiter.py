def strategy(my_history: list[int], opponent_history: list[int], rounds: int | None) -> int:
    # Initialization phase - first 5% of rounds or minimum 3 rounds
    init_phase = rounds and (len(my_history) < max(3, rounds // 20))

    # Always cooperate on first move
    if not opponent_history:
        return 1

    # Classify opponent into one of three types:
    # 1. "exploiter" - cooperates <30% of the time
    # 2. "mirror" - move sums differ by ≤2 (mirror-like behavior)
    # 3. "random" - all other cases
    opponent_type = (
        "exploiter" if sum(opponent_history) / len(opponent_history) < 0.3
        else "mirror" if abs(sum(opponent_history) - sum(my_history)) <= 2
        else "random"
    )

    # Strategy against each opponent type:
    if opponent_type == "exploiter":
        # Always defect against exploiters
        return 0

    elif opponent_type == "mirror":
        # Quantum-inspired probabilistic response against mirrors
        # Deterministic "randomness" based on game history
        quantum_state = (sum(my_history) * len(opponent_history)) % 7
        return 1 if quantum_state > 3 else 0  # ~57% cooperation rate

    else:  # random
        # Against random opponents: defect only if last 3 moves were all defects
        last_three = opponent_history[-3:] if len(opponent_history) >= 3 else [1]
        return 0 if sum(last_three) == 0 else 1
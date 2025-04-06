# Algorithm Description
Quantum Arbiter Algorithm - Detailed Technical Description

Core Mechanics:

Opponent Classification System (real-time analysis):

Tracks opponent's cooperation rate (CoopRate = total cooperations/total moves)

Calculates move symmetry (absolute difference between player's and opponent's cooperation counts)

Categorizes into 3 behavioral profiles:
Exploiter: CoopRate < 30% (consistently defective)
Mirror: Move difference ≤ 2 (tit-for-tat like patterns)
Random: All other behavioral patterns

Dynamic Response Protocols:

Against Exploiters: Permanent defection (100% D) after identification

Against Mirrors: Quantum-inspired response using deterministic formula:
(sum_player_moves × total_rounds) % 7 > 3 → Cooperate (57% C / 43% D)

Against Random: Pattern-triggered defection (only defects after 3 consecutive opponent defects)

Key Technical Features:

First-move cooperation (NEAT compliant initialization)

Pure deterministic logic (no random module required)

Constant-time complexity (O(1) operations per round)

Round-count awareness (adapts to game length when available)

Strategic Advantages:

Anti-exploitation: Immediate punitive response to aggressive opponents

Mirror management: Maintains profitable cooperation through controlled unpredictability

Pattern recognition: Effective against stochastic strategies without unnecessary retaliation

Tournament compliant: No external dependencies, memory-efficient

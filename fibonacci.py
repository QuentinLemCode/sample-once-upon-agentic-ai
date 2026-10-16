# ✨ The Ancient Scroll of Fibonacci ✨
# Inscribed by Kiro the Grey Hat
# A spell to summon the sacred sequence of numbers

def cast_fibonacci_spell(n):
    """Cast the Fibonacci spell to conjure the first n numbers of the sequence."""
    print("🔮 Kiro raises his staff and chants the ancient incantation...")
    print("━" * 45)

    sequence = []
    a, b = 0, 1

    for i in range(n):
        sequence.append(a)
        a, b = b, a + b  # The magic: each number is the sum of the two before it!

    print(f"✨ The Fibonacci spell has conjured {n} sacred numbers:")
    print()
    for i, num in enumerate(sequence):
        print(f"   Position {i + 1:>2}  →  🌀 {num}")

    print()
    print(f"   Sequence: {sequence}")
    print()
    print("━" * 45)
    print("🌟 The ancient scroll has spoken. The spell is complete!")

# Invoke the spell for the first 10 Fibonacci numbers
cast_fibonacci_spell(10)

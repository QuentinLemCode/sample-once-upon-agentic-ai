from strands import Agent, tool

@tool
def roll_dice(faces: int = 6) -> int:
    """Roll a single die and return the result.

    Use this tool for every die roll (one call per die). For multiple dice,
    such as 4d6, call it once for each die.

    Args:
        faces: Number of faces on the die (e.g. 4, 6, 8, 10, 12, 20). Defaults to 6.

    Returns:
        A random integer between 1 and faces, inclusive.
    """

    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)


print(roll_dice.tool_spec)  # what Strands tells the model about your tool

dice_master = Agent(
    tools=[roll_dice],
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in D&D adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about D&D mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die."""
)

dice_master("Help me create a new D&D character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")


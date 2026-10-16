from strands import Agent
import logging
from strands.models import BedrockModel

# Configuration avec Bedrock
bedrock_model = BedrockModel(
    model_id="openai.gpt-6-luna",
    region_name='us-west-2',
    temperature=0.3,
)


# TODO: Step 1 - Add debug logging to see what your agent is thinking

# Configure the root strands logger
logging.getLogger("strands").setLevel(logging.DEBUG)

# Add a handler to see the logs
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)


# TODO: Step 2 - Create the agent with the following system prompt: "You are a game master for a Dungeon & Dragon game"
agent = Agent(
    system_prompt=(
        "You are a game master for a Dungeon & Dragon game. "
    ),

)
# TODO: Step 3 - Invoke your agent with a basic query such as "Hi, I am an adventurer ready for adventure!"
agent("Hi, I am an adventurer ready for adventure!")
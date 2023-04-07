import openai
import config
from logger import logger
logger = logger.get_logger()


# Set up OpenAI API credentials
openai.api_key =  config.OPEN_API_KEY

# Set up the prompt and parameters
def get_answer(prompt):
  # Send the request to the OpenAI API
  response = openai.Completion.create(
    engine=config.MODEL,
    prompt=prompt,
    max_tokens=config.MAX_TOKENS,
    temperature=config.TEMPERATURE
  )
  # Get the response text
  response_text = response.choices[0].text.strip()

  # Print the response text
  logger.info(response_text)
  return response_text


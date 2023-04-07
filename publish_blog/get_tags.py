import spacy
import config
from utills.get_distinct_string import get_distinct_strings
from logger import logger
logger = logger.get_logger()
# Load the English language model in spaCy
nlp = spacy.load(config.SPECY_MODEL_NAME)


def get_tags(sentence):
    # Parse the sentence with spaCy
    doc = nlp(sentence)

    # Extract the main tags from the sentence
    tags = [token.text for token in doc if token.pos_ == "NOUN" or token.pos_ == "PROPN"]
    
    # Print the main tags
    logger.info({
        "sentence": sentence,
        "tags": tags
    })
    # get the distinct
    return get_distinct_strings(tags)
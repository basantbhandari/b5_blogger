from logger import logger
logger = logger.get_logger()

def get_all_question(file_name):
    logger.info("reading the questions")
    try:
        # Open the text file in read mode
        with open(file_name, 'r') as f:

            # Read each line of the file
            all_question = []
            for line in f:
                logger.info(line)
                # accumulate the question
                all_question.append(line.strip())
        return all_question
    except Exception as exe:
        logger.error("error while reading the questions", exc_info= True)
        return None


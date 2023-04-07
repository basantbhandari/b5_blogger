import config
from prepare_answer.get_answer import get_answer
from utills.get_all_questions import get_all_question
from checks.check_not_nullable import check_not_nullable
from publish_blog.publish_articles import publish_all_articles
from logger import logger
logger = logger.get_logger()

if __name__ == "__main__":
    
    logger.info('starting the program')
    try:
        if check_not_nullable(config.FILE_PATH_QUESTION):
            all_questions = get_all_question(config.FILE_PATH_QUESTION)
            if all_questions is not None:
                logger.info(all_questions)
                post_object = []
                for each_question in all_questions:
                    answer = get_answer(each_question)
                    post_object.append({
                        "q": each_question,
                        "a": answer
                    })
                logger.info(post_object)

                publish_all_articles(post_object)

            else:
                logger.info("no question is there")
        else:
            logger.info('question path is none')
    
    except Exception as exe:
        logger.info("error while running the main program")









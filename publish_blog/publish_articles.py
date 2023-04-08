from publish_blog.get_tags import get_tags
from publish_blog.create_article import create_article
from logger import logger
logger = logger.get_logger()

def publish_all_articles(post_objects):
    for each_post_object in post_objects:
        tags = get_tags(each_post_object.get("a"))
        title = each_post_object.get("q")
        content = each_post_object.get("a")
        logger.info({
            "tags": tags,
            "title": title,
            "content": content
        })
        article = create_article(title, content, tags)
        logger.info(f'Created article response: {article}')


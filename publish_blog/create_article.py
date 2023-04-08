import config
import requests
import json
from publish_blog.get_processed_tags import get_processed_tags
from logger import logger
logger = logger.get_logger()



def create_article(title, content, tags):
    query = """
        mutation createStory($input: CreateStoryInput!) {
        createStory(input: $input) {
            code
            success
            message
            post {
            sourcedFromGithub
            isRepublished
            followersCount
            cuid
            slug
            title
            type
            partOfPublication
            dateUpdated
            totalReactions
            numCollapsed
            isDelisted
            isFeatured
            isActive
            replyCount
            responseCount
            popularity
            dateAdded
            contentMarkdown
            content
            brief
            coverImage
            }
        }
        }
    """
    data = {
	"input": {
		"title": title,
        "isPartOfPublication": {
        "publicationId": config.PUBLICATION_ID
            },
		"contentMarkdown": content,
		"tags": get_processed_tags(tags=tags)
	    }
    }

    payload = {
        "query": query,
        "variables": data
    }
    headers = {
    'Authorization': f'{config.HASH_NODE_API_KEY}',
    'Content-Type': 'application/json'
    }
    method = "POST"
    response = requests.request(method=method, url=config.HASH_NODE_API_ENDPOINT, headers=headers, data=json.dumps(payload))
    if response.status_code in range(200,210):
        logger.info("article successfully created")
    else:
        logger.info("failed to creat article")
    return response.text






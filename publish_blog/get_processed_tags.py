import uuid


def get_processed_tags(tags):
    result = []
    for item in tags:
        result.append({
			"_id": str(uuid.uuid1()),
			"slug": item,
			"name": item
		})
    return result
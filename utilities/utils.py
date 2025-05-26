import logging
logger = logging.getLogger(__name__)


def scheduled_on_day(response, day):
    days = response.json()["schedule"]["days"]
    assert day in days


def actor_in_show(response, actor):
    logger.info(f"Searching for actor: {actor}")
    cast_list = response.json()
    for person in cast_list:
        if person["person"]["name"] == actor:
            logger.info(f"Actor {actor} found in cast")
            return  # Exit when found

    logger.error(f"Actor {actor} not found in cast")
    assert False, f"Actor '{actor}' not found in cast"


def verify_pagination(response, pagination_length):
    actual_length = len(response.json())
    logger.info(f"Checking pagination: {actual_length} <= {pagination_length}")
    assert actual_length <= pagination_length

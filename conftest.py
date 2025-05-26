import pytest
import time
# from utilities import custom_logger
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def tavern_global_cfg():
    logger.info("Loading environment configuration")
    load_dotenv()
    base_url = os.environ.get("BASE_URL", "")
    logger.info(f"Using BASE_URL: {base_url}")
    return {
        "tv_maze": {
            "url": base_url,
        },
        "security": {
            "sql_injection_query": os.environ.get("SQL_INJECTION_QUERY"),
        }
    }


@pytest.fixture(scope="module")
def setup():
    print("running setup")
    yield
    print("running teardown")


@pytest.fixture(name="time_request")
def fix_time_request():
    t0 = time.time()

    yield

    t1 = time.time()

    logger.info(f"Test took {t1 - t0} seconds")

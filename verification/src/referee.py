from checkio_referee import RefereeBase

from checkio_referee import covercodes, representations, ENV_NAME


import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "three_words"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "threeWords"
    }


from fastapi import Depends, FastAPI

from configs.Environment import get_environment_variables
from metadata import Tags

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
)


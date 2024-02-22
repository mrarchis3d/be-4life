
from fastapi import FastAPI, __version__
from time import time
from app.config.Environment import get_environment_variables
from app.metadata import Tags

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
)


@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}

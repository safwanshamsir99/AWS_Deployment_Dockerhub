from fastapi import FastAPI, status, HTTPException, Header
from typing import Annotated, Union
from app.schema import Input, Output
from dotenv import load_dotenv
import logging
import os

description = """
This is a RESTful API using FastAPI to return addition of two numbers for AWS Deployment tutorial purposes
"""

app = FastAPI(
    title="AWS Deployment Tutorial API",
    description=description,
    version="1.0.0",
    docs_url='/docs',
    openapi_url='/openapi.json',
    license_info={
        "name": "MIT",
        "identifier":"MIT"
    }
)

load_dotenv()
log_info = logging.getLogger(__name__)

@app.get("/", status_code=status.HTTP_200_OK, tags=["test"])
def root():
    return {"status": "ok", "type": "api_deployment_tutorial"}

@app.get("/test_api_key", status_code=status.HTTP_200_OK, tags=["test"])
def develop_apikey_logic(
    api_key: Annotated[Union[str, None], Header()] = None,
):
    try:
        check_api_key = (
            True if api_key == os.getenv("BACKEND_API_KEY") else False
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No API key existed.",
        )

    if not check_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong API key!"
        )

    else:
        return {"status": "API key is correct."}

@app.post("/add", response_model=Output, tags=["addition"])
async def add(
    input: Input,
    api_key: Annotated[Union[str, None], Header()] = None
    ):
    '''
    Endpoint to produce num3 which is the sum num1 and num2
    
    Request:

        - num1: first number [float]
        - num2: second number [float]
        
    Return:

        - num3: Addition of num1 and num2 [float]
    '''
    # APIKEY HANDLING
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is required in header.",
        )

    request_user = True if api_key == os.getenv("BACKEND_API_KEY") else False
    if not request_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is not matched.",
        )
    num3 = input.num1 + input.num2
    data = {
        "num3": num3
        }
    return data
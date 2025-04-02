from fastapi import FastAPI
from app.api.spreadsheets import router as spreadsheets_router
from app.api.worksheets import router as worksheets_router
from app.api.authentication import router as auth_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title = "Python Google Sheets API",
    description= "A python API to interact with Google Sheets",
    version = "1.0",
    #docs_url="/",
    docs_url="/",
    openapi_tags=[
        {
            "name":"authentication",
            "description": "Authenticate clients to access the API"
        },
        {
            "name":"spreadsheets",
            "description": "Operations on spreadsheets"
        },
        {
            "name":"worksheets",
            "description": "Operations on worksheets"
        }
    ],
    swagger_ui_parameters={
        "defaultModelsExpandDepth":-1
    }
)

# this makes our app allow any origins front end api
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(spreadsheets_router)

app.include_router(worksheets_router)

app.include_router(auth_router)

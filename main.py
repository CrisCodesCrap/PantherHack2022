from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from schemes import LoginInfo,RegisterInfo
from login import LoginHandler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.post('/users/login/{username}')
async def login(data:LoginInfo):
    if LoginHandler.CheckExistingUserDataForLogin(data.username, data.password):
        return {'message': True}
    return {'message': False}

@app.post('/users/register/{username}')
async def register(data:RegisterInfo):
    if LoginHandler.CheckExistingUserDataForRegister(data.username, data.email):
        if LoginHandler.NewUserAssignment(data.username, data.password, data.email):
            return {'message': True}
    return {'message': False}
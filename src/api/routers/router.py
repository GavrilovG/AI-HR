# from fastapi import APIRouter, Depends, HTTPException, Response
# from authx import AuthX, AuthXConfig
# from pydantic import BaseModel

# config = AuthXConfig()
# config.JWT_SECRET_KEY = "your_secret_key"
# config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
# config.JWT_TOKEN_LOCATION = ["cookies"]

# security = AuthX(config=config)

# class UserLoginSchema(BaseModel):
#     username: str
#     password: str


# @router.post("/login")
# async def login(creds: UserLoginSchema, response: Response):
#     if creds.username == "admin" and creds.password == "password":
#         authx = AuthX(config)
#         access_token = authx.create_access_token(uid='12345') # , identity=creds.username
#         response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, access_token)
#         return {"access_token": access_token}
#     raise HTTPException(status_code=401, detail="Invalid credentials")


# @router.get("/setting", dependencies=[Depends(security.access_token_required)])
# async def setting():
#     return {"message": "You are authenticated as HR and can set interview parameters."}


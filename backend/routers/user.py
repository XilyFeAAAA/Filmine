# Fundamental
from fastapi import APIRouter, Depends, Body, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
# Core Related
from core import user as coreUser
from core.utils import is_valid_token
from core.security import authenticate_admin, generate_token

# Models Related
from models.user import NewUserModel
from models.response import Response400, ResponseToken,Response200

router = APIRouter()

@router.post('/register', response_model=Response200 | Response400)
async def register(request: Request, new_user_info: NewUserModel = Body(...)) -> Response200 | Response400:
    '''用户路由 - 注册事件'''
    try:
        await coreUser.register(new_user_info=new_user_info)
    except Exception as e:
        return Response400(err_msg=e.__class__.__name__)
    return Response200()


@router.post('/login', response_model=Response400 | ResponseToken)
async def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()) -> Response400 | ResponseToken:
    '''用户路由 - 登陆事件'''
    try:
        user_info = await coreUser.login(form_data.username, form_data.password)
    except Exception as e:
        return Response400(err_msg=e.__class__.__name__)
    # 生成token令牌
    token = await generate_token(user_info=user_info)
    return ResponseToken(data={'token': f"bearer {token}"}, access_token=token)


@router.post('/delete', response_model=Response200 | Response400)
async def delete(request: Request, username: str = Body(),
                 payload: dict = Depends(authenticate_admin)) -> Response400 | ResponseToken:
    '''用户路由 - 登陆事件'''
    try:
        await coreUser.delete(username=username)
    except Exception as e:
        return Response400(err_msg=e.__class__.__name__)
    return Response200()


@router.post('/verify', response_model=Response200)
async def verify(request: Request, payload: dict = Depends(authenticate_admin)) -> Response200:
    '''管理员路由 - 鉴权事件'''
    return Response200(data={'auth_payload': payload})


@router.get("/verify-account/{token}")
async def verify_email(request: Request, token: str) -> Response400:
    try: 
        email = await is_valid_token(token)
        await coreUser.verify_user(email)
    except Exception as e:
        return Response400(err_msg=e.__class__.__name__)
    return RedirectResponse(url='http://127.0.0.1:8080/login')
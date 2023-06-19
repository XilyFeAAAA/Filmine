from datetime import datetime,  timedelta
from passlib.context import CryptContext
from fastapi import Request, HTTPException,Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import configs

# Core Related
from models.user import SafeUserModel
from models.exceptions import NoAuthority

security = HTTPBearer()


async def authenticate(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    '''中间件来验证令牌'''
    if not credentials:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    token = credentials.credentials.replace('bearer ',"")
    try:
        payload = jwt.decode(token, key=configs.security.JWT_SECRET_KEY, algorithms=[configs.security.ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    return payload

async def authenticate_admin(payload: dict = Depends(authenticate)):
    if not payload['admin_auth']:
        raise NoAuthority()
    return payload

async def generate_token(user_info: SafeUserModel, expires_delta: timedelta = timedelta(minutes=configs.security.ACCESS_TOKEN_EXPIRE_MINUTE)):
    '''生成JWT令牌'''
    expires_at = datetime.utcnow() + expires_delta
    payload = {
        'username': user_info.username,
        'email': user_info.email,
        'admin_auth': True,
        'expires_at': expires_at.timestamp()
    }
    token = jwt.encode(payload, key=configs.security.JWT_SECRET_KEY, algorithm=configs.security.ALGORITHM)
    return token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''验证密码'''
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    '''哈希加密'''
    return pwd_context.hash(password)



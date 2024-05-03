from account.application.token_service import TokenService
from account.application.user_service import UserService
from config.django.base import JWT_EXPIRATION_DELTA_SECONDS, JWT_ISSUSER, JWT_SECRET_KEY

token_service: TokenService = TokenService(
    jwt_secret_key=JWT_SECRET_KEY,
    jwt_exp_delta_seconds=JWT_EXPIRATION_DELTA_SECONDS,
    jwt_issuer=JWT_ISSUSER,
)

user_service: UserService = UserService()

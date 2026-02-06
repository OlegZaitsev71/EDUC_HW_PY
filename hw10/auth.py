from authx import AuthX, AuthXConfig

config = AuthXConfig(
    JWT_SECRET_KEY='ZOA_SECRET_KEY',
    JWT_ACCESS_COOKIE_NAME='access_token',
    JWT_TOKEN_LOCATION=['cookies']
)

security = AuthX(config=config)
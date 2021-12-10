import os
from typing import Dict

from fastapi import FastAPI
from fastapi_opa import OPAConfig
from fastapi_opa import OPAMiddleware
from fastapi_opa.auth import OIDCAuthentication
from fastapi_opa.auth import OIDCConfig

opa_host = os.getenv("D4SERVICE_OPA_URI")
oidc_config = OIDCConfig(
    well_known_endpoint=None,
    app_uri=os.getenv("D4SERVICE_ADAPTER_URI"),
    client_id=os.getenv("D4SERVICE_OAUTH2_CLIENT_ID"),
    client_secret=os.getenv("D4SERVICE_OAUTH2_CLIENT_SECRET"),
    issuer=os.getenv("D4SERVICE_OAUTH2_ISSUER"),
    authorization_endpoint=os.getenv("D4SERVICE_OAUTH2_AUTH_ENDPOINT"),
    token_endpoint=os.getenv("D4SERVICE_OAUTH2_TOKEN_ENDPOINT"),
    jwks_uri=os.getenv("D4SERVICE_OAUTH2_JWKS_URI"),
    userinfo_endpoint=os.getenv("D4SERVICE_OAUTH2_USERINFO_ENDPOINT"),
)

oidc_auth = OIDCAuthentication(oidc_config)
opa_config = OPAConfig(authentication=oidc_auth, opa_host=opa_host)

app = FastAPI()
app.add_middleware(OPAMiddleware, config=opa_config)


@app.get("/finance/salary/{name}")
async def salary(name: str) -> Dict:
    return {"msg": "success", "name": name}

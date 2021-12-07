import os
from typing import Dict

from fastapi import FastAPI
from fastapi_opa import OPAConfig
from fastapi_opa import OPAMiddleware
from fastapi_opa.auth import OIDCAuthentication
from fastapi_opa.auth import OIDCConfig



opa_host = os.getenv("D4SERVICE_OPA_URI")
oidc_config = OIDCConfig(
    # well_known_endpoint=None,
    well_known_endpoint=os.getenv("D4SERVICE_OAUTH2_WELL_KNOWN_ENDPOINT"),
    app_uri=os.getenv("D4SERVICE_CACHE_URI"),
    client_id=os.getenv("D4SERVICE_OAUTH2_CLIENT_ID"),
    client_secret=os.getenv("D4SERVICE_OAUTH2_CLIENT_SECRET"),
    issuer=os.getenv("D4SERVICE_OAUTH2_ISSUER"),
    authorization_endpoint=os.getenv("D4SERVICE_OAUTH2_AUTHORIZATION_ENDPOINT"),
    token_endpoint=os.getenv("D4SERVICE_OAUTH2_TOKEN_ENDPOINT"),
    jwks_uri=os.getenv("D4SERVICE_OAUTH2_JWKS_URI"),
    userinfo_endpoint=os.getenv("D4SERVICE_OAUTH2_USERINFO_ENDPOINT"),
)

import pprint
pprint.pprint(oidc_config.__dict__)

oidc_auth = OIDCAuthentication(oidc_config)
opa_config = OPAConfig(authentication=oidc_auth, opa_host=opa_host)

app = FastAPI()
app.add_middleware(OPAMiddleware, config=opa_config)


@app.get("/finance/salary/{name}")
async def salary(name: str) -> Dict:
    return {"msg": "success", "name": name}

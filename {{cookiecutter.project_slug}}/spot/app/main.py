from typing import Dict

from fastapi import FastAPI
from fastapi_opa import OPAConfig
from fastapi_opa import OPAMiddleware
from fastapi_opa.auth import OIDCAuthentication
from fastapi_opa.auth import OIDCConfig

opa_host = "http://opa:8181"
oidc_config = OIDCConfig(
    app_uri="http://spot:9030",
    client_id="d4-client",
    client_secret="1f02bb76-eb58-40e2-928d-13f5c35794c1",
    # ---------------------------------------------------------------------------
    # well_known_endpoint="http://keycloak:8080/auth/realms/{{cookiecutter.test_auth_realm}}/.well-known/openid-configuration",  # noqa
    well_known_endpoint=None,
    issuer='http://keycloak:8080/auth/realms/{{cookiecutter.test_auth_realm}}',
    authorization_endpoint='http://keycloak:8080/auth/realms/{{cookiecutter.test_auth_realm}}/protocol/openid-connect/auth',
    token_endpoint='http://keycloak:8080/auth/realms/{{cookiecutter.test_auth_realm}}/protocol/openid-connect/token',
    jwks_uri='http://keycloak:8080/auth/realms/{{cookiecutter.test_auth_realm}}/protocol/openid-connect/certs',
    userinfo_endpoint='http://keycloak:8080/auth/realms/{{cookiecutter.test_auth_realm}}/protocol/openid-connect/userinfo'
)

oidc_auth = OIDCAuthentication(oidc_config)
opa_config = OPAConfig(authentication=oidc_auth, opa_host=opa_host)

app = FastAPI()
app.add_middleware(OPAMiddleware, config=opa_config)


@app.get("/finance/salary/{name}")
async def salary(name: str) -> Dict:
    return {"msg": "success", "name": name}

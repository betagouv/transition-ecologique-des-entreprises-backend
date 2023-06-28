from fastapi import APIRouter
from tee_backend.web.api.insee.schema import Siret, Etablissement
from tee_backend.settings import settings

import requests
import json
from loguru import logger

router = APIRouter()

def build_headers_siren (token):
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'authorization': f"Bearer {token}"
    }
    return headers

@router.post("/get_by_siret", response_model=Etablissement)
async def get_by_siret(
    incoming_siret: Siret,
) -> Etablissement:
    """
    Sends echo back to user.

    :param incoming_siret: incoming message.
    :returns: siret same as the incoming.
    """

    logger.debug(f'incoming_siret : {incoming_siret}')

    api_url_base = settings.api_siren
    logger.debug(f'api_url_base : {api_url_base}')

    api_url = api_url_base + "/siret/" + incoming_siret.siret
    logger.debug(f'api_url : {api_url}')

    token = settings.token_api_siren
    logger.debug(f'token : {token}')

    headers = build_headers_siren(token)
    logger.debug(f'headers : {headers}')

    resp = requests.get(api_url, headers=headers)
    logger.debug(f'resp : {resp}')
    data = resp.json()
    json_str = json.dumps(data, indent=4)
    logger.debug(f'json_str : \n{json_str}')

    return data


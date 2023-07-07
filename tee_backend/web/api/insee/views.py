from fastapi import APIRouter, HTTPException
# from fastapi.encoders import jsonable_encoder
from tee_backend.web.api.insee.schema import Siret, Siren, Etablissement, UniteLegale
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

def build_api_url(endpoint, siret):
    api_url_base = settings.api_siren
    # logger.debug(f'api_url_base : {api_url_base}')
    api_url = api_url_base + endpoint + siret
    # logger.debug(f'api_url : {api_url}')

    token = settings.token_api_siren
    # logger.debug(f'token : {token}')

    headers = build_headers_siren(token)
    # logger.debug(f'headers : {headers}')

    return {
        "url": api_url,
        "headers": headers
    }

@router.post("/get_by_siret", response_model=Etablissement)
async def get_by_siret(
    incoming_siret: Siret,
) -> Etablissement:
    """
    Sends etablissement back to user.

    :param incoming_siret: incoming message.
    :returns: établissement.
    """

    logger.debug(f'incoming_siret : {incoming_siret}')

    params = build_api_url('/siret/', incoming_siret.siret)
    logger.debug(f'params : {params}')

    resp = requests.get(params['url'], headers=params['headers'])
    logger.debug(f'resp : {resp}')
    logger.debug(f'resp.ok : {resp.ok}')
    # json_compatible_item_data = jsonable_encoder(resp)
    # logger.debug(f'json_compatible_item_data : {json_compatible_item_data}')
    data = resp.json()
    logger.debug(f'data : {data}')

    if not resp.ok :
        message = data["header"]["message"]
        raise HTTPException(status_code=404, detail=message)

    json_str = json.dumps(data, indent=4)
    logger.debug(f'json_str : \n{json_str}')

    return data

@router.post("/get_by_siren", response_model=UniteLegale)
async def get_by_siren(
    incoming_siren: Siren,
) -> UniteLegale:
    """
    Sends UniteLegale back to user.

    :param incoming_siret: incoming message.
    :returns: unité légale.
    """

    logger.debug(f'incoming_siren : {incoming_siren}')

    params = build_api_url('/siren/', incoming_siren.siren)
    logger.debug(f'params : {params}')

    resp = requests.get(params['url'], headers=params['headers'])
    logger.debug(f'resp : {resp}')
    data = resp.json()
    json_str = json.dumps(data, indent=4)
    logger.debug(f'json_str : \n{json_str}')

    return data

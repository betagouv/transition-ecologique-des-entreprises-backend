from fastapi import APIRouter
from tee_backend.web.api.brevo.schema import Contact
from tee_backend.settings import settings

# import requests
import json
from loguru import logger

router = APIRouter()

def build_headers_brevo (token):
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'api-key': f'{token}'
    }
    return headers

def build_api_url(endpoint, value=""):
    api_url_base = settings.api_brevo
    # logger.debug(f'api_url_base : {api_url_base}')
    api_url = api_url_base + endpoint + value
    # logger.debug(f'api_url : {api_url}')

    token = settings.token_api_brevo
    # logger.debug(f'token : {token}')

    headers = build_headers_brevo(token)
    # logger.debug(f'headers : {headers}')

    return {
        "url": api_url,
        "headers": headers
    }

@router.post("/add_contact", response_model=Contact)
async def add_contact(
    incoming_contact: Contact,
) -> Contact:
    """
    Sends echo back to user.

    :param incoming_contact: incoming message.
    :returns: contact same as the incoming.
    """
    logger.debug(f'incoming_contact : {incoming_contact}')
    contact_json = json.dumps(incoming_contact.dict(), indent=4)
    logger.debug(f'contact_json : \n{contact_json}')

    params = build_api_url('/contact')
    params_json = json.dumps(params, indent=4)
    logger.debug(f'params_json : \n{params_json}')

    # resp = requests.post(api_url, data=incoming_contact.dict(), headers=headers)
    # logger.debug(f'resp : {resp}')
    # data = resp.json()
    # json_str = json.dumps(data, indent=4)
    # logger.debug(f'json_str : \n{json_str}')

    return incoming_contact


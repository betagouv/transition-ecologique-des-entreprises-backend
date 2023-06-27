from fastapi import APIRouter
from tee_backend_test.web.api.brevo.schema import Message

router = APIRouter()

@router.post("/", response_model=Message)
async def send_echo_message(
    incoming_message: Message,
) -> Message:
    """
    Sends echo back to user.

    :param incoming_message: incoming message.
    :returns: message same as the incoming.
    """
    return incoming_message

@router.get("/add_contact")
def add_contact() -> None:
    """
    Add contact from form.

    It returns 200 if the project is healthy.
    """

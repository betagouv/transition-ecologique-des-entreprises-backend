from fastapi import APIRouter

router = APIRouter()


@router.get("/add_contact")
def add_contact() -> None:
    """
    Add contact from form.

    It returns 200 if the project is healthy.
    """

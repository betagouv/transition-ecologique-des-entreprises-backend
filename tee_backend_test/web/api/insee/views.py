from fastapi import APIRouter

router = APIRouter()


@router.get("/get_siret")
def get_siret() -> None:
    """
    Get entreprise data from SIRET number.

    It returns 200 if the project is healthy.
    """

from pydantic import BaseModel, validator, EmailStr
from typing import Optional, List

class ContactAttributes(BaseModel):
    """Simple contact attributes model."""

    # name: str = "contact"
    # surname: str = "multi"
    # tel: Optional[str] = "06 83 65 84 91"
    # opt_in: bool = False
    # siret: str = "83014132100034"

    NOM: str
    PRENOM: str
    TEL: str
    SIRET: str
    FORM_NEEDS: str
    OPT_IN: str
    PROJECT_NEEDS: str
    PROJECT_SECTORS: str
    USER_ROLES: str
    USER_GOALS: str
    PROJECT_STATUS: str
    STRUCTURE_SIZE: str
    PROGRAM_ID: str

    @validator("SIRET")
    def siret_validator(cls, value):
        if len(value) != 14 and len(value) != 9 :
            raise ValueError("Invalid siret")
        return value

class Contact(BaseModel):
    """Simple contact model."""
    email: EmailStr = "contact@multi.coop"
    listIds: List[int] = [4]
    attributes: ContactAttributes


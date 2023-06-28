from pydantic import BaseModel, validator, EmailStr
from typing import Optional, List, Union

class ContactAttributes(BaseModel):
    """Simple contact attributes model."""

    NOM: str = "contact"
    PRENOM: str = "multi"
    TEL: Optional[str] = "06 83 65 84 91"
    SIRET: str = "83014132100034"
    OPT_IN: Union[str, bool] = False
    # FORM_NEEDS: str
    PROJECT_NEEDS: str = "advices"
    PROJECT_SECTORS: str = "industry"
    USER_ROLES: str = "manager"
    USER_GOALS: str = "impact"
    # PROJECT_STATUS: str = ""
    STRUCTURE_SIZE: str = "tpe"
    PROGRAM_ID: str = "diag-decarbon-action"

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


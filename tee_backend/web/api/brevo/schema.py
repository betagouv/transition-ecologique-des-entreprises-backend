from pydantic import BaseModel, validator, EmailStr
from typing import Optional

class Contact(BaseModel):
    """Simple contact model."""

    name: str = "contact"
    surname: str = "multi"
    email: EmailStr = "contact@multi.coop"
    tel: Optional[str] = "06 83 65 84 91"

    opt_in: bool = False

    siret: str = "83014132100034"
    @validator("siret")
    def siret_validator(cls, value):
        if len(value) != 14 and len(value) != 9 :
            raise ValueError("Invalid siret")
        return value

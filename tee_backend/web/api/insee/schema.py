from pydantic import BaseModel, validator
from typing import Optional

class Siren(BaseModel):
    """Simple siren model."""

    siren: str = "830141321"

    @validator("siren")
    def siren_validator(cls, value):
        if len(value) != 9:
            raise ValueError("Invalid siren")
        return value

class Siret(BaseModel):
    """Simple siret model."""

    siret: str = "83014132100034"

    @validator("siret")
    def siret_validator(cls, value):
        if len(value) != 14:
            raise ValueError("Invalid siret")
        return value

class Etablissement (BaseModel):
    """Simple etablissement model."""

    header: dict
    etablissement: Optional[dict]

class UniteLegale (BaseModel):
    """Simple uniteLegale model."""

    header: dict
    uniteLegale: Optional[dict]

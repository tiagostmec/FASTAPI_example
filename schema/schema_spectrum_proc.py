from pydantic import BaseModel, Field, validator
from typing import List
from schema.validator import size

class SpectrumRequest(BaseModel):
    frequencies: List[float]
    amplitudes: List[float]
    '''
    Validator for checking the data.
    Needs to be 2 or more in size, to avoid api crash.
    '''

    @validator('frequencies', 'amplitudes')
    def validate_size(cls, v, field):
        return size(v, field.name,'spectrum_process')

class SpectrumResponse(BaseModel):
    status: str
    accuracy: dict

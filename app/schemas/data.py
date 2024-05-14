import re
from pydantic import BaseModel, Field, validator

class DataSchema(BaseModel):
    phone: str
    address: str

    @validator('phone')
    def validate_phone_length(cls, value):
        if len(value) != 11:
            raise ValueError('Phone number must be 11 characters long')
        return value
    
    @validator('phone')
    def validate_phone_format(cls, value):
        if not re.match(r'^8\d{10}$', value):
            raise ValueError('Phone number must be in the format 89090000000')
        return value

    @validator('address')
    def validate_address_length(cls, value):
        if len(value) < 1 or len(value) > 255:
            raise ValueError('Address must be between 1 and 255 characters long')
        return value
    

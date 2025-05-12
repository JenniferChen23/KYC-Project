from pydantic import BaseModel

class CompanyRequest(BaseModel):
    companyName: str
    location: str

class Description(BaseModel):
    companyDescription: str
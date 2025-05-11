from pydantic import BaseModel

class CompanyRequest(BaseModel):
    companyName: str
    location: str
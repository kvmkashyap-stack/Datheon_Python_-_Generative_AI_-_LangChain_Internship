from pydantic import BaseModel, Field , EmailStr

class Education(BaseModel):
    degree: str | None= None
    institution: str | None= None
    graduation_year: int | None= None

class ResumeData(BaseModel):
    name: str | None=None
    email: EmailStr | None=None
    phone: str | None=None
    skills: list[str] = Field(default_factory=list)
    experience_years: float | None = Field(default=None, ge=0)
    education: list[Education] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)
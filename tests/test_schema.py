
import pytest
from pydantic import ValidationError

from schemas.resume import ResumeData


def test_valid_resume():
    resume = ResumeData(
        name="Rahul",
        email="rahul@example.com",
        skills=["Python", "FastAPI"],
        experience_years=2,
    )

    assert resume.name == "Rahul"
    assert resume.experience_years == 2
    assert "Python" in resume.skills


def test_missing_fields_use_defaults():
    resume = ResumeData(name="Priya")

    assert resume.name == "Priya"
    assert resume.skills == []
    assert resume.education == []
    assert resume.projects == []


def test_negative_experience_is_rejected():
    with pytest.raises(ValidationError):
        ResumeData(
            name="Rahul",
            experience_years=-2,
        )


def test_invalid_email_is_rejected():
    with pytest.raises(ValidationError):
        ResumeData(
            name="Rahul",
            email="not-an-email",
        )

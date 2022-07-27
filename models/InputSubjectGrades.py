from typing import List
import pydantic
from custom_exceptions.GradeFormatError import GradeFormatError
from custom_exceptions.NameFormatError import NameFormatError


class InputSubjectGrades(pydantic.BaseModel):
    subject: str
    grades: List[int]

    @pydantic.validator("subject")
    def subject_validation(cls, value):
        if any(char.isdigit() for char in value):
            raise NameFormatError(value=value, message=f"Subject name should not contain digits. ({value})")
        return value

    @pydantic.validator("grades")
    def grade_validation(cls, value):
        for grade in value:
            if not 0 <= float(grade) <= 100:
                raise GradeFormatError(value=value, message=f"Grade should be between 1 and 100. ({grade})")
        return value

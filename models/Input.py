import random
from datetime import datetime
import pydantic
import uuid
from typing import Optional, List
from custom_exceptions.AgeFormatError import AgeFormatError
from custom_exceptions.BehaviourGradeFormatError import BehaviourGradeFormatError
from custom_exceptions.DateFormatError import DateFormatError
from custom_exceptions.GenderFormatError import GenderFormatError
from models.InputStudentDetails import InputStudentDetails
from models.InputSubjectGrades import InputSubjectGrades

input_data = {
  "studentDetails": {
    "firstName": "Raz",
    "lastName": "Matzliah",
    "id": 322717570
  },
  "subjectGrades": [
    {
      "subject": "Math",
      "grades": [
        100,
        50,
        84
      ]
    },
    {
      "subject": "English",
      "grades": [
        100,
        70,
        84
      ]
    }
  ],
  "birthDate": "27/06/2000",
  "age": 22,
  "gender": "זכר",
  "behaviourGrade": 8,
  "notes": "hi"
}


class Input(pydantic.BaseModel):

    studentDetails: InputStudentDetails
    subjectGrades: List[InputSubjectGrades]
    birthDate: str
    age: int
    gender: str
    behaviourGrade: int
    notes: Optional[str]

    @pydantic.validator('birthDate')
    def validate_birthdate(cls, value):
        try:
            datetime.strptime(str(value), '%d/%m/%Y')
        except ValueError:
            raise DateFormatError(value=value, message=f"Invalid date format. ({value})")
        return value

    @pydantic.root_validator
    def validate_age(cls, values: dict):
        if (datetime.now() - datetime.strptime(values["birthDate"], "%d/%m/%Y")).days // 365 != values["age"]:
            raise AgeFormatError(value=values["age"], message=f"Age does not match birth date. ({values['age']}) ({values['birthDate']})")
        return values

    @pydantic.validator('gender')
    def validate_gender(cls, value):
        if value not in ["נקבה", "אחר", "זכר"]:
            raise GenderFormatError(value=value, message=f"Gender must be זכר/נקבה/אחר ({value})")
        return value

    @pydantic.validator("behaviourGrade")
    def validate_behaviour_grade(cls, value):
        if value < 1 or value > 10:
            raise BehaviourGradeFormatError(value=value, message=f"Behaviour grade must be between 1 and 10. ({value})")
        return value


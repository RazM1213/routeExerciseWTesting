from dataclasses import dataclass
from typing import List, Optional
from models.InputStudentDetails import InputStudentDetails
from models.InputSubjectGrades import InputSubjectGrades


@dataclass
class TestInput:
    studentDetails: InputStudentDetails
    subjectGrades: List[InputSubjectGrades]
    birthDate: str
    age: int
    gender: str
    behaviourGrade: int
    notes: Optional[str]
    extraField: Optional[str]
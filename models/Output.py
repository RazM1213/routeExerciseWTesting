from dataclasses import dataclass
from typing import Optional, List
from models.OutputStudentDetails import OutputStudentDetails
from models.OutputSubjectGrades import OutputSubjectGrades


@dataclass
class Output:
    studentDetails: OutputStudentDetails
    subjectGrades: List[OutputSubjectGrades]
    totalAvg: float
    birthDate: str
    age: int
    gender: str
    isGoodBehaviour: str
    notes: Optional[str] = None

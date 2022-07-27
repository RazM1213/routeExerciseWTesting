import json
import os
from dataclasses import asdict
from models.Input import Input
from models.Output import Output
from models.OutputStudentDetails import OutputStudentDetails
from models.OutputSubjectGrades import OutputSubjectGrades


class Parser:
    def __init__(self, input_data):
        self.input = Input(**input_data)

    def parse_output(self):
        return Output(
            self.parse_student_details(),
            self.parse_subject_grades(),
            self.parse_total_avg(),
            self.input.birthDate,
            self.input.age,
            self.parse_gender(),
            self.parse_isgoodbehaviour(),
            self.input.notes
        )

    def parse_student_details(self):
        first_name = self.input.studentDetails.firstName
        last_name = self.input.studentDetails.lastName
        id = self.input.studentDetails.id
        full_name = first_name + " " + last_name
        return OutputStudentDetails(first_name, last_name, full_name, id)

    def parse_subject_grades(self):
        subjects_avg = []
        for subject in self.input.subjectGrades:
            subject_name = subject.subject
            avg = sum(subject.grades) / len(subject.grades)
            subject_avg = OutputSubjectGrades(subject_name, avg)
            subjects_avg.append(subject_avg)
        return subjects_avg

    def parse_total_avg(self):
        sum = 0
        for subject in self.parse_subject_grades():
            sum += subject.avg
        return sum / len(self.parse_subject_grades())

    def parse_gender(self):
        gender_mapping = {
             "זכר": "MALE",
             "נקבה": "FEMALE",
             "אחר": "OTHER",
        }

        return gender_mapping[self.input.gender]

    def parse_isgoodbehaviour(self):
        if self.input.behaviourGrade >= 5:
            return True
        return False

    def create_text_file(self):
        save_path = 'C:/Users/razm1/PycharmProjects/routeExercise/students'
        fullname = self.parse_output().studentDetails.fullName
        complete_path = os.path.join(save_path, fullname.replace(' ', '_') + ".txt")

        with open(complete_path, 'w') as f:
            data = json.dumps(asdict(self.parse_output()), indent=4)
            f.write(data)
import pydantic
from custom_exceptions.IdFormatError import IdFormatError
from custom_exceptions.NameFormatError import NameFormatError


class InputStudentDetails(pydantic.BaseModel):
    firstName: str
    lastName: str
    id: int

    @pydantic.validator("firstName")
    def firstname_validation(cls, value):
        if any(char.isdigit() for char in value):
            raise NameFormatError(value=value, message=f"First name should not contain digits. ({value})")
        return value

    @pydantic.validator("lastName")
    def lastname_validation(cls, value):
        if any(char.isdigit() for char in value):
            raise NameFormatError(value=value, message=f"Last name should not contain digits. ({value})")
        return value

    @pydantic.validator("id")
    def id_validation(cls, value):
        if len(str(value)) != 9:
            raise IdFormatError(value=value, message=f"Id should contain 9 digits. ({value})")
        return value




from project.module.exception_format import AppError


class PhoneNumberExist(AppError):

    description="phone already exist"
    http_code=404


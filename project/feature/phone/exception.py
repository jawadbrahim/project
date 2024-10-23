from project.module.exception_format import AppError


class PhoneNumberExist(AppError):
    description="phone_number already exist"
    http_code=404
    

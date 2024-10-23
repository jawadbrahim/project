from project.module.exception_format import AppError

class FailedToCreateUser(AppError):
    description="failed to create user"
    http_code=404
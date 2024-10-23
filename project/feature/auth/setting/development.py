from .option import OrmSqlAlchemyOption,RequestValidatoroption,DefaultOption,ResponseSerializerOption


class Development:
    ORM_SQLALCHEMY=OrmSqlAlchemyOption.ORMSQLACHEMY
    REQUEST_VALIDATOR=RequestValidatoroption.PYDANTIC_MODEL
    AUTH_SERVICE=DefaultOption.DEFAULT
    RESPONSE_SERIALIZER=ResponseSerializerOption.PYDANTC_JSON
from .options import OrmSqlAlchemyOption,UserServiceOption,RequestValidatorOption,ResponseSerializeOption

class Development:
    ORM_SQLALCHEMY=OrmSqlAlchemyOption.ORMSQLALCHEMY
    USER_SERVICE=UserServiceOption.DEFAULT
    REQUEST_VALIDATOR=RequestValidatorOption.PYDANTIC_MODEL
    RESPONSE_SERIALIZE=ResponseSerializeOption.PYDANTIC_JSON
from typing import Callable, Optional


def field_cannot_be_null(message: Optional[str] = None) -> Callable:
    message = message or 'Поле не может быть пустым!'

    def validator(value):
        if value is None:
            raise ValueError(message)
        return value
    return validator
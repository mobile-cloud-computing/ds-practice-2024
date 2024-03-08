from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("greeting",)
    GREETING_FIELD_NUMBER: _ClassVar[int]
    greeting: str
    def __init__(self, greeting: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("name", "contact")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    name: str
    contact: str
    def __init__(self, name: _Optional[str] = ..., contact: _Optional[str] = ...) -> None: ...

class CreditCard(_message.Message):
    __slots__ = ("number", "expirationDate", "cvv")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    CVV_FIELD_NUMBER: _ClassVar[int]
    number: str
    expirationDate: str
    cvv: str
    def __init__(self, number: _Optional[str] = ..., expirationDate: _Optional[str] = ..., cvv: _Optional[str] = ...) -> None: ...

class FraudDetectionRequest(_message.Message):
    __slots__ = ("user", "creditCard")
    USER_FIELD_NUMBER: _ClassVar[int]
    CREDITCARD_FIELD_NUMBER: _ClassVar[int]
    user: User
    creditCard: CreditCard
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., creditCard: _Optional[_Union[CreditCard, _Mapping]] = ...) -> None: ...

class FraudDetectionResponse(_message.Message):
    __slots__ = ("is_fraudulent",)
    IS_FRAUDULENT_FIELD_NUMBER: _ClassVar[int]
    is_fraudulent: bool
    def __init__(self, is_fraudulent: bool = ...) -> None: ...

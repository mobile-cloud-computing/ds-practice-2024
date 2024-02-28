from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectFraudRequest(_message.Message):
    __slots__ = ("userName", "creditCard")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CREDITCARD_FIELD_NUMBER: _ClassVar[int]
    userName: str
    creditCard: CreditCard
    def __init__(self, userName: _Optional[str] = ..., creditCard: _Optional[_Union[CreditCard, _Mapping]] = ...) -> None: ...

class DetectFraudResponse(_message.Message):
    __slots__ = ("isFraud",)
    ISFRAUD_FIELD_NUMBER: _ClassVar[int]
    isFraud: bool
    def __init__(self, isFraud: bool = ...) -> None: ...

class CreditCard(_message.Message):
    __slots__ = ("number", "expirationDate", "cvv")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    CVV_FIELD_NUMBER: _ClassVar[int]
    number: str
    expirationDate: str
    cvv: str
    def __init__(self, number: _Optional[str] = ..., expirationDate: _Optional[str] = ..., cvv: _Optional[str] = ...) -> None: ...

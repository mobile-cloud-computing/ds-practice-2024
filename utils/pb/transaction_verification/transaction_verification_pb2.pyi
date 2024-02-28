from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckoutRequest(_message.Message):
    __slots__ = ("creditcard",)
    CREDITCARD_FIELD_NUMBER: _ClassVar[int]
    creditcard: CreditCard
    def __init__(self, creditcard: _Optional[_Union[CreditCard, _Mapping]] = ...) -> None: ...

class CreditCard(_message.Message):
    __slots__ = ("number", "expirationDate", "cvv")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    CVV_FIELD_NUMBER: _ClassVar[int]
    number: str
    expirationDate: str
    cvv: str
    def __init__(self, number: _Optional[str] = ..., expirationDate: _Optional[str] = ..., cvv: _Optional[str] = ...) -> None: ...

class Determination(_message.Message):
    __slots__ = ("determination",)
    DETERMINATION_FIELD_NUMBER: _ClassVar[int]
    determination: bool
    def __init__(self, determination: bool = ...) -> None: ...

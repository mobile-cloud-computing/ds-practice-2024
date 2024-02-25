from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

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

class FraudDetectionRequest(_message.Message):
    __slots__ = ("creditCardNumber", "creditCardExpirationDate", "creditCardCVV", "discountCode")
    CREDITCARDNUMBER_FIELD_NUMBER: _ClassVar[int]
    CREDITCARDEXPIRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    CREDITCARDCVV_FIELD_NUMBER: _ClassVar[int]
    DISCOUNTCODE_FIELD_NUMBER: _ClassVar[int]
    creditCardNumber: str
    creditCardExpirationDate: str
    creditCardCVV: str
    discountCode: str
    def __init__(self, creditCardNumber: _Optional[str] = ..., creditCardExpirationDate: _Optional[str] = ..., creditCardCVV: _Optional[str] = ..., discountCode: _Optional[str] = ...) -> None: ...

class FraudDetectionResponse(_message.Message):
    __slots__ = ("isFraud", "message")
    ISFRAUD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    isFraud: bool
    message: str
    def __init__(self, isFraud: bool = ..., message: _Optional[str] = ...) -> None: ...

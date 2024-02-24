from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerificationRequest(_message.Message):
    __slots__ = ("items", "userName", "userContact", "discountCode", "billingAddress")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USERCONTACT_FIELD_NUMBER: _ClassVar[int]
    DISCOUNTCODE_FIELD_NUMBER: _ClassVar[int]
    BILLINGADDRESS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TransactionItem]
    userName: str
    userContact: str
    discountCode: str
    billingAddress: BillingAddressInfo
    def __init__(self, items: _Optional[_Iterable[_Union[TransactionItem, _Mapping]]] = ..., userName: _Optional[str] = ..., userContact: _Optional[str] = ..., discountCode: _Optional[str] = ..., billingAddress: _Optional[_Union[BillingAddressInfo, _Mapping]] = ...) -> None: ...

class TransactionItem(_message.Message):
    __slots__ = ("name", "quantity")
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    quantity: int
    def __init__(self, name: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...

class BillingAddressInfo(_message.Message):
    __slots__ = ("street", "city", "state", "zip", "country")
    STREET_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    street: str
    city: str
    state: str
    zip: str
    country: str
    def __init__(self, street: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., zip: _Optional[str] = ..., country: _Optional[str] = ...) -> None: ...

class VerificationResponse(_message.Message):
    __slots__ = ("isVerified", "message")
    ISVERIFIED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    isVerified: bool
    message: str
    def __init__(self, isVerified: bool = ..., message: _Optional[str] = ...) -> None: ...

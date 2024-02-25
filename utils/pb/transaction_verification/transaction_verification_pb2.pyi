from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Item(_message.Message):
    __slots__ = ("item_id", "name", "quantity", "price")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    name: str
    quantity: str
    price: str
    def __init__(self, item_id: _Optional[str] = ..., name: _Optional[str] = ..., quantity: _Optional[str] = ..., price: _Optional[str] = ...) -> None: ...

class UserId(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ShippingAddress(_message.Message):
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

class PaymentDetails(_message.Message):
    __slots__ = ("number", "expiration_date", "cvv", "cardholder_name")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    CVV_FIELD_NUMBER: _ClassVar[int]
    CARDHOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    number: str
    expiration_date: str
    cvv: str
    cardholder_name: str
    def __init__(self, number: _Optional[str] = ..., expiration_date: _Optional[str] = ..., cvv: _Optional[str] = ..., cardholder_name: _Optional[str] = ...) -> None: ...

class TransactionRequest(_message.Message):
    __slots__ = ("items", "user_id", "shipping_address", "payment_details")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    user_id: UserId
    shipping_address: ShippingAddress
    payment_details: PaymentDetails
    def __init__(self, items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., user_id: _Optional[_Union[UserId, _Mapping]] = ..., shipping_address: _Optional[_Union[ShippingAddress, _Mapping]] = ..., payment_details: _Optional[_Union[PaymentDetails, _Mapping]] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ("is_valid", "message")
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    is_valid: bool
    message: str
    def __init__(self, is_valid: bool = ..., message: _Optional[str] = ...) -> None: ...

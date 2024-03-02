from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SuggestionRequest(_message.Message):
    __slots__ = ("book_titles",)
    BOOK_TITLES_FIELD_NUMBER: _ClassVar[int]
    book_titles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, book_titles: _Optional[_Iterable[str]] = ...) -> None: ...

class SuggestionResponse(_message.Message):
    __slots__ = ("book_suggestions",)
    BOOK_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    book_suggestions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, book_suggestions: _Optional[_Iterable[str]] = ...) -> None: ...

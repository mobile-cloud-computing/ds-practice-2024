from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BookSuggestion(_message.Message):
    __slots__ = ("id", "title", "author")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    author: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ...) -> None: ...

class SuggestionRequest(_message.Message):
    __slots__ = ("bookTitles",)
    BOOKTITLES_FIELD_NUMBER: _ClassVar[int]
    bookTitles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, bookTitles: _Optional[_Iterable[str]] = ...) -> None: ...

class SuggestionResponse(_message.Message):
    __slots__ = ("suggestions",)
    SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    suggestions: _containers.RepeatedCompositeFieldContainer[BookSuggestion]
    def __init__(self, suggestions: _Optional[_Iterable[_Union[BookSuggestion, _Mapping]]] = ...) -> None: ...

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: suggestions.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11suggestions.proto\x12\x0bsuggestions\"&\n\x04Item\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"5\n\x11SuggestionRequest\x12 \n\x05items\x18\x04 \x03(\x0b\x32\x11.suggestions.Item\"5\n\x04\x42ook\x12\x0e\n\x06\x62ookId\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\"`\n\x12SuggestionResponse\x12\x0f\n\x07orderId\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12)\n\x0esuggestedBooks\x18\x03 \x03(\x0b\x32\x11.suggestions.Book\".\n\rErrorResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2d\n\x12SuggestionsService\x12N\n\x0bSuggestions\x12\x1e.suggestions.SuggestionRequest\x1a\x1f.suggestions.SuggestionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'suggestions_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ITEM']._serialized_start=34
  _globals['_ITEM']._serialized_end=72
  _globals['_SUGGESTIONREQUEST']._serialized_start=74
  _globals['_SUGGESTIONREQUEST']._serialized_end=127
  _globals['_BOOK']._serialized_start=129
  _globals['_BOOK']._serialized_end=182
  _globals['_SUGGESTIONRESPONSE']._serialized_start=184
  _globals['_SUGGESTIONRESPONSE']._serialized_end=280
  _globals['_ERRORRESPONSE']._serialized_start=282
  _globals['_ERRORRESPONSE']._serialized_end=328
  _globals['_SUGGESTIONSSERVICE']._serialized_start=330
  _globals['_SUGGESTIONSSERVICE']._serialized_end=430
# @@protoc_insertion_point(module_scope)
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: primefactor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='primefactor.proto',
  package='primefactor',
  syntax='proto3',
  serialized_pb=_b('\n\x11primefactor.proto\x12\x0bprimefactor\"\x16\n\x07Request\x12\x0b\n\x03num\x18\x01 \x01(\x03\"\x1a\n\x08Response\x12\x0e\n\x06result\x18\x01 \x01(\x03\x32H\n\x07\x46\x61\x63tors\x12=\n\x0cPrimeFactors\x12\x14.primefactor.Request\x1a\x15.primefactor.Response\"\x00\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='primefactor.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='primefactor.Request.num', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=56,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='primefactor.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='primefactor.Response.result', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'primefactor_pb2'
  # @@protoc_insertion_point(class_scope:primefactor.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'primefactor_pb2'
  # @@protoc_insertion_point(class_scope:primefactor.Response)
  ))
_sym_db.RegisterMessage(Response)



_FACTORS = _descriptor.ServiceDescriptor(
  name='Factors',
  full_name='primefactor.Factors',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=86,
  serialized_end=158,
  methods=[
  _descriptor.MethodDescriptor(
    name='PrimeFactors',
    full_name='primefactor.Factors.PrimeFactors',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FACTORS)

DESCRIPTOR.services_by_name['Factors'] = _FACTORS

# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: addr.proto

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
  name='addr.proto',
  package='proto_py',
  serialized_pb=_b('\n\naddr.proto\x12\x08proto_py\"\xd4\x01\n\x04\x41\x64\x64r\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12)\n\x05phone\x18\x04 \x03(\x0b\x32\x1a.proto_py.Addr.PhoneNumber\x1aK\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x02(\t\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x18.proto_py.Addr.PhoneType:\x04HOME\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"+\n\x0b\x41\x64\x64ressBook\x12\x1c\n\x04\x61\x64\x64r\x18\x01 \x03(\x0b\x32\x0e.proto_py.Addr')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ADDR_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='proto_py.Addr.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=194,
  serialized_end=237,
)
_sym_db.RegisterEnumDescriptor(_ADDR_PHONETYPE)


_ADDR_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='proto_py.Addr.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='proto_py.Addr.PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='proto_py.Addr.PhoneNumber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=192,
)

_ADDR = _descriptor.Descriptor(
  name='Addr',
  full_name='proto_py.Addr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto_py.Addr.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='proto_py.Addr.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='proto_py.Addr.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone', full_name='proto_py.Addr.phone', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ADDR_PHONENUMBER, ],
  enum_types=[
    _ADDR_PHONETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=237,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='proto_py.AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='proto_py.AddressBook.addr', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=282,
)

_ADDR_PHONENUMBER.fields_by_name['type'].enum_type = _ADDR_PHONETYPE
_ADDR_PHONENUMBER.containing_type = _ADDR
_ADDR.fields_by_name['phone'].message_type = _ADDR_PHONENUMBER
_ADDR_PHONETYPE.containing_type = _ADDR
_ADDRESSBOOK.fields_by_name['addr'].message_type = _ADDR
DESCRIPTOR.message_types_by_name['Addr'] = _ADDR
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK

Addr = _reflection.GeneratedProtocolMessageType('Addr', (_message.Message,), dict(

  PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), dict(
    DESCRIPTOR = _ADDR_PHONENUMBER,
    __module__ = 'addr_pb2'
    # @@protoc_insertion_point(class_scope:proto_py.Addr.PhoneNumber)
    ))
  ,
  DESCRIPTOR = _ADDR,
  __module__ = 'addr_pb2'
  # @@protoc_insertion_point(class_scope:proto_py.Addr)
  ))
_sym_db.RegisterMessage(Addr)
_sym_db.RegisterMessage(Addr.PhoneNumber)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSBOOK,
  __module__ = 'addr_pb2'
  # @@protoc_insertion_point(class_scope:proto_py.AddressBook)
  ))
_sym_db.RegisterMessage(AddressBook)


# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proto_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='person.proto',
  package='proto_py',
  serialized_pb=_b('\n\x0cperson.proto\x12\x08proto_py\x1a\x0bproto.proto\"\xbd\x02\n\x06Person\x12\x1e\n\x05proto\x18\x01 \x03(\x0b\x32\x0f.proto_py.Proto\x12\x0b\n\x03\x61ge\x18\x02 \x02(\x05\x12\x0c\n\x04name\x18\x03 \x02(\t\x12%\n\x05score\x18\x04 \x03(\x0b\x32\x16.proto_py.Person.Score\x12,\n\x06number\x18\x05 \x01(\x0b\x32\x1c.proto_py.Person.PhoneNumber\x1a&\n\x05Score\x12\x0e\n\x06object\x18\x01 \x02(\t\x12\r\n\x05score\x18\x02 \x01(\x05\x1aN\n\x0bPhoneNumber\x12\r\n\x05phone\x18\x01 \x02(\x05\x12\x30\n\x04type\x18\x02 \x01(\x0e\x32\x1a.proto_py.Person.PhoneType:\x06MOBILE\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04WORK\x10\x01\x12\x08\n\x04HOME\x10\x02\"9\n\tPersonOne\x12\n\n\x02id\x18\x01 \x02(\x05\x12 \n\x06people\x18\x02 \x02(\x0b\x32\x10.proto_py.Person')
  ,
  dependencies=[proto_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PERSON_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='proto_py.Person.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=314,
  serialized_end=357,
)
_sym_db.RegisterEnumDescriptor(_PERSON_PHONETYPE)


_PERSON_SCORE = _descriptor.Descriptor(
  name='Score',
  full_name='proto_py.Person.Score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object', full_name='proto_py.Person.Score.object', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='proto_py.Person.Score.score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=194,
  serialized_end=232,
)

_PERSON_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='proto_py.Person.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='proto_py.Person.PhoneNumber.phone', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='proto_py.Person.PhoneNumber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=234,
  serialized_end=312,
)

_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='proto_py.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proto', full_name='proto_py.Person.proto', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='age', full_name='proto_py.Person.age', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto_py.Person.name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='proto_py.Person.score', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number', full_name='proto_py.Person.number', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSON_SCORE, _PERSON_PHONENUMBER, ],
  enum_types=[
    _PERSON_PHONETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=357,
)


_PERSONONE = _descriptor.Descriptor(
  name='PersonOne',
  full_name='proto_py.PersonOne',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto_py.PersonOne.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='people', full_name='proto_py.PersonOne.people', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=359,
  serialized_end=416,
)

_PERSON_SCORE.containing_type = _PERSON
_PERSON_PHONENUMBER.fields_by_name['type'].enum_type = _PERSON_PHONETYPE
_PERSON_PHONENUMBER.containing_type = _PERSON
_PERSON.fields_by_name['proto'].message_type = proto_pb2._PROTO
_PERSON.fields_by_name['score'].message_type = _PERSON_SCORE
_PERSON.fields_by_name['number'].message_type = _PERSON_PHONENUMBER
_PERSON_PHONETYPE.containing_type = _PERSON
_PERSONONE.fields_by_name['people'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['PersonOne'] = _PERSONONE

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(

  Score = _reflection.GeneratedProtocolMessageType('Score', (_message.Message,), dict(
    DESCRIPTOR = _PERSON_SCORE,
    __module__ = 'person_pb2'
    # @@protoc_insertion_point(class_scope:proto_py.Person.Score)
    ))
  ,

  PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), dict(
    DESCRIPTOR = _PERSON_PHONENUMBER,
    __module__ = 'person_pb2'
    # @@protoc_insertion_point(class_scope:proto_py.Person.PhoneNumber)
    ))
  ,
  DESCRIPTOR = _PERSON,
  __module__ = 'person_pb2'
  # @@protoc_insertion_point(class_scope:proto_py.Person)
  ))
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.Score)
_sym_db.RegisterMessage(Person.PhoneNumber)

PersonOne = _reflection.GeneratedProtocolMessageType('PersonOne', (_message.Message,), dict(
  DESCRIPTOR = _PERSONONE,
  __module__ = 'person_pb2'
  # @@protoc_insertion_point(class_scope:proto_py.PersonOne)
  ))
_sym_db.RegisterMessage(PersonOne)


# @@protoc_insertion_point(module_scope)

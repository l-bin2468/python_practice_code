# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto.proto

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
  name='proto.proto',
  package='proto_py',
  serialized_pb=_b('\n\x0bproto.proto\x12\x08proto_py\"\"\n\x05Proto\x12\x0b\n\x03\x61ge\x18\x02 \x02(\x05\x12\x0c\n\x04name\x18\x03 \x02(\t\"1\n\x03One\x12\n\n\x02id\x18\x01 \x02(\r\x12\x1e\n\x05proto\x18\x02 \x02(\x0b\x32\x0f.proto_py.Proto\",\n\x03Two\x12\t\n\x01x\x18\x01 \x02(\r\x12\x1a\n\x03one\x18\x02 \x02(\x0b\x32\r.proto_py.One\".\n\x05Three\x12\t\n\x01y\x18\x01 \x02(\r\x12\x1a\n\x03two\x18\x02 \x02(\x0b\x32\r.proto_py.Two')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROTO = _descriptor.Descriptor(
  name='Proto',
  full_name='proto_py.Proto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='age', full_name='proto_py.Proto.age', index=0,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto_py.Proto.name', index=1,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=25,
  serialized_end=59,
)


_ONE = _descriptor.Descriptor(
  name='One',
  full_name='proto_py.One',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto_py.One.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proto', full_name='proto_py.One.proto', index=1,
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
  serialized_start=61,
  serialized_end=110,
)


_TWO = _descriptor.Descriptor(
  name='Two',
  full_name='proto_py.Two',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='proto_py.Two.x', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='one', full_name='proto_py.Two.one', index=1,
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
  serialized_start=112,
  serialized_end=156,
)


_THREE = _descriptor.Descriptor(
  name='Three',
  full_name='proto_py.Three',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='y', full_name='proto_py.Three.y', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='two', full_name='proto_py.Three.two', index=1,
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
  serialized_start=158,
  serialized_end=204,
)

_ONE.fields_by_name['proto'].message_type = _PROTO
_TWO.fields_by_name['one'].message_type = _ONE
_THREE.fields_by_name['two'].message_type = _TWO
DESCRIPTOR.message_types_by_name['Proto'] = _PROTO
DESCRIPTOR.message_types_by_name['One'] = _ONE
DESCRIPTOR.message_types_by_name['Two'] = _TWO
DESCRIPTOR.message_types_by_name['Three'] = _THREE

Proto = _reflection.GeneratedProtocolMessageType('Proto', (_message.Message,), dict(
  DESCRIPTOR = _PROTO,
  __module__ = 'proto_pb2'
  # @@protoc_insertion_point(class_scope:proto_py.Proto)
  ))
_sym_db.RegisterMessage(Proto)

One = _reflection.GeneratedProtocolMessageType('One', (_message.Message,), dict(
  DESCRIPTOR = _ONE,
  __module__ = 'proto_pb2'
  # @@protoc_insertion_point(class_scope:proto_py.One)
  ))
_sym_db.RegisterMessage(One)

Two = _reflection.GeneratedProtocolMessageType('Two', (_message.Message,), dict(
  DESCRIPTOR = _TWO,
  __module__ = 'proto_pb2'
  # @@protoc_insertion_point(class_scope:proto_py.Two)
  ))
_sym_db.RegisterMessage(Two)

Three = _reflection.GeneratedProtocolMessageType('Three', (_message.Message,), dict(
  DESCRIPTOR = _THREE,
  __module__ = 'proto_pb2'
  # @@protoc_insertion_point(class_scope:proto_py.Three)
  ))
_sym_db.RegisterMessage(Three)


# @@protoc_insertion_point(module_scope)

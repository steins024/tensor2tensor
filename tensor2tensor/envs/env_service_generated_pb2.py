# coding=utf-8
# Copyright 2019 The Tensor2Tensor Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# pylint: skip-file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensor2tensor/envs/env_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensor2tensor/envs/env_service.proto',
  package='tensor2tensor.trax.rlax.envs',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\n$tensor2tensor/envs/env_service.proto\x12\x1ctensor2tensor.trax.rlax.envs\x1a&tensorflow/core/framework/tensor.proto\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"d\n\x06\x41\x63tion\x12\x19\n\x0f\x64iscrete_action\x18\x01 \x01(\x03H\x00\x12\x34\n\x11\x63ontinuous_action\x18\x02 \x01(\x0b\x32\x17.tensorflow.TensorProtoH\x00\x42\t\n\x07payload\";\n\x0bObservation\x12,\n\x0bobservation\x18\x01 \x01(\x0b\x32\x17.tensorflow.TensorProto\"y\n\x04Info\x12\x41\n\x08info_map\x18\x01 \x03(\x0b\x32/.tensor2tensor.trax.rlax.envs.Info.InfoMapEntry\x1a.\n\x0cInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"C\n\x0bStepRequest\x12\x34\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32$.tensor2tensor.trax.rlax.envs.Action\"\x9e\x01\n\x0cStepResponse\x12>\n\x0bobservation\x18\x01 \x01(\x0b\x32).tensor2tensor.trax.rlax.envs.Observation\x12\x0e\n\x06reward\x18\x02 \x01(\x01\x12\x0c\n\x04\x64one\x18\x03 \x01(\x08\x12\x30\n\x04info\x18\x04 \x01(\x0b\x32\".tensor2tensor.trax.rlax.envs.Info\"\x0e\n\x0cResetRequest\"O\n\rResetResponse\x12>\n\x0bobservation\x18\x01 \x01(\x0b\x32).tensor2tensor.trax.rlax.envs.Observation\"\x0e\n\x0c\x43loseRequest\"\x0f\n\rCloseResponse\"\x1d\n\rRenderRequest\x12\x0c\n\x04mode\x18\x01 \x01(\t\"P\n\x0eRenderResponse\x12>\n\x0bobservation\x18\x01 \x01(\x0b\x32).tensor2tensor.trax.rlax.envs.Observation\"\x10\n\x0e\x45nvInfoRequest\"\xa9\x01\n\x08SpaceBox\x12#\n\x05\x64type\x18\x01 \x01(\x0e\x32\x14.tensorflow.DataType\x12+\n\x05shape\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12$\n\x03low\x18\x03 \x01(\x0b\x32\x17.tensorflow.TensorProto\x12%\n\x04high\x18\x04 \x01(\x0b\x32\x17.tensorflow.TensorProto\"$\n\rSpaceDiscrete\x12\x13\n\x0bnum_actions\x18\x01 \x01(\x05\"\xae\x01\n\x08GymSpace\x12\x1d\n\x13unimplemented_space\x18\x01 \x01(\x08H\x00\x12\x35\n\x03\x62ox\x18\x02 \x01(\x0b\x32&.tensor2tensor.trax.rlax.envs.SpaceBoxH\x00\x12?\n\x08\x64iscrete\x18\x03 \x01(\x0b\x32+.tensor2tensor.trax.rlax.envs.SpaceDiscreteH\x00\x42\x0b\n\tgym_space\"(\n\x0bRewardRange\x12\x0b\n\x03low\x18\x01 \x01(\x01\x12\x0c\n\x04high\x18\x02 \x01(\x01\"\xe7\x01\n\x0f\x45nvInfoResponse\x12\x41\n\x11observation_space\x18\x01 \x01(\x0b\x32&.tensor2tensor.trax.rlax.envs.GymSpace\x12<\n\x0c\x61\x63tion_space\x18\x02 \x01(\x0b\x32&.tensor2tensor.trax.rlax.envs.GymSpace\x12?\n\x0creward_range\x18\x03 \x01(\x0b\x32).tensor2tensor.trax.rlax.envs.RewardRange\x12\x12\n\nbatch_size\x18\x04 \x01(\x03\x32\x89\x04\n\nEnvService\x12\x62\n\x05Reset\x12*.tensor2tensor.trax.rlax.envs.ResetRequest\x1a+.tensor2tensor.trax.rlax.envs.ResetResponse\"\x00\x12_\n\x04Step\x12).tensor2tensor.trax.rlax.envs.StepRequest\x1a*.tensor2tensor.trax.rlax.envs.StepResponse\"\x00\x12\x62\n\x05\x43lose\x12*.tensor2tensor.trax.rlax.envs.CloseRequest\x1a+.tensor2tensor.trax.rlax.envs.CloseResponse\"\x00\x12\x65\n\x06Render\x12+.tensor2tensor.trax.rlax.envs.RenderRequest\x1a,.tensor2tensor.trax.rlax.envs.RenderResponse\"\x00\x12k\n\nGetEnvInfo\x12,.tensor2tensor.trax.rlax.envs.EnvInfoRequest\x1a-.tensor2tensor.trax.rlax.envs.EnvInfoResponse\"\x00\x42\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])




_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='tensor2tensor.trax.rlax.envs.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='discrete_action', full_name='tensor2tensor.trax.rlax.envs.Action.discrete_action', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='continuous_action', full_name='tensor2tensor.trax.rlax.envs.Action.continuous_action', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='tensor2tensor.trax.rlax.envs.Action.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=195,
  serialized_end=295,
)


_OBSERVATION = _descriptor.Descriptor(
  name='Observation',
  full_name='tensor2tensor.trax.rlax.envs.Observation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation', full_name='tensor2tensor.trax.rlax.envs.Observation.observation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=356,
)


_INFO_INFOMAPENTRY = _descriptor.Descriptor(
  name='InfoMapEntry',
  full_name='tensor2tensor.trax.rlax.envs.Info.InfoMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensor2tensor.trax.rlax.envs.Info.InfoMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensor2tensor.trax.rlax.envs.Info.InfoMapEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=433,
  serialized_end=479,
)

_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='tensor2tensor.trax.rlax.envs.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info_map', full_name='tensor2tensor.trax.rlax.envs.Info.info_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INFO_INFOMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=479,
)


_STEPREQUEST = _descriptor.Descriptor(
  name='StepRequest',
  full_name='tensor2tensor.trax.rlax.envs.StepRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='tensor2tensor.trax.rlax.envs.StepRequest.action', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=548,
)


_STEPRESPONSE = _descriptor.Descriptor(
  name='StepResponse',
  full_name='tensor2tensor.trax.rlax.envs.StepResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation', full_name='tensor2tensor.trax.rlax.envs.StepResponse.observation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='tensor2tensor.trax.rlax.envs.StepResponse.reward', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='done', full_name='tensor2tensor.trax.rlax.envs.StepResponse.done', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='tensor2tensor.trax.rlax.envs.StepResponse.info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=709,
)


_RESETREQUEST = _descriptor.Descriptor(
  name='ResetRequest',
  full_name='tensor2tensor.trax.rlax.envs.ResetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=711,
  serialized_end=725,
)


_RESETRESPONSE = _descriptor.Descriptor(
  name='ResetResponse',
  full_name='tensor2tensor.trax.rlax.envs.ResetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation', full_name='tensor2tensor.trax.rlax.envs.ResetResponse.observation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=727,
  serialized_end=806,
)


_CLOSEREQUEST = _descriptor.Descriptor(
  name='CloseRequest',
  full_name='tensor2tensor.trax.rlax.envs.CloseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=808,
  serialized_end=822,
)


_CLOSERESPONSE = _descriptor.Descriptor(
  name='CloseResponse',
  full_name='tensor2tensor.trax.rlax.envs.CloseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=824,
  serialized_end=839,
)


_RENDERREQUEST = _descriptor.Descriptor(
  name='RenderRequest',
  full_name='tensor2tensor.trax.rlax.envs.RenderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='tensor2tensor.trax.rlax.envs.RenderRequest.mode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=841,
  serialized_end=870,
)


_RENDERRESPONSE = _descriptor.Descriptor(
  name='RenderResponse',
  full_name='tensor2tensor.trax.rlax.envs.RenderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation', full_name='tensor2tensor.trax.rlax.envs.RenderResponse.observation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=872,
  serialized_end=952,
)


_ENVINFOREQUEST = _descriptor.Descriptor(
  name='EnvInfoRequest',
  full_name='tensor2tensor.trax.rlax.envs.EnvInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=954,
  serialized_end=970,
)


_SPACEBOX = _descriptor.Descriptor(
  name='SpaceBox',
  full_name='tensor2tensor.trax.rlax.envs.SpaceBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensor2tensor.trax.rlax.envs.SpaceBox.dtype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensor2tensor.trax.rlax.envs.SpaceBox.shape', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='tensor2tensor.trax.rlax.envs.SpaceBox.low', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='tensor2tensor.trax.rlax.envs.SpaceBox.high', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=973,
  serialized_end=1142,
)


_SPACEDISCRETE = _descriptor.Descriptor(
  name='SpaceDiscrete',
  full_name='tensor2tensor.trax.rlax.envs.SpaceDiscrete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_actions', full_name='tensor2tensor.trax.rlax.envs.SpaceDiscrete.num_actions', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1144,
  serialized_end=1180,
)


_GYMSPACE = _descriptor.Descriptor(
  name='GymSpace',
  full_name='tensor2tensor.trax.rlax.envs.GymSpace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unimplemented_space', full_name='tensor2tensor.trax.rlax.envs.GymSpace.unimplemented_space', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='box', full_name='tensor2tensor.trax.rlax.envs.GymSpace.box', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discrete', full_name='tensor2tensor.trax.rlax.envs.GymSpace.discrete', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='gym_space', full_name='tensor2tensor.trax.rlax.envs.GymSpace.gym_space',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1183,
  serialized_end=1357,
)


_REWARDRANGE = _descriptor.Descriptor(
  name='RewardRange',
  full_name='tensor2tensor.trax.rlax.envs.RewardRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='low', full_name='tensor2tensor.trax.rlax.envs.RewardRange.low', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='tensor2tensor.trax.rlax.envs.RewardRange.high', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1359,
  serialized_end=1399,
)


_ENVINFORESPONSE = _descriptor.Descriptor(
  name='EnvInfoResponse',
  full_name='tensor2tensor.trax.rlax.envs.EnvInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation_space', full_name='tensor2tensor.trax.rlax.envs.EnvInfoResponse.observation_space', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action_space', full_name='tensor2tensor.trax.rlax.envs.EnvInfoResponse.action_space', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward_range', full_name='tensor2tensor.trax.rlax.envs.EnvInfoResponse.reward_range', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='tensor2tensor.trax.rlax.envs.EnvInfoResponse.batch_size', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1402,
  serialized_end=1633,
)

_ACTION.fields_by_name['continuous_action'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_ACTION.oneofs_by_name['payload'].fields.append(
  _ACTION.fields_by_name['discrete_action'])
_ACTION.fields_by_name['discrete_action'].containing_oneof = _ACTION.oneofs_by_name['payload']
_ACTION.oneofs_by_name['payload'].fields.append(
  _ACTION.fields_by_name['continuous_action'])
_ACTION.fields_by_name['continuous_action'].containing_oneof = _ACTION.oneofs_by_name['payload']
_OBSERVATION.fields_by_name['observation'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_INFO_INFOMAPENTRY.containing_type = _INFO
_INFO.fields_by_name['info_map'].message_type = _INFO_INFOMAPENTRY
_STEPREQUEST.fields_by_name['action'].message_type = _ACTION
_STEPRESPONSE.fields_by_name['observation'].message_type = _OBSERVATION
_STEPRESPONSE.fields_by_name['info'].message_type = _INFO
_RESETRESPONSE.fields_by_name['observation'].message_type = _OBSERVATION
_RENDERRESPONSE.fields_by_name['observation'].message_type = _OBSERVATION
_SPACEBOX.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_SPACEBOX.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_SPACEBOX.fields_by_name['low'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_SPACEBOX.fields_by_name['high'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_GYMSPACE.fields_by_name['box'].message_type = _SPACEBOX
_GYMSPACE.fields_by_name['discrete'].message_type = _SPACEDISCRETE
_GYMSPACE.oneofs_by_name['gym_space'].fields.append(
  _GYMSPACE.fields_by_name['unimplemented_space'])
_GYMSPACE.fields_by_name['unimplemented_space'].containing_oneof = _GYMSPACE.oneofs_by_name['gym_space']
_GYMSPACE.oneofs_by_name['gym_space'].fields.append(
  _GYMSPACE.fields_by_name['box'])
_GYMSPACE.fields_by_name['box'].containing_oneof = _GYMSPACE.oneofs_by_name['gym_space']
_GYMSPACE.oneofs_by_name['gym_space'].fields.append(
  _GYMSPACE.fields_by_name['discrete'])
_GYMSPACE.fields_by_name['discrete'].containing_oneof = _GYMSPACE.oneofs_by_name['gym_space']
_ENVINFORESPONSE.fields_by_name['observation_space'].message_type = _GYMSPACE
_ENVINFORESPONSE.fields_by_name['action_space'].message_type = _GYMSPACE
_ENVINFORESPONSE.fields_by_name['reward_range'].message_type = _REWARDRANGE
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['Observation'] = _OBSERVATION
DESCRIPTOR.message_types_by_name['Info'] = _INFO
DESCRIPTOR.message_types_by_name['StepRequest'] = _STEPREQUEST
DESCRIPTOR.message_types_by_name['StepResponse'] = _STEPRESPONSE
DESCRIPTOR.message_types_by_name['ResetRequest'] = _RESETREQUEST
DESCRIPTOR.message_types_by_name['ResetResponse'] = _RESETRESPONSE
DESCRIPTOR.message_types_by_name['CloseRequest'] = _CLOSEREQUEST
DESCRIPTOR.message_types_by_name['CloseResponse'] = _CLOSERESPONSE
DESCRIPTOR.message_types_by_name['RenderRequest'] = _RENDERREQUEST
DESCRIPTOR.message_types_by_name['RenderResponse'] = _RENDERRESPONSE
DESCRIPTOR.message_types_by_name['EnvInfoRequest'] = _ENVINFOREQUEST
DESCRIPTOR.message_types_by_name['SpaceBox'] = _SPACEBOX
DESCRIPTOR.message_types_by_name['SpaceDiscrete'] = _SPACEDISCRETE
DESCRIPTOR.message_types_by_name['GymSpace'] = _GYMSPACE
DESCRIPTOR.message_types_by_name['RewardRange'] = _REWARDRANGE
DESCRIPTOR.message_types_by_name['EnvInfoResponse'] = _ENVINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.Action)
  })
_sym_db.RegisterMessage(Action)

Observation = _reflection.GeneratedProtocolMessageType('Observation', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATION,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.Observation)
  })
_sym_db.RegisterMessage(Observation)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), {

  'InfoMapEntry' : _reflection.GeneratedProtocolMessageType('InfoMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _INFO_INFOMAPENTRY,
    '__module__' : 'tensor2tensor.envs.env_service_pb2'
    # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.Info.InfoMapEntry)
    })
  ,
  'DESCRIPTOR' : _INFO,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.Info)
  })
_sym_db.RegisterMessage(Info)
_sym_db.RegisterMessage(Info.InfoMapEntry)

StepRequest = _reflection.GeneratedProtocolMessageType('StepRequest', (_message.Message,), {
  'DESCRIPTOR' : _STEPREQUEST,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.StepRequest)
  })
_sym_db.RegisterMessage(StepRequest)

StepResponse = _reflection.GeneratedProtocolMessageType('StepResponse', (_message.Message,), {
  'DESCRIPTOR' : _STEPRESPONSE,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.StepResponse)
  })
_sym_db.RegisterMessage(StepResponse)

ResetRequest = _reflection.GeneratedProtocolMessageType('ResetRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETREQUEST,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.ResetRequest)
  })
_sym_db.RegisterMessage(ResetRequest)

ResetResponse = _reflection.GeneratedProtocolMessageType('ResetResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETRESPONSE,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.ResetResponse)
  })
_sym_db.RegisterMessage(ResetResponse)

CloseRequest = _reflection.GeneratedProtocolMessageType('CloseRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSEREQUEST,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.CloseRequest)
  })
_sym_db.RegisterMessage(CloseRequest)

CloseResponse = _reflection.GeneratedProtocolMessageType('CloseResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSERESPONSE,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.CloseResponse)
  })
_sym_db.RegisterMessage(CloseResponse)

RenderRequest = _reflection.GeneratedProtocolMessageType('RenderRequest', (_message.Message,), {
  'DESCRIPTOR' : _RENDERREQUEST,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.RenderRequest)
  })
_sym_db.RegisterMessage(RenderRequest)

RenderResponse = _reflection.GeneratedProtocolMessageType('RenderResponse', (_message.Message,), {
  'DESCRIPTOR' : _RENDERRESPONSE,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.RenderResponse)
  })
_sym_db.RegisterMessage(RenderResponse)

EnvInfoRequest = _reflection.GeneratedProtocolMessageType('EnvInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENVINFOREQUEST,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.EnvInfoRequest)
  })
_sym_db.RegisterMessage(EnvInfoRequest)

SpaceBox = _reflection.GeneratedProtocolMessageType('SpaceBox', (_message.Message,), {
  'DESCRIPTOR' : _SPACEBOX,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.SpaceBox)
  })
_sym_db.RegisterMessage(SpaceBox)

SpaceDiscrete = _reflection.GeneratedProtocolMessageType('SpaceDiscrete', (_message.Message,), {
  'DESCRIPTOR' : _SPACEDISCRETE,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.SpaceDiscrete)
  })
_sym_db.RegisterMessage(SpaceDiscrete)

GymSpace = _reflection.GeneratedProtocolMessageType('GymSpace', (_message.Message,), {
  'DESCRIPTOR' : _GYMSPACE,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.GymSpace)
  })
_sym_db.RegisterMessage(GymSpace)

RewardRange = _reflection.GeneratedProtocolMessageType('RewardRange', (_message.Message,), {
  'DESCRIPTOR' : _REWARDRANGE,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.RewardRange)
  })
_sym_db.RegisterMessage(RewardRange)

EnvInfoResponse = _reflection.GeneratedProtocolMessageType('EnvInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENVINFORESPONSE,
  '__module__' : 'tensor2tensor.envs.env_service_pb2'
  # @@protoc_insertion_point(class_scope:tensor2tensor.trax.rlax.envs.EnvInfoResponse)
  })
_sym_db.RegisterMessage(EnvInfoResponse)


DESCRIPTOR._options = None
_INFO_INFOMAPENTRY._options = None

_ENVSERVICE = _descriptor.ServiceDescriptor(
  name='EnvService',
  full_name='tensor2tensor.trax.rlax.envs.EnvService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1636,
  serialized_end=2157,
  methods=[
  _descriptor.MethodDescriptor(
    name='Reset',
    full_name='tensor2tensor.trax.rlax.envs.EnvService.Reset',
    index=0,
    containing_service=None,
    input_type=_RESETREQUEST,
    output_type=_RESETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Step',
    full_name='tensor2tensor.trax.rlax.envs.EnvService.Step',
    index=1,
    containing_service=None,
    input_type=_STEPREQUEST,
    output_type=_STEPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Close',
    full_name='tensor2tensor.trax.rlax.envs.EnvService.Close',
    index=2,
    containing_service=None,
    input_type=_CLOSEREQUEST,
    output_type=_CLOSERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Render',
    full_name='tensor2tensor.trax.rlax.envs.EnvService.Render',
    index=3,
    containing_service=None,
    input_type=_RENDERREQUEST,
    output_type=_RENDERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetEnvInfo',
    full_name='tensor2tensor.trax.rlax.envs.EnvService.GetEnvInfo',
    index=4,
    containing_service=None,
    input_type=_ENVINFOREQUEST,
    output_type=_ENVINFORESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENVSERVICE)

DESCRIPTOR.services_by_name['EnvService'] = _ENVSERVICE

# @@protoc_insertion_point(module_scope)
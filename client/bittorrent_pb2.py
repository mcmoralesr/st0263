# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: bittorrent.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'bittorrent.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x62ittorrent.proto\";\n\x08PeerInfo\x12\x0f\n\x07peer_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\r\n\x05\x66iles\x18\x03 \x03(\t\" \n\x0b\x46ileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"$\n\x08PeerList\x12\x18\n\x05peers\x18\x01 \x03(\x0b\x32\t.PeerInfo\"6\n\x0c\x43hunkRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x13\n\x0b\x63hunk_index\x18\x02 \x01(\x05\"-\n\x05\x43hunk\x12\x13\n\x0b\x63hunk_index\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"\x19\n\x06Status\x12\x0f\n\x07message\x18\x01 \x01(\t2Y\n\x0eTrackerService\x12\"\n\x0cRegisterPeer\x12\t.PeerInfo\x1a\x07.Status\x12#\n\x08GetPeers\x12\x0c.FileRequest\x1a\t.PeerList24\n\x0bPeerService\x12%\n\x0cRequestChunk\x12\r.ChunkRequest\x1a\x06.Chunkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bittorrent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PEERINFO']._serialized_start=20
  _globals['_PEERINFO']._serialized_end=79
  _globals['_FILEREQUEST']._serialized_start=81
  _globals['_FILEREQUEST']._serialized_end=113
  _globals['_PEERLIST']._serialized_start=115
  _globals['_PEERLIST']._serialized_end=151
  _globals['_CHUNKREQUEST']._serialized_start=153
  _globals['_CHUNKREQUEST']._serialized_end=207
  _globals['_CHUNK']._serialized_start=209
  _globals['_CHUNK']._serialized_end=254
  _globals['_STATUS']._serialized_start=256
  _globals['_STATUS']._serialized_end=281
  _globals['_TRACKERSERVICE']._serialized_start=283
  _globals['_TRACKERSERVICE']._serialized_end=372
  _globals['_PEERSERVICE']._serialized_start=374
  _globals['_PEERSERVICE']._serialized_end=426
# @@protoc_insertion_point(module_scope)
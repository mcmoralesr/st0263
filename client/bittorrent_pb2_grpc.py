# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import bittorrent_pb2 as bittorrent__pb2

GRPC_GENERATED_VERSION = '1.68.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in bittorrent_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TrackerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterPeer = channel.unary_unary(
                '/TrackerService/RegisterPeer',
                request_serializer=bittorrent__pb2.PeerInfo.SerializeToString,
                response_deserializer=bittorrent__pb2.Status.FromString,
                _registered_method=True)
        self.GetPeers = channel.unary_unary(
                '/TrackerService/GetPeers',
                request_serializer=bittorrent__pb2.FileRequest.SerializeToString,
                response_deserializer=bittorrent__pb2.PeerList.FromString,
                _registered_method=True)


class TrackerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterPeer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrackerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterPeer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPeer,
                    request_deserializer=bittorrent__pb2.PeerInfo.FromString,
                    response_serializer=bittorrent__pb2.Status.SerializeToString,
            ),
            'GetPeers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeers,
                    request_deserializer=bittorrent__pb2.FileRequest.FromString,
                    response_serializer=bittorrent__pb2.PeerList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TrackerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('TrackerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TrackerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterPeer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TrackerService/RegisterPeer',
            bittorrent__pb2.PeerInfo.SerializeToString,
            bittorrent__pb2.Status.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPeers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TrackerService/GetPeers',
            bittorrent__pb2.FileRequest.SerializeToString,
            bittorrent__pb2.PeerList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class PeerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RequestChunk = channel.unary_unary(
                '/PeerService/RequestChunk',
                request_serializer=bittorrent__pb2.ChunkRequest.SerializeToString,
                response_deserializer=bittorrent__pb2.Chunk.FromString,
                _registered_method=True)


class PeerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RequestChunk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PeerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RequestChunk': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestChunk,
                    request_deserializer=bittorrent__pb2.ChunkRequest.FromString,
                    response_serializer=bittorrent__pb2.Chunk.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PeerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('PeerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PeerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RequestChunk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PeerService/RequestChunk',
            bittorrent__pb2.ChunkRequest.SerializeToString,
            bittorrent__pb2.Chunk.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

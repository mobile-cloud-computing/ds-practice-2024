# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from suggestions import suggestions_pb2 as suggestions_dot_suggestions__pb2


class SuggestionsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SuggestItems = channel.unary_unary(
                '/suggestions.SuggestionsService/SuggestItems',
                request_serializer=suggestions_dot_suggestions__pb2.SuggestionsRequest.SerializeToString,
                response_deserializer=suggestions_dot_suggestions__pb2.SuggestionsResponse.FromString,
                )


class SuggestionsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SuggestItems(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SuggestionsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SuggestItems': grpc.unary_unary_rpc_method_handler(
                    servicer.SuggestItems,
                    request_deserializer=suggestions_dot_suggestions__pb2.SuggestionsRequest.FromString,
                    response_serializer=suggestions_dot_suggestions__pb2.SuggestionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'suggestions.SuggestionsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SuggestionsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SuggestItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/suggestions.SuggestionsService/SuggestItems',
            suggestions_dot_suggestions__pb2.SuggestionsRequest.SerializeToString,
            suggestions_dot_suggestions__pb2.SuggestionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

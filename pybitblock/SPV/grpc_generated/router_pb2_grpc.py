# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from grpc_generated import router_pb2 as router__pb2


class RouterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendPayment = channel.unary_stream(
        '/routerrpc.Router/SendPayment',
        request_serializer=router__pb2.SendPaymentRequest.SerializeToString,
        response_deserializer=router__pb2.PaymentStatus.FromString,
        )
    self.TrackPayment = channel.unary_stream(
        '/routerrpc.Router/TrackPayment',
        request_serializer=router__pb2.TrackPaymentRequest.SerializeToString,
        response_deserializer=router__pb2.PaymentStatus.FromString,
        )
    self.EstimateRouteFee = channel.unary_unary(
        '/routerrpc.Router/EstimateRouteFee',
        request_serializer=router__pb2.RouteFeeRequest.SerializeToString,
        response_deserializer=router__pb2.RouteFeeResponse.FromString,
        )
    self.SendToRoute = channel.unary_unary(
        '/routerrpc.Router/SendToRoute',
        request_serializer=router__pb2.SendToRouteRequest.SerializeToString,
        response_deserializer=router__pb2.SendToRouteResponse.FromString,
        )
    self.ResetMissionControl = channel.unary_unary(
        '/routerrpc.Router/ResetMissionControl',
        request_serializer=router__pb2.ResetMissionControlRequest.SerializeToString,
        response_deserializer=router__pb2.ResetMissionControlResponse.FromString,
        )
    self.QueryMissionControl = channel.unary_unary(
        '/routerrpc.Router/QueryMissionControl',
        request_serializer=router__pb2.QueryMissionControlRequest.SerializeToString,
        response_deserializer=router__pb2.QueryMissionControlResponse.FromString,
        )
    self.QueryProbability = channel.unary_unary(
        '/routerrpc.Router/QueryProbability',
        request_serializer=router__pb2.QueryProbabilityRequest.SerializeToString,
        response_deserializer=router__pb2.QueryProbabilityResponse.FromString,
        )
    self.BuildRoute = channel.unary_unary(
        '/routerrpc.Router/BuildRoute',
        request_serializer=router__pb2.BuildRouteRequest.SerializeToString,
        response_deserializer=router__pb2.BuildRouteResponse.FromString,
        )


class RouterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SendPayment(self, request, context):
    """*
    SendPayment attempts to route a payment described by the passed
    PaymentRequest to the final destination. The call returns a stream of
    payment status updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TrackPayment(self, request, context):
    """*
    TrackPayment returns an update stream for the payment identified by the
    payment hash.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EstimateRouteFee(self, request, context):
    """*
    EstimateRouteFee allows callers to obtain a lower bound w.r.t how much it
    may cost to send an HTLC to the target end destination.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendToRoute(self, request, context):
    """*
    SendToRoute attempts to make a payment via the specified route. This method
    differs from SendPayment in that it allows users to specify a full route
    manually. This can be used for things like rebalancing, and atomic swaps.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetMissionControl(self, request, context):
    """*
    ResetMissionControl clears all mission control state and starts with a clean
    slate.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QueryMissionControl(self, request, context):
    """*
    QueryMissionControl exposes the internal mission control state to callers.
    It is a development feature.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QueryProbability(self, request, context):
    """*
    QueryProbability returns the current success probability estimate for a
    given node pair and amount.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BuildRoute(self, request, context):
    """*
    BuildRoute builds a fully specified route based on a list of hop public
    keys. It retrieves the relevant channel policies from the graph in order to
    calculate the correct fees and time locks.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RouterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendPayment': grpc.unary_stream_rpc_method_handler(
          servicer.SendPayment,
          request_deserializer=router__pb2.SendPaymentRequest.FromString,
          response_serializer=router__pb2.PaymentStatus.SerializeToString,
      ),
      'TrackPayment': grpc.unary_stream_rpc_method_handler(
          servicer.TrackPayment,
          request_deserializer=router__pb2.TrackPaymentRequest.FromString,
          response_serializer=router__pb2.PaymentStatus.SerializeToString,
      ),
      'EstimateRouteFee': grpc.unary_unary_rpc_method_handler(
          servicer.EstimateRouteFee,
          request_deserializer=router__pb2.RouteFeeRequest.FromString,
          response_serializer=router__pb2.RouteFeeResponse.SerializeToString,
      ),
      'SendToRoute': grpc.unary_unary_rpc_method_handler(
          servicer.SendToRoute,
          request_deserializer=router__pb2.SendToRouteRequest.FromString,
          response_serializer=router__pb2.SendToRouteResponse.SerializeToString,
      ),
      'ResetMissionControl': grpc.unary_unary_rpc_method_handler(
          servicer.ResetMissionControl,
          request_deserializer=router__pb2.ResetMissionControlRequest.FromString,
          response_serializer=router__pb2.ResetMissionControlResponse.SerializeToString,
      ),
      'QueryMissionControl': grpc.unary_unary_rpc_method_handler(
          servicer.QueryMissionControl,
          request_deserializer=router__pb2.QueryMissionControlRequest.FromString,
          response_serializer=router__pb2.QueryMissionControlResponse.SerializeToString,
      ),
      'QueryProbability': grpc.unary_unary_rpc_method_handler(
          servicer.QueryProbability,
          request_deserializer=router__pb2.QueryProbabilityRequest.FromString,
          response_serializer=router__pb2.QueryProbabilityResponse.SerializeToString,
      ),
      'BuildRoute': grpc.unary_unary_rpc_method_handler(
          servicer.BuildRoute,
          request_deserializer=router__pb2.BuildRouteRequest.FromString,
          response_serializer=router__pb2.BuildRouteResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'routerrpc.Router', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

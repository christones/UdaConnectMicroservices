import grpc

import coordinates_event_pb2
import coordinates_event_pb2_grpc

"""
Simulates user mobiles sending coordinates to gRPC
"""

print("Coordinates sending...")

channel = grpc.insecure_channel("127.0.0.1:30003")
stub = coordinates_event_pb2_grpc.ItemServiceStub(channel)

# Update this with desired payload
user_coordinates = coordinates_event_pb2.EventCoordinatesMessage(
    userId=340,
    latitude=-180,
    longitude=125
)

user_coordinates_2 = coordinates_event_pb2.EventCoordinatesMessage(
    userId=402,
    latitude=-156,
    longitude=39
)

user_coordinates_3 = coordinates_event_pb2.EventCoordinatesMessage(
    userId=150,
    latitude=-200,
    longitude=89
)

user_coordinates_4 = coordinates_event_pb2.EventCoordinatesMessage(
    userId=100,
    latitude=-200,
    longitude=300
)

response_1 = stub.Create(user_coordinates)
response_2 = stub.Create(user_coordinates_2)
response_3 = stub.Create(user_coordinates_3)
response_4 = stub.Create(user_coordinates_4)


print("Coordinates sent...")
print(user_coordinates, user_coordinates_2, user_coordinates_3, user_coordinates_4 )

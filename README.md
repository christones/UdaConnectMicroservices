# UdaConnect
## Overview
### Background
Conferences and conventions are hotspots for making connections. Professionals in attendance often share the same interests and can make valuable business and personal connections with one another. At the same time, these events draw a large crowd and it's often hard to make these connections in the midst of all of these events' excitement and energy. To help attendees make connections, we are building the infrastructure for a service that can inform attendees if they have attended the same booths and presentations at an event.

### Planning message passing strategies 
From studying the source code of the Udaconnect application we derived a dependency graph of three services : connection service, location service and person service. The connection service depends on the two others while location service requests and information about the identifier of the person to locate so as to retrieve his/her longitude and latitude. The remaining part of the system links solely to the connection service which each instance provides to the rest of the world attendees information. We are therefore going to use the three message passing techniques : gRPC, REST and kafka message queues.

### Diagram of the microservices architecture
![image](docs/architecture_design.png) 

### Justifying each strategy 
The message passing techniques we are going to use are gRPC, REST and Kafka message queues. The gRPC will be used by the connection service to access the object values of each location with its corresponding person at the same time. This is because gRPC may be used by modules in a microservice to pass messages with one another. The REST will be implemented between the person service standing as a client to request his/her longitude and latitude to the location service. This is because the response to the request will be received as JSON formattted information. The Kafka message queue shall be made between the user of the application or main program and the connection service. At this level the connection service will act as the producer while the main program will simply consume.

### Screenshots of the pod and services deployments 

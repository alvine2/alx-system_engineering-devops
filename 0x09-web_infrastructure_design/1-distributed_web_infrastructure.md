Design a Three-Server Web Infrastructure for www.foobar.com
Infrastructure Overview
Load Balancer (HAProxy)
Web Server (Nginx)
Application Server
Database Server (MySQL)
Diagram
                             +---------------------+
                             |     Load Balancer   |
                             |      (HAProxy)      |
                             +---------+-----------+
                                       |
              +------------------------+------------------------+
              |                                                 |
      +-------+-------+                                 +-------+-------+
      |   Web Server   |                                 | App Server     |
      |    (Nginx)     |                                 |                |
      +-------+-------+                                 +-------+-------+
              |                                                 |
              +------------------------+------------------------+
                                       |
                               +-------+-------+
                               |   Database    |
                               |    (MySQL)    |
                               +---------------+
##Components and Justifications
##Load Balancer (HAProxy)

Purpose: Distributes incoming traffic across multiple servers to ensure no single server becomes a bottleneck, thus increasing availability and reliability.
Distribution Algorithm: Round Robin
How it works: Requests are distributed evenly across all servers in the pool in a circular order. Each server gets the same amount of requests in turn, ensuring equal load distribution.
Setup: Active-Active
Active-Active: Multiple servers handle traffic simultaneously, providing load balancing and high availability.
Active-Passive: One server handles traffic while another waits on standby to take over in case of failure.
Web Server (Nginx)

Purpose: Serves static content, handles HTTP requests, and forwards dynamic requests to the application server.
Setup: Handles incoming requests for static files (HTML, CSS, JavaScript) and proxies dynamic requests to the application server.
Application Server

Purpose: Runs the application codebase, processes dynamic requests, interacts with the database, and generates dynamic content.
Setup: Executes the business logic of the application and responds to requests from the web server.
Database Server (MySQL)

Purpose: Stores and manages application data, handles database queries.
Setup: Primary-Replica (Master-Slave) configuration.
Primary Node: Handles all write operations and can also serve read requests.
Replica Node: Handles read operations, replicates data from the primary node to ensure data availability and load distribution.
Issues and Considerations
Single Points of Failure (SPOF)

Database Server: If the primary database server fails, data availability is compromised unless a failover mechanism to the replica is in place.
Load Balancer: If the load balancer fails, the entire web infrastructure becomes inaccessible.
Security Issues

No Firewall: Without a firewall, the servers are exposed to potential unauthorized access and attacks.
No HTTPS: Lack of HTTPS means data is transmitted in plaintext, vulnerable to interception and tampering.
No Monitoring

Issue: Without monitoring, there is no way to track the health and performance of the infrastructure, leading to potential downtime and undiagnosed issues.
Solution: Implement monitoring tools to keep track of server health, load, and performance metrics.


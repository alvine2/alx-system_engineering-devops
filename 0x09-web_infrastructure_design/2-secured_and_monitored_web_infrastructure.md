Design a Secure and Monitored Three-Server Web Infrastructure for www.foobar.com
Infrastructure Overview
Load Balancer (HAProxy) with SSL Termination
Web Server (Nginx)
Application Server
Database Server (MySQL)
Firewalls
SSL Certificate
Monitoring Clients
                     +---------------+
                     | Firewall 1    |
                     +------+--------+
                            |
                            |
                     +------+--------+
                     | Load Balancer |
                     |  (HAProxy)    |
                     +------+--------+
                            | HTTPS
                            |
             +--------------+--------------+
             |                             |
        +----+----+                    +---+----+
        | Firewall 2|                   | Firewall 3|
        +----+----+                    +---+----+
             |                             |
             |                             |
       +-----+-----+                 +-----+-----+
       | Web Server |                 | App Server |
       |   (Nginx)  |                 |            |
       +-----+-----+                 +-----+-----+
             |                             |
             +-------------+---------------+
                           |
                   +-------+-------+
                   |  Database      |
                   |   (MySQL)      |
                   +-------+-------+

Components and Justifications
Load Balancer (HAProxy) with SSL Termination

Purpose: Distributes incoming traffic evenly across multiple servers to ensure no single server becomes a bottleneck, thus increasing availability and reliability.
SSL Termination: Handles SSL encryption/decryption to offload this work from the backend servers, improving their performance.
Distribution Algorithm: Round Robin
How it works: Requests are distributed evenly across all servers in the pool in a circular order.
Web Server (Nginx)

Purpose: Serves static content and handles HTTP/HTTPS requests. Proxies dynamic requests to the application server.
Setup: Secures web traffic and forwards requests to the application server.
Application Server

Purpose: Executes the business logic of the application, processes dynamic requests, interacts with the database, and generates dynamic content.
Setup: Processes requests from the web server and interacts with the database server.
Database Server (MySQL)

Purpose: Stores and manages application data, handles database queries.
Setup: Primary-Replica (Master-Slave) configuration.
Primary Node: Handles all write operations and can also serve read requests.
Replica Node: Handles read operations, replicates data from the primary node to ensure data availability and load distribution.
Firewalls

Purpose: Protects the network by controlling incoming and outgoing traffic based on predetermined security rules.
Firewall 1: Protects the load balancer from unauthorized access.
Firewall 2: Protects the web server from unauthorized access.
Firewall 3: Protects the application server from unauthorized access.
SSL Certificate

Purpose: Encrypts data between the client and the server to ensure secure communication.
Reason: Protects sensitive data and ensures privacy and data integrity.
Monitoring Clients

Purpose: Collects data about the performance and health of the servers.
Setup: Install monitoring clients (e.g., Sumologic) on each server to collect metrics and logs.
How it works: The monitoring clients gather data and send it to a central monitoring service for analysis and alerting.
Issues and Considerations
Terminating SSL at the Load Balancer

Issue: Terminating SSL at the load balancer means the traffic between the load balancer and backend servers is unencrypted, which can be a security risk.
Solution: Use end-to-end encryption to ensure traffic remains encrypted between the load balancer and backend servers.
Single MySQL Server for Writes

Issue: Having only one MySQL server capable of accepting writes creates a single point of failure and can become a performance bottleneck.
Solution: Implement MySQL clustering or database sharding to distribute the write load and increase availability.
Homogeneous Server Components

Issue: If all servers have the same components (database, web server, application server), it can lead to inefficient resource usage and increased complexity in management.
Solution: Separate the roles of servers (e.g., dedicated web, application, and database servers) to optimize resource utilization and simplify management.
Monitoring Specifics
Purpose of Monitoring

Purpose: Monitoring ensures the infrastructure is operating correctly, identifies issues before they become critical, and provides data for performance tuning.
Data Collection: Monitoring clients collect metrics (CPU, memory usage, disk I/O, network traffic) and logs (error messages, access logs) and send them to a central monitoring service.
Monitoring Web Server QPS (Queries Per Second)

###Steps:
Configure the monitoring client to track the number of HTTP requests per second.
Send this data to the central monitoring service.
Set up alerts to notify when QPS exceeds a certain threshold, indicating potential performance issues or traffic spikes.
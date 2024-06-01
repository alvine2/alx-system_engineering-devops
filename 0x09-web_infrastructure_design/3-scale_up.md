Infrastructure Design for www.foobar.com
This document outlines the design of a secure, scalable, and monitored web infrastructure for hosting the website www.foobar.com. The infrastructure incorporates the separation of web server, application server, and database components, and includes redundancy and monitoring for improved performance and reliability.

Components and Configuration
Servers

Load Balancers (HAProxy)
Two HAProxy instances configured in a cluster to distribute incoming traffic evenly and provide redundancy.
Web Server
One Nginx server dedicated to serving static content and forwarding dynamic requests to the application server.
Application Server
One server dedicated to running the application code, processing business logic, and handling dynamic requests.
Database Server
One MySQL server for storing and managing application data.
Load Balancer (HAProxy)

Purpose: Distributes incoming traffic across web and application servers to ensure high availability and load balancing.
Configuration: Active-Active cluster setup to provide redundancy and improve fault tolerance.
Algorithm: Round Robin
How it works: Requests are distributed evenly across all servers in a circular order.
Web Server (Nginx)

Purpose: Handles HTTP/HTTPS requests, serves static content, and forwards dynamic requests to the application server.
Setup: Secures web traffic using HTTPS and communicates with the application server for dynamic content.
Application Server

Purpose: Executes business logic, processes dynamic content, and interacts with the database server.
Setup: Isolated from the web server to optimize performance and security.
Database Server (MySQL)

Purpose: Manages and stores application data, handles database queries.
Setup: Primary-Replica configuration to distribute load and ensure data availability.
Additional Elements and Justifications
Server Addition

Purpose: Adds redundancy and load distribution capabilities.
Reason: Ensures high availability and improves the system’s fault tolerance by distributing the load among multiple servers.
Load Balancer Cluster

Purpose: Provides load balancing with redundancy.
Reason: An Active-Active HAProxy cluster ensures that if one load balancer fails, the other can seamlessly take over, thus preventing downtime.
Split Components

Web Server, Application Server, Database Server
Purpose: Separates different roles to optimize resource usage and security.
Reason: Isolating the web server, application server, and database server improves performance and security by ensuring each server is dedicated to a specific role.
Application Server vs. Web Server
Web Server (Nginx)

Handles: HTTP/HTTPS requests, serving static content (HTML, CSS, JavaScript), and proxying dynamic requests to the application server.
Example: Nginx is often used for handling static content efficiently and forwarding dynamic content requests to backend servers.
Application Server

Handles: Business logic, processing dynamic requests, interacting with the database, and generating dynamic content.
Example: An application server runs the application code (e.g., Node.js, Django, Ruby on Rails) to process user requests.
URLs
HAProxy Documentation
Nginx Documentation
MySQL Documentation
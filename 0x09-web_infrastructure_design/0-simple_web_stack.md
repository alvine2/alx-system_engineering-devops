# One Server Web Infrastructure for www.foobar.com

## Overview

A lot of websites are powered by simple web infrastructure, often composed of a single server with a LAMP stack. Here, we design a one-server web infrastructure that hosts a website reachable via www.foobar.com.

## Components and Roles

1. **Server**: A device or virtual instance with a unique IP address (e.g., 8.8.8.8).
2. **Domain Name**: foobar.com with a www record pointing to the server's IP address.
3. **DNS Record Type**: The `www` in www.foobar.com is a CNAME record pointing to an A record for foobar.com.
4. **Web Server (Nginx)**: Handles HTTP requests, serves static files, forwards dynamic requests to the application server.
5. **Application Server**: Runs the application logic and processes dynamic requests.
6. **Database (MySQL)**: Stores and manages the website's data.
7. **Communication Protocol**: HTTP/HTTPS for secure data transmission between the server and the user's computer.

## Detailed Explanation

### What is a Server?

A server is a device, virtual machine, or program that provides functionality for other programs or devices, known as "clients". In this setup, the server hosts the web server, application server, and database.

### Role of the Domain Name

A domain name provides a human-readable address for a website, making it easier to remember than an IP address. In this case, foobar.com is the domain name.

### DNS Record for www.foobar.com

The `www` is a CNAME record that points to the main domain, which has an A record pointing to the IP address 8.8.8.8.

### Role of the Web Server (Nginx)

The web server (Nginx) handles incoming HTTP/HTTPS requests from users. It serves static content (like HTML, CSS, JavaScript) and forwards dynamic content requests to the application server.

### Role of the Application Server

The application server processes dynamic requests, runs the application logic, and communicates with the database to fetch or store data.

### Role of the Database (MySQL)

The database stores the website’s data in an organized manner, allowing efficient data retrieval and management.

### Communication Protocol

The server uses HTTP/HTTPS to communicate with the user's computer, ensuring secure data transmission.

## Issues with This Infrastructure

1. **Single Point of Failure (SPOF)**: If the server fails, the website becomes unavailable.
2. **Downtime During Maintenance**: Updating the web server or deploying new code requires restarting Nginx, causing temporary downtime.
3. **Scalability**: Limited by the capacity of a single server; high traffic can overwhelm it.



## References

- [Nginx Documentation](https://nginx.org/en/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [DNS Basics](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [HTTPS Overview](https://www.cloudflare.com/learning/ssl/what-is-https/)
- [Web Server Basics](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)


# One Server Web Infrastructure for www.foobar.com

## Design Diagram

![Web Infrastructure Diagram](https://github.com/alvine2/alx-system_engineering-devops.git)

## Components and Roles

1. **Server**: A device or virtual instance with a unique IP address (e.g., 8.8.8.8).
2. **Domain Name**: foobar.com with a www record pointing to the server's IP address.
3. **DNS Record Type**: CNAME record for `www`, A record for `foobar.com`.
4. **Web Server (Nginx)**: Handles HTTP requests, serves static files, forwards dynamic requests.
5. **Application Server**: Runs the application logic and processes dynamic requests.
6. **Database (MySQL)**: Stores and manages the website's data.
7. **Communication Protocol**: HTTP/HTTPS for secure data transmission.

## Issues with This Infrastructure

1. **Single Point of Failure (SPOF)**: If the server fails, the website is unavailable.
2. **Downtime During Maintenance**: Updating the web server or deploying new code requires restarting Nginx, causing temporary downtime.
3. **Scalability**: Limited by the capacity of a single server; high traffic can overwhelm it.

## References

- [Nginx Documentation](https://nginx.org/en/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [DNS Basics](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [HTTPS Overview](https://www.cloudflare.com/learning/ssl/what-is-https/)
- [Web Server Basics](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)


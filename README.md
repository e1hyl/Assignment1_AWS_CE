# UniEvent - University Event Management System

## Overview
UniEvent is a cloud-hosted web application deployed on Amazon Web Services (AWS) that allows university students to browse and discover events. The system automatically fetches real-time event data from the Ticketmaster API and presents them as official university events.

## Architecture
The application is built using the following AWS services:

- **IAM** – Manages secure access and permissions between AWS services
- **VPC** – Isolated network with public and private subnets across two Availability Zones
- **EC2** – Two t2.micro instances running in private subnets hosting the Flask web application
- **S3** – Stores event-related media and posters securely
- **Application Load Balancer** – Distributes incoming traffic across both EC2 instances, ensuring high availability and fault tolerance

## External API
This project uses the **Ticketmaster Discovery API** to fetch real-time event data including event title, date, and venue. Ticketmaster was chosen because it provides structured JSON responses, is publicly available, free to access, and contains rich event information relevant to university students.

## Features
- Browse real-time events fetched from Ticketmaster
- Fault-tolerant design — system remains available even if one EC2 instance fails
- Secure architecture — EC2 instances are in private subnets, only accessible through the load balancer
- Scalable infrastructure following AWS best practices

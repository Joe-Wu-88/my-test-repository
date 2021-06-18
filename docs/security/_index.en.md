---
title: WAF & Shield Automations
weight: 45
---

AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits and bots that may affect availability, compromise security, or consume excessive resources. AWS Shield Advanced is a managed Distributed Denial of Service (DDoS) protection service. Both WAF and Shield Advanced can be deployed on CloudFront.

This solution provides a template for using WAF and Shield Advanced on CloudFront, it will automatically deploy a set of WAF rules and Shield protection groups into your AWS account to secure your web application against DDoS attack, badbot, SQL injection attack, XSS attack and block the IP which has bad reputation.

## Architecture
![Architecture](/images/waf_arch.png)

The CloudFormation template of this solution will automatically deploy a security template which contains AWS services such as WAF, Shield Advanced, Lambda, Athena and API Gateway.

Shield Deployment Lambda function will automatically deploy a protection group and protected resource to protect against DDoS attack. Log Parser Lambda function also invokes Athena to query CloudFront access log and WAF log to find the request whose times is above the threshold, add the IP into WAF to protect against DDoS attack.

When the crawler triggers the trap URL, Badbot Parser Lambda function will add the IP into WAF to stop the crawler crawling the web site content.

CloudWatch will invoke IP List Parser Lambda function at a fixed interval to update the malicious IP list from the third party website.

The automated deployed WAF rules will protect against SQL injection attack and XSS attack.

The components of this solution can be grouped into the following areas of protection: 


* AWS Managed Rules (A): This set of AWS managed core rules provides protection against exploitation of a wide range of common application vulnerabilities or other unwanted traffic.
* Manual IP lists (B and C): This component creates two specific AWS WAF rules that allow you to manually insert IP addresses that you want to block or allow.
* SQL Injection (D) and XSS (E): The solution configures two native AWS WAF rules that are designed to protect against common SQL injection or cross-site scripting (XSS) patterns in the URI, query string, or body of a request.
* HTTP flood (F): This component protects against attacks that consist of a large number of requests from a particular IP address, such as a web-layer DDoS attack or a brute-force login attempt.
* Scanners and Probes (G): This component parses application access logs searching for suspicious behavior, such as an abnormal amount of errors generated by an origin. It then blocks those suspicious source IP addresses for a customer-defined period of time.
* IP Reputation Lists (H): This component is the IP Lists Parser AWS Lambda function which checks third-party IP reputation lists hourly for new ranges to block.
* Bad Bots (I): This component automatically sets up a honeypot, which is a security mechanism intended to lure and deflect an attempted attack.
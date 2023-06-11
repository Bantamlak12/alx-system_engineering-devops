# 0x19. Postmortem

-   Disclaimer: The incident below is self-created for learning purposes; this outage did not happen in ALX.

## Issue Summary

From 3:25 AM to 3:59 AM EAT, the ALX intranet dashboard returned a connectivity issue. It blocked 100% of the students at the school from accessing the learning intranet dashboard for 34 minutes. The root cause of this outage was an invalid configuration of UFW (Uncomplicated Firewall).

## Timeline (all times East African Time)
-   3:25 AM: Outage begins
-   3:25 AM: Monitoring alert
-   3:27 AM: Engineer noticed the connectivity issue
-   3:34 AM: Investigation started on the networking components
-   3:46 AM: networking team found the UFW configuration issue
-   3:52 AM: The configuration was corrected
-   3:59 AM: 100% of connectivity is back online

## Root cause and resolution

The issue was caused by an invalid configuration of UFW (Uncomplicated Firewall) on the server hosting the ALX intranet. This misconfiguration resulted in the server being blocked by ufw, preventing students from accessing the learning dashboard. The invalid firewall rules blocked all incoming connections, including the ones required for students to access the intranet.

To resolve the issue, the network team identified the incorrect UFW configuration and corrected it. The necessary firewall rules were added to allow incoming connections to the ALX intranet. Once the configuration was fixed, the server regained connectivity, and students were able to access the learning dashboard again.

## Corrective and Preventative Measures

To prevent similar issues in the future:
-   Improve firewall configuration review process
-   Implement a thorough review process for firewall configurations to avoid any invalid or incorrect rules being applied.
-   Conduct regular audits and testing of firewall configurations to ensure they align with security best practices and do not inadvertently block legitimate traffic.

### Tasks to Address the Issue:

-   Conduct a comprehensive review of all firewall configurations to identify any other potential misconfigurations.
-   Establish a regular auditing process to review firewall configurations.
-   Provide additional training and documentation to the team responsible for managing firewall configurations.

We apologize for the inconvenience caused by this outage and are committed to continuously improving our systems to provide a seamless learning experience for all ALX School students.
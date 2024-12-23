**AWS Control Tower Cost Monitoring Architecture**
This repository contains a Python script that generates a visual architecture diagram of an AWS-based cost monitoring solution using the Diagrams library. The diagram includes AWS services like Control Tower, Organizations, Cost Explorer, Cost Anomaly Detection, QuickSight, and more.

The goal of the architecture is to demonstrate how to monitor AWS cost and usage across multiple organizational units (OUs) within AWS Control Tower, leveraging services like SNS for alerts, Lambda for custom functions, and CloudWatch for monitoring.

**Table of Contents**
Prerequisites
Installation
How to Use
Architecture Overview
Diagram
License

**Prerequisites:**
Python 3.x
Diagrams Library: Used to create the AWS architecture diagram.
Graphviz: Required by the Diagrams library for rendering the visual.

**How to Use**
***1. Run the Python script:***
After setting up the environment and dependencies, run the Python script to generate the architecture diagram:

python Cost_Anomolgy_design.py

***2. View the Diagram:***
The diagram will be saved as a PNG image, and you can open it to visualize the AWS architecture.

**Architecture Overview**
This solution illustrates how AWS services interact for cost monitoring within AWS Control Tower:

**Control Tower:** Manages AWS landing zones and governance across multiple AWS accounts.

**Organizations**: Organizes AWS accounts into different Organizational Units (OUs) such as Development, Testing, and Production.

**Cost and Usage Reports (CUR):** Collects detailed cost and usage data.

**Cost Explorer:** Allows visualization and analysis of cost and usage data.

**Cost Anomaly Detection:** Detects cost anomalies and triggers alerts.

**SNS Topics: **Sends notifications for detected anomalies.

**Lambda Functions:** Executes custom logic based on triggered alerts.

**CloudWatch:** Monitors AWS resources and triggers actions based on defined metrics.

**QuickSight:** Visualizes cost data in custom dashboards for easier analysis.

**Diagram Flow**
AWS Control Tower manages the overall organizational structure and governance.
The Organization Units (OU) represent different business units or environments (Dev, Test, Prod).
Cost & Usage Reports capture the data, which is then processed by Cost Explorer and Cost Anomaly Detection.
Alerts are sent through SNS to Lambda Functions and logged in CloudWatch.
The cost data is visualized using QuickSight Dashboards.
Diagram
Here is an overview of the generated architecture:

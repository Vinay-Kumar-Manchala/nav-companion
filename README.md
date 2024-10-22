# nav-companion

Nav-Companion is a compact application that tracks real-time mutual fund net asset values (NAVs) using Groww's APIs. It provides up-to-date price information for small-cap, mid-cap, and large-cap funds, enabling users to make well-informed, one-time investment decisions (before 2 PM) based on current market conditions.

Tech Stack Used: AWS Lambda, AWS EventBridge, AWS EC2, AWS RDS, Python, Docker, HTML(a little bit). 

AWS Lambda: Python code triggered by AWS EventBridge. 

AWS EventBridge: Scheduled to run from 9:15 AM to 3:45 PM, Monday through Friday with an interval of 30 min.

AWS EC2: A small Fast-API-based application that runs in the docker container of an EC2 instance. This is for visualizing the data at any time we want.

AWS RDS: A PostgreSQL instance for storing the data. Used in Lambda & EC2.

Note: Since this is hosted on AWS Free Tier, the link below might become inactive in the future.

Link: http://ec2-52-54-171-51.compute-1.amazonaws.com:9999/mutual-funds

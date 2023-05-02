Two Way Integrations
==========================

# Video Presentation

https://youtu.be/il_PBq8g7Zo


Prerequisites
-------------

-   Docker and Pyhton should be installed

Setup
-----

1.  Clone this repository and cd into it

2.  Create a virtual environment and activate it

`python3 -m venv env
source env/bin/activate`

3.  Install the project requirements

`pip install -r requirements.txt`

4.  Run the start script

`bash start.sh`

1.  Access the Django application Once the containers are running, you can access the Django application by navigating to `http://localhost:8000` in your web browser.



Additional Notes
----------------

+ Use your stripe key for in workers.
+ use ngrok to tunnel the webhook to `api/v1/myproduct/stripewebhook/`


# For Extending this project

Salesfore customers
-------------------

Plan for Adding a Second Integration with Salesforce's Customer Catalog

To add a second integration with Salesforce's customer catalog, we need to create a new module in our product's codebase that communicates with the Salesforce API to retrieve customer information. We should follow a similar design pattern as the Stripe integration, where we have a queueing system that allows for async communication between our product and Salesforce.

The first step is to create a Salesforce module that handle API calls to retrieve customer data. We can use a library like simple-salesforce to simplify the integration process. Once we have retrieved the customer data, we need to transform it to match the format of our product's customer table (ID, name, email).

Next, we need to integrate this module with our existing architecture that we built for stripe. We should create a worker that listens to a different Kafka topic, where the Salesforce module will publish customer updates. The worker should consume these events and update the customer table in our product's database.

We need to ensure that the Salesforce integration is built in a way that doesn't impact the existing Stripe integration. We should separate the two integrations by creating separate Kafka topics and queues for each integration. This will also allow us to scale each integration independently.

Extending the Integrations to Support Other Systems
---------------------------------------------------

To extend the integrations to support other systems within this project, we will have a modular approach to our code. We should create separate modules for each system that we want to integrate with. These modules should follow a similar pattern as the Salesforce and Stripe integrations, where we retrieve data from the external system, transform it to match our product's data model, and publish it to a Kafka topic.

For integrating with the invoice catalog into our product, we can create a new module that retrieves invoice data from our database and publishes it to a Kafka topic. The format of the data in this topic should match the format of the invoice data in the external system that we want to integrate with.
Similarly, we can create another module that retrieves invoice data from an external system and publishes it to another Kafka topic. This module should also transform the data to match the format of our product's data model.

Once we have data from multiple systems in Kafka topics, we need to merge them into a single topic that is consumed by a worker responsible for updating our product's database. We can use Kafka Streams to create a new topic that aggregates all customer updates from the various systems. The worker can then consume this topic and update the customer table in our product's database.

We are following modular approach to our code design when integrating with other systems within our product. Create separate modules for each system that we want to integrate with and ensure that they follow a similar pattern to our existing integrations.

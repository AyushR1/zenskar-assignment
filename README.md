Two Way Integrations
==========================

#Video Presentation

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
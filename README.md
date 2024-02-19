Welcome to my pizza app! Here's how to get started.

Building and running locally: install all of the dependencies listed in the requirements.txt file. This can be done using 'pip install -r requirements.txt'. To run the application locally, simply run the 'main.py' file using 'python main.py'. This will run the application locally to port 8080. It can be accessed in a web browser by accessing http://127.0.0.1:8080/.

Deployed application: The current version of the application is hosted on GCP, at https://pizza-app-414501.uw.r.appspot.com/.

Testing: Tests are included and are written in Pytest. To run them, navigate to the project folder and run 'pytest' or 'python -m pytest' in a terminal.

Application overview and design choices: I attempted to keep the UI simple, while still making it clear and responsive. To that end I used basic HTML/CSS/Javascript, resulting in a neat and straightforward design. The data is stored in MongoDB collections, which was my choice for a data persistent solution. I used Flask and PyMongo for familiarity and ease of use which allowed me to connect the backend and frontend nicely. Regarding the tests, I wrote them in Pytest which wasn't difficult to configure and setup for the application.

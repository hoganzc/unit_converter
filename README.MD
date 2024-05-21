How to use:
Make sure you have requests, flask, and jsonify installed.
Clone the repository.
Run server.py to start the server.
The microservice will be running at http://127.0.0.1:5000. This can be changed.
Request Data:

To do a conversion a reminder, send a GET request to http://127.0.0.1:5000/api/convert with the data: { "unit": "(insert unit)","amount": (insert number)}

Created and fetched reminders are in JSON format.
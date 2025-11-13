from flask import Flask

# Create an instance of the Flask class.
# __name__ is a convenient shortcut that provides the module's name,
# which helps Flask locate resources like templates and static files.
app = Flask(__name__)

# Use the route() decorator to associate a URL path with a function.
# When a user navigates to the root URL ("/"), this function will be executed.
@app.route("/")
def hello_world():
    # The function returns the content that will be displayed in the browser.
    return "<p>Hello, World!</p>"

# This block ensures the application runs only when the script is executed directly,
# not when imported as a module.
if __name__ == "__main__":
    # Start the Flask development server.
    # debug=True enables debug mode, which provides an interactive debugger
    # and automatically reloads the server on code changes.
    app.run(debug=True)
from OB import create_site
from flask import Flask
from OB import views

# Database configuration
app = create_site()  # application instance

if __name__ == "__main__":
    app.run(debug=True)

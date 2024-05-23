from flask import Flask, render_template, url_for, session, flash, redirect
from functools import wraps
from templates import create_site

#Database configuration
app = create_site()  # application instance

if __name__ == "__main__":
    app.run(debug=True)

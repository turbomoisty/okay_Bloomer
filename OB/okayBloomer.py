from flask import Flask, render_template, url_for, session, flash, redirect
from functools import wraps
from templates import create_site

app = create_site()

if __name__ == "__main__":
    app.run(debug=True)

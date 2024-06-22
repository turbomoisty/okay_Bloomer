from OB import create_site

app = create_site()

if __name__ == "__main__":
    #If something goes wrong with model not recognizing columns, just reset database
   # with app.app_context():
   #     db.drop_all()
   #     db.create_all()
    app.run(debug=True)
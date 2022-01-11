from website import create_app

# To initialize the app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
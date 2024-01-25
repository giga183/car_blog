from src.ext import app

if __name__ == "__main__":
    from src.routes import *
    app.run(debug=True)

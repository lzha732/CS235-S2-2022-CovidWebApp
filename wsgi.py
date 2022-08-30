"""App entry point."""
from covid import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='localhost', port=6000, threaded=False)


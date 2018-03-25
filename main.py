from flask import Flask
import entertainment_center

app = Flask(__name__)


@app.route('/')
def run():
    entertainment_center.run()


if __name__ == "__main__":
    run()

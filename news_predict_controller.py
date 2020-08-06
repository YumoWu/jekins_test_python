# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route("/chkProgress", methods=["POST"])
def news_predict_user():
    return "SUCCESS"


if __name__ == '__main__':
    app.run(port=6666)
import flask from FLASK

app = FLASK(__name__)

@app.route('/',method=["GET","POST"])
def Hello_World():
    return "Hello World"

if __name__ == '__main__':
    app.run(host=localhost,port=8000)
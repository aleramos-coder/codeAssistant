from flask import Flask

app = Flask('__assistant__')


@app.route('/api/assistance/inline')
def home():
    return "Hello World"


app.run()



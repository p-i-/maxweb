'''

To test:
    In chrome URL bar: http://127.0.0.1:5000/?a=42&b=1

NOTE:
    When testing on localhost, it works the first time
    but not subsequet times

    This is the issue:
        https://www.reddit.com/r/flask/comments/ttawkw/access_to_127001_was_denied/

    Solution:
        chrome://net-internals/#sockets
            and "Clear Socket Pools" (!)
'''

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    total = a + b

    # return "Hello world!" + str(total)
    return f'The sum of {a} and {b} is: {total}'

    #if you want to render a .html file, 
    # import render_template from flask and use 
    #render_template("index.html") here.


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080) #go to http://localhost:5000/ to view the page.

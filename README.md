# Hello Web

# Usage


- Run the backend:
```
pip install flask
python myFlask.py
```
^ It's gona run a localhost webserver on port 8080

- Disable CORS in Chrome
    https://chrome.google.com/webstore/detail/cors-unblock/lfhmikememgdcahcdlaciloancbhjino/related?hl=en

    ^ Install this addon, and pin it to the Chrome addons tray

- In Chrome, open `add.html` and click the new addon's icon to DISABLE CORS-control


# Issues:

- Check myFlask.py -- often we need to go to chrome://net-internals/#sockets and "Clear Socket Pools"

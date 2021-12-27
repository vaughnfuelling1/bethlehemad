from flask import Flask
import beth_app

server = Flask(__name__)
created_app = beth_app.CreateApp(server) # create layouts
if __name__ == '__main__':
    print(dir(beth_app))
    created_app.dash_app.run_server(debug=True)


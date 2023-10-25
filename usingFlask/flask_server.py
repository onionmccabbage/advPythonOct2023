from flask import Flask # may need to pip install flask
import sys

# flask offers a pre-built micro-service for a web server
def main():
    '''declare a Flask server'''
    app = Flask(__name__)
    # we define routes within this server
    @app.route('/') # root of the web server
    def root():
        return 'Welcome to this Flask server'
    @app.route('/about')
    def about():
        msg = ' '.join(sys.argv)
        return f'this is the ABOUT content. {msg}'
    @app.route('/web')
    def web():
        page = f'''
<h3>Welcome<h3>
<p>This is an HTML page</p>
<pre>The file server is running: {sys.argv[0]}</pre>
'''
        return page
        
    # kick the server into play....
    app.run()


if __name__ == '__main__':
    main()

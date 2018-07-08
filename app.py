#!flask/bin/python
from flask import Flask, request, Response
from trie.trie import Trie
import json
import sys
from os.path import isfile

app = Flask(__name__)


@app.route('/')
def index():
    keyword = request.args.get('keyword')
    return Response(json.dumps(trie.search(keyword)), status=200, mimetype='application/json')


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if isfile(sys.argv[1]):
            trie = Trie(sys.argv[1])
        else:
            print "File not found"
            exit(1)

    else:
        print "Autocomplete API."
        print "Flask should be installed."
        print "Can be easily install by command: 'pip install flask' "
        print "\t Runs flask API on 127.0.0.1:5000"
        print "\t API request format is 127.0.0.1:5000?keyword=<<keyword>>"
        print "Usage: python app.py <<file_path>>"
        print "\t Warns if the file does not exist."
        print "Quit: You can stop the server by ctrl+c combination"
        exit(1)
    app.run(debug=True)

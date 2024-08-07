from __main__ import app


@app.route('/', methods=['GET'])
def root():
    return 'basic app works'


@app.route('/signup', methods=['PUT'])
def signup(foo):
    # TODO
    return "stuff happened " + foo



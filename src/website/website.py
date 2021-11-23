from bottle import route
import bottle


def load_html(path):
	with open("src/website/public/{path}.html".format(**locals())) as f:
		return bottle.template(f.read())


@route('/static/<filepath:path>')
def server_static(filepath):
	return bottle.static_file(filepath, root='public/')


@route('/')
def home():
	return load_html('/index')

if __name__ == "__main__":
    bottle.run(host="localhost", port=8080, root="public/")
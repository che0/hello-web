import socket
import jinja2
import requests
from flask import Flask


app = Flask(__name__)
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))

FALLBACK_CAT_URL = 'data:image/png,' \
    + 'iVBORw0KGgoAAAANSUhEUgAAAZAAAADIAQMAAAD82yWhAAAABlBMVEUAAAD/AAAb/40iAAAACXBI' \
    + 'WXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH4wMPDCgMHjay7wAAABl0RVh0Q29tbWVudABDcmVhdGVk' \
    + 'IHdpdGggR0lNUFeBDhcAAAItSURBVGje7dgxrtwgEAZgLApKjuBrpIjki0XCXa5FlzJX4AahRAoy' \
    + 'MeC3C/Yw3lklKZL5pV1pn/zZ2MAYnhAcDofD4XA4HA7n38tnOtnIYoLInMLpKN/8kAAxKaW1+4ts' \
    + 'T6EAsovkx0RfyZRJLOerl3RCxrbZESblTPNaL+lURwJGbP3hO7J4hCwHCR0xDiHmILEnFiLrUo7Z' \
    + 'bxwgpw6oZL9yGJIJIltrL/cyJWQMyUw+qZ/9E4PGy4OoTIQKkyUQX8j+aYiKCNGF6N9AAkJmkGiM' \
    + 'LFeirNAeJeFMtBMzRsyPC5lvSPpeiD8Rh5FvV+JRMqWvEFlwEl8mujwqmRRILERqHVObvBA9IHmK' \
    + '2AFx0DyuZG+wjk8Snr1/Q7YzyR28jskcaMTmEjf9WSLzQzZOJ4AkkNijkKaXyfYxKukkUclEJyrV' \
    + 'oUYgmk7m94ghE5tHLelegiAT8SD6xYb58kruyT7FqGSfyAjJxSd/euLhwY+QGSWmJf41Yuv9dARv' \
    + 'WBoROyYrlZR1R156fRC93pP6BsvTxmVSKsKoJnckr039fqQuRGGkVspY16Y7KQVUSAe+X+STqAcx' \
    + 'lRxdPCCxJUeZPt6wGJEtsY8BMCBTqF9Pst4R4etXaZI+atrRmzc7B7MdBSq8suxpFlTNxgEk1zWa' \
    + 'bPYN0BJOQGv6iO5FbiLfIIm+FYNKzE2SpRNHJsaTyRLJZKY/ZU0nf6f739iJiy/8Lw8Oh8PhcDgc' \
    + 'Duc/yS9O2VrJbYYKJgAAAABJRU5ErkJggg=='

@app.route("/")
def hello():
    return "Hello World, from {}".format(socket.gethostname())


@app.route("/cat")
def cat():
    try:
        response = requests.get(
            'https://api.thecatapi.com/v1/images/search',
            timeout=1)
        cat_url = response.json()[0]['url']
    except requests.exceptions.Timeout:
        cat_url = FALLBACK_CAT_URL

    template = jinja_env.get_template('cat.html')
    return template.render({
        'cat_url': cat_url,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

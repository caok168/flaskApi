from . import inference


@inference.route("/")
def index():
    return "index"


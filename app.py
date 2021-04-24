from flask import Flask, request, render_template, jsonify
from textgenrnn import textgenrnn

# from os import path, walk

app = Flask(__name__)


TEXTGENRNN = textgenrnn(
    weights_path="weights/birmd_weights.hdf5",
    vocab_path="weights/birmd_vocab.json",
    config_path="weights/birmd_config.json",
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_birmd", methods=["GET"])
def get_birmd():
    birmd_name = TEXTGENRNN.generate(return_as_list=True, temperature=1.2)[0]
    return jsonify({"birmd_name": birmd_name})


# if __name__ == "__main__":
#     extra_dirs = ["templates", "static"]
#     extra_files = extra_dirs[:]
#     for extra_dir in extra_dirs:
#         for dirname, dirs, files in walk(extra_dir):
#             for filename in files:
#                 filename = path.join(dirname, filename)
#                 if path.isfile(filename):
#                     extra_files.append(filename)
#     app.run(extra_files=extra_files, debug=True)

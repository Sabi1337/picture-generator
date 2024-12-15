from flask import Flask, request, jsonify, render_template, send_file
from pathlib import Path
from datetime import datetime
import requests
import io
import base64
from PIL import Image
import webbrowser
import threading

STATIC_GENERATED_IMAGES = Path("static/generated_images")
DOWNLOADS_FOLDER = Path.home() / "Downloads"
API_URL = "http://127.0.0.1:7860"

app = Flask(__name__, static_folder="static")

STATIC_GENERATED_IMAGES.mkdir(parents=True, exist_ok=True)

def get_available_samplers():
    try:
        response = requests.get(f"{API_URL}/sdapi/v1/samplers")
        if response.status_code == 200:
            samplers = response.json()
            return [sampler["name"] for sampler in samplers]
        else:
            print(f"Keine Samplers gefunden: {response.status_code}, {response.text}")
            return []
    except Exception as e:
        print(f"Error fetching samplers: {e}")
        return []

def get_available_models():
    try:
        response = requests.get(f"{API_URL}/sdapi/v1/sd-models")
        if response.status_code == 200:
            models = response.json()
            return [model["model_name"] for model in models]
        else:
            print(f"Keine modelle gefunden: {response.status_code}, {response.text}")
            return []
    except Exception as e:
        print(f"Error fetching models: {e}")
        return []

@app.route("/")
def index():
    models = get_available_models()
    samplers = get_available_samplers()
    return render_template("index.html", styles=models, samplers=samplers)

@app.route("/generate_txt2img", methods=["POST"])
def generate_txt2img():
    try:
        prompt = request.form.get("prompt", "")
        negative_prompt = request.form.get("negative-prompt", "")
        model = request.form.get("model", get_available_models()[0])
        width = int(request.form.get("width", 256))
        height = int(request.form.get("height", 256))
        steps = int(request.form.get("steps", 20))
        sampler = request.form.get("sampler", get_available_samplers()[0])

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"generated_image_{timestamp}.png"
        file_path = STATIC_GENERATED_IMAGES / file_name

        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "styles": [""],
            "seed": -1,
            "subseed": -1,
            "width": width,
            "height": height,
            "steps": steps,
            "sampler_index": sampler,
            "cfg_scale": 25,
            "send_images": True,
            "save_images": False,
            "alwayson_scripts": {},
            "sd_model_checkpoint": model
        }

        response = requests.post(url=f"{API_URL}/sdapi/v1/txt2img", json=payload)
        if response.status_code == 200:
            r = response.json()
            if "images" not in r:
                return jsonify({"error": "Kein Bild generated"}), 500

            image_data = base64.b64decode(r["images"][0])
            image = Image.open(io.BytesIO(image_data))
            image.save(file_path, "PNG")

            return jsonify({
                "message": "Erfolgreich!",
                "image_url": f"/static/generated_images/{file_name}"
            })
        else:
            return jsonify({"error": f"API error: {response.status_code}, {response.text}"}), 500
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/generate_img2img", methods=["POST"])
def generate_img2img():
    try:
        prompt = request.form.get("prompt", "")
        negative_prompt = request.form.get("negative-prompt", "")
        model = request.form.get("model", get_available_models()[0])
        width = int(request.form.get("width", 512))
        height = int(request.form.get("height", 512))
        steps = int(request.form.get("steps", 50))
        sampler = request.form.get("sampler", "Euler")

        input_image_file = request.files.get("input-image")
        if not input_image_file:
            return jsonify({"error": "Kein Bild für Img2Img gefunden."}), 400

        input_image = Image.open(input_image_file)
        img_byte_arr = io.BytesIO()
        input_image.save(img_byte_arr, format=input_image.format)
        input_image_data = img_byte_arr.getvalue()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"generated_img2img_{timestamp}.png"
        file_path = STATIC_GENERATED_IMAGES / file_name

        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "steps": steps,
            "sampler_index": sampler,
            "init_images": [base64.b64encode(input_image_data).decode("utf-8")],
            "cfg_scale": 25,
            "send_images": True,
            "save_images": False,
            "sd_model_checkpoint": model,
        }

        response = requests.post(f"{API_URL}/sdapi/v1/img2img", json=payload)

        if response.status_code == 200:
            r = response.json()
            if "images" not in r:
                return jsonify({"error": "Keine Bilder gefunden!"}), 500

            image_data = base64.b64decode(r["images"][0])
            image = Image.open(io.BytesIO(image_data))
            image.save(file_path, "PNG")

            return jsonify({
                "message": "Erfolgreich ein Bild erstellt!",
                "image_url": f"/static/generated_images/{file_name}"
            })
        else:
            return jsonify({"error": f"API error: {response.status_code}, {response.text}"}), 500
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/static/generated_images/<filename>")
def serve_generated_image(filename):
    file_path = STATIC_GENERATED_IMAGES / filename
    if file_path.exists():
        return send_file(file_path, mimetype="image/png")
    else:
        return jsonify({"error": "File not found"}), 404

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(debug=True, use_reloader=False)).start()
    threading.Timer(1, open_browser).start()
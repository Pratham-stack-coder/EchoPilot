from flask import Flask, render_template, jsonify
import psutil, platform, socket, datetime, subprocess

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stats")
def stats():
    battery = psutil.sensors_battery()
    disk = psutil.disk_usage("/").percent
    return jsonify({
        "cpu": psutil.cpu_percent(interval=0.2),
        "ram": psutil.virtual_memory().percent,
        "disk": disk,
        "battery": battery.percent if battery else "N/A",
        "hostname": socket.gethostname(),
        "os": platform.system()+" "+platform.release(),
        "time": datetime.datetime.now().strftime("%I:%M:%S %p")
    })

@app.post("/open/chrome")
def open_chrome():
    subprocess.Popen("start chrome", shell=True)
    return {"status":"success"}

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

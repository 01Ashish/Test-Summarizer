from flask import  Flask, render_template, url_for
import requests
from flask import request as req

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/Text_Summarizer",methods=['GET','POST'])
def Text_Summarizer():
    if req.method == "POST":
        headers = {"Authorization": f"Bearer {Token}"}
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

        data = req.form["data"]
        
        maxL = int(req.form["maxL"])
        minL = maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        
        output = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL}
        }
        )[0]
        return render_template('index.html',result=output['summary_text'])
    else:
         return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)

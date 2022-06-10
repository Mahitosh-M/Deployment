from flask import Flask, render_template, request
import pred as p
app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    print("Get method of get method")
    return render_template("index.html")


@app.route("/",methods = ['POST'])
def predict():
    print("Post method of image")
    imagefile= request.files['imagefile']
    image_path= "./images/" + imagefile.filename
    imagefile.save(image_path)
    
    predicted=p.Cancerprediction(image_path)
    
    return render_template('index.html',prediction=predicted)

 


if __name__ == "__main__":
    app.run(port=3008,debug=True)

from flask import Flask,render_template,request
import base64

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods = ['GET','POST'])
def encodePagw():
    if request.method == 'GET':
        return render_template('encode.html')
    else:
        # name = request.form.get('nm')
        # message = request.form.get('msg')
        
        sample_string = request.form.get('nm')
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        return render_template('encodedText.html',base64_string = base64_string)

@app.route('/decode',methods = ['GET','POST'])
def decodePagew():
    if request.method == 'GET':
        return render_template('decode.html')
    else:
    
        base64_string = request.form.get('decodenm')

        base64_bytes = base64_string.encode("ascii")
  
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")

        return render_template('decodedText.html',base64_string = base64_string, sample_string = sample_string)



        

    

        

    
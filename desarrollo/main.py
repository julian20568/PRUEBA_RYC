from flask import Flask, render_template, jsonify, request
import json
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")
    
@app.route('/api/ordenamiento')
def ordenamiento():
    #datos=json.dumps(open('conjunto_numeros.json', encoding="utf8").read())
    datos=json.dumps('conjunto_numeros.json', sort_keys=True)
    return (jsonify(json.loads(open('conjunto_numeros.json').read())))

# Carpeta de subida
app.config['UPLOAD_FOLDER'] = 'C:/wamp64/www/PRUEBA_RYC/desarrollo/Archivos'
#ALLOWED_EXTENSIONS = set(["png","jpg","jpge","gif","pdf","docx","zip","xls","rar"]) validar si queremos subir un tipo de rachivo en especifico

@app.route("/api/archivo")
def upload_file():
 return render_template('archivos.html')

@app.route("/upload", methods=['POST'])
def uploader():
    archivo =''
    cont = {'minusculas': 0, 'mayusculas': 0}
    if request.method == 'POST':
     f = request.files['archivo']
     filename = secure_filename(f.filename)
     f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
     
    for i in archivo:
        if i == i.upper():
            cont['mayusculas'] += 1
        elif i == i.lower():
            cont['minusculas'] += 1
       
    return f"""
            <p>Numero de Mayusculas {cont}</p>
    """

@app.route("/mayusculas/<string:cadena>")
def Contarmayusculas(cadena):
    cont = {'minusculas': 0, 'mayusculas': 0} 
    for i in cadena:
        if i == i.upper():
            cont['mayusculas'] += 1
        elif i == i.lower():
            cont['minusculas'] += 1
       
    return f"""
            <p>Numero de Mayusculas {cont}</p>
    """

  
if __name__ == '__main__':
    app.run(debug=True)

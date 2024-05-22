from flask import Flask, render_template, request
from dati import dabut_rindinas, pierakstit_klat

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def teksts():
    return render_template("teksts.html")

@app.route("/bilde")
def bilde():
    return render_template("bilde.html")

@app.route("/saraksts")
def saraksts():
    saraksts = ["anna", "Katls", "Kartupelis","jyfgnuykascrgu"]
    bildes = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmXZud0R5S1SSQNyGlUlX5eIcAHO1SqTVD0meMrnu0yQ&s","https://arkolat.lv/storage/uploads/global/product_images/image/000/055/684/large/ef387b5ad94e9169c7f220dda11f92da.jpg","https://www.darzaabc.lv/public/assets/images/products/Agrimatco/kartupe%C4%BCi/kartupeli-monalisa-dzeltenie-seklas-kartupelu-stadamais-materials.jpg"]
    kopejais_saraksts=[]
    faila_rindas = dabut_rindinas()
    for rinda in faila_rindas:
        elements=rinda.split(",")
        kopejais_saraksts.append(elements)    
    
    return render_template("saraksts.html", vardi=saraksts, bilde=bildes, garums=len(saraksts), visi=kopejais_saraksts)

@app.route("/info", methods=['POST', 'GET'])
def info():
    if request.method == "POST":
        nosaukums = request.form["nosaukums"]
        adrese = request.form["adrese"]
        rinda = nosaukums + ", " + adrese
        pierakstit_klat(rinda)
    return render_template("info.html")

if __name__ =='__main__':
    app.run(port=5000)


from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = 'senha secreta'

@app.route('/')
def index():
    if 'lista' not in session:
        print("limpando...")
        session['lista'] = []
    print(session['lista'])
    return render_template('tarefas.html', lista=session['lista'])
     
@app.route('/add',methods=['post'])
def adicionar():
    nova = request.form.get('nova')
    lista = session['lista']
    lista.append(nova)
    session['lista'] = lista 
    return redirect('/')

@app.route('/delete/<int:indice>')
def remover(indice):
    lista = session['lista']
    lista.pop(indice)
    session['lista'] = lista
    return redirect('/')

if __name__ == "__main__":
    app.run()
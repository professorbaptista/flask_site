

from flask import Flask, render_template, url_for, redirect, request, flash, session, send_from_directory
import database

app = Flask(__name__)



# secret-key
app.secret_key = 'nzinganzonene2212'
# Criando tabelas
database.criar_tabelas()

# Dicionario de tradução
TRANSLATIONS = {
    'pt': {
        'title': 'Seja bem-vindo ao meu site',
        'cv_link': 'Baixar meu curriculo',
        'change_lang': 'Mudar para inglês'
           },

    'en': {
        'title': 'Well come to my website',
        'cv_link': 'Download My Resume',
        'change_lang': 'Switch to portuguese'
    }
}

# ROTAS 
@app.route("/")
def home():
    # Tradução da lingua portuguesa
    lang = session.get('lang', 'pt')
    texts = TRANSLATIONS[lang]
    return render_template('home.html', texts = texts)

# Rota para tradução
@app.route('/change-lang')
def change_lang():
    current = session.get('lang', 'pt')
    session['lang'] = 'en' if current == 'pt' else 'pt'
    return redirect(url_for('home'))
#Rota Sobre mim
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

# Rota para baixar pdf
@app.route('/download-cv')
def download_cv():
    return send_from_directory("static/livros", "curriculo.pdf", as_attachment=True)

# Rota para envio de contactos.

@app.route('/enviar-contacto', methods=['POST'])
def enviar_contacto():
    name = request.form.get('name')
    email = request.form.get('email')  
    message = request.form.get('message')
    # data = request.form.get('data')  # pode estar vazio se não estiver no form
    print(name, email, message) 

    if not name or not email or not message:
        flash('Todos os campos são obrigatórios.')
        return redirect(url_for('contacts'))  # troque por rota correta

    try:
        conn = database.connectar()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO contactos (name, email, message) VALUES (?, ?, ?)',
            (name, email, message)
        )
        conn.commit()

    except Exception as e:
       
        flash('Erro ao enviar mensagem.')
    finally:
        conn.close()

    flash('Mensagem enviada com sucesso!')
    return redirect(url_for('contacts'))  

@app.route('/enviar-depoimentos', methods=['POST'])
def enviar_depoimentos():
    name = request.form.get('name')
    message = request.form.get('message')
    # data = request.form.get('data')

    if not name or not message:
        flash('Todos os campos são obrigatórios.')
        return redirect(url_for('depoimentos'))

    try:
        conn = database.connectar()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO depoimentos (name, message) VALUES (?, ?)',
            (name, message)
        )
        conn.commit()
    except Exception as e:
        print('Erro ao inserir depoimento: ', e)
        flash('Erro ao enviar depoimento.')
    finally:
        conn.close()

    flash('Depoimento enviado com sucesso!')
    return redirect(url_for('depoimentoDeixado'))

# # Rota para formulario de depoimento
@app.route('/depoimentos', methods=['GET', 'POST'])
def depoimentos():

    return render_template('depoimento.html')

# Rota para exibir os depoimentos
@app.route('/depoimentoDeixado')
def depoimentoDeixado():

    conn = database.connectar()
    cursor = conn.cursor()
    cursor.execute("SELECT name, message, data FROM depoimentos ORDER BY data DESC")

    depoimentos = cursor.fetchall()
    conn.close()
    
    return render_template('depoimentoDeixado.html', depoimentos = depoimentos) 

# Rota para ver os contactos enviados.
@app.route('/contactos-recebidos') 
def contactos_recebidos():
    conn = database.connectar()
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, message, data FROM contactos ORDER BY data DESC")

    contactos = cursor.fetchall()
   
    conn.close()

    return render_template('contactos_recebidos.html', contactos = contactos)

# Rota de informações de contactos
@app.route("/contacts")
def contacts():
   
    return render_template('contacts.html')

# Rota de Login do administrador
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        senha = request.form.get('password')
        if senha == 'nzinganzonene2025':
            session['autenticado'] = True
            flash('Login efetuado com sucesso!')
            return redirect(url_for('admin'))
        else:
            flash('Senha incorreta!')
            return redirect(url_for('login'))

    return render_template('login.html')


# Rota protegida
@app.route('/admin')
def admin():

    if not session.get('autenticado'):
        return redirect(url_for('login'))
    
    conn = database.connectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM contactos")
    total_contactos = cursor.fetchone()[0]
    print('Total de ontactos: ', total_contactos)

    cursor.execute("SELECT COUNT(*) FROM depoimentos")
    total_depoimentos = cursor.fetchone()[0]
    print('Depoimentos: ', total_depoimentos)
    conn.close()

    print("Total contactos:", total_contactos)
    print("Total depoimentos:", total_depoimentos)

    return render_template('admin.html', 
                           total_contactos=total_contactos,
                           total_depoimentos=total_depoimentos)

# Logout
@app.route('/logout')
def logout():
    session.pop('autenticado', None)
    flash('Sessão encerrada!')
    return redirect(url_for('home'))

@app.route("/index")
def index():
    return render_template('index.html')


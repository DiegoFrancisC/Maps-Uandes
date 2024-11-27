from flask import Flask, request, render_template

app = Flask(__name__)

# Base de datos de links de YouTube
youtube_links = {
    "Sala B-32A": "https://www.youtube.com/watch?v=i8OD_r5QUbQ",
    "Laboratorio Innovacion": "https://www.youtube.com/watch?v=8sekyV_o2pM",
    "Aula Magna": "https://www.youtube.com/watch?v=D9G1VOjN_84"
}

@app.route('/')
def home():
    """
    Página principal con un formulario para consultar links.
    """
    return render_template('index.html', variables=list(youtube_links.keys()))

@app.route('/get_link', methods=['POST'])
def get_link():
    """
    Obtiene el link de YouTube asociado al nombre ingresado por el usuario.
    """
    variable = request.form['variable_name']
    link = youtube_links.get(variable)
    if link:
        return render_template('index.html', variables=list(youtube_links.keys()), result=f"El link asociado a '{variable}' es: {link}")
    else:
        return render_template('index.html', variables=list(youtube_links.keys()), result=f"No se encontró un link asociado a '{variable}'. Intenta de nuevo.")

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)  # Habilita el modo de depuración


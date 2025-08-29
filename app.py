from flask import Flask, render_template, request

# Inicializa la aplicación Flask.
app = Flask(__name__)

# Lógica del chatbot basada en reglas.
def get_bot_response(message):
    message = message.lower()
    
    # Reglas para preguntas frecuentes (FAQs)
    if "hola" in message or "saludo" in message:
        return "¡Hola! ¿En qué puedo ayudarte hoy?"
    elif "adios" in message or "chao" in message or "nos vemos" in message:
        return "¡Hasta luego! Si tienes más preguntas, no dudes en volver."
    elif "producto" in message or "catalogo" in message:
        return "Puedes encontrar nuestro catálogo de productos en nuestra página web principal."
    elif "pedido" in message or "orden" in message:
        return "Para rastrear tu pedido, por favor ingresa tu número de orden en la sección 'Seguimiento de pedidos'."
    elif "soporte" in message or "ayuda" in message:
        return "Si necesitas ayuda adicional, puedes contactar a un agente de soporte en vivo. ¿Quieres que te conecte con uno?"
    else:
        # Respuesta por defecto para consultas no reconocidas.
        return "Lo siento, no entiendo esa pregunta. ¿Puedes ser más específico?"

@app.route("/")
def home():
    # Renderiza la plantilla HTML para la interfaz de usuario del chatbot.
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response_api():
    # Recibe el mensaje del usuario de la solicitud POST.
    user_message = request.form["msg"]
    # Obtiene la respuesta del chatbot.
    response = get_bot_response(user_message)
    # Devuelve la respuesta como texto.
    return response

if __name__ == "__main__":
    # Ejecuta el servidor de Flask. El host 0.0.0.0 es necesario para Cloud Run.
    app.run(host='0.0.0.0', port=8080)
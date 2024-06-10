from flask import Flask, render_template, request, jsonify

import code1  # Thay bằng tên module của bạn

app = Flask(__name__)

context = code1.context
model = code1.model
tokenizer = code1.tokenizer

def get_chatbot_response(question):
    context1 = code1.get_context(context, question)
    answer = code1.answer_question(context1, question, model, tokenizer)
    return answer

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["message"]
    bot_response = get_chatbot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(port=5000)  # Ensure the port matches the one used with Ngrok

from flask import Flask, request, jsonify
import openai

openai.api_key = 'XXXX'

app = Flask(__name__)

@app.route('/chat', methods=['GET'])
def chat():
    message = request.args.get('message')
    
    if message is None:
        return jsonify({'error': 'No message provided'}), 400

    messages = [
        {"role": "system", "content": "You are a intelligent assistant."},
        {"role": "user", "content": message}
    ]

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )

    reply = chat.choices[0].message.content

    response = {
        "result": {
            "query": message,
            "reply": reply
        }
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify

from codeAssistantApi.AssistantInlineService import AssistantInlineService

app = Flask('__assistant__')


@app.route('/api/assistance/inline', methods=['POST'])
def getInlineAssistance():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400
    code = data.get('code')
    service = AssistantInlineService()
    try:
        response = service.getInlineAssistance(code)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500


app.run()



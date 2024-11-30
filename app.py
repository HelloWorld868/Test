from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求


@app.route('/')
def index():
    return render_template('index.html')  # 渲染前端页面（假定前端代码放在templates/index.html）


@app.route('/process', methods=['POST'])
def process_form():
    # 从请求中提取数据
    job_description = request.form.get('jobDescription', '')
    resume_data = request.form.get('resumeData', '')
    llm_provider = request.form.get('llmProvider', '')
    api_key = request.form.get('apiKey', '')
    action = request.form.get('action', '')

    # 合并所有表单字段
    combined_data = (
        f"Job Description Text: {job_description}\n"
        f"Resume or Related Data: {resume_data}\n"
        f"LLM Provider: {llm_provider}\n"
        f"API Key: {api_key}\n"
    )

    # 根据不同的按钮，添加相应的附加信息
    if action == 'Get Resume':
        combined_data += "\nGet Resume"
    elif action == 'Get Advice':
        combined_data += "\nGet Advice"
    elif action == 'Resume + Advice':
        combined_data += "\nGet Resume + Advice"

    # 将结果返回为JSON格式，前端处理后显示
    return jsonify({'combinedData': combined_data})


if __name__ == '__main__':
    app.run(debug=True, port=5000)

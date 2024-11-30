import streamlit as st

# 后端处理函数
def process_form(job_description, resume_data, llm_provider, api_key, action):
    """
    模拟后端逻辑，根据用户的操作返回结果。
    """
    result = (
        f"Job Description Text: {job_description}\n"
        f"Resume or Related Data: {resume_data}\n"
        f"LLM Provider: {llm_provider}\n"
        f"API Key: {api_key}\n"
    )
    if action == "Get Resume":
        result += "\nAction: Get Resume"
    elif action == "Get Advice":
        result += "\nAction: Get Advice"
    elif action == "Resume + Advice":
        result += "\nAction: Get Resume + Advice"
    return result


# 加载自定义 HTML/CSS 前端
def render_custom_frontend():
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CareerLift</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #1e1e2e;
                color: #fff;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #282a36;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 600px;
            }
            h1 {
                font-size: 30px;
                text-align: center;
                margin-bottom: 20px;
            }
            .highlight {
                color: green;
                font-weight: bold;
            }
            form {
                display: flex;
                flex-direction: column;
                gap: 15px;
            }
            textarea, input[type="password"], select {
                background-color: #3a3b47;
                color: #fff;
                border: 1px solid #5a5b6b;
                padding: 10px;
                border-radius: 5px;
            }
            .buttons {
                display: flex;
                gap: 10px;
                justify-content: space-between;
            }
            .btn {
                flex: 1;
                padding: 10px;
                background-color: #dc3545;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            .btn:hover {
                background-color: #c82333;
            }
            #result-container {
                margin-top: 20px;
                padding: 20px;
                background-color: #3a3b47;
                border-radius: 8px;
                color: #f1f1f1;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1><span class="highlight">CareerLift:</span> Get Job Aligned Resume</h1>
            <form id="resume-form">
                <label for="job-description">Job Description Text</label>
                <textarea id="job-description" placeholder="Paste Job Description Text Here..."></textarea>

                <label for="resume-upload">Upload Your Resume or Related Data (Text)</label>
                <textarea id="resume-upload" placeholder="Paste Related Data Here..."></textarea>

                <label for="llm-provider">Select LLM Provider:</label>
                <select id="llm-provider">
                    <option value="openai">OpenAI</option>
                </select>

                <label for="api-key">Enter API Key:</label>
                <input type="password" id="api-key" placeholder="API Key">

                <div class="buttons">
                    <button type="button" class="btn" onclick="submitForm('Get Resume')">Get Resume</button>
                    <button type="button" class="btn" onclick="submitForm('Get Advice')">Get Advice</button>
                    <button type="button" class="btn" onclick="submitForm('Resume + Advice')">Resume + Advice</button>
                </div>
            </form>
            <div id="result-container"></div>
        </div>
        <script>
            function submitForm(action) {
                const jobDescription = document.getElementById('job-description').value;
                const resumeData = document.getElementById('resume-upload').value;
                const llmProvider = document.getElementById('llm-provider').value;
                const apiKey = document.getElementById('api-key').value;

                if (!jobDescription || !resumeData || !apiKey) {
                    alert("Please fill in all fields.");
                    return;
                }

                const resultContainer = document.getElementById('result-container');
                resultContainer.textContent = `Processing with action: ${action}...\n\nJob Description: ${jobDescription}\nResume Data: ${resumeData}\nLLM Provider: ${llmProvider}\nAPI Key: ${apiKey}`;
            }
        </script>
    </body>
    </html>
    """
    st.components.v1.html(html_code, height=800)

# Streamlit 应用主函数
def main():
    st.title("CareerLift Web App")
    st.write("This app integrates a custom front-end with Streamlit.")

    # 渲染前端
    render_custom_frontend()


if __name__ == "__main__":
    main()

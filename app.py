import streamlit as st

# 后端处理函数
def process_form(job_description, resume_data, llm_provider, api_key, action):
    """
    模拟后端逻辑，根据用户的操作返回结果。
    """
    # 合并输入数据
    result = (
        f"Job Description Text: {job_description}\n"
        f"Resume or Related Data: {resume_data}\n"
        f"LLM Provider: {llm_provider}\n"
        f"API Key: {api_key}\n"
    )
    
    # 根据用户选择的操作添加相应信息
    if action == "Get Resume":
        result += "\nAction: Get Resume"
    elif action == "Get Advice":
        result += "\nAction: Get Advice"
    elif action == "Resume + Advice":
        result += "\nAction: Get Resume + Advice"
    
    return result

# Streamlit 应用程序
def main():
    st.title("CareerLift: Get Job Aligned Resume")
    st.markdown("### A tool to generate resumes aligned with job descriptions.")
    
    # 输入表单
    with st.form("resume_form"):
        st.write("Fill in the details below:")
        
        # 职位描述
        job_description = st.text_area(
            "Job Description Text",
            placeholder="Paste Job Description Text Here...",
            max_chars=5500
        )
        
        # 简历数据
        resume_data = st.text_area(
            "Upload Your Resume or Related Data (Text)",
            placeholder="Paste Related Data Here...",
            max_chars=5500
        )
        
        # 选择 LLM 提供商
        llm_provider = st.selectbox(
            "Select LLM Provider:",
            options=["OpenAI"]
        )
        
        # 输入 API Key
        api_key = st.text_input(
            "Enter API Key",
            placeholder="API Key",
            type="password"
        )
        
        # 提交按钮
        submitted = st.form_submit_button("Submit")

        # 选择具体的操作
        action = st.radio(
            "Select Action:",
            options=["Get Resume", "Get Advice", "Resume + Advice"]
        )

    # 处理提交逻辑
    if submitted:
        if not job_description or not resume_data or not api_key:
            st.error("Please fill in all the fields.")
        else:
            # 调用后端处理函数
            result = process_form(job_description, resume_data, llm_provider, api_key, action)
            # 显示结果
            st.success("Processing Complete!")
            st.text_area("Result", result, height=300)

# 运行主程序
if __name__ == "__main__":
    main()

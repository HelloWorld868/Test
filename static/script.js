document.addEventListener("DOMContentLoaded", () => {
    // Initialize form elements
    const jobDescriptionInput = document.getElementById("job-description");
    const resumeUploadInput = document.getElementById("resume-upload");
    const charLimitElems = document.querySelectorAll(".char-limit");
    const apiKeyInput = document.getElementById("api-key");
    const toggleVisibilityButton = document.querySelector(".toggle-visibility");
    const resultContent = document.getElementById("result-content");

    // Update character counter
    const updateCharCount = (inputElement, charLimitElem) => {
        charLimitElem.textContent = `${inputElement.value.length}/${inputElement.maxLength}`;
    };

    // Initialize character counters for input fields
    updateCharCount(jobDescriptionInput, charLimitElems[0]);
    updateCharCount(resumeUploadInput, charLimitElems[1]);

    // Attach event listeners to input fields to dynamically update character counters
    jobDescriptionInput.addEventListener("input", () => updateCharCount(jobDescriptionInput, charLimitElems[0]));
    resumeUploadInput.addEventListener("input", () => updateCharCount(resumeUploadInput, charLimitElems[1]));

    // Toggle API key visibility
    toggleVisibilityButton.addEventListener("click", () => {
        if (apiKeyInput.type === "password") {
            apiKeyInput.type = "text";
            toggleVisibilityButton.textContent = "🙈";
        } else {
            apiKeyInput.type = "password";
            toggleVisibilityButton.textContent = "👁️";
        }
    });

    // Handle form submission
    const resumeForm = document.getElementById("resume-form");
    resumeForm.addEventListener("submit", (event) => {
        event.preventDefault(); // Prevent default form submission behavior

        // Extract form data
        const jobDescription = jobDescriptionInput.value.trim();
        const resumeData = resumeUploadInput.value.trim();
        const llmProvider = document.getElementById("llm-provider").value;
        const apiKey = apiKeyInput.value.trim();
        const action = event.submitter.textContent.trim(); // Retrieve the label of the clicked submit button

        // Validate mandatory fields
        if (!jobDescription || !resumeData || !apiKey) {
            alert("Please ensure all required fields are completed!");
            return;
        }

        // Send form data to the backend server
        fetch("http://127.0.0.1:5000/process", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({
                jobDescription: jobDescription,
                resumeData: resumeData,
                llmProvider: llmProvider,
                apiKey: apiKey,
                action: action,
            }),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response returned an error.");
                }
                return response.json();
            })
            .then(data => {
                // Render response data in the UI
                resultContent.textContent = data.combinedData; // Display the output in the preformatted content area
            })
            .catch(error => {
                console.error("Error:", error);
                resultContent.textContent = "An error occurred. Please try again later.";
            });
    });
});

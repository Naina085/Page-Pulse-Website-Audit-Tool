const errorBox = document.getElementById("errorMessage");

// Hide previous error
errorBox.style.display = "none";
errorBox.innerHTML = "";
const button = document.getElementById("analyzeBtn");

button.addEventListener("click", async () => {

    const url = document.getElementById("urlInput").value.trim();

    if (url === "") {
        alert("Please enter a website URL.");
        return;
    }

    // Loading state
    document.getElementById("status").innerHTML = "Analyzing...";
    document.getElementById("statusDot").style.display = "none";
    document.getElementById("responseTime").innerHTML = "--";
    document.getElementById("title").innerHTML = "--";
    document.getElementById("meta").innerHTML = "--";
    document.getElementById("h1Count").innerHTML = "--";
    document.getElementById("missingAlt").innerHTML = "--";
    document.getElementById("wordCount").innerHTML = "--";

    const scoreElement = document.getElementById("seoScore");
    scoreElement.innerHTML = "Analyzing...";
    scoreElement.style.color = "#2563eb";

    button.disabled = true;
    button.innerHTML = "Analyzing...";

    try {

        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        const data = await response.json();

        const statusElement = document.getElementById("status");
        const statusDot = document.getElementById("statusDot");

        statusElement.innerHTML = data.status;
        // Reset
        statusDot.style.background = "#9ca3af";

        // Success
        if (data.status == 200) {
            statusDot.style.display = "inline-block";
            statusDot.style.background = "#22c55e";
        }
        // Redirect
        else if (data.status >= 300 && data.status < 400) {
            statusDot.style.display = "inline-block";
            statusDot.style.background = "#f59e0b";
        }
        // Error
        else {
            statusDot.style.display = "inline-block";
            statusDot.style.background = "#ef4444";
        }
        document.getElementById("responseTime").innerHTML = data.response_time;
        document.getElementById("title").innerHTML = data.title;
        document.getElementById("meta").innerHTML = data.meta;
        document.getElementById("h1Count").innerHTML = data.h1_count;
        document.getElementById("missingAlt").innerHTML = data.missing_alt;
        document.getElementById("wordCount").innerHTML = data.word_count;

        // Show user-friendly error messages
        const errorBox = document.getElementById("errorMessage");

        errorBox.style.display = "none";
        errorBox.innerHTML = "";

        if (data.status === "Timeout") {
            errorBox.style.display = "block";
            errorBox.innerHTML = "⏱️ The request timed out. Please try again.";
        }
        else if (data.status === "Invalid URL") {
            errorBox.style.display = "block";
            errorBox.innerHTML = "❌ Please enter a valid website URL.";
        }
        else if (data.status === "Network Error") {
            errorBox.style.display = "block";
            errorBox.innerHTML = "🌐 Unable to connect to the website.";
        }
        else if (data.status === "Error") {
            errorBox.style.display = "block";
            errorBox.innerHTML =
                "⚠️ Unable to analyze this website. Please try again.";
        }
        // SEO Score
        scoreElement.innerHTML = `${data.seo_score} / 100`;

        if (data.seo_score >= 80) {
            scoreElement.style.color = "#16a34a"; // Green
        } else if (data.seo_score >= 50) {
            scoreElement.style.color = "#f59e0b"; // Orange
        } else {
            scoreElement.style.color = "#dc2626"; // Red
        }

        // Backend error (optional)
        if (data.error) {
            console.log("Backend Error:", data.error);
        }

    } catch (error) {

        console.error(error);

        document.getElementById("status").innerHTML = "Error";
        statusDot.style.display = "inline-block";
        statusDot.style.background = "#ef4444";
        document.getElementById("status").innerHTML = "Error";
        document.getElementById("statusDot").style.background = "#ef4444"; // Red Dot
        document.getElementById("responseTime").innerHTML = "--";
        document.getElementById("title").innerHTML = "Unable to analyze";
        document.getElementById("meta").innerHTML = "--";
        document.getElementById("h1Count").innerHTML = "--";
        document.getElementById("missingAlt").innerHTML = "--";
        document.getElementById("wordCount").innerHTML = "--";

        scoreElement.innerHTML = "-- / 100";
        scoreElement.style.color = "#dc2626";

        errorBox.style.display = "block";
        errorBox.innerHTML =
            "❌ Something went wrong. Please try again.";
    } finally {

        button.disabled = false;
        button.innerHTML = "Analyze";

    }

});
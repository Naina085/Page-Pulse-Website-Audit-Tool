const button = document.getElementById("analyzeBtn");

button.addEventListener("click", async () => {

    const url = document.getElementById("urlInput").value.trim();

    if (url === "") {
        alert("Please enter a website URL.");
        return;
    }

    // Loading state
    document.getElementById("status").innerHTML = "Analyzing...";
    document.getElementById("responseTime").innerHTML = "--";
    document.getElementById("title").innerHTML = "--";
    document.getElementById("meta").innerHTML = "--";
    document.getElementById("h1Count").innerHTML = "--";
    document.getElementById("missingAlt").innerHTML = "--";
    document.getElementById("wordCount").innerHTML = "--";

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

        document.getElementById("status").innerHTML = data.status;
        document.getElementById("responseTime").innerHTML = data.response_time;
        document.getElementById("title").innerHTML = data.title;
        document.getElementById("meta").innerHTML = data.meta;
        document.getElementById("h1Count").innerHTML = data.h1_count;
        document.getElementById("missingAlt").innerHTML = data.missing_alt;
        document.getElementById("wordCount").innerHTML = data.word_count;

        // Show backend error if any
        if (data.error) {
            console.log("Backend Error:", data.error);
        }

    } catch (error) {

        console.error(error);

        document.getElementById("status").innerHTML = "Error";
        document.getElementById("responseTime").innerHTML = "--";
        document.getElementById("title").innerHTML = "Unable to analyze";
        document.getElementById("meta").innerHTML = "--";
        document.getElementById("h1Count").innerHTML = "--";
        document.getElementById("missingAlt").innerHTML = "--";
        document.getElementById("wordCount").innerHTML = "--";

        alert("Something went wrong while analyzing the website.");

    } finally {

        button.disabled = false;
        button.innerHTML = "Analyze";

    }

});
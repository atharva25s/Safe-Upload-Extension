document.getElementById("predictBtn").addEventListener("click", async () => {
  const metadata = {
    filename: document.getElementById("filename").value,
    completefilepath: document.getElementById("filepath").value,
    fileextension: document.getElementById("extension").value,
    filesize_str: document.getElementById("filesize").value
  };

  try {
    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(metadata)
    });

    const result = await response.json();
    document.getElementById("result").innerHTML = `
      <p><strong>Linear Regression:</strong> ${result.linear_regression_prediction.toFixed(2)}</p>
      <p><strong>Random Forest:</strong> ${result.random_forest_prediction.toFixed(2)}</p>
    `;
  } catch (err) {
    document.getElementById("result").innerText = "Failed to get prediction. Check if the server is running.";
    console.error(err);
  }
});
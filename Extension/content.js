document.addEventListener("change", async (event) => {
  console.log("📦 File Checker Extension content script loaded.");
  if (event.target.type === "file" && event.target.files.length > 0) {
    const file = event.target.files[0];

    const metadata = {
      filename: file.name,
      completefilepath: "unknown", // browser security doesn't allow full path access
      fileextension: file.name.split(".").pop(),
      filesize_str: (file.size / 1024).toFixed(2) + "KB",
    };
    console.log(metadata.filename, metadata.fileextension, metadata.filesize_str);
    
    try {
      const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(metadata)
      });

      const result = await response.json();
      if (result.random_forest_prediction > 0.75) {
        const warning = document.createElement("div");
        warning.innerText = `⚠️ Warning: This file may be sensitive! Score: ${result.random_forest_prediction.toFixed(2)}`;
        warning.style.position = "fixed";
        warning.style.top = "10px";
        warning.style.right = "10px";
        warning.style.backgroundColor = "#ffcc00";
        warning.style.padding = "10px";
        warning.style.border = "2px solid #000";
        warning.style.zIndex = 9999;
        warning.style.fontWeight = "bold";
        document.body.appendChild(warning);

        setTimeout(() => warning.remove(), 8000);
      }else{
        console.log("File is safe", result.random_forest_prediction);
      }
    } catch (err) {
      console.error("Prediction failed:", err);
    }
  }
});
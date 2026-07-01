document.getElementById("surveyForm").addEventListener("submit", function(event) {
  event.preventDefault();

  const formData = {
    name: document.getElementById("name").value,
    age: document.getElementById("age").value,
    satisfaction: document.getElementById("satisfaction").value,
    comments: document.getElementById("comments").value
  };

  fetch("http://127.0.0.1:5000/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formData)
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    alert("Thank you! Your response has been saved.");
    document.getElementById("surveyForm").reset();
  })
  .catch(error => {
    console.error("Error:", error);
    alert("Something went wrong saving your response.");
  });
});
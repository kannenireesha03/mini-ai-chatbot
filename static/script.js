function sendMessage() {
  const userInput = document.getElementById("userInput");
  const chatBox = document.getElementById("chatBox");
  const message = userInput.value.trim();

  if (!message) return;

  // Add user message
  chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;

  fetch("/get", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: message })
  })
    .then(res => res.json())
    .then(data => {
      chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    });

  userInput.value = "";
}

const headers = [
  "Professional mobile mechanic",
  "You don’t have to leave your house or office",
  "We come to you, in your safe space."
];

let index = 0;
const headingElement = document.getElementById("dynamic-heading");

function typeHeader(text, callback) {
  headingElement.textContent = "";
  headingElement.style.width = "0";

  let charIndex = 0;
  function typeChar() {
    if (charIndex < text.length) {
      headingElement.textContent += text.charAt(charIndex);
      charIndex++;
      setTimeout(typeChar, 100); // Adjust typing speed
    } else {
      setTimeout(callback, 3000); // Hold the text before moving to the next
    }
  }
  typeChar();
}

function displayHeaders() {
  typeHeader(headers[index], () => {
    index = (index + 1) % headers.length;
    displayHeaders();
  });
}

window.onload = displayHeaders;

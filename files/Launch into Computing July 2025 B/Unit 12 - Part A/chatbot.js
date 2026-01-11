// Chatbot in Javascript 
const readline = require('readline');

// Create the interface for reading input and displaying output
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log("Chatbot: Hello there im your helper, Type 'bye' to exit.");

// Event listener for the line input
rl.on('line', (input) => {
  const msg = input.toLowerCase();  // Convert user input to lowercase

  // Check for different types of responses
  if (msg === 'bye') {
    console.log("Chatbot: Goodbye!");
    rl.close();  // Close the interface when the user types "bye"
  } else if (msg.includes('hello')) {
    console.log("Chatbot: Hi there!");
  } else if (msg.includes('how are you')) {
    console.log("Chatbot: For more advanced answers, contact Amnon my creator!");
  } else {
    console.log("Chatbot: I don't understand that.");
  }
});

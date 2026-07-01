const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("What is your first word? ", (word1) => {
  rl.question("What is your second word? ", (word2) => {
    rl.question("What is your third word? ", (word3) => {
      rl.question("What is your fourth word? ", (word4) => {
        rl.question("What is your fifth word? ", (word5) => {
          rl.question("What is your end for the sentence? ", (end) => {
            
            // Your madlibs function goes here
            function madlibs() {
              console.log(word1, word2, word3, word4, word5 + end);
            }
            
            madlibs();
            rl.close(); // This stops the terminal from hanging
          });
        });
      });
    });
  });
});

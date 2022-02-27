function processData(input) {
  //Enter your code here
  const arr = input.split('\n').slice(1)

  arr.forEach((sentence) => {
    let leftString = []
    let rightString = []

    for (const i in sentence) {
      i % 2 === 0 ? leftString += sentence[i] : rightString += sentence[i]
    }
    console.log(`${leftString} ${rightString}`)
  })
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
  _input += input;
});

process.stdin.on("end", function () {
  processData(_input);
});
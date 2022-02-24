process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
  input_stdin += data;
});

process.stdin.on('end', function () {
  input_stdin_array = input_stdin.split("\n");
  main();
});

// Reads complete line from STDIN
function readLine() {
  return input_stdin_array[input_currentline++];
}

function main() {
  var i = 4
  var d = 4.0
  var s = "HackerRank "
  // Declare second integer, double, and String variables.
  let int_value, double_value, str_value;

  // Read and save an integer, double, and String to your variables.
  int_value = +(readLine());
  double_value = +(readLine());
  str_value = readLine();

  // Print the sum of both integer variables on a new line.
  console.log(i + int_value);

  // Print the sum of the double variables on a new line.
  console.log((d + double_value).toFixed(1));

  // Concatenate and print the String variables on a new line
  // The 's' variable above should be printed first.
  console.log(s + str_value);

}
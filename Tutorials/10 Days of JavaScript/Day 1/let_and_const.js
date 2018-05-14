function main() {
  const PI = Math.PI;

  let r         = parseFloat(readLine());
  let area      = PI * (r * r);
  let perimeter = PI * (2 * r);

  console.log(area);
  console.log(perimeter);

  // Note: There is no closing bracket due to how the HackerRank problem was
  // written.


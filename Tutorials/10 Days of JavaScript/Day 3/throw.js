function isPositive(a) {
  if (a < 0)
    throw Error("Negative Error");

  if (a === 0)
    throw Error("Zero Error");

  return "YES";
}


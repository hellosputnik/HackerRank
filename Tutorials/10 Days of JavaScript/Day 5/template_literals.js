function sides(literals, ...expressions) {
  const [area, perimeter] = expressions;

  const root = Math.sqrt((perimeter * perimeter) - (16 * area))

  const s1 = (perimeter - root) / 4;
  const s2 = (perimeter + root) / 4;

  return ([s1, s2]);
}


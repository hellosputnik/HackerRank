function getCount(objects) {
  let count = 0;

  objects.forEach((object) => count += (object.x == object.y));

  return count;
}


class Polygon {
  constructor(array) {
    this.sides = array;
  }

  perimeter() {
    return this.sides.reduce((sum, side) => sum + side);
  }
}


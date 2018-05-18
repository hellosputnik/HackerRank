function getSecondLargest(nums) {
  let largest = nums[0];
  let secondLargest = nums[0];

  for (let i = 1; i < nums.length; ++i) {
    const num = nums[i];

    // If the number is greater than our current largest, then shift this is
    // our new largest and our previous largest is our second largest.
    if (num > largest) {
      secondLargest = largest;
      largest = num;
      continue;
    }

    if (num !== largest && num > secondLargest) {
      secondLargest = num;
    }
  }

  return secondLargest;
}


function vowelsAndConsonants(s) {
  const vowels = ['a', 'e', 'i', 'o', 'u'];

  const array = s.split("")

  array.filter(c => vowels.includes(c)).map(c => console.log(c));
  array.filter(c => !(vowels.includes(c))).map(c => console.log(c));
}


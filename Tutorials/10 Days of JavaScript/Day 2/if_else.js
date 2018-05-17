function getGrade(score) {
  let grade;

  if (25 < score && score <= 30)
    grade = 'A';

  if (20 < score && score <= 25)
    grade = 'B';

  if (15 < score && score <= 20)
    grade = 'C';

  if (10 < score && score <= 15)
    grade = 'D';

  if (5 < score && score <= 10)
    grade = 'E';

  if (score <= 5)
    grade = 'F';

  return grade;
}

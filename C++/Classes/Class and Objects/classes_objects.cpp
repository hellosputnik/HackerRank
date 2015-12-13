class Student
{

private:

    int scores[5];

public:

    void Input();
    int CalculateTotalScore();

};

void Student::Input()
{
    for(int n = 0; n < 5; ++n)
        cin >> scores[n];
}

int Student::CalculateTotalScore()
{
    int total = 0;

    for(int n = 0; n < 5; ++n)
        total += scores[n];

    return total;
}


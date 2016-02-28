#include <string>

int professors = 1;
int students = 1;

class Person
{

private:

	int age;
	string name;

public:

	virtual void getdata()
    {
        cin >> name >> age;
    }

	virtual void putdata()
    {
        cout << name << " " << age << " ";
    }

};

class Professor : public Person
{
    int id;
    int publications;

public:

    Professor() 
    {
        id = professors++;
    }

    void getdata()
    {
        Person::getdata();

        cin >> publications;
    }

    void putdata()
    {
        Person::putdata();

        cout << publications << " " << id << endl;
    }

};

class Student : public Person
{
    int id;
    int marks[6];

public:

    Student()
    {
        id = students++;
    }

    void getdata()
    {
        Person::getdata();

        cin >> marks[0];
        cin >> marks[1];
        cin >> marks[2];
        cin >> marks[3];
        cin >> marks[4];
        cin >> marks[5];
    }

    void putdata()
    {
        Person::putdata();

        int sum = 0;
        for(int n = 0; n < 6; ++n)
            sum += marks[n];

        cout << sum << " " << id << endl;
    }

};


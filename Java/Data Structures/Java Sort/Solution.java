class Sorter implements Comparator<Student>
{
    public int compare(Student s1, Student s2)
    {
        if(s1.getCgpa() < s2.getCgpa())
            return 1;

        if(s1.getCgpa() == s2.getCgpa())
        {
            if(s1.getFname().compareTo(s2.getFname()) != 0)
                return s1.getFname().compareTo(s2.getFname());
            else
                return s2.getId() - s1.getId();
        }

        // if(s1.getCgpa() > s2.getCgpa())
        return -1;
    }
}


class Add
{
    void add(int... values)
    {
        int sum = 0;

        for(int i = 0; i < values.length; ++i)
        {
            int value = values[i];
            sum += value;
            if(i == (values.length - 1))
                System.out.print(value);
            else
                System.out.print(value + "+");
        }

        System.out.println("=" + sum);
    }
}

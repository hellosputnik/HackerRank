class Printer<E>
{
    public void printArray(E [] array)
    {
        for(int i = 0; i < array.length; ++i)
            System.out.println(array[i]);
    }
}

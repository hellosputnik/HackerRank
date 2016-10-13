// Disclaimer: I did not design this class.
class Calculate
{
    public Calculate output;
    private Scanner cin;

    public Calculate()
    {
        output = this;
        cin = new Scanner(System.in);
    }

    public int get_int_val() throws IOException
    {
        int val = cin.nextInt();

        if(val <= 0)
            throw new NumberFormatException("All the values must be positive");

        return val;
    }

    public double get_double_val() throws IOException
    {
        double val = cin.nextDouble();

        if(val <= 0.0)
            throw new NumberFormatException("All the values must be positive");

        return val;
    }

    public static Volume do_calc()
    {
        return new Volume();
    }

    public void display(double volume)
    {
        System.out.printf("%.3f\n", volume);
    }
}

class Volume
{
    private static final double PI = 3.14159265;

    public double get_volume(int a)
    {
        return (double)(a * a * a);
    }

    public double get_volume(int l, int b, int h)
    {
        return (double)(l * b * h);
    }

    public double get_volume(double r)
    {
        return r * r * r * (2.0 / 3.0) * PI;
    }

    public double get_volume(double r, double h)
    {
        return r * r * h * PI;
    }
}


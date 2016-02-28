class D : public A, public B, public C
{

private:

    int val;

public:

    D()
    {
        val = 1;
    }

    void update_val(int new_val)
    {
        while(!(new_val % 2))
        {
            new_val /= 2;
            A::func(val);
        }
        while(!(new_val % 3))
        {
            new_val /= 3;
            B::func(val);
        }
        while(!(new_val % 5))
        {
            new_val /= 5;
            C::func(val);
        }
    }

    void check(int);

};


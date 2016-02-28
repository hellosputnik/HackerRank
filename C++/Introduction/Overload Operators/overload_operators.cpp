
Complex operator+(const Complex &lhs, const Complex &rhs)
{
    Complex c;

    c.a = lhs.a + rhs.a;
    c.b = lhs.b + rhs.b;

    return c;
}

ostream& operator<<(ostream& out, const Complex& c)
{
    return out << c.a << "+i" << c.b;
}


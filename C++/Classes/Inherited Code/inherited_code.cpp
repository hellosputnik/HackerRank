class BadLengthException : public exception
{
    int n;

public:

    BadLengthException(int n) { this-> n = n; }

    const char* what() const throw ()
    {
        return std::to_string(n).c_str();
    }
};


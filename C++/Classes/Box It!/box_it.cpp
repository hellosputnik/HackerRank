class Box
{

private:

    long long b;
    long long h;
    long long l;

public:

    Box()
    {
        b = 0;
        h = 0;
        l = 0;

        BoxesCreated++;
    }
    
    Box(int length, int breadth, int height)
    {
        b = breadth;
        h = height;
        l = length;

        BoxesCreated++;
    }
    
    Box(const Box& B) : b(B.b), h(B.h), l(B.l)
    {
        BoxesCreated++;
    }
    
    ~Box()
    {
        BoxesDestroyed++;
    }

    int getBreadth() 
    { 
        return b; 
    }
    int getHeight() 
    { 
        return h; 
    }
    int getLength() 
    { 
        return l; 
    }

    long long CalculateVolume()
    {
        return (b * h * l);
    }

    bool operator<(Box &B)
    {
        if(l < B.l)
            return true;
        if(b < B.b && l == B.l)
            return true;
        if(h < B.h && b == B.b && l == B.l)
            return true;
        return false;
    }

};

ostream& operator<<(ostream& out, Box B)
{
    return out << B.getLength() << " " << B.getBreadth() << " " << B.getHeight();
}


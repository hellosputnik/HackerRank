class Rectangle
{

protected:

    int width;
    int height;

public:

    void Display() { std::cout << width << " " << height << std::endl; }

};

class RectangleArea : public Rectangle
{

public:

    void Input() { std::cin >> width >> height; }
    void Display() { std::cout << (width * height) << std::endl; }

};


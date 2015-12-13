template <typename T>
class AddElements
{

private:

    T element;

public:

    AddElements(T element) : element(element) {}
    T add(T element) { return this->element + element; }
    T concatenate(T element) { return this->element + element; }

};


template <typename = void>
int reversed_binary_value()
{
    return 0;
}

template <bool head, bool... tail>
int reversed_binary_value()
{
    return head + 2 * reversed_binary_value<tail...>();
}

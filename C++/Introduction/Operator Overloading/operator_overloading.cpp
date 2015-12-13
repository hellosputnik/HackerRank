#include <vector>

class Matrix
{
public:
    std::vector<std::vector<int>> a;

    friend Matrix operator+(Matrix lhs, const Matrix& rhs)
    {
        Matrix result;

        for(int y = 0; y < lhs.a.size(); ++y)
        {
            vector<int> buffer;

            for(int x = 0; x < lhs.a[y].size(); ++x)
                buffer.push_back(lhs.a[y][x] + rhs.a[y][x]);

            result.a.push_back(buffer);
        }

        return result;
    }
};


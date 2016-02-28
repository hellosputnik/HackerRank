#include <utility>

struct Workshop
{
    int start_time;
    int duration;
    int end_time;
};

struct Available_Workshops
{
    int n;
    Workshop *workshops;
};

Available_Workshops* initialize(int start_time[], int duration[], int n)
{
    Available_Workshops* aw = new Available_Workshops;

    aw->n = n;
    aw->workshops = new Workshop[n];

    for(int i = 0; i < n; ++i)
    {
        aw->workshops[i].start_time = start_time[i];
        aw->workshops[i].duration = duration[i];
        aw->workshops[i].end_time = (start_time[i] + duration[i]);
    }

    return aw;
}

int CalculateMaxWorkshops(Available_Workshops* ptr)
{
    vector<pair<int, int>> pairs;

    for(int i = 0; i < ptr->n; ++i)
        pairs.push_back(make_pair(ptr->workshops[i].end_time, ptr->workshops[i].start_time));

    sort(pairs.begin(), pairs.end());

    int count = 0, end = -1;
    for(auto it = pairs.begin(); it != pairs.end(); ++it)
    {
        if(it->first > end && end <= it->second)
        {
            ++count;
            end = it->first;
        }
    }

    return count;
}


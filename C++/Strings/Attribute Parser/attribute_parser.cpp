#include <iostream>
#include <iterator>
#include <map>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

struct element
{
    std::string name;
    std::map<std::string, std::string> attributes;
    std::string parent;
};

int main(int argc, char **argv)
{
    using namespace std;

    int N, Q;
    vector<string> code, queries;
    map<string, element*> elements;

    cin >> N >> Q;
    cin.ignore(256, '\n');

    string line;

    for(int n = 0; n < N; ++n)
    {
        getline(cin, line);
        code.push_back(line);
    }

    for(int q = 0; q < Q; ++q)
    {
        getline(cin, line);
        queries.push_back(line);
    }

    string parent = "NULL";
    for(auto it = code.begin(); it != code.end(); ++it)
    {
        line = *it;
        line = string(line.begin() + 1, line.end() - 1);

        if(line[0] == '/')
        {
            parent = elements[parent]->parent;
            continue;
        }

        stringstream stream(line);
        vector<string> tokens {istream_iterator<string>{stream}, istream_iterator<string>{}};

        element *e = new element;
        e->name = tokens[0];
        for(auto token = tokens.begin() + 1; token != tokens.end(); ++token)
        {
            e->attributes[*token] = *(token + 2);
            e->attributes[*token] = string(e->attributes[*token].begin() + 1, e->attributes[*token].end() - 1);

            token += 2;
        }
        e->parent = parent;
        parent = e->name;

        elements[e->name] = e;
    }

    for(auto query = queries.begin(); query != queries.end(); ++query)
    {
        line = *query;

        stack<string> tags;
        string attribute, tag;
        for(int i = 0; i < line.size(); ++i)
        {
            switch(line[i])
            {
            case '.':
                tags.push(tag);
                tag = "";
                break;
            case '~':
                tags.push(tag);
                attribute = string(line.begin() + (i + 1), line.end());
                i = line.size();
                break;
            default:
                tag += line[i];
                break;
            }
        }

        string top = tags.top();
        bool print = true;

        string previous = top;
        while(!tags.empty())
        {
            if(tags.size() == 1)
            {
                if(elements.find(tags.top()) == elements.end() || elements[tags.top()]->parent != "NULL")
                    print = false;
                break;
            }

            tags.pop();

            if(elements.find(previous) == elements.end() || elements[previous]->parent != tags.top())
            {
                print = false;
                break;
            }
            previous = tags.top();
        }

        if(print)
            if(elements[top]->attributes.find(attribute) != elements[top]->attributes.end())
                cout << elements[top]->attributes[attribute] << endl;
            else
                cout << "Not Found!" << endl;
        else
            cout << "Not Found!" << endl;
    }

    return 0;
}


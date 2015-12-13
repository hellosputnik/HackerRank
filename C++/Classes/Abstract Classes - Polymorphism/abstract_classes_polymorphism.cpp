class LRUCache : public Cache
{

private:

    int c;
    void remove(Node *n);

public:

    LRUCache(int capacity);

    void set(int, int);
    int get(int);

};

void LRUCache::remove(Node *n)
{
    if(!head)
        return;

    auto it = mp.find(n->key);

    if(it == mp.end())
    {
        return;
    } else {
        if(it->second->key == head->key)
            head = head->next;
        else
            it->second->prev = it->second->next;
        delete it->second;
        mp.erase(it);
        c--;
    }

    /*
    if(head->key == n->key)
    {
        Node *buffer = head;
        head = head->next;
        delete buffer;
        c--;
        return;
    }

    Node *pointer = head;
    while(pointer->next)
    {
        if(pointer->key == n->key)
        {
            Node *buffer = pointer;
            pointer->prev->next = pointer->next; 
            delete buffer;
            c--;
            return;
        }
        pointer = pointer->next;
    }
    */
}

LRUCache::LRUCache(int capacity) 
{
    c = 0;
    cp = capacity;

    head = nullptr;
    tail = nullptr;
}

void LRUCache::set(int key, int value)
{
    Node *n = new Node(key, value);

    if(!head)
    {
        head = n;
        tail = n;
        mp[key] = n;
        c++;
        return;
    }

    // Remove from node from cache if present
    remove(n);

    // Add node to cache as most recently used
    n->next = head;
    head = n;
    mp[key] = n;
    c++;

    // Delete least recently used node if cache is at capacity
    if(c > cp)
    {
        auto it = mp.find(tail->key);
        delete it->second;
        mp.erase(it);

        // Node *buffer = tail;
        // tail = tail->prev;
        // delete buffer;

        c--;
    }
}

int LRUCache::get(int key)
{
    return mp.find(key) != mp.end() ? mp[key]->value : -1;
}


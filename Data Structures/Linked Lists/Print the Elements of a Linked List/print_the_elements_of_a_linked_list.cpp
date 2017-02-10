void Print(Node *head)
{
    while(head)
    {
        std::cout << head->data << std::endl;
        head = head->next;
    }
}


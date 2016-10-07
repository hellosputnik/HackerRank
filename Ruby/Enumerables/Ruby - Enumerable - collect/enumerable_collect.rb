def rot13(secret_messages)
    # Personally, I like secret_messages.map() more.
    return secret_messages.collect() { |message| message.tr("a-z", "n-za-m"); }
end

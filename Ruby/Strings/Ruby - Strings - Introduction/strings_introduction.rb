def single_quote
    return 'Hello World and others!';
end

def double_quote
    return "Hello World and others!";
end

def here_doc
    string = <<-HERE
        Hello World and others!
    HERE

    return string;
end


def group_by_marks(marks, n)
    return marks.group_by() { |key, value| (value < n) ? "Failed" : "Passed"; }
end


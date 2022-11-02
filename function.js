window.function = function (str, start, end) {
    
    str = str.value ?? "";
    start = start.value ?? 0;
    end = end.value;

    return str.substring(start, end);
}













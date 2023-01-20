url = input()

if "=" in url:
    format_a = url.split("=")
    print(format_a[1])
else:
    format_b = url.rsplit("/", 1)
    print(format_b[-1])

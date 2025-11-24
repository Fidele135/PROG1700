def read_file_to_string(filename: str) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error. file Not Found. {filename}")
        return ""

print(read_file_to_string("plaintext.txt"))
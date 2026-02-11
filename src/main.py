# print('Hello from repository!')

def print_author():
    author=""
    # Допишите здесь ваш код
    with open(".env", "r") as f:
        key, var = f.read().split('=')
    if key == "AUTHOR":
        author = var
    print(f"Автор проекта: {author}")

if __name__ == "__main__":
    print_author()

def print_sample_lines(filename, num_lines=20):
    with open(filename, 'r', encoding='utf-8') as f:
        for _ in range(num_lines):
            print(f.readline(), end="")  # end="" is to avoid double newline
    print("\n----------------------------------\n")

if __name__ == "__main__":
    print("Sample lines from tweets_JDOviedoA.txt:")
    print_sample_lines("tweets_JDOviedoA.txt")

    print("Sample lines from tweets_GustavoBolivar.txt:")
    print_sample_lines("tweets_GustavoBolivar.txt")

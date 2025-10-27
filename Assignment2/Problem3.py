import collections


def analyze_powerball(filename="pbnumbers.txt"):
    white_ball_freq = collections.Counter()
    powerball_freq = collections.Counter()
    last_seen = {}
    total_lines = 0

    try:
        with open(filename, 'r') as f:
            for line_number, line in enumerate(f, 1):
                total_lines = line_number
                parts = line.strip().split()
                if not parts or len(parts) != 6:
                    continue

                try:
                    numbers = [int(p) for p in parts]
                except ValueError:
                    continue

                white_balls = numbers[:5]
                powerball = numbers[5]

                white_ball_freq.update(white_balls)
                powerball_freq.update([powerball])

                for num in white_balls:
                    last_seen[num] = line_number

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    if total_lines == 0:
        print("The file is empty or could not be read.")
        return

    print("--- 10 Most Common Numbers (1-69) ---")
    for num, freq in white_ball_freq.most_common(10):
        print(f"Number {num}: {freq} times")

    print("\n--- 10 Least Common Numbers (1-69) ---")
    all_white_freqs = []
    for i in range(1, 70):
        all_white_freqs.append((i, white_ball_freq[i]))

    all_white_freqs.sort(key=lambda x: x[1])

    for num, freq in all_white_freqs[:10]:
        print(f"Number {num}: {freq} times")

    print("\n--- 10 Most Overdue Numbers (1-69) ---")
    overdue_list = []
    for i in range(1, 70):
        last_draw = last_seen.get(i, 0)
        draws_ago = total_lines - last_draw
        overdue_list.append((i, draws_ago))

    overdue_list.sort(key=lambda x: x[1], reverse=True)

    for num, ago in overdue_list[:10]:
        if ago == total_lines:
            print(f"Number {num}: Never drawn in this dataset")
        else:
            print(f"Number {num}: Last drawn {ago} draws ago")

    print("\n--- Frequency of Each Number (1-69) ---")
    for i in range(1, 70):
        print(f"Number {i:2}: {white_ball_freq[i]:3} times")

    print("\n--- Frequency of Each PowerBall Number (1-26) ---")
    for i in range(1, 27):
        print(f"PowerBall {i:2}: {powerball_freq[i]:3} times")


if __name__ == "__main__":
    analyze_powerball()

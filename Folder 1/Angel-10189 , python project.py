# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

# Read CSV file
try:
    df = pd.read_csv("results.csv")
except FileNotFoundError:
    print("File not found")
    exit()

# 3. Storing marks
marks = []

for i in range(len(df)):
    m = df["Marks"][i]

    if pd.isna(m):
        print("Warning: Row", i+1, "skipped - marks are missing")

    elif m < 0 or m > 100:
        print("Warning: Row", i+1,
              "skipped - marks must be between 0 and 100")

    else:
        marks.append(m)

# 4. Check  marks are valid or not
if len(marks) == 0:
    print("No valid marks found . Nothing to analyse.")

else:

    # printing statements
    while True:
        print("\n1. Show Statistics")
        print("2. Pass Percentage and Distribution")
        print("3. Exit")

        choice = input("Enter choice: ")

        #  Statistics
        if choice == "1":

            total = len(marks)
            passed = 0

            for m in marks:
                if m >= 40:
                    passed += 1

            print("Students:", total)
            print("Mean:", round(np.mean(marks), 2))
            print("Median:", round(np.median(marks), 2))
            print("Mode:", statistics.mode(marks))
            print("Highest:", max(marks))
            print("Lowest:", min(marks))

            if total == 1:
                sd = 0
            else:
                sd = np.std(marks, ddof=1)

            print("Standard deviation:", round(sd, 2))
            print("Pass percentage:", round(passed*100/total, 2), "%")

        #  Pass Percentage and Distribution
        elif choice == "2":

            passed = 0
            failed = 0

            a = 0
            b = 0
            c = 0
            d = 0

            for m in marks:

                if m >= 40:
                    passed += 1
                else:
                    failed += 1

                if m < 40:
                    a += 1
                elif m < 60:
                    b += 1
                elif m < 80:
                    c += 1
                else:
                    d += 1

            print("Passed:", passed)
            print("Failed:", failed)
            print("Pass percentage:",
                  round(passed*100/len(marks), 2), "%")

            print("0-39:", a)
            print("40-59:", b)
            print("60-79:", c)
            print("80-100:", d)

            # Creating Bar Chart
            plt.bar(
                ["0-39", "40-59", "60-79", "80-100"],
                [a, b, c, d]
            )

            plt.xlabel("Marks Range")
            plt.ylabel("Number of Students")
            plt.title("Marks Distribution")
            plt.show()

        # End the program
        elif choice == "3":
            print("Program ended")
            break

        else:
            print("Invalid choice")
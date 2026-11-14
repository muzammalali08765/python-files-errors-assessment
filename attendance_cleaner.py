import csv
from pathlib import Path

INPUT_FILE = Path("attendance.txt")
OUTPUT_FILE = Path("attendance_clean.csv")


def main():
    try:
        with INPUT_FILE.open("r", encoding="utf-8") as file:
            original_names = file.readlines()
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} was not found.")
        print("Place attendance.txt in the same folder as this program.")
        return

    # Clean whitespace and capitalization using a list comprehension.
    cleaned_names = [
        " ".join(name.strip().split()).title()
        for name in original_names
        if name.strip()
    ]

    # A set removes duplicates after names have been standardized.
    unique_students = set(cleaned_names)
    sorted_students = sorted(unique_students)

    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["student_name"])
        for name in sorted_students:
            writer.writerow([name])

    print(f"Original number of records: {len(original_names)}")
    print(f"Unique student count: {len(unique_students)}")
    print("\nCleaned attendance list:")
    for number, name in enumerate(sorted_students, start=1):
        print(f"{number}. {name}")

    print(f"\nCleaned list saved to {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()

import csv

def analyze_transactions(file_path):
    total_income = 0
    total_expense = 0

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            amount = float(row['amount'])
            if amount > 0:
                total_income += amount
            else:
                total_expense += amount

    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Net Balance: {total_income + total_expense}")

if __name__ == "__main__":
    file_path = input("Enter the path to your transactions CSV file: ")
    analyze_transactions(file_path)

import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
    file_path = "expenses.csv"
    
    if not os.path.exists(file_path):
        print("❌ Error: expenses.csv file not found!")
        return None

    try:
        df = pd.read_csv(file_path)

        if df.empty:
            print("❌ Error: Dataset is empty!")
            return None

        if "Category" not in df.columns or "Amount" not in df.columns:
            print("❌ Error: Required columns missing!")
            return None

        return df

    except Exception as e:
        print("❌ Error reading file:", e)
        return None


def analyze_data(df):
    total = df["Amount"].sum()
    avg = df["Amount"].mean()
    max_exp = df["Amount"].max()

    category_sum = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    percentage = (category_sum / total) * 100

    return total, avg, max_exp, category_sum, percentage


def show_analysis(total, avg, max_exp, category_sum, percentage):
    top_category = category_sum.idxmax()

    print("\n========== EXPENSE ANALYSIS ==========\n")

    print(f"Total Expense        : {total}")
    print(f"Average Expense      : {round(avg, 2)}")
    print(f"Maximum Expense      : {max_exp}")

    print("\n----- Category-wise Expense -----")
    print(category_sum.to_string())

    print("\n----- Contribution (%) -----")
    print(percentage.round(2).to_string())

    print(f"\nTop spending category: {top_category}")

    print("\n----- INSIGHTS -----")
    print(f"• Highest spending on: {top_category}")
    print(f"• Total spending     : {total}")
    print(f"• Avg transaction    : {round(avg, 2)}")

    if percentage[top_category] > 40:
        print(f"\n ALERT: High spending on {top_category}!")


def search_category(category_sum):
    category = input("\nEnter category: ").strip().lower()

    category_dict = {cat.lower(): cat for cat in category_sum.index}

    if category in category_dict:
        actual = category_dict[category]
        print(f"{actual} spending: {category_sum[actual]}")
    else:
        print("❌ Category not found")


def visualize(category_sum):
    try:
        category_sum.plot(kind="bar")
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("❌ Error generating chart:", e)


def main():
    df = load_data()

    if df is None:
        print("Exiting program due to errors.")
        return

    total, avg, max_exp, category_sum, percentage = analyze_data(df)

    while True:
        print("\n====== EXPENSE ANALYZER ======")
        print("1. Show Analysis")
        print("2. Search Category")
        print("3. Show Chart")
        print("4. Exit")

        choice = input("Enter choice: ").strip().lower()

        if choice in ["1", "analysis", "show analysis"]:
            show_analysis(total, avg, max_exp, category_sum, percentage)

        elif choice in ["2", "search"]:
            search_category(category_sum)

        elif choice in ["3", "chart", "show chart"]:
            visualize(category_sum)

        elif choice in ["4", "exit", "quit"]:
            print("🎉 Exiting... Thank you!")
            break

        else:
            print("❌ Invalid choice. Try again.")


main()
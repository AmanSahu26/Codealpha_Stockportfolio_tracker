# ============================================================
#   CODEALPHA INTERNSHIP — TASK 2
#   Project  : Stock Portfolio Tracker
#   Author   : Itachi
#   Platform : CodeAlpha Python Programming Internship
# ============================================================

import csv
import os
from datetime import datetime

# ---------- Hardcoded Stock Prices (in USD) ----------
STOCK_PRICES = {
    "AAPL":  182.50,   # Apple Inc.
    "TSLA":  248.00,   # Tesla Inc.
    "GOOGL": 175.30,   # Alphabet Inc.
    "MSFT":  415.20,   # Microsoft Corp.
    "AMZN":  195.80,   # Amazon.com Inc.
    "META":  530.10,   # Meta Platforms Inc.
    "NFLX":  680.40,   # Netflix Inc.
    "NVDA":  875.60,   # NVIDIA Corp.
    "INFY":   21.50,   # Infosys Ltd.
    "TCS":    43.90    # Tata Consultancy Services
}

# ---------- Helper Functions ----------

def show_available_stocks():
    """Display all available stocks with their prices."""
    print("\n" + "-"*40)
    print(f"  {'SYMBOL':<10} {'COMPANY / PRICE':>20}")
    print("-"*40)
    company_names = {
        "AAPL": "Apple Inc.",
        "TSLA": "Tesla Inc.",
        "GOOGL": "Alphabet Inc.",
        "MSFT": "Microsoft Corp.",
        "AMZN": "Amazon.com Inc.",
        "META": "Meta Platforms Inc.",
        "NFLX": "Netflix Inc.",
        "NVDA": "NVIDIA Corp.",
        "INFY": "Infosys Ltd.",
        "TCS": "TCS Ltd."
    }
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<10} ${price:>8.2f}   {company_names[symbol]}")
    print("-"*40)

def get_stock_input():
    """
    Get stock name and quantity from user.
    Returns (symbol, quantity) or None to stop.
    """
    while True:
        symbol = input("\n  Enter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            return None

        if symbol not in STOCK_PRICES:
            print(f"  ⚠  '{symbol}' not found. Please choose from the list above.")
            continue

        while True:
            try:
                qty = int(input(f"  Enter quantity for {symbol}: ").strip())
                if qty <= 0:
                    print("  ⚠  Quantity must be a positive number.")
                else:
                    return (symbol, qty)
            except ValueError:
                print("  ⚠  Please enter a valid integer quantity.")

def calculate_portfolio(portfolio):
    """
    Calculate value of each holding and total investment.
    Returns list of dicts with details.
    """
    results = []
    total   = 0.0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        results.append({
            "symbol": symbol,
            "quantity": qty,
            "price_per_share": price,
            "total_value": value
        })

    return results, total

def display_portfolio(results, total):
    """Pretty-print the portfolio summary."""
    print("\n" + "="*60)
    print("            📊  YOUR STOCK PORTFOLIO SUMMARY")
    print("="*60)
    print(f"  {'SYMBOL':<8} {'QTY':>5} {'PRICE/SHARE':>14} {'TOTAL VALUE':>14}")
    print("-"*60)
    for row in results:
        print(f"  {row['symbol']:<8} {row['quantity']:>5} "
              f"${row['price_per_share']:>12.2f} "
              f"${row['total_value']:>12.2f}")
    print("-"*60)
    print(f"  {'TOTAL INVESTMENT':.<40} ${total:>12.2f}")
    print("="*60)

def save_to_csv(results, total, filename="portfolio_report.csv"):
    """Save portfolio results to a CSV file."""
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["CodeAlpha Stock Portfolio Tracker"])
        writer.writerow(["Generated On:", timestamp])
        writer.writerow([])
        writer.writerow(["Symbol", "Quantity", "Price Per Share (USD)", "Total Value (USD)"])
        for row in results:
            writer.writerow([
                row["symbol"],
                row["quantity"],
                f"{row['price_per_share']:.2f}",
                f"{row['total_value']:.2f}"
            ])
        writer.writerow([])
        writer.writerow(["", "", "TOTAL INVESTMENT", f"{total:.2f}"])

    print(f"\n  💾  Portfolio saved to: {filepath}")

def save_to_txt(results, total, filename="portfolio_report.txt"):
    """Save portfolio results to a TXT file."""
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "w") as f:
        f.write("=" * 60 + "\n")
        f.write("   CodeAlpha — Stock Portfolio Tracker Report\n")
        f.write(f"   Generated On: {timestamp}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"  {'SYMBOL':<8} {'QTY':>5} {'PRICE/SHARE':>14} {'TOTAL VALUE':>14}\n")
        f.write("-" * 60 + "\n")
        for row in results:
            f.write(f"  {row['symbol']:<8} {row['quantity']:>5} "
                    f"${row['price_per_share']:>12.2f} "
                    f"${row['total_value']:>12.2f}\n")
        f.write("-" * 60 + "\n")
        f.write(f"  {'TOTAL INVESTMENT':.<40} ${total:>12.2f}\n")
        f.write("=" * 60 + "\n")

    print(f"  📄  Portfolio also saved to: {filepath}")

# ---------- Main ----------

def main():
    print("\n" + "="*60)
    print("    💹  WELCOME TO STOCK PORTFOLIO TRACKER  💹")
    print("         CodeAlpha Python Internship — Task 2")
    print("="*60)

    # Show available stocks
    print("\n  📌  Available Stocks:")
    show_available_stocks()

    # Collect user portfolio
    portfolio = {}
    print("\n  Enter your stock holdings (type 'done' when finished):")

    while True:
        result = get_stock_input()
        if result is None:
            if not portfolio:
                print("\n  ⚠  You haven't added any stocks yet!")
                continue
            break
        symbol, qty = result
        if symbol in portfolio:
            portfolio[symbol] += qty
            print(f"  ✅  Updated {symbol}: total quantity = {portfolio[symbol]}")
        else:
            portfolio[symbol] = qty
            print(f"  ✅  Added {symbol} x {qty}")

    # Calculate and display
    results, total = calculate_portfolio(portfolio)
    display_portfolio(results, total)

    # Save option
    print("\n  Do you want to save the report?")
    print("  1 → Save as CSV")
    print("  2 → Save as TXT")
    print("  3 → Save as both CSV and TXT")
    print("  4 → Don't save")

    choice = input("\n  Your choice (1/2/3/4): ").strip()
    if choice == "1":
        save_to_csv(results, total)
    elif choice == "2":
        save_to_txt(results, total)
    elif choice == "3":
        save_to_csv(results, total)
        save_to_txt(results, total)
    else:
        print("\n  Report not saved.")

    print("\n  Thank you for using Stock Portfolio Tracker! 📈\n")

# ---------- Run ----------
if __name__ == "__main__":
    main()

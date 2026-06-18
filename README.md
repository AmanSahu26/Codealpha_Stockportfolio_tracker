# 💹 Stock Portfolio Tracker — CodeAlpha Python Internship Task 2

## 📌 Project Overview
A command-line Stock Portfolio Tracker that lets users input stock names and quantities. It calculates the total investment value based on hardcoded stock prices and optionally saves the report as a `.csv` or `.txt` file.

## 🚀 Features
- 10 predefined stocks with realistic prices (AAPL, TSLA, GOOGL, MSFT, AMZN, META, NFLX, NVDA, INFY, TCS)
- User inputs stock symbol and quantity
- Calculates per-stock value and total investment
- Handles duplicate entries (adds quantities)
- Save report as CSV, TXT, both, or skip
- Timestamps saved reports automatically
- Clean tabular display in terminal

## 🛠 Concepts Used
- Dictionary (`STOCK_PRICES`)
- User `input()` / `print()` (I/O)
- Basic arithmetic
- File handling — `csv` module + `open()` for `.txt`
- `datetime` module
- Functions & loops

## 📁 File Structure
```
CodeAlpha_StockPortfolioTracker/
├── stock_tracker.py
├── portfolio_report.csv   ← generated after saving
└── portfolio_report.txt   ← generated after saving
```

## ▶️ How to Run
```bash
python stock_tracker.py
```

## 📊 Sample Output
```
============================================================
            📊  YOUR STOCK PORTFOLIO SUMMARY
============================================================
  SYMBOL    QTY   PRICE/SHARE     TOTAL VALUE
------------------------------------------------------------
  AAPL        5       $182.50         $912.50
  TSLA       10       $248.00       $2480.00
  NVDA        2       $875.60       $1751.20
------------------------------------------------------------
  TOTAL INVESTMENT................................   $5143.70
============================================================
```

## 👤 Author
**Itachi** — CodeAlpha Python Programming Internship

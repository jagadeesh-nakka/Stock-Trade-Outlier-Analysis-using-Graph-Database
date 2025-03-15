# Stock-Trade-Outlier-Analysis-using-Graph-Database
# Stock Trade Outlier Analysis using Graph Database

## 📌 Project Overview
This project analyzes stock trade transactions to identify **outliers** using a **graph database (Neo4j)**. It applies **Failure Mode and Effect Analysis (FMEA)** to detect anomalies such as:
- **High-value trades** exceeding a threshold.
- **Repeated transactions** within a short time.
- **Unusual trading patterns** between entities.

## 🔧 Technologies Used
- **Neo4j** - Graph database for storing and querying stock transactions.
- **Python** - Data analysis and automation.
- **Pandas** - Handling stock trade datasets.
- **NetworkX & Matplotlib** - Graph visualization.
- **Cypher Query Language (CQL)** - Querying Neo4j for anomaly detection.

## 📂 Dataset
The input dataset (`transactions.csv`) contains:
| Column        | Description  |
|--------------|-------------|
| `transaction_id` | Unique ID for each trade |
| `amount` | Trade value ($) |
| `type` | Trade type (Buy/Sell) |
| `timestamp` | Date & time of trade |
| `sender_id` | Trader initiating the transaction |
| `receiver_id` | Trader receiving the transaction |

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/jagadeesh-nakka/Stock-Trade-Outlier-Analysis-using-Graph-Database.git
cd Stock-Trade-Outlier-Analysis-using-Graph-Database
```
### 2️⃣ Install Dependencies
```sh
pip install pandas neo4j networkx matplotlib
```
### 3️⃣ Start Neo4j Database
- Download & install **Neo4j Desktop** or run a **Neo4j Docker container**.
- Open Neo4j and create a database.
- Set **username** and **password** in the `.env` file.

### 4️⃣ Load Data into Neo4j
Run the script to ingest data:
```sh
python load_data.py
```

## 🧐 How It Works
1. **Load Transactions** → Import CSV data into Neo4j.
2. **Graph Construction** → Model transactions as a graph.
3. **Detect Outliers** → Apply FMEA to identify anomalies.
4. **Visualization** → Highlight suspicious trades in a graph.
5. **Generate Reports** → Output flagged transactions.

## 📊 Sample Query (Cypher)
Find all **high-value transactions (> $10,000):**
```cypher
MATCH (t:Transaction) WHERE t.amount > 10000 RETURN t
```

## 🎯 Future Enhancements
- Integrate **real-time anomaly detection**.
- Use **machine learning** to predict fraudulent trades.
- Enhance visualization with **D3.js**.

## 📝 License
This project is **MIT Licensed** – feel free to use and improve it! 😊

---
🚀 **Contributions are welcome!** Feel free to submit a PR or report issues. 😊


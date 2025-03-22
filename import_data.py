import sqlite3
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv("symptom_disease.csv")  # 确保这个 CSV 在当前目录下！

# 连接 SQLite 数据库（如果不存在，会自动创建）
conn = sqlite3.connect("medical.db")
cursor = conn.cursor()

# 创建 symptom_disease 表
cursor.execute("""
CREATE TABLE IF NOT EXISTS symptom_disease (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom TEXT,
    disease TEXT,
    probability REAL
)
""")

# 插入数据
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO symptom_disease (symptom, disease, probability) VALUES (?, ?, ?)",
        (row["symptom"], row["disease"], row["probability"])
    )

conn.commit()
conn.close()

print("✅ CSV 数据已导入到 medical.db！")

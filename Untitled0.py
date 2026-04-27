import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. VERİ YÜKLEME
# Veriyi Kaggle'dan indirdiğin isimle buraya yaz
df = pd.read_csv('covid_data.csv') 

# 2. VERİ ÖN İŞLEME (Eksik verileri temizleme)
df = df.dropna()
# Kategorik verileri sayısal yapma (Örnek: Yes=1, No=0)
df = df.replace({'Yes': 1, 'No': 0, 'Positive': 1, 'Negative': 0})

# 3. ÖZELLİK SEÇİMİ
X = df.drop('Corona', axis=1) # Bağımsız değişkenler (Semptomlar)
y = df['Corona']             # Hedef değişken (Sonuç)

# 4. EĞİTİM VE TEST AYIRMA (%80 Eğitim, %20 Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. MODEL EĞİTİMİ (RANDOM FOREST)
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)

# 6. PERFORMANS DEĞERLENDİRME
print("--- Random Forest Sonuçları ---")
print(f"Accuracy Score: {accuracy_score(y_test, y_pred)}")
print("\nKarmaşıklık Matrisi (Confusion Matrix):")
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.show()

print("\nDetaylı Rapor:")
print(classification_report(y_test, y_pred))

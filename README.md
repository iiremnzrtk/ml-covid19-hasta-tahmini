# 🦠 COVID-19 Hasta Tahmini - Makine Öğrenmesi Projesi

Bu proje, klinik verilere dayanarak bir bireyin COVID-19 test sonucunun pozitif mi yoksa negatif mi olduğunu tahmin etmek için geliştirilmiştir.

## 📊 1. Veri Seti Tanıtımı
Bu projede Kaggle üzerinde bulunan [COVID-19 Dataset](https://www.kaggle.com/datasets/meirnizri/covid19-dataset) kullanılmıştır. Veri seti; hastaların semptomları (öksürük, ateş, boğaz ağrısı vb.) ve demografik bilgilerini içermektedir.

## 🛠️ 2. Veri Ön İşleme (EDA & Cleaning)
* *Eksik Veri Analizi:* Belirsiz (NaN) değerler temizlendi.
* *Kategorik Veri Dönüştürme:* "Evet/Hayır" şeklindeki veriler, modellerin anlayabileceği 0 ve 1 değerlerine dönüştürüldü (Label Encoding).
* *Veri Görselleştirme:* Hasta olan ve olmayan kişilerin semptom dağılımları incelendi.

## 🤖 3. Kullanılan Algoritmalar
Bu projede performansı karşılaştırmak amacıyla iki farklı algoritma kullanılmıştır:
1. *Logistic Regression:* İstatistikel bir sınıflandırma yöntemidir.
2. *Random Forest:* Birden fazla karar ağacı kullanarak daha yüksek doğruluk sağlar.

## 📈 4. Model Performans Karşılaştırması

| Metrik | Logistic Regression | Random Forest |
| :--- | :--- | :--- |
| *Accuracy* | %85 | %92 |
| *Precision* | %83 | %90 |
| *Recall* | %80 | %88 |

---

## 🚀 Nasıl Çalıştırılır?
1. Kütüphaneleri yükleyin: pip install -r requirements.txt
2. Notebook dosyasını çalıştırın: jupyter notebook covid_prediction.ipynb

---
*Hazırlayan:* İrem Nisa Öztürk  
*Bölüm:* Yapay Zekâ Operatörlüğü  
*Üniversite:* Bartın Üniversitesi

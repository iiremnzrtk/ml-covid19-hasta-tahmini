import seaborn as sns
import matplotlib.pyplot as plt

# Hangi semptomun hastalığı ne kadar etkilediğini gösteren grafik
plt.figure(figsize=(10,6))
feat_importances = pd.Series(rf_model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh', color='teal')
plt.title("COVID-19 Tahmininde En Önemli 10 Belirti")
plt.xlabel("Etki Oranı")
plt.show()

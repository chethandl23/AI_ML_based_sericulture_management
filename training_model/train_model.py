import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os 
import logging
from datetime import datetime
# Set up logging
log_dir = r"C:\major_project_sericulture\logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"model_training_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


df = pd.read_csv(r"C:\major_project_sericulture\data\seri_data.csv")
X = df[['Temperature','Humidity','AQI','air_pressure']]
y = df['Cocoon_SuccessRate']
logging.info("Data loaded successfully from CSV.")
logging.info(f"total data points: {len(df)}")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
models = {
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "SVR": SVR(kernel='rbf'),
    "KNeighbors": KNeighborsRegressor(n_neighbors=5)
}
results = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results[model_name] = {
        "MAE": mae,
        "MSE": mse,
        "R2_Score": r2
    }
    
    print(f"{model_name} Results:")
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")
    print(f"R2 Score: {r2}\n")

    msg = (f"{model_name} - MAE: {mae}, MSE: {mse}, R2 Score: {r2}")
    logging.info(msg)
# Save the best model based on R2 Score
best_model_name = max(results, key=lambda x: results[x]["R2_Score"])
best_model = models[best_model_name]
logging.info(f"Best model selected: {best_model_name} with R2 Score: {results[best_model_name]['R2_Score']}")


joblib.dump(best_model, r"C:\major_project_sericulture\model\best_model.pkl")
logging.info("Best model saved successfully.")
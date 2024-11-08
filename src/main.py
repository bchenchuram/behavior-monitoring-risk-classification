from src.preprocess import load_data, clean_data, feature_engineering, scale_features
from src.model import split_data, train_model, save_model
from src.evaluate import evaluate_model

# Step 1: Load and preprocess the data
df = load_data('data/transactions.csv')
df = clean_data(df)
df = feature_engineering(df)
df = scale_features(df, columns=['transaction_amount', 'transaction_hour'])

# Step 2: Split data and train the model
X_train, X_test, y_train, y_test = split_data(df, target_column='risk_label')
model = train_model(X_train, y_train)

# Step 3: Save and evaluate the model
save_model(model)
evaluate_model(model, X_test, y_test)
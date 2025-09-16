# E-commerce Customer Retention Predictor

This project simulates how an **e-commerce company** can leverage transaction data to **predict which customers are most likely to make repeat purchases**. It implements a complete data science pipeline with a local data lake structure and deep learning model for customer retention prediction.

## 🎯 Project Overview

The project demonstrates a end-to-end machine learning pipeline for customer retention prediction, including:
- **Data Lake Architecture**: Raw → Stage → Processed data layers
- **Data Simulation**: Synthetic e-commerce transaction data
- **Feature Engineering**: RFM analysis, behavioral patterns, and seasonality
- **Deep Learning Model**: TensorFlow neural network for retention prediction
- **Comprehensive Analysis**: Business insights and model interpretability

## 📁 Project Structure

```
ecommerce-retention-predictor/
├── data/
│   ├── raw/                    # Raw data layer
│   │   ├── customers.csv       # Customer information
│   │   ├── products.csv        # Product catalog
│   │   └── transactions.csv    # Transaction history
│   ├── stage/                  # Staging data layer
│   │   ├── cleaned_customers.csv
│   │   ├── cleaned_products.csv
│   │   ├── cleaned_transactions.csv
│   │   └── data_quality_summary.json
│   └── processed/              # Processed data layer
│       ├── customer_features.csv
│       ├── training_data.csv
│       ├── X_features.csv
│       ├── y_target.csv
│       ├── label_encoders.pkl
│       └── feature_engineering_summary.json
├── notebooks/
│   ├── 01_data_ingestion.ipynb      # Data simulation and ingestion
│   ├── 02_data_cleaning.ipynb       # Data cleaning and validation
│   ├── 03_feature_engineering.ipynb # Feature engineering and RFM analysis
│   └── 04_model_training.ipynb      # TensorFlow model training
├── models/
│   ├── retention_model.h5           # Trained TensorFlow model
│   ├── scaler.pkl                   # Feature scaling parameters
│   ├── feature_importance.csv       # Feature importance analysis
│   ├── model_metadata.json          # Model configuration and metrics
│   └── training_history.csv         # Training history
├── requirements.txt             # Python dependencies
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone the repository
git clone https://github.com/KingGeorgeIII/ecommerce-retention-predictor.git
cd ecommerce-retention-predictor

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Pipeline

Execute the notebooks in order:

1. **Data Ingestion**: `notebooks/01_data_ingestion.ipynb`
   - Generates synthetic customer, product, and transaction data
   - Simulates realistic e-commerce patterns and behaviors

2. **Data Cleaning**: `notebooks/02_data_cleaning.ipynb`
   - Performs data quality checks and cleaning
   - Handles missing values and data validation

3. **Feature Engineering**: `notebooks/03_feature_engineering.ipynb`
   - Creates RFM (Recency, Frequency, Monetary) features
   - Develops behavioral and seasonality features
   - Generates target variable for repurchase prediction

4. **Model Training**: `notebooks/04_model_training.ipynb`
   - Trains TensorFlow deep learning model
   - Evaluates model performance
   - Provides business insights and interpretability

## 📊 Key Features

### Data Lake Architecture
- **Raw Layer**: Original data as received from source systems
- **Staging Layer**: Cleaned and validated data
- **Processed Layer**: Analysis-ready features for machine learning

### Feature Engineering
- **RFM Analysis**: Recency, Frequency, Monetary value scoring
- **Behavioral Features**: Purchase patterns, lifetime value, frequency
- **Product Preferences**: Category preferences, price sensitivity
- **Seasonality**: Time-based purchasing patterns
- **Demographics**: Age, gender, location-based features

### Machine Learning Model
- **Architecture**: Deep neural network with 256→128→64→32→1 layers
- **Techniques**: Dropout, batch normalization, L2 regularization
- **Optimization**: Adam optimizer with learning rate scheduling
- **Class Balancing**: Weighted loss function for imbalanced data

## 📈 Model Performance

The trained model achieves strong performance on customer retention prediction:
- **AUC Score**: Typically >0.85 (excellent discriminative ability)
- **Accuracy**: High accuracy with balanced precision/recall
- **Feature Importance**: RFM scores and recent activity are top predictors

## 🔍 Business Insights

Key findings for customer retention:

1. **Recency Matters**: Recent purchase activity is the strongest predictor
2. **Purchase Frequency**: Historical buying frequency indicates future behavior
3. **Monetary Value**: Customer lifetime value correlates with retention
4. **Behavioral Patterns**: Consistent purchasing patterns increase retention probability

## 🛠 Technologies Used

- **Python 3.8+**: Core programming language
- **TensorFlow 2.13+**: Deep learning framework
- **Pandas & NumPy**: Data manipulation and analysis
- **Scikit-learn**: Machine learning utilities and metrics
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebooks**: Interactive development environment

## 📝 Model Usage Example

```python
import tensorflow as tf
import pickle
import numpy as np

# Load trained model and scaler
model = tf.keras.models.load_model('models/retention_model.h5')
with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Predict retention probability for new customer
new_customer_features = scaler.transform(customer_data)
retention_probability = model.predict(new_customer_features)[0][0]

print(f'Customer retention probability: {retention_probability:.3f}')
```

## 📄 Data Schema

### Customers Dataset
- `customer_id`: Unique customer identifier
- `age`, `gender`: Demographics
- `registration_date`: Account creation date
- `city`, `state`: Location information
- `preferred_category`: Primary product category

### Products Dataset
- `product_id`: Unique product identifier
- `product_name`, `brand`: Product information
- `category`: Product category
- `price`, `cost`: Pricing information
- `rating`: Customer rating

### Transactions Dataset
- `transaction_id`: Unique transaction identifier
- `customer_id`, `product_id`: Foreign keys
- `transaction_date`: Purchase date
- `quantity`, `unit_price`, `total_amount`: Purchase details
- `payment_method`, `order_status`: Transaction metadata

## 🤝 Contributing

This project is designed for educational and demonstration purposes. Feel free to:
- Fork the repository and experiment with different features
- Try different model architectures or algorithms
- Add new data sources or features
- Improve the business insights and interpretability

## 📜 License

This project is open source and available under the MIT License.

## 🙋‍♂️ Support

For questions or issues:
1. Check the notebook documentation and comments
2. Review the generated metadata files in each data layer
3. Examine the model training logs and metrics

---

**Note**: This project uses synthetic data for demonstration purposes. In a real-world scenario, you would replace the data simulation step with actual data ingestion from your e-commerce platform.

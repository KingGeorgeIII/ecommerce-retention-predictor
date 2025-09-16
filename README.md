# 🛒 E-commerce Retention Predictor

Este proyecto simula cómo una empresa de **e-commerce** puede aprovechar sus datos de transacciones para **predecir qué clientes tienen mayor probabilidad de volver a comprar**.  

El flujo implementado cubre todo el ciclo de datos:  
**Data Lake → Limpieza → Feature Engineering → Deep Learning → Agente de consultas**.

---

## 🌍 Contexto

En e-commerce, la **retención de clientes** es clave: cuesta mucho menos mantener un cliente que adquirir uno nuevo.  
Sin embargo, muchas empresas no saben **qué clientes tienen más probabilidad de recompra**, y terminan gastando presupuesto en campañas de marketing poco efectivas.

---

## ❌ Problema de negocio

- Los datos de ventas y clientes están dispersos y desorganizados.  
- No existe un pipeline de ingestión ni limpieza.  
- El equipo de marketing trabaja con campañas masivas en lugar de segmentadas.  

---

## ✅ Solución propuesta

1. **Data Lake local**  
   Repositorio de datos organizado en capas (`raw`, `stage`, `processed`).

2. **Pipeline de ingestión y limpieza**  
   - Ingesta de transacciones (ejemplo: dataset simulado de compras).  
   - Limpieza de valores nulos, duplicados y outliers.

3. **Feature Engineering**  
   Variables clave generadas:  
   - Frecuencia de compras.  
   - Monto total gastado.  
   - Tiempo desde la última compra.  
   - Categorías más compradas.

4. **Modelo de Deep Learning**  
   - Red neuronal en TensorFlow/Keras.  
   - Predice la **probabilidad de recompra** en los próximos 30 días.  

5. **Agente de consultas**  
   Una interfaz sencilla (funciones Python) que permite hacer preguntas al modelo, por ejemplo:  
   - *“¿Cuál es la probabilidad de que el cliente 123 vuelva a comprar este mes?”*  
   - *“Dame los 10 clientes más propensos a recomprar.”*

---

## 🎯 Valor de negocio

- **Marketing más inteligente** → campañas dirigidas a los clientes con mayor probabilidad de recompra.  
- **Mejor ROI** → reducción de costos de adquisición y mayor efectividad.  
- **Escalabilidad** → el pipeline se adapta a cualquier dataset de ventas en e-commerce.  

---

## 📂 Estructura del repositorio
```
ecommerce-retention-predictor/
│
├── data/
│ ├── raw/ # datos crudos (ventas, clientes, transacciones)
│ ├── stage/ # datos limpios
│ └── processed/ # datasets listos para ML
│
├── notebooks/
│ ├── 01_ingesta.ipynb # carga de datos en el data lake
│ ├── 02_limpieza.ipynb # limpieza y normalización
│ ├── 03_features.ipynb # feature engineering
│ └── 04_modelo.ipynb # deep learning
│
├── README.md
├── requirements.txt
└── .gitignore


---

## 🚀 Cómo usarlo

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/TUUSUARIO/ecommerce-retention-predictor.git
   cd ecommerce-retention-predictor

   
## 🔮 Próximos pasos
- Integración con FastAPI para exponer el modelo como API.
- Automatización del pipeline con Airflow o Prefect.
- Experimentos con modelos más avanzados (XGBoost, Transformers tabulares).

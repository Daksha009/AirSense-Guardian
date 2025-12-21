# 📊 Model Training Parameters

## 🎯 **Three Main Parameter Categories**

The AQI prediction model is trained using **three main categories of parameters**:

---

## 1️⃣ **Historical AQI Data (Temporal Features)**

These parameters capture the **past AQI patterns** to predict future values:

### **Lag Features:**
- `aqi_lag1` - AQI value 1 hour ago
- `aqi_lag2` - AQI value 2 hours ago
- `aqi_lag3` - AQI value 3 hours ago

### **Rolling Averages:**
- `aqi_rolling_mean_3h` - Average AQI over last 3 hours
- `aqi_rolling_mean_6h` - Average AQI over last 6 hours

### **Current AQI:**
- `aqi` - Current AQI value

**Purpose:** Captures temporal patterns and trends in air quality

---

## 2️⃣ **Time-Based Features (Temporal Context)**

These parameters capture **time-related patterns** that affect air quality:

- `hour` - Hour of the day (0-23)
- `day_of_week` - Day of the week (0-6)
- `month` - Month of the year (1-12)
- `is_weekend` - Binary indicator (0 or 1)

**Purpose:** Captures daily, weekly, and seasonal patterns (e.g., rush hour pollution, weekend patterns)

---

## 3️⃣ **Weather Parameters (Environmental Factors)**

These are the **three key weather parameters** that directly influence air quality:

### **1. Wind Speed** (`wind_speed`)
- **Unit:** km/h
- **Impact:** Higher wind speed disperses pollutants faster
- **Range:** Typically 5-25 km/h

### **2. Humidity** (`humidity`)
- **Unit:** Percentage (%)
- **Impact:** Affects particle suspension and chemical reactions
- **Range:** Typically 30-90%

### **3. Temperature** (`temperature`)
- **Unit:** Celsius (°C)
- **Impact:** Affects chemical reactions and thermal inversions
- **Range:** Typically 15-35°C

**Purpose:** Weather conditions directly affect how pollutants disperse and accumulate

---

## 📋 **Complete Feature List**

The model uses **13 total features**:

1. `aqi` - Current AQI
2. `aqi_lag1` - AQI 1 hour ago
3. `aqi_lag2` - AQI 2 hours ago
4. `aqi_lag3` - AQI 3 hours ago
5. `aqi_rolling_mean_3h` - 3-hour rolling average
6. `aqi_rolling_mean_6h` - 6-hour rolling average
7. `hour` - Hour of day
8. `day_of_week` - Day of week
9. `month` - Month
10. `is_weekend` - Weekend indicator
11. `wind_speed` - Wind speed (km/h)
12. `humidity` - Humidity (%)
13. `temperature` - Temperature (°C)

---

## 🎯 **Model Performance**

With these parameters, the model achieves:
- **R² Score:** 0.733 (73.3% variance explained)
- **RMSE:** 10.56 AQI points
- **MAE:** 8.39 AQI points
- **MAPE:** 8.82%

---

## 🔍 **Why These Three Categories?**

1. **Historical AQI Data:** 
   - Air quality has strong temporal autocorrelation
   - Past values are the best predictors of future values

2. **Time-Based Features:**
   - Pollution patterns follow daily/weekly/seasonal cycles
   - Rush hours, weekends, and seasons affect pollution levels

3. **Weather Parameters:**
   - Wind disperses pollutants
   - Humidity affects particle behavior
   - Temperature influences chemical reactions and inversions

---

## 📊 **Feature Importance**

Based on Random Forest model:
- **Most Important:** Historical AQI features (lag and rolling means)
- **Moderately Important:** Weather parameters (wind, humidity, temperature)
- **Supporting:** Time-based features (hour, day, month)

---

*Documented: 2025-12-20*


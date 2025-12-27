#!/usr/bin/env python3
# Author: Daksha009
# Repo: https://github.com/Daksha009/AirSense-Guardian.git

"""
Complete Training Pipeline Runner
Collects data and trains the model
"""
import sys
import os
import pandas as pd

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_collector import AQIDataCollector
from train_model import AQIModelTrainer

def main():
    print("="*70)
    print("AirSense Guardian - Complete Training Pipeline")
    print("="*70)
    print()
    
    # Step 1: Collect Data
    print("STEP 1: Data Collection")
    print("-" * 70)
    collector = AQIDataCollector()
    
    # Collect from multiple locations for better dataset
    locations = [
        (28.6139, 77.2090, "Delhi"),  # Delhi, India
        (19.0760, 72.8777, "Mumbai"),  # Mumbai, India
        (12.9716, 77.5946, "Bangalore"),  # Bangalore, India
    ]
    
    all_dfs = []
    for lat, lon, city in locations:
        print(f"\nCollecting data for {city} ({lat}, {lon})...")
        openaq_df = collector.fetch_openaq_data(lat, lon, days=30)
        aqicn_df = collector.fetch_aqicn_data(city, days=30)
        
        combined_df = collector.combine_and_process([openaq_df, aqicn_df])
        if not combined_df.empty:
            all_dfs.append(combined_df)
    
    # Combine all location data
    if all_dfs:
        final_df = pd.concat(all_dfs, ignore_index=True)
    else:
        print("\nNo data collected. Using synthetic data generation in training...")
        final_df = None
    
    # Enrich with weather if we have data
    if final_df is not None and not final_df.empty:
        final_df = collector.enrich_with_weather(final_df)
        collector.save_data(final_df, 'aqi_training_data.csv')
        print(f"\nTotal data points collected: {len(final_df)}")
    else:
        print("\nNote: Will use synthetic data generation during training")
    
    print("\n" + "="*70)
    
    # Step 2: Train Model
    print("\nSTEP 2: Model Training")
    print("-" * 70)
    trainer = AQIModelTrainer()
    trainer.train_full_pipeline()
    
    print("\n" + "="*70)
    print("Training Pipeline Complete!")
    print("="*70)
    print("\nYour model is ready to use. Start the Flask server with: python app.py")

if __name__ == '__main__':
    main()


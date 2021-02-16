
# Sample shell script for automating production assets

This simple script does the following:

1. Pull latest copy of production code from main branch
2. Update all production data assets
3. Trigger Streamlit app deployment to refresh UI

```
#!/bin/sh

# Change to project directory and pull down the main branch.
# This ensures the latest production code is deployed
cd ds-squad-project
git checkout main
git pull

# Update all production data assets
python fetch_insert_incidents.py
python train_model.py
python insert_predictions.py
python update_reports.py

# Trigger Streamlit app deployment to refresh visualizations
git commit --allow-empty -m "trigger current streamlit deploy"
git push



```

#!/bin/bash

echo "Creating Customer Experience Dashboard project structure..."

# Create directories
mkdir -p data
mkdir -p modules
mkdir -p assets

# Create main project files
touch app.py
touch requirements.txt
touch README.md
touch innovation_brief.md

# Create module files
touch modules/data_loader.py
touch modules/analysis.py
touch modules/visualizations.py
touch modules/utils.py

# Add default content into requirements.txt
echo "streamlit
pandas
plotly
nltk
numpy
python-dateutil" > requirements.txt

# Add basic README template
echo "# Customer Experience Dashboard
A Streamlit-based web application for analyzing customer feedback.

## Run the app
streamlit run app.py
" > README.md

echo "Project structure created successfully!"

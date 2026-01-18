# Running the Dashboard Locally

The Grand Prix Project includes an interactive dashboard built with Streamlit that allows you to explore F1 telemetry data interactively.

## Prerequisites

Make sure you have Python 3.7+ installed and navigate to the project directory:

```bash
cd "content/projects/Grand Prix Project"
```

## Installation

### Option 1: Using pip with requirements.txt

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Option 2: Manual Installation

```bash
pip install streamlit pandas plotly
```

## Running the Dashboard

Once dependencies are installed, run:

```bash
streamlit run dashboard.py
```

This will:
1. Start a local Streamlit server
2. Open the dashboard automatically in your default browser at `http://localhost:8501`

If it doesn't open automatically, navigate to: **http://localhost:8501**

## Dashboard Features

The interactive dashboard includes:

### Sidebar Controls
- **Select Grand Prix**: Choose between Abu Dhabi, Miami, and Singapore
- **Select Compounds**: Filter by tire type (Hard, Medium, Soft)

### Key Metrics (Top Row)
- Average Lap Time
- Best Lap Time
- Number of Laps Analyzed
- Number of Compounds Used

### Interactive Tabs

**Tab 1: Pace Evolution**
- Line chart showing lap time progression across all laps
- Color-coded by tire compound
- Identifies performance trends and consistency

**Tab 2: Tire Degradation**
- Scatter plot with trend lines showing tire degradation curves
- X-axis: Tire Life (laps)
- Y-axis: Lap Time
- Visualizes how different compounds degrade

**Tab 3: Sector Analysis**
- Box plots comparing sector performance by tire compound
- Identifies which sectors are affected by tire degradation
- Helps identify circuit-specific challenges

## Data Requirements

The dashboard requires `f1_clean_data.csv` to be present in the same directory. This file is already included in the project.

If you're modifying the data:
1. Ensure CSV contains these columns: LAP, NOR_TIME, NOR_COMPOUND, NOR_TIRE_LIFE, NOR_S1, NOR_S2, NOR_S3, Race
2. Place the updated CSV in the project directory
3. Restart the Streamlit app

## Troubleshooting

### Port Already in Use
If port 8501 is already in use:
```bash
streamlit run dashboard.py --server.port 8502
```

### Module Not Found
If you get import errors:
```bash
pip install --upgrade streamlit pandas plotly
```

### Data File Not Found
Ensure `f1_clean_data.csv` is in the same directory as `dashboard.py`

## Tips

- Use the sidebar filters to focus on specific races or tire strategies
- Toggle between tabs to compare different aspects of the data
- The trend lines in the Tire Degradation tab help identify optimal tire performance windows
- Sector analysis reveals where aerodynamic or tire issues manifest

## Next Steps

After exploring the dashboard:
1. Review the analysis in `2_analysis.ipynb` for detailed insights
2. Check `1_Data_Cleaning.ipynb` to understand data processing
3. Export any interesting visualizations for presentations

---

For more information, see the full project page on the portfolio website!

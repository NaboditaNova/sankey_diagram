# Plastic Waste Management Sankey Diagram

This project processes Excel files containing plastic waste management data and generates an interactive Sankey diagram using Plotly. The code is modularized into several Python scripts that handle preprocessing, visualization, and additional helper functions.

## Project Structure

```
.
├── main.py
├── preprocess.py
├── visualization.py
├── additionals.py
├── README.md
├── requirements.txt
└── *.xlsx

```

- **main.py**  
  The main script that orchestrates the data preprocessing and visualization. It also provides an option to enable or disable node annotations.

- **preprocess.py**  
  Contains functions to:
  - Combine and process data from multiple Excel sheets.
  - Generate a summary Excel file.
  - Extract material composition data.
  - Generate an annotations dictionary (HTML–formatted) for specific nodes.

- **visualization.py**  
  Contains functions to:
  - Process hierarchical data from the summary Excel file.
  - Prepare the data for Plotly’s Sankey diagram (build node labels, mapping, and link indices).
  - Create and display the Sankey diagram (with optional annotations).

- **additionals.py**  
  Contains helper functions to:
  - Generate node and link colors.
  - Define node positions (x, y coordinates) based on the desired layout.
  - Generate a list of Plotly annotation dictionaries based on the annotations dictionary.

## Prerequisites

- Python 3.x

Install the required Python libraries using pip:

```bash
pip install requirements.txt
```

## How It Works

1. **Preprocessing (`preprocess.py`)**  
   The code reads an input Excel file (e.g., `2025_01_29_combined_table_implementation.xlsm`) and processes data from multiple sheets. It creates:
   - A combined summary table.
   - A material composition table.
   - An annotations dictionary where each key is a node label and its value is a string.

2. **Data Preparation and Visualization (`visualization.py`)**  
   The summary Excel file is read and used to construct a list of nodes and links. A mapping from node label to index is created so that the link data can reference node indices. The Sankey diagram is then created using Plotly.  
   If annotations are provided, these are added to the diagram.

3. **Additional Functions (`additionals.py`)**  
   This module provides:
   - A function to generate node colors and corresponding link colors.
   - A function to generate x and y positions for each node.
   - A function to generate annotation objects from the annotations dictionary.

4. **Main Script (`main.py`)**  
   The main script performs the following steps:
   - Processes the input Excel file to generate the summary and material composition files.
   - Prepares the nodes, links, colors, and positions for the Sankey diagram.
   - Optionally generates annotations.
   - Calls the visualization function to render the interactive Sankey diagram.

## How to Run the Code

1. **Prepare the Input File:**  
   Ensure that your input Excel file  is in the folder. You can adjust the file paths in `main.py`.

2. **Run the Main Script:**  
   Open a terminal in the project directory and run (or you can run in your IDE of choice):

   ```bash
   python main.py
   ```

   This will:
   - Process the Excel files.
   - Generate the necessary intermediate files.
   - Render and display an interactive Sankey diagram in your web browser.


## Customization

- **Node Positions:**  
  The node positions are defined in `additionals.py` within `generate_node_positions`. You can adjust these values to change the layout of your diagram.

- **Colors:**  
  The color schemes for nodes and links are defined in `additionals.py` within `generate_color_options`. Feel free to modify the RGBA or RGB values as desired.

## License

This project is provided as-is without any warranty.

---

Enjoy visualizing your plastic waste management data!

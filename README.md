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
   - A combined summary table (saved as an Excel file).
   - A material composition table (also saved as an Excel file).
   - An annotations dictionary where each key is a node label and its value is an HTML-formatted string (with the label in bold and extra details following on new lines using `<br>` tags).

2. **Data Preparation and Visualization (`visualization.py`)**  
   The summary Excel file is read and used to construct a list of nodes and links. A mapping from node label to index is created so that the link data can reference node indices. The Sankey diagram is then created using Plotly.  
   If annotations are provided (via a generated list of annotation dictionaries), these are added to the diagram so that extra information is displayed next to specific nodes.

3. **Additional Functions (`additionals.py`)**  
   This module provides:
   - A function to generate 49 preset node colors and corresponding link colors.
   - A function to generate x and y positions for each node (based on a six–level layout).
   - A function to generate annotation objects from the annotations dictionary, using the node positions and the label-to-index mapping.

4. **Main Script (`main.py`)**  
   The main script performs the following steps:
   - Processes the input Excel file to generate the summary and material composition files.
   - Prepares the nodes, links, colors, and positions for the Sankey diagram.
   - Optionally (if enabled via a Boolean flag) generates annotations.
   - Calls the visualization function to render the interactive Sankey diagram.

## How to Run the Code

1. **Prepare the Input File:**  
   Ensure that your input Excel file (e.g., `2025_01_29_combined_table_implementation.xlsm`) is in the expected location. You can adjust the file paths in `main.py` if necessary.

2. **Toggle Annotations (Optional):**  
   In `main.py`, set the variable `show_annotations` to `True` if you want annotations to appear on the diagram, or `False` if you do not.

3. **Run the Main Script:**  
   Open a terminal in the project directory and run:

   ```bash
   python main.py
   ```

   This will:
   - Process the Excel files.
   - Generate the necessary intermediate files.
   - Render and display an interactive Sankey diagram in your web browser.

## Customization

- **Annotations:**  
  The annotations are generated from the material composition Excel file. They include the node label in bold and additional details (with `<br>` used for line breaks). You can customize the formatting in the function `process_excel_generate_annotations` in `preprocess.py`.

- **Node Positions:**  
  The node positions are defined in `additionals.py` within `generate_node_positions`. You can adjust these values to change the layout of your diagram.

- **Colors:**  
  The color schemes for nodes and links are defined in `additionals.py` within `generate_color_options`. Feel free to modify the RGBA or RGB values as desired.

## License

This project is provided as-is without any warranty. You are free to modify and use the code for your own purposes.

---

Enjoy visualizing your plastic waste management data!


Simply copy the above text and paste it into your Markdown editor (or save it as `README.md`) to use it in your project.

#################################
#   Author: Nabodita Anam Nova  #
#################################

import preprocess
import visualization
import color_options as co

input_path = r'2025_01_29_combined_table_implementation.xlsm'
output_path = r'YOUR_FILE_PATH_HERE.xlsx'

preprocess.process_excel(input_path, output_path)

nodes, links = visualization.process_data_hierarchical(output_path)
node_labels, label_to_idx, source_idx, target_idx, values = visualization.prepare_data_for_plotly_sankey(nodes, links)

color_0, color_1 = co.generate_color_options()

diagram_title = "YOUR DIAGRAM TITLE HERE"
visualization.create_sankey_diagram(node_labels, source_idx, target_idx, values, color_0, color_1, diagram_title)
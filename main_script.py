#################################
#   Author: Nabodita Anam Nova  #
#################################

import preprocess
import visualization
import color_options as co

input_excel_path = r'2025_01_29_combined_table_implementation.xlsm'
output_excel_path = r'combined_summary_full_v3.xlsx'
material_composition_output_path = r'combined_material_composition.xlsx'

preprocess.process_excel(input_excel_path, output_excel_path)
preprocess.process_excel_generate_material_composition(input_excel_path, material_composition_output_path)
annotations_dict = preprocess.process_excel_generate_annotations(material_composition_output_path)

nodes, links = visualization.process_data_hierarchical(output_excel_path)
node_labels, label_to_index, source_indices, target_indices, values = visualization.prepare_data_for_plotly_sankey(nodes, links)

node_colors, link_colors = co.generate_color_options(links, label_to_index)
node_x, node_y = co.generate_node_positions()

annotations = co.generate_annotations(annotations_dict, label_to_index, node_x, node_y)

diagram_title = "Plastic Waste Management - Sankey Diagram"
visualization.create_sankey_diagram(node_labels, source_indices, target_indices, values, node_colors, link_colors, node_x, node_y, diagram_title, annotations)
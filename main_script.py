import preprocess
import visualization
import color_options as co

file_path = r'2025_01_29_combined_table_implementation.xlsm'
output_excel_path = r'combined_summary_full_v3.xlsx'

preprocess.process_excel(file_path, output_excel_path)

nodes, links = visualization.process_data_hierarchical(output_excel_path)
node_labels, label_to_index, source_indices, target_indices, values = visualization.prepare_data_for_plotly_sankey(nodes, links)

node_colors, link_colors = co.generate_color_options(links, label_to_index)

diagram_title = "Plastic Waste Management - Sankey Diagram"
visualization.create_sankey_diagram(node_labels, source_indices, target_indices, values, node_colors, link_colors, diagram_title)
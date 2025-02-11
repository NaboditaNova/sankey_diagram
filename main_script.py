#################################
#   Author: Nabodita Anam Nova  #
#################################

import preprocess
import visualization
import additionals

def main():
    # Toggle annotations on or off
    show_annotations = False

    # Define file paths
    input_excel_path = r'2025_01_29_combined_table_implementation.xlsm'
    output_excel_path = r'combined_summary_full_v3.xlsx'
    material_composition_output_path = r'combined_material_composition.xlsx'

    # Run preprocessing steps
    preprocess.process_excel(input_excel_path, output_excel_path)
    preprocess.process_excel_generate_material_composition(input_excel_path, material_composition_output_path)

    # Process data for the Sankey diagram
    nodes, links = visualization.process_data_hierarchical(output_excel_path)
    node_labels, label_to_index, source_indices, target_indices, values = visualization.prepare_data_for_plotly_sankey(nodes, links)

    # Generate colors and positions
    node_colors, link_colors = additionals.generate_color_options(links, label_to_index)
    node_x, node_y = additionals.generate_node_positions()

    # Conditionally generate annotations
    annotations = None
    if show_annotations:
        # Process Excel to generate annotations dictionary (keys are node labels)
        annotations_dict = preprocess.process_excel_generate_annotations(material_composition_output_path)
        # Use the helper to generate a list of annotation dictionaries.
        annotations = additionals.generate_annotations(annotations_dict, label_to_index, node_x, node_y)

    diagram_title = "Plastic Waste Management - Sankey Diagram"
    
    # Create the Sankey diagram.
    # The create_sankey_diagram function now accepts label_to_index and annotations.
    visualization.create_sankey_diagram(
        node_labels,
        source_indices,
        target_indices,
        values,
        node_colors,
        link_colors,
        node_x,
        node_y,
        diagram_title,
        annotations
    )

if __name__ == "__main__":
    main()
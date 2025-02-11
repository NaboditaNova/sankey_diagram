
import pandas as pd
import plotly.graph_objects as go

# Load the Excel file
file_path = r'C:\Users\nabod\combined_summary.xlsx'
def load_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# Process data to extract nodes and links for Sankey Diagram
# Explicitly handle the hierarchy of the flows

def process_data_hierarchical():
    nodes = []
    links = []

    # Define the flow structure as described (collection -> sorting -> recycling)
    flow_data = [
        # Process_collection
        {"input": "Plastics in Households", "outputs": {"PET Deposit": 425.0, "Plastics in Different DS": 1198.7, "Waste": 538.1}},

        # Process_sorting_flow_1
        {"input": "Plastics in Different DS", "outputs": {"Mixed Plastics": 419.0, "PP-flow": 186.2, "PET-flow": 147, "PS-flow": 38.9, "HDPE_flow": 104.9, "Film_flow": 302.7}},

        # Process_sorting_flow_2
        {"input": "PP-flow", "outputs": {"PP in PP sorted products": 106.9, "PP in other sorted products": 79.3}},

        # Recycling
        {"input": "PP in PP sorted products", "outputs": {"Food PP": 33.4, "Non-food PP": 19.6, "Mixed Packaging PP": 15, "Trays PP": 6.5, "MaD PP": 26.2, "PP recycling residues": 6.1}},
    ]

    # Create node mapping and links
    node_map = {}

    for flow in flow_data:
        input_material = flow["input"]
        if input_material not in node_map:
            node_map[input_material] = len(nodes)
            nodes.append(input_material)

        for output_material, value in flow["outputs"].items():
            if output_material not in node_map:
                node_map[output_material] = len(nodes)
                nodes.append(output_material)

            links.append((node_map[input_material], node_map[output_material], value))

    return nodes, links

# Create Sankey Diagram
def create_sankey(nodes, links):
    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=nodes,
        ),
        link=dict(
            source=[link[0] for link in links],
            target=[link[1] for link in links],
            value=[link[2] for link in links]
        )
    ))

    fig.update_layout(title_text="Plastic Waste Management - Sankey Diagram", font_size=12)
    fig.show()

# Main function
def main():
    nodes, links = process_data_hierarchical()
    create_sankey(nodes, links)

# # Run the script
if __name__ == "__main__":
    main()
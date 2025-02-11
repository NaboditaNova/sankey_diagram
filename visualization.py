#################################
#   Author: Nabodita Anam Nova  #
#################################

import pandas as pd
import plotly.graph_objects as go
import color_options as co



def process_data_hierarchical(input_file_path):
    df = pd.read_excel(input_file_path)
    df = df.fillna(method='ffill')

    # Extract values from the first row (row index 0)
    node_label_1 = df.iloc[0, 0]  # Value at position (0,0)
    node_label_2 = df.iloc[0, 1]  # Value at position (0,1)
    link_value   = df.iloc[0, 2]  # Value at position (0,2)

    # Create the nodes part:
    nodes = [
        {'label': node_label_1},
        {'label': node_label_2}
    ]

    # Create the link part:
    links = [
        {
            'source': node_label_1,  # from the value at (0,0)
            'target': node_label_2,  # from the value at (0,1)
            'value': link_value      # from the value at (0,2)
        }
    ]

    df = df.drop(columns=['Process Name', 'Input Material Amount'])

    node_labels = {node_label_1, node_label_2}

    for idx, row in df.iterrows():
        src = row[0]  # first column as source
        tgt = row[1]  # second column as target
        val = row[2]  # third column as link value

        # Check and add the source node if not already present
        if src not in node_labels:
            nodes.append({'label': src})
            node_labels.add(src)

        # Check and add the target node if not already present
        if tgt not in node_labels:
            nodes.append({'label': tgt})
            node_labels.add(tgt)

        # Append the link from source to target with the given value
        links.append({
            'source': src,
            'target': tgt,
            'value': val
        })

    return nodes, links

def prepare_data_for_plotly_sankey(nodes, links):
    # Create a list of node labels (the order matters for indices)
    node_labels = [node['label'] for node in nodes]

    # Create a mapping from node label to its index in the node_labels list
    label_to_index = {label: idx for idx, label in enumerate(node_labels)}

    # Convert link information to use node indices rather than labels
    source_indices = [label_to_index[link['source']] for link in links]
    target_indices = [label_to_index[link['target']] for link in links]
    values = [link['value'] for link in links]

    return node_labels, label_to_index, source_indices, target_indices, values


# Create Sankey Diagram
def create_sankey_diagram(node_labels, source_indices, target_indices, values, node_colors, link_colors, node_x, node_y, diagram_title, annotations=None):
    fig = go.Figure(data=[go.Sankey(
    arrangement="freeform",
    valueformat = ".0f",
    valuesuffix = "ton",  # perpendicular, freeform, fixed, or snap
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=node_labels,
        # color="blue"
        color = node_colors,
        x=node_x,
        y=node_y,
    ),
    link=dict(
        source=source_indices,  # List of source node indices
        target=target_indices,  # List of target node indices
        value=values,           # List of link values
        # color="gray"
        color = link_colors
    )
    )])

    
    # If annotations_dict is provided, generate annotations using the mapping.
    if annotations is not None:
        fig.update_layout(annotations=annotations)

    fig.update_layout(title_text=diagram_title, font_size=12)
    # fig.update_layout(title_text="Plastic Waste Management - Sankey Diagram", font=dict(size = 10, color = 'white'), plot_bgcolor='black', paper_bgcolor='black')

    fig.show()


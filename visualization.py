#################################
#   Author: Nabodita Anam Nova  #
#################################

import pandas as pd
import plotly.graph_objects as go



def process_data_hierarchical(input_file_path):
    df = pd.read_excel(input_file_path).fillna(method='ffill')

    node_label_1 = df.iloc[0, 0]  
    node_label_2 = df.iloc[0, 1]  
    link_value   = df.iloc[0, 2]  

    nodes = [
        {'label': node_label_1},
        {'label': node_label_2}
    ]

    links = [
        {
            'src': node_label_1,  
            'tgt': node_label_2,  
            'val': link_value      
        }
    ]

    df = df.drop(columns=['Process Name', 'Input Material Amount'])

    node_labels = {node_label_1, node_label_2}

    for idx, row in df.iterrows():
        src = row[0]  
        tgt = row[1]  
        val = row[2]  

        if src not in node_labels:
            nodes.append({'label': src})
            node_labels.add(src)

        if tgt not in node_labels:
            nodes.append({'label': tgt})
            node_labels.add(tgt)

        links.append({
            'src': src,
            'tgt': tgt,
            'val': val
        })

    return nodes, links

def prepare_data_for_plotly_sankey(nodes, links):

    node_labels = [node['label'] for node in nodes]

    label_to_index = {label: idx for idx, label in enumerate(node_labels)}

    source_indices = [label_to_index[link['src']] for link in links]
    target_indices = [label_to_index[link['tgt']] for link in links]
    values = [link['val'] for link in links]

    return node_labels, label_to_index, source_indices, target_indices, values


# Create Sankey Diagram
def create_sankey_diagram(node_labels, source_indices, target_indices, values, node_colors, link_colors, diagram_title):
    fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=node_labels,
        color=node_colors
    ),
    link=dict(
        source=source_indices,  
        target=target_indices, 
        value=values,         
        color=link_colors
    )
    )])

    fig.update_layout(title_text=diagram_title, font_size=12)
    # fig.update_layout(title_text="Plastic Waste Management - Sankey Diagram", font=dict(size = 10, color = 'white'), plot_bgcolor='black', paper_bgcolor='black')

    fig.show()


#################################
#   Author: Nabodita Anam Nova  #
#################################

import pandas as pd
import plotly.graph_objects as go


def process_data_hierarchical(input_file_path):
    df = pd.read_excel(input_file_path).fillna(method='ffill')

    label_0 = df.iloc[0, 0]  
    label_1 = df.iloc[0, 1]  
    value_0   = df.iloc[0, 2]  

    nodes = [
        {'label': label_0},
        {'label': label_1}
    ]

    links = [
        {
            'src': label_0,  
            'tgt': label_1,  
            'val': value_0      
        }
    ]

    df = df.drop(columns=['Process Name', 'Input Material Amount'])

    labels = {label_0, label_1}

    for idx, row in df.iterrows():
        src = row[0]  
        tgt = row[1]  
        val = row[2]  

        if src not in labels:
            nodes.append({'label': src})
            labels.add(src)

        if tgt not in labels:
            nodes.append({'label': tgt})
            labels.add(tgt)

        links.append({
            'src': src,
            'tgt': tgt,
            'val': val
        })

    return nodes, links

def prepare_data_for_plotly_sankey(nodes, links):

    labels = [node['label'] for node in nodes]

    labels_idx = {label: idx for idx, label in enumerate(labels)}

    src_idx = [labels_idx[link['src']] for link in links]
    tgt_idx = [labels_idx[link['tgt']] for link in links]
    values = [link['val'] for link in links]

    return labels, labels_idx, src_idx, tgt_idx, values


# Create Sankey Diagram
def create_sankey_diagram(node_labels, source_indices, target_indices, values, color_0, color_1, diagram_title):
    fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=node_labels,
        color=color_0
    ),
    link=dict(
        source=source_indices,  
        target=target_indices, 
        value=values,         
        color=color_1
    )
    )])

    fig.update_layout(title_text=diagram_title, font_size=12)

    fig.show()
#################################
#   Author: Nabodita Anam Nova  #
#################################

import pandas as pd
import plotly.graph_objects as go


def process_data_hierarchical(input_file_path):
    df = pd.read_excel(input_file_path)
    df = df.fillna(method='ffill')

    label_0 = df.iloc[0, 0]
    label_1 = df.iloc[0, 1]
    val_0   = df.iloc[0, 2]

    nodes = [
        {'label': label_0},
        {'label': label_1}
    ]

    links = [
        {
            'source': label_0,
            'target': label_1,
            'value': val_0
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
            'source': src,
            'target': tgt,
            'value': val
        })

    return nodes, links

def prepare_data_for_plotly_sankey(nodes, links):
    labels = [node['label'] for node in nodes]

    label_idx = {label: idx for idx, label in enumerate(labels)}

    src_idx = [label_idx[link['source']] for link in links]
    tgt_idx = [label_idx[link['target']] for link in links]
    values = [link['value'] for link in links]

    return labels, label_idx, src_idx, tgt_idx, values


# Create Sankey Diagram
def create_sankey_diagram(labels, src_idx, tgt_idx, values, node_colors, link_colors, node_x, node_y, diagram_title, annotations=None):
    fig = go.Figure(data=[go.Sankey(
    arrangement="freeform",
    valueformat = ".0f",
    valuesuffix = "ton",
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color = node_colors,
        x=node_x,
        y=node_y,
    ),
    link=dict(
        source=src_idx,
        target=tgt_idx,
        value=values,
        color = link_colors
    )
    )])

    
    if annotations is not None:
        fig.update_layout(annotations=annotations)

    fig.update_layout(title_text=diagram_title, font_size=12)

    fig.show()


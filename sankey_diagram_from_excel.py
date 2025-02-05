import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel('combined_summary_full_v3.xlsx')
df = df.fillna(method='ffill')

# Extract values from the first row (row index 0)
node_label_1 = df.iloc[0, 0]  # Value at position (0,0)
node_label_2 = df.iloc[0, 1]  # Value at position (0,1)
link_value   = df.iloc[0, 2]  # Value at position (0,2)

# Create the nodes part:
# Since you want a list of nodes (each node being a dictionary with a 'label' key)
nodes = [
    {'label': node_label_1},
    {'label': node_label_2}
]

# Create the link part:
# Each link is a dictionary with 'source', 'target', and 'value'
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

# ------------------------------------
# Step 1: Prepare Data for Plotly Sankey
# ------------------------------------
# Create a list of node labels (the order matters for indices)
node_labels = [node['label'] for node in nodes]

# Create a mapping from node label to its index in the node_labels list
label_to_index = {label: idx for idx, label in enumerate(node_labels)}

# Convert link information to use node indices rather than labels
source_indices = [label_to_index[link['source']] for link in links]
target_indices = [label_to_index[link['target']] for link in links]
values = [link['value'] for link in links]

# node_colors = [
#     # "rgba(31, 119, 180, 0.8)",  # Process_collection
#     # "goldenrod", # Process_collection
#     "lavender", # Process_collection
#     # "rgba(255, 127, 14, 0.8)",  # Plastics in Households
#     "mediumaquamarine", # Plastics in Households
#     "rgba(44, 160, 44, 0.8)",   # PET Deposit
#     # "rgba(214, 39, 40, 0.8)",   # Plastics in Different DS
#     # "slateblue", # Plastics in Different DS
#     "darksalmon", # Plastics in Different DS
#     "rgba(148, 103, 189, 0.8)", # Waste
#     "rgba(140, 86, 75, 0.8)",   # Mixed Plastics
#     "rgba(227, 119, 194, 0.8)", # PP-flow
#     "rgba(127, 127, 127, 0.8)", # PS-flow
#     "rgba(188, 189, 34, 0.8)",  # PET-flow
#     "rgba(23, 190, 207, 0.8)",  # HDPE-flow
#     "rgba(31, 119, 180, 0.8)",  # Film-flow
#     "rgba(255, 127, 14, 0.8)",  # PP in PP sorted Products
#     "rgba(44, 160, 44, 0.8)",   # PP in other sorted products
#     "rgba(214, 39, 40, 0.8)",   # Food PP
#     "rgba(148, 103, 189, 0.8)", # Non-food PP
#     "rgba(140, 86, 75, 0.8)",   # Mixed Packaging PP
#     "rgba(227, 119, 194, 0.8)", # Trays PP
#     "rgba(127, 127, 127, 0.8)", # MaD PP
#     "rgba(188, 189, 34, 0.8)"   # PP recycling residues
# ]

# For link colors, we assign each link the color of its source node.
# link_colors = [node_colors[label_to_index[link['source']]] for link in links]


# For links, we'll use a uniform color extracted from the JSON snippet's link colors.
# (Alternatively, you could assign a list of colors if you wish each link to be different.)
# link_colors = ["rgba(0,0,96,0.2)"] * len(links)


# ------------------------------------
# Step 2: Create the Sankey Diagram with Plotly
# ------------------------------------
fig = go.Figure(data=[go.Sankey(
    arrangement="freeform",  # perpendicular, freeform, fixed, or snap
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=node_labels,
        # color="blue"
        # color = node_colors
    ),
    link=dict(
        source=source_indices,  # List of source node indices
        target=target_indices,  # List of target node indices
        value=values,           # List of link values
        # color="gray"
        # color = link_colors
    )
)])

fig.update_layout(title_text="Plastic Waste Management - Sankey Diagram", font_size=12)
# fig.update_layout(title_text="Plastic Waste Management - Sankey Diagram", font=dict(size = 10, color = 'white'), plot_bgcolor='black', paper_bgcolor='black')

fig.show()

#### https://plotly.github.io/plotly.py-docs/generated/plotly.graph_objects.Sankey.html
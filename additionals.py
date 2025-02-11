#################################
#   Author: Nabodita Anam Nova  #
#################################

def generate_color_options(links, label_to_index):
    node_colors = [
        "rgba(114, 174, 214, 0.8)",
        "rgba(145, 212, 201, 0.8)",
        "rgba(44,160,44,0.8)",
        "rgba(145, 161, 231, 0.8)",
        "rgba(0, 0, 0, 0.8)",  
        "rgba(140,86,75,0.8)",    
        "rgba(25, 206, 37, 0.8)",  
        "rgba(244, 213, 36, 0.93)",  
        "rgba(188,189,34,0.8)",    
        "rgba(0, 85, 255, 0.99)",  
        "rgba(189, 47, 210, 0.8)",  
        "rgb(255, 0, 0)",   
        "rgba(152,223,138,0.8)",   
        "rgb(0, 255, 187)",  
        "rgba(197,176,213,0.8)",   
        "rgba(196,156,148,0.8)",   
        "rgba(247,182,210,0.8)",   
        "rgba(204, 255, 0, 0.8)",   
        "rgba(219,219,141,0.8)",   
        "rgb(0, 217, 255)",  
        "rgba(255,0,0,0.8)",       
        "rgba(0,255,0,0.8)",     
        "rgba(0,0,255,0.8)", 
        "rgba(255,255,0,0.8)", 
        "rgba(0,255,255,0.8)",   
        "rgba(255,0,255,0.8)", 
        "rgba(128,0,0,0.8)", 
        "rgba(0,128,0,0.8)",
        "rgba(0,0,128,0.8)",
        "rgba(128,128,0,0.8)",
        "rgba(0,128,128,0.8)",
        "rgba(128,0,128,0.8)",
        "rgba(192,192,192,0.8)",
        "rgba(255,165,0,0.8)",
        "rgba(173,216,230,0.8)",
        "rgba(240,230,140,0.8)",
        "rgba(152,251,152,0.8)",
        "rgba(255,192,203,0.8)",
        "rgba(221,160,221,0.8)",
        "rgba(135,206,235,0.8)",
        "rgba(250,128,114,0.8)",
        "rgba(244,164,96,0.8)",
        "rgba(46,139,87,0.8)",
        "rgba(102,205,170,0.8)",
        "rgba(139,69,19,0.8)",
        "rgba(255,105,180,0.8)",
        "rgba(75,0,130,0.8)",
        "rgba(199,21,133,0.8)",
        "rgba(72,61,139,0.8)"
    ]

    link_colors = [node_colors[label_to_index[link['source']]] for link in links]

    return node_colors, link_colors

def generate_node_positions():

    node_x = [
        0.0,             
        0.2,             
        0.4, 0.4, 0.4,   
        0.6, 0.6, 0.6, 0.6, 0.6, 0.6,
        0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8,
        *[1.0]*25,
        0.8, 0.8, 0.8
    ]

    node_y = [
        0.5,            
        0.5,             
        0.15, 0.5, 0.85, 
        0.143, 0.286, 0.429, 0.571, 0.714, 0.857,  
        0.286,
        0.357,
        0.429,
        0.500,
        0.571,
        0.643,
        0.714,
        0.786,
        0.857,
        0.929,
        1/26, 2/26, 3/26, 4/26, 5/26, 6/26, 7/26, 8/26, 9/26, 10/26,
        11/26, 12/26, 13/26, 14/26, 15/26, 16/26, 17/26, 18/26, 19/26, 20/26,
        21/26, 22/26, 23/26, 24/26, 25/26,

        1/14, 2/14, 3/14
    ]

    return node_x, node_y

def generate_annotations(annotations_dict, label_to_index, node_x, node_y):
    annotations = []
    for label, text in annotations_dict.items():
        if label in label_to_index:
            idx = label_to_index[label]
            annotations.append(dict(
                x=node_x[idx],
                y=node_y[idx],
                xref="paper",
                yref="paper",
                text=text,
                showarrow=True,
                arrowhead=2,
                ax=0,
                ay=-30,
                font=dict(color="black", size=10)
            ))
    return annotations
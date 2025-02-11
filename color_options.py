#################################
#   Author: Nabodita Anam Nova  #
#################################

def generate_color_options(links, label_to_index):
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

    # -------------------------------------------------
    # Step 2: Define 49 individual node colors
    # -------------------------------------------------
    node_colors = [
        "rgba(114, 174, 214, 0.8)",    #  1. Process_collection
        "rgba(145, 212, 201, 0.8)",    #  2. Plastics in Households
        "rgba(44,160,44,0.8)",     #  3. PET Deposit
        "rgba(145, 161, 231, 0.8)",     #  4. Plastics in Different DS
        "rgba(0, 0, 0, 0.8)",   #  5. Waste
        "rgba(140,86,75,0.8)",     #  6. Mixed Plastics
        "rgba(25, 206, 37, 0.8)",   #  7. PP-flow
        "rgba(244, 213, 36, 0.93)",   #  8. PS-flow
        "rgba(188,189,34,0.8)",    #  9. PET-flow
        "rgba(0, 85, 255, 0.99)",    # 10. HDPE-flow
        "rgba(189, 47, 210, 0.8)",   # 11. Film-flow
        "rgb(255, 0, 0)",   # 12. PP in PP sorted products
        "rgba(152,223,138,0.8)",   # 13. PP in other sorted products
        "rgb(0, 255, 187)",   # 14. PS in PS sorted products
        "rgba(197,176,213,0.8)",   # 15. PS in other sorted products
        "rgba(196,156,148,0.8)",   # 16. PET in PET sorted products
        "rgba(247,182,210,0.8)",   # 17. PET in other sorted products
        "rgba(204, 255, 0, 0.8)",   # 18. HDPE in HDPE sorted products
        "rgba(219,219,141,0.8)",   # 19. HDPE in other sorted products
        "rgb(0, 217, 255)",   # 20. Film in film sorted products
        "rgba(255,0,0,0.8)",       # 21. Film in other sorted products
        "rgba(0,255,0,0.8)",       # 22. Food PP
        "rgba(0,0,255,0.8)",       # 23. Non-food PP
        "rgba(255,255,0,0.8)",     # 24. Mixed Packaging PP
        "rgba(0,255,255,0.8)",     # 25. Trays PP
        "rgba(255,0,255,0.8)",     # 26. MaD PP
        "rgba(128,0,0,0.8)",       # 27. PP recycling residues
        "rgba(0,128,0,0.8)",       # 28. Rigids PS
        "rgba(0,0,128,0.8)",       # 29. Mixed Packaging PS
        "rgba(128,128,0,0.8)",     # 30. MaD PS
        "rgba(0,128,128,0.8)",     # 31. PS recycling residues
        "rgba(128,0,128,0.8)",     # 32. Food PET
        "rgba(192,192,192,0.8)",   # 33. Non-food PET
        "rgba(255,165,0,0.8)",     # 34. Mixed Packaging PET
        "rgba(173,216,230,0.8)",   # 35. Trays PET
        "rgba(240,230,140,0.8)",   # 36. MaD PET
        "rgba(152,251,152,0.8)",   # 37. PET recycling residues
        "rgba(255,192,203,0.8)",   # 38. Food HDPE
        "rgba(221,160,221,0.8)",   # 39. Non-food HDPE
        "rgba(135,206,235,0.8)",   # 40. Mixed Packaging HDPE
        "rgba(250,128,114,0.8)",   # 41. MaD HDPE
        "rgba(244,164,96,0.8)",    # 42. HDPE recycling residues
        "rgba(46,139,87,0.8)",     # 43. <A4 Film
        "rgba(102,205,170,0.8)",   # 44. >A4 Film
        "rgba(139,69,19,0.8)",     # 45. MaD Film
        "rgba(255,105,180,0.8)",   # 46. Film recycling residues
        "rgba(75,0,130,0.8)",      # 47. MPO
        "rgba(199,21,133,0.8)",    # 48. MaD MP
        "rgba(72,61,139,0.8)"      # 49. MP recycling residues
    ]

    # For link colors, we assign each link the color of its source node.
    link_colors = [node_colors[label_to_index[link['source']]] for link in links]


    # For links, we'll use a uniform color extracted from the JSON snippet's link colors.
    # (Alternatively, you could assign a list of colors if you wish each link to be different.)
    # link_colors = ["rgba(0,0,96,0.2)"] * len(links)

    return node_colors, link_colors

def generate_node_positions():

    # -- Build the x–coordinate list (by node index) --
    node_x = [
        0.0,             # index 0, level 1
        0.2,             # index 1, level 2
        0.4, 0.4, 0.4,   # indices 2–4, level 3
        0.6, 0.6, 0.6, 0.6, 0.6, 0.6,  # indices 5–10, level 4
        # indices 11–20 (level 5 sorted–products)
        0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8,
        # indices 21–45 (level 6)
        *[1.0]*25,
        # indices 46–48 (level 5: MPO, MaD MP, MP recycling residues)
        0.8, 0.8, 0.8
    ]

    # -- Build the y–coordinate list (by node index) --
    node_y = [
        0.5,             # index 0, level 1
        0.5,             # index 1, level 2
        0.25, 0.5, 0.75, # indices 2–4, level 3
        0.143, 0.286, 0.429, 0.571, 0.714, 0.857,  # indices 5–10, level 4

        # For level 5, we assign according to the desired overall rank (1 to 13):
        # (Note: although in your node list the sorted–products come first, we want
        #  the three that should be at the top (MPO, etc.) to have the lowest y values.)
        # Here we “pretend” that the 10 sorted–products nodes (which are at indices 11–20)
        # get ranks 4–13.
        0.286,  # rank 4 → index 11 ("PP in PP sorted products")
        0.357,  # rank 5 → index 12 ("PP in other sorted products")
        0.429,  # rank 6 → index 13 ("PS in PS sorted products")
        0.500,  # rank 7 → index 14 ("PS in other sorted products")
        0.571,  # rank 8 → index 15 ("PET in PET sorted products")
        0.643,  # rank 9 → index 16 ("PET in other sorted products")
        0.714,  # rank 10 → index 17 ("HDPE in HDPE sorted products")
        0.786,  # rank 11 → index 18 ("HDPE in other sorted products")
        0.857,  # rank 12 → index 19 ("Film in film sorted products")
        0.929,  # rank 13 → index 20 ("Film in other sorted products")

        # Level 6: 25 nodes, using y = rank/26
        1/26, 2/26, 3/26, 4/26, 5/26, 6/26, 7/26, 8/26, 9/26, 10/26,
        11/26, 12/26, 13/26, 14/26, 15/26, 16/26, 17/26, 18/26, 19/26, 20/26,
        21/26, 22/26, 23/26, 24/26, 25/26,

        # Level 5 (the three that should be at the top) – assign ranks 1, 2, 3:
        1/14, 2/14, 3/14
    ]

    return node_x, node_y

def generate_annotations(annotations_dict, label_to_index, node_x, node_y):
    """
    Generate a list of annotation dictionaries for Plotly layout,
    based on the annotations_dict where keys are node labels and values
    are the HTML-formatted annotation text.
    """
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

    # annotations = []
    # for label, text in annotations_dict.items():
    #     if label in label_to_position:
    #         x_pos, y_pos = label_to_position[label]
    #         annotations.append(dict(
    #             x=x_pos,
    #             y=y_pos,
    #             xref="paper",
    #             yref="paper",
    #             text=text,
    #             showarrow=True,
    #             arrowhead=2,
    #             ax=0,
    #             ay=0,
    #             font=dict(color="black", size=10)
    #         ))
    # return annotations
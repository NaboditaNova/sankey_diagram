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
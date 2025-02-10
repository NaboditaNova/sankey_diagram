#################################
#   Author: Nabodita Anam Nova  #
#################################

import pandas as pd

def process_excel(input_path, output_path):

    sheet_names = [
    "Process_collection", 
    "Process_sorting_flow_1", 
    "Process_sorting_flow_2_PP",
    "Process_sorting_flow_2_PS",
    "Process_sorting_flow_2_PET",
    "Process_sorting_flow_2_HDPE",
    "Process_sorting_flow_2_Film",
    "Process_recycling_PP",
    "Process_recycling_PS",
    "Process_recycling_PET",
    "Process_recycling_HDPE",
    "Process_recycling_Film",
    "Process_recycling_MP"
    ]

    # List to hold all summary rows from all sheets
    all_summary_rows = []

    # Process each sheet one by one
    for sheet in sheet_names:
        # Read the current sheet into a DataFrame
        df = pd.read_excel(input_path, sheet_name=sheet)
        
        # ===== Extract Input Data (Row 15) =====
        # Excel row 15 corresponds to pandas index 13
        # Columns: B, D, and E correspond to indices 1, 3, and 4 respectively.
        input_row = df.iloc[13, [1, 3, 4]]
        input_material_name = input_row.iloc[0]       # e.g., "Plastics in Households"
        input_material_amount = input_row.iloc[1]       # e.g., 2170.3
        # (Optionally, you could extract the unit from input_row.iloc[2] if needed.)
        
        # ===== Extract Output Data (Rows 79–81) =====
        # Excel rows 79–81 correspond approximately to indices 77–83 (we use 77:84 for a safe block)
        output_block = df.iloc[77:84, [1, 3, 4]]
        # Remove any rows where the output material name is NaN
        output_block = output_block.dropna(subset=[output_block.columns[0]])
        
        # ===== Build the Summary Rows for this Sheet =====
        # For the first valid output row, include the input information;
        # for subsequent output rows, leave the input columns blank.
        first_output = True
        for idx, row in output_block.iterrows():
            if first_output:
                all_summary_rows.append({
                    "Process Name": sheet,
                    "Input Material Name": input_material_name,
                    "Input Material Amount": input_material_amount,
                    "Output Material Name": row.iloc[0],
                    "Output Material Amount": row.iloc[1]
                })
                first_output = False
            else:
                all_summary_rows.append({
                    "Process Name": "",
                    "Input Material Name": "",
                    "Input Material Amount": "",
                    "Output Material Name": row.iloc[0],
                    "Output Material Amount": row.iloc[1]
                })

    # Combine all summary rows into a single DataFrame
    summary_df = pd.DataFrame(all_summary_rows)

    # Display the combined summary DataFrame (optional)
    print("Combined Summary Table:")
    print(summary_df)

    # ===== Write the Combined Summary to a Single Excel File =====
    output_excel_path = output_path
    summary_df.to_excel(output_excel_path, index=False)
    print(f"\nCombined summary has been written to: {output_excel_path}")

def process_material_composition(input_path, output_path):
    # List of sheet names to process (provide the names here)
    
    # sheet_names = [
    #     "MFA_Template_collection",  # Add other sheet names here
    #     "MFA_Template_sorting_flow_1",   # Example sheet names
    #     "MFA_Template_sorting_flow_2_PP",
    #     "MFA_Template_sorting_flow_2_PS",
    #     "MFA_Template_sorting_flow_2_PET",
    #     "MFA_Template_sorting_flow_2_HDP",
    #     "MFA_Template_sorting_flow_2_Fil"

    #     # Add all other required sheet names here
    # ]

    sheet_names = [
        "MFA_Template_collection",  # Add other sheet names here
        "MFA_Template_sorting_flow_2_PP",
        "MFA_Template_sorting_flow_2_PS",
        "MFA_Template_sorting_flow_2_PET",
        "MFA_Template_sorting_flow_2_HDP",
        "MFA_Template_sorting_flow_2_Fil"

        # Add all other required sheet names here
    ]

    # Initialize an empty DataFrame to hold all data
    combined_data = pd.DataFrame()

    # Loop through each sheet
    for sheet_name in sheet_names:
        # Read the current sheet into a DataFrame
        df = pd.read_excel(input_path, sheet_name=sheet_name, header=0)
        
        # Extract the "Material Name" from the column names
        material_name = df.columns[2]  # Extract header of the third column (Column C in Excel)

        # Extract relevant rows for "Name of the Materials" and "Amount"
        materials_df = df.iloc[14:30, [1, 2]]  # Rows 15–25 (indices 14–24), Columns B and C
        
        # Rename the columns for clarity
        materials_df.columns = ["Name of the Materials", "Amount"]
        
        # Remove rows with blank values in the "Name of the Materials" or "Amount" columns
        materials_df = materials_df.dropna(subset=["Name of the Materials", "Amount"])
        
        # Add the "Name of the sheet" and "Material name" columns to the extracted data
        materials_df["Name of the sheet"] = sheet_name
        materials_df["Material name"] = material_name
        
        # Reorder columns to match the desired format
        materials_df = materials_df[["Name of the sheet", "Material name", "Name of the Materials", "Amount"]]
        
        # Append the current sheet's data to the combined DataFrame
        combined_data = pd.concat([combined_data, materials_df], ignore_index=True)

    # Write the combined data to a new Excel file
    combined_data.to_excel(output_path, index=False)

    print(f"Combined Excel file has been created: {output_path}")

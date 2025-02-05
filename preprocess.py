import pandas as pd

def process_excel(input_path, output_path):

    sheet_names = [
    "Process_collection", 
    "Process_sorting_flow_1", 
    "Process_sorting_flow_2_PP", 
    "Process_recycling_PP"
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


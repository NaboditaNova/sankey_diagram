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

    summary = []

    for sheet in sheet_names:

        df = pd.read_excel(input_path, sheet_name=sheet)
        
        input_row = df.iloc[13, [1, 3, 4]]
        input_material_name = input_row.iloc[0]       
        input_material_amount = input_row.iloc[1]       

        output_block = df.iloc[77:84, [1, 3, 4]]
        output_block = output_block.dropna(subset=[output_block.columns[0]])
        
        output_0 = True

        for idx, row in output_block.iterrows():

            if output_0:
                summary.append({
                    "Process Name": sheet,
                    "Input Material Name": input_material_name,
                    "Input Material Amount": input_material_amount,
                    "Output Material Name": row.iloc[0],
                    "Output Material Amount": row.iloc[1]
                })
                output_0 = False

            else:
                summary.append({
                    "Process Name": "",
                    "Input Material Name": "",
                    "Input Material Amount": "",
                    "Output Material Name": row.iloc[0],
                    "Output Material Amount": row.iloc[1]
                })

    summary_df = pd.DataFrame(summary)

    output_excel_path = output_path
    summary_df.to_excel(output_excel_path, index=False)
    print(f"\nCombined summary has been written to: {output_excel_path}")
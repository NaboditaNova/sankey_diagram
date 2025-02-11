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

    all_summary_rows = []

    for sheet in sheet_names:
        df = pd.read_excel(input_path, sheet_name=sheet)
        
        input_row = df.iloc[13, [1, 3, 4]]
        input_material_name = input_row.iloc[0]
        input_material_amount = input_row.iloc[1]
        
        output_block = df.iloc[77:84, [1, 3, 4]]
        output_block = output_block.dropna(subset=[output_block.columns[0]])
        
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

    summary_df = pd.DataFrame(all_summary_rows)

    print("Combined Summary Table:")
    print(summary_df)

    output_excel_path = output_path
    summary_df.to_excel(output_excel_path, index=False)
    print(f"\nCombined summary has been written to: {output_excel_path}")

def process_excel_generate_material_composition(input_path, output_path):

    sheet_names = [
        "MFA_Template_collection",
        "MFA_Template_sorting_flow_2_PP",
        "MFA_Template_sorting_flow_2_PS",
        "MFA_Template_sorting_flow_2_PET",
        "MFA_Template_sorting_flow_2_HDP",
        "MFA_Template_sorting_flow_2_Fil",        
    ]

    combined_data = pd.DataFrame()

    for sheet_name in sheet_names:
        df = pd.read_excel(input_path, sheet_name=sheet_name, header=0)
        
        material_name = df.columns[2] 

        materials_df = df.iloc[14:30, [1, 2]]
        
        materials_df.columns = ["Name of the Materials", "Amount"]
        
        materials_df = materials_df.dropna(subset=["Name of the Materials", "Amount"])
        
        materials_df["Name of the sheet"] = sheet_name
        materials_df["Material name"] = material_name
        
        materials_df = materials_df[["Name of the sheet", "Material name", "Name of the Materials", "Amount"]]
        
        combined_data = pd.concat([combined_data, materials_df], ignore_index=True)

    combined_data.to_excel(output_path, index=False)

    print(f"Combined Excel file has been created: {output_path}")


def process_excel_generate_annotations(file_path):
    df = pd.read_excel(file_path)

    df = df.drop(columns=["Name of the sheet"])

    annotations_dict = {}

    for index, row in df.iterrows():
        label = row["Material name"]
        
        material_value = str(row["Name of the Materials"])
        amount_value = str(row["Amount"]).strip()
        
        if not amount_value.endswith("%"):
            amount_value += "%"
        
        text_line = f"{material_value}: {amount_value}"
        
        if label in annotations_dict:
            annotations_dict[label] += "<br>" + text_line
        else:
            annotations_dict[label] = f"<b>{label}</b><br>" + text_line

    return annotations_dict
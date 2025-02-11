#################################
#   Author: Nabodita Anam Nova  #
#################################

import pandas as pd

def process_excel(input_path, output_path):

    sh_nms = [
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

    summ_all = []

    for sheet in sh_nms:
        df = pd.read_excel(input_path, sheet_name=sheet)
        
        row = df.iloc[13, [1, 3, 4]]
        in_name = row.iloc[0]
        in_amnt = row.iloc[1]
        
        out_blk = df.iloc[77:84, [1, 3, 4]]
        out_blk = out_blk.dropna(subset=[out_blk.columns[0]])
        
        first_output = True
        for idx, row in out_blk.iterrows():
            if first_output:
                summ_all.append({
                    "Process Name": sheet,
                    "Input Material Name": in_name,
                    "Input Material Amount": in_amnt,
                    "Output Material Name": row.iloc[0],
                    "Output Material Amount": row.iloc[1]
                })
                first_output = False
            else:
                summ_all.append({
                    "Process Name": "",
                    "Input Material Name": "",
                    "Input Material Amount": "",
                    "Output Material Name": row.iloc[0],
                    "Output Material Amount": row.iloc[1]
                })

    summary_df = pd.DataFrame(summ_all)

    print("Combined Summary Table:")
    print(summary_df)

    output_excel_path = output_path
    summary_df.to_excel(output_excel_path, index=False)
    print(f"\nCombined summary has been written to: {output_excel_path}")

def process_excel_generate_material_composition(input_path, output_path):

    sh_nms = [
        "MFA_Template_collection",
        "MFA_Template_sorting_flow_2_PP",
        "MFA_Template_sorting_flow_2_PS",
        "MFA_Template_sorting_flow_2_PET",
        "MFA_Template_sorting_flow_2_HDP",
        "MFA_Template_sorting_flow_2_Fil",        
    ]

    cm_dat = pd.DataFrame()

    for sheet_name in sh_nms:
        df = pd.read_excel(input_path, sheet_name=sheet_name, header=0)
        
        m_name = df.columns[2] 

        m_df = df.iloc[14:30, [1, 2]]
        
        m_df.columns = ["Name of the Materials", "Amount"]
        
        m_df = m_df.dropna(subset=["Name of the Materials", "Amount"])
        
        m_df["Name of the sheet"] = sheet_name
        m_df["Material name"] = m_name
        
        m_df = m_df[["Name of the sheet", "Material name", "Name of the Materials", "Amount"]]
        
        cm_dat = pd.concat([cm_dat, m_df], ignore_index=True)

    cm_dat.to_excel(output_path, index=False)

    print(f"Combined Excel file has been created: {output_path}")


def process_excel_generate_annotations(file_path):
    df = pd.read_excel(file_path)

    df = df.drop(columns=["Name of the sheet"])

    anno = {}

    for index, row in df.iterrows():
        label = row["Material name"]
        
        m_val = str(row["Name of the Materials"])
        amt_val = str(row["Amount"]).strip()
        
        if not amt_val.endswith("%"):
            amt_val += "%"
        
        txt_ = f"{m_val}: {amt_val}"
        
        if label in anno:
            anno[label] += "<br>" + txt_
        else:
            anno[label] = f"<b>{label}</b><br>" + txt_

    return anno
import preprocess
import visualization

file_path = r'C:\Users\nabod\short_excel.xlsm'
output_excel_path = r'C:\Users\nabod\combined_summary_4.xlsx'

preprocess.process_excel(file_path, output_excel_path)

nodes, links = visualization.process_data_hierarchical()
visualization.create_sankey(nodes, links)
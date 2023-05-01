import os

path = r"C:\Users\..."
dir_list = os.listdir(path)
for x in  dir_list:
        if x.endswith('mol2'):
                with open (f"C:\\Users\\...\\{x}") as file:
                    text = file.read()
                    print(f'obabel {x}', f' -O {x}'.replace('mol2', 'pdbqt'))
print('Done')

import shutil

shutil.copy('chart.yaml','chart_bk.yaml')

def chartModif(chart_version):
    with open("chart.yaml", 'r') as f:
        content = f.readlines()
        #print(content)


    with open("chart.yaml", 'w') as f1:
        for line in content:
            if 'version' in line:
                f1.write(f'version: {chart_version}\n')
            else:
                f1.write(line)

chartModif('4.0')
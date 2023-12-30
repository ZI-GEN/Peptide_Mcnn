import argparse
import subprocess

def execute_script(script_name, args):
    command = ['python', script_name] + args
    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description='執行特定的 Python 腳本')
    parser.add_argument('script_number', type=int, choices=[1, 2, 3], help='選擇要執行的腳本代號 (1 - get_mmseqs2.py, 2 - get_Binary_Matrix.py, 3 - get_ProtTrans.py)')
    parser.add_argument('-in', dest='input_path', help='輸入路徑')
    parser.add_argument('-out', dest='output_path', help='輸出路徑')
    
    args = parser.parse_args()
    scripts_to_execute = []

    if args.script_number == 1:
        scripts_to_execute.append(('get_Mmseqs2.py', ['-in', args.input_path, '-out', args.output_path]))
    elif args.script_number == 2:
        scripts_to_execute.append(('get_Binary_Matrix.py', ['-in', args.input_path, '-out', args.output_path]))
    elif args.script_number == 3:
        scripts_to_execute.append(('get_ProtTrans.py', ['-in', args.input_path, '-out', args.output_path]))

    # 執行選擇的腳本
    for script, script_args in scripts_to_execute:
        execute_script(script, script_args)
    

if __name__ == "__main__":
    main()

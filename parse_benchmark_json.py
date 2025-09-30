import json
import os
import argparse

def parse_benchmark_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON file.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Parse benchmark_throughput JSON files and print the results for easy copy-pasting.")
    parser.add_argument("--folder", type=str, help="Path to the benchmark JSON folder")
    args = parser.parse_args()

    for file_name in os.listdir(args.folder):
        if file_name.endswith('.json'):
            file_path = os.path.join(args.folder, file_name)
            result = parse_benchmark_json(file_path)
            if result:
                print(result["tokens_per_second"])

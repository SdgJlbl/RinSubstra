import pickle
import substratools as tools
import subprocess


@tools.register
def run_script(inputs, outputs, task_properties):
    file_path = inputs["datasamples"]
    raw_output = subprocess.run(['Rscript', 'test.R', file_path], capture_output=True)
    model = int(raw_output.stdout.strip())
    save_model(model, outputs["model"])

    
def save_model(model, path):
    with open(path, "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    tools.execute()
import pickle
import substratools as tools
import sh


@tools.register
def run_script(inputs, outputs, task_properties):
    raw_output = sh.Rscript('test.R')
    model = int(parse_r_output(raw_output))
    save_model(model, outputs["model"])

    
def save_model(model, path):
    with open(path, "wb") as f:
        pickle.dump(model, f)
        

def parse_r_output(s):
    return s.strip().split('] ')[-1]


if __name__ == "__main__":
    tools.execute()
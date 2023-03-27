import pickle
import substratools as tools
import sh


@tools.register
def run_script(inputs, outputs, task_properties):
    X = inputs["datasamples"]
    raw_output = sh.Rscript('test.R', str(X))
    model = int(raw_output)
    save_model(model, outputs["model"])

    
def save_model(model, path):
    with open(path, "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    tools.execute()
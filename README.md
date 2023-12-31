# SingleCell-Project

## Install
This project is based on [DANCE](https://github.com/OmicsML/dance)https://github.com/OmicsML/dance. To install it, follow the instructions below:
First create a conda environment for dance
```
conda create -n dance python=3.8 -y && conda activate dance
```
Then, install pytorch, pyg and dgl:
```
# install pytorch
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# install pyg
pip install torch_geometric
# Optional dependencies for pyg:
pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.1.0+cu118.html

# install dgl
pip install  dgl -f https://data.dgl.ai/wheels/cu118/repo.html
pip install  dglgo -f https://data.dgl.ai/wheels-test/repo.html
```
You may also need to install pyro:
```
 pip3 install pyro-ppl 
```

## Usage
You can simply run the code by running main.py:
```
python main.py
```

# PythonForMATLABUsers

### Introductory MATLAB -> Python 3.5+ introductory talk given at MIT, 2018
Note: this talk assumes a UNIX machine (MacOSX, Linux); if you use windows, you're on your own.

### 0.1 Setting up a virtual environment:
1. install Python 3.5+ on your machine, find the location of the binary 
2. set up a virtual environment using the Python venv module by following the directions here: https://docs.python.org/3/tutorial/venv.html -- note that you can substitute your Python 3 binary for "python3"
3. activate the virtual environment with `source path/to/[your_venv_name]/bin/activate`; you should see 
```
(your_venv_name) $ 
```
in your terminal

4. when done, run `deactivate` to leave the virtual environment

### 0.2 Setting up jupyter notebooks in a virtual environment:

Exit any virtual environment. Make sure that `jupyter` is installed on your system with `which jupyter`. If nothing is found, install it with

```
$ python3 -m pip install --upgrade pip
$ python3 -m pip install jupyter
```

Once it is installed, running `jupyter notebook` will launch Jupyter, but the libraries will be your
system's, not the libraries installed in your virtual environment. To use Jupyter within a virtual
environment, we will need to activate the virtual environment and install a specific iPython kernel to
the virtual environment. This step only needs to be done once.

1.  activate your virtual environment
2. `pip install ipykernel`
3. `ipython kernel install --user --name=[your_venv_name]`

Now, when you run `jupyter notebook` from console, select kernel->change kernel and choose the one
named `your_venv_name. Everything should work. If you find that it is not, a good way to begin
debugging it is the following:

1. in your virtual environment run `jupyter kernelspec list`
2. find the `[your_env_name]` kernel in the list
3. follow the path listed, and open the file `kernel.json`

you should see 
```
{
   "display_name": "[your_venv_name]", 
   "language": "python3", 
   "argv": [
   "path/to/[your_venv_name]/bin/python", 
   "-m", 
   "ipykernel_launcher", 
   "-f", 
   "{connection_file}"
  ]
}
```

chances are, your path to the python binary or "language" are incorrect. You can manually fix them
and save the file. Reactivate your virtualenv, run `jupyter notebook` again and restart the kernel.

### 0.3 Modifying the `PYTHONPATH` variable in a virtual environment

In the case of larger projects, you may want your `PYTHONPATH` variable to point to the top level project
directory. In that case, navigate to [venv_dir]/bin/activate and modify the file, adding the line

```
export PYTHONPATH="/top/level/directory"
```

to the end. Now `echo $PYTHONPATH` should show the top level directory upon restarting the virtual environment.

### 0.4 Making paths discoverable using Conda

If using a conda environment, the `PYTHONPATH` solution above is not good practice. Instead, navigate to the `site-packaes` folder, e.g., `anaconda3/envs/[your_conda_env]/lib/python2.7/site-packages`, and add a file with a `.pth` extension. This is a newline-separated list of directories to be added to `sys.path` upon startup of the conda env. 

### 0.5 Adding a jupyter kernel for a Conda env
`ipython kernel install --user --name=[name_of_env]`
`conda install nb_conda_kernels`

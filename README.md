# PythonForMATLABUsers

"'Clever' is not a compliment in the Python community." - Alex Martelli

Introductory MATLAB -> Python 3.5+ introductory talk given at MIT
Note: this talk is aimed at UNIX machines (MacOSX, Linux); if you use windows, you're on your own.

Setting up a virtual environment:
1. install Python 3.5+ on your machine, find the location of the binary 
2. set up a virtual environment using the Python venv module by following the directions here: https://docs.python.org/3/tutorial/venv.html -- note that you can substitute your Python 3 binary for "python3"
3. activate the virtual environment with `source [venv dir]/bin/activate; you should see 
```
(venv name) $ 
```
4. when done, run `deactivate` to leave the virtual environment

For jupyter notebooks in a virtual environment:

1. activate your virtual environment
2. `pip install ipykernel`
3. `ipython kernel install --user --name=[venv_name]`

Then when you run `jupyter notebook` from console, select kernel->change kernel and choose the [venv_name] one





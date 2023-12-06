## Qdrant presentation code


#TODO add description




### Install dependencies

To run the script, you'll need to set up a virtual environment and install the dependencies. You can do this by running the following commands:
Create a venv
```shell

python3 -m venv venv
```
Activate the venv
```shell
source venv/bin/activate
```
Install requirements
```shell
pip install -r requirements.txt
```

In case of issues, you might need to install Rust

Add the following lines to your profile file to set the PATH and RUSTUP_TOOLCHAIN environment variables:
https://stackoverflow.com/questions/77265938/cargo-rustc-failed-with-code-101-could-not-build-wheels-for-tokenizers-which
bash
```
export PATH="$HOME/.cargo/bin:$PATH"
export RUSTUP_TOOLCHAIN=1.72.1
```
Save the file and restart your terminal, or source the profile file to apply the changes.
``` shell
source ~/.zshrc
```
Before running code run in your terminal:
``` shell
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
```

### Set up postgres

```shell
docker-compose up 
```
Run command 
    
```shell
docker-compose up 
```
Then run: 

```shell
python create_database.py
```

And then to load the data run:

```shell
python load_database.py
```

### Run evals
Now you are ready to run the evals.
To run them, simply run:
```shell
python evals.py
```

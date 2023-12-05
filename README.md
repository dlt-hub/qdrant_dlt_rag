## Qdrant presentation code





### Install dependencies


One of the dependencies needed is Rust:


Add the following lines to your profile file to set the PATH and RUSTUP_TOOLCHAIN environment variables:
https://stackoverflow.com/questions/77265938/cargo-rustc-failed-with-code-101-could-not-build-wheels-for-tokenizers-which
bash

export PATH="$HOME/.cargo/bin:$PATH"
export RUSTUP_TOOLCHAIN=1.72.1
Save the file and restart your terminal, or source the profile file to apply the changes. For Zsh, use:

Before running code run in your terminal:
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python




bash

source ~/.zshrc

```shell

### Run postgres

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


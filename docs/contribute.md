# Developer setup

Developer documentation is still been worked on.

## Install the package in editable mode

Activate your virtual environment and run the following commands.

```bash
pip install -e ".[testing]"
make migrate
make load
```

Run the testing app.

```bash
make run
```

## Frontend

If you wish to alter the css or javascript.

```bash
nvm use
npm install
npm run build
```

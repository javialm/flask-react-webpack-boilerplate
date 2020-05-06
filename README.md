# flask-react-webpack-boilerplate
This is a simple boilerplate with Flask as backend and React + Webpack as frontend

## Dependencies

To install the boilerplate dependencies, you can run:

```bash
git clone https://github.com/javialm/flask-react-webpack-boilerplate
cd flask-react-webpack-boilerplate
npm install
pip install -r requirements.txt
```

## Quickstart

Once the dependencies are installed, you can start the api with the following command:

```bash
npm run build 
npm run dev 
npm run watch
```

## Compile translations
```bash
cd flaskr
pybabel compile -d translations
```

## Tests (NOT AVAILABLE)

To run the Javascript tests (located in `src/tests/`), run:

```bash
npm run jest
```
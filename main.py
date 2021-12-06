from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def	index():
	return {'data':{'name':'Dillondoes'}}


@app.get('/about')
def about():
	return {'data':'about page'}

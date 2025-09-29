from fastapi import FastAPI

app = FastAPI(docs_url='/', title='schoolflix', version='v1')


@app.get('/health')
async def health():
	return {



		





	}

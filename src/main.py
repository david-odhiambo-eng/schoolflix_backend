from fastapi import FastAPI


import os

from pathlib import Path

app = FastAPI(docs_url='/', title='schoolflix', version='v1')


@app.get('/health')
async def health():
	return {}

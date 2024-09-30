from fastapi import FastAPI, status, Response
from schemas import ScrapeSettings
from manager import ScrapingManager
from constants import JobStatus


app = FastAPI()


@app.get("/")
def index():
    return { 'data': None, 'message': 'success' }


@app.get("/order")
def allOrders(limit: int):
    return { 'data': { 'records': [], 'per_page': limit }, 'message': 'success' }

@app.get("/order/{id}")
def showOrders(id: int):
    return { 'data': 'order1', 'message': 'success' }

@app.post("/scraping", status_code=status.HTTP_201_CREATED)
def start_scraping(settings: ScrapeSettings, response: Response):
    if ScrapingManager.get_status() == JobStatus.idle:
        manager = ScrapingManager(settings)
        manager.run()
        return { 'message': 'scraping starts', 'status': JobStatus.processing }
    else:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return { 'message': 'Another job is in progress', 'status': JobStatus.failed }
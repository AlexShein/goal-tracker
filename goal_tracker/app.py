from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
async def redirect_root() -> RedirectResponse:
    """
    Redirect root route to docs endpoint
    """
    return RedirectResponse(url="/docs")

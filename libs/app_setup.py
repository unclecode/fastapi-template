from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from colorama import Fore, Style, init
import logging, traceback

def setup_app(app: FastAPI, logger: logging.Logger ):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        trace_str = traceback.format_exc()
        logger.error(f"Error [handle_request]: {exc.detail}")
        print(f"{Fore.RED}Error [handle_request]: {exc.detail}\nTraceback: {trace_str}{Style.RESET_ALL}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        trace_str = traceback.format_exc()
        print(f"{Fore.RED}Unexpected error: {exc}\nTraceback: {trace_str}{Style.RESET_ALL}")
        logger.error(f"Unexpected error: {exc}")
        return JSONResponse(
            status_code=500,
            content={"detail": "An unexpected error occurred."},
        )
import datetime

import aiofiles
import ujson
from aiofiles import os

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from core.const import EMPTY_VALUE, BASE_DIR
from infrastructures.logger.schemas import RequestJsonLogSchema


class LoggingMiddleware(BaseHTTPMiddleware):

    @staticmethod
    async def get_protocol(request: Request) -> str:
        protocol = str(request.scope.get('type', ''))
        http_version = str(request.scope.get('http_version', ''))
        if protocol.lower() == 'http' and http_version:
            return f'{protocol.upper()}/{http_version}'
        return EMPTY_VALUE

    async def dispatch(self, request: Request, call_next):
        request_headers: dict = dict(request.headers.items())
        response: Response = await call_next(request)
        response_headers: dict = dict(response.headers.items())

        log = RequestJsonLogSchema(
            request_url=str(request.url),
            request_referer=request_headers.get('referer', EMPTY_VALUE),
            request_protocol=await self.get_protocol(request),
            request_method=request.method,
            request_path=request.url.path,
            request_host=request.url.hostname,
            request_size=int(request_headers.get('content-length', 0)),
            request_content_type=request_headers.get(
                'content-type', EMPTY_VALUE),
            request_headers=ujson.dumps(request_headers),
            request_body=str(await request.body()),
            request_direction='in',
            remote_ip=request.client[0],
            remote_port=request.client[1],
            response_status_code=response.status_code,
            response_size=int(response_headers.get('content-length', 0)),
            response_headers=ujson.dumps(response_headers),
        )
        date = datetime.datetime.today()
        today = f'{date.day}.{date.month}.{date.year}'
        file_name = f'{today}.json'
        log_path = f'{BASE_DIR}/logs/'
        log_file_path = log_path + file_name

        if not await os.path.exists(log_path):
            await os.mkdir(log_path)
            async with aiofiles.open(log_file_path, 'w') as f:
                await f.write(ujson.dumps(log.dict()) + '\n')

        async with aiofiles.open(log_file_path, 'a') as f:
            await f.write(ujson.dumps(log.dict()) + '\n')
        return response

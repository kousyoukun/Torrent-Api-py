import asyncio

from .asyncioPoliciesFix import decorator_asyncio_fix


class Scraper:
    @decorator_asyncio_fix
    async def _get_html(self, session, url):
        try:
            async with session.get(
                url,
                headers={
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "accept-encoding": "gzip, deflate",
                    "cache-control": "max-age=0"
                },
            ) as r:
                return await r.text(encoding="utf-8")
        except Exception as e:
            print(e)
            return None

    async def get_all_results(self, session, url):
        return await asyncio.gather(asyncio.create_task(self._get_html(session, url)))

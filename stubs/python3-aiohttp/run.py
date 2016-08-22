import argparse
import asyncio
import ssl

import aiohttp

@asyncio.coroutine
def main(conn, url):
    with aiohttp.ClientSession(connector=conn) as session:
        try:
            response = yield from session.get(url)
            yield from response.release()
        except aiohttp.errors.ClientOSError as exc:
            while exc is not None:
                exc = exc.__cause__
                if isinstance(exc, ssl.SSLError):
                    print('REJECT')
                    break
            else:
                raise
        except ssl.CertificateError:
            print('REJECT')
        else:
            print('ACCEPT')

ap = argparse.ArgumentParser()
ap.add_argument('host')
ap.add_argument('port')
ap.add_argument('cafile', nargs='?')
options = ap.parse_args()
url = 'https://{host}:{port}'.format(**vars(options))
if options.cafile is not None:
    context = ssl.create_default_context(cafile=options.cafile)
    conn = aiohttp.TCPConnector(ssl_context=context)
else:
    conn = None
loop = asyncio.get_event_loop()
loop.run_until_complete(main(conn, url))

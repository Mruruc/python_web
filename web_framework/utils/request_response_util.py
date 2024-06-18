from urllib.parse import unquote


def extract_request_info(request):
    # Extracting the request information
    request_arr = request.split('\r\n\r\n', 1)
    headers_part = request_arr[0]
    body_part = request_arr[1] if len(request_arr) > 1 else ""

    headers_arr = headers_part.split('\r\n')
    request_line = headers_arr[0].split(' ')

    request_map = {
        'method': request_line[0],
        'path': request_line[1],
        'protocol': request_line[2]
    }

    # Request headers
    headers = {}
    for line in headers_arr[1:]:
        if line == '':
            break
        key, value = line.split(': ', 1)
        headers[key] = value
    request_map['headers'] = headers

    # Cookie
    if headers.get('Cookie') is not None:
        cookies = {}
        for cookie in headers.get('Cookie').strip().split(';'):
            key, value = cookie.strip().split('=')
            cookies[key] = value
        request_map['cookies'] = cookies

    # Request body
    if request_map['method'] in ('POST', 'PUT'):
        if headers.get("Content-Type") == "application/json":
            request_map['body_data'] = body_part
        else:
            body = {}
            application_url_encoded_data = body_part
            list_of_data = application_url_encoded_data.strip().split('&')
            for data in list_of_data:
                key, value = data.split('=')
                body[key] = unquote(value)
            request_map['body_data'] = body

    return request_map

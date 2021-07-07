def getImg(img_url):
    import requests
    from urllib import parse
    img_name = parse.parse_qs(parse.urlparse(img_url).query)['attname'][0]
    try:
        r = requests.get(img_url, stream=True)
    except:
        return 0
    img_path = f'./tmp/{img_name}'
    with open(img_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)
    return img_path


def getrec(img, api):
    import requests
    import json
    import base64
    import os
    if api == '':
        return ''
    headers = {'Pragma': 'no-cache', 'Cache-Control': 'no-cache',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/74.0.3729.157 Safari/537.36',
               'Accept': '*/*', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 'Content-Type': 'application/json'}
    try:
        with open(img, 'rb') as f:
            img_base64 = str(base64.b64encode(f.read()).decode('utf-8'))
        post_dict = {"images": [img_base64]}
        r = requests.post(api, headers=headers, json=post_dict)
        res = json.loads(r.text)
        if res['status'] == '000':
            text = ''
            for result_list in res['results']:
                for result in result_list:
                    text += result['text'] + '\n'
            ret = text
        else:
            ret = ''
    except:
        ret = ''
    finally:
        os.remove(img)
    return ret


def configReader():
    import json
    try:
        with open('./config/config.json') as f:
            data = json.load(f)
            api = data['url']
    except:
        api = ''
    return api

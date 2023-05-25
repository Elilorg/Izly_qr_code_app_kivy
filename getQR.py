import requests
import base64


def get_data_url_qr():

    session = requests.Session()
    headers_get_request = {"Host": "mon-espace.izly.fr",
                           "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv",
                           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate, br", "Referer": "https", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-site", "Sec-Fetch-User": "?1"}

    get_response = session.get(
        "https://mon-espace.izly.fr/", headers=headers_get_request)

    print(get_response)
    html_page = get_response.text
    index_string = html_page.find(
        "name=\"__RequestVerificationToken\" type=\"hidden\" value=\"")

    RequestVerificationToken = html_page[index_string: index_string + 500].split('value=\"')[
        1].split('"')[0]
    print(RequestVerificationToken)

    headers_post_request = {"Host": "mon-espace.izly.fr",
                            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                            "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
                            "Accept-Encoding": "gzip,deflate,br",
                            "Content-Type": "application/x-www-form-urlencoded",
                            "Content-Length": "201",
                            "Origin": "https://mon-espace.izly.fr",
                            "Connection": "keep-alive",
                            "Referer": "https://mon-espace.izly.fr/Home/Logon?ReturnUrl=%2f",

                            "Upgrade-Insecure-Requests": "1",
                            "Sec-Fetch-Dest": "document",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-Site": "same-origin",
                            "Sec-Fetch-User": "?1"}

    ADRESSEMAIL =
    MOT_DE_PASSE =

    params_post_request = {"__RequestVerificationToken": RequestVerificationToken,
                           "ReturnUrl": "/", "Username": ADRESSE_MAIL, "Password": MOT_DE_PASSE}

    response = session.post("https://mon-espace.izly.fr/Home/Logon",
                            headers=headers_post_request, data=params_post_request)
    print(response)

    qr_code_request = session.post(
        "https://mon-espace.izly.fr/Home/CreateQrCodeImg", data={"nbrOfQrCode": "1"})
    print(qr_code_request)
    data_utl_qr = qr_code_request.json()[0]['Src']
    return data_utl_qr


def data_url_to_png(data_url):

    image_data = data_url.split(",")[1]

    # decode the base64 encoded image data
    decoded_image_data = base64.b64decode(image_data)
    return decoded_image_data

def get_qr_code_binary():
    qr_data_url = get_data_url_qr()
    return data_url_to_png(qr_data_url)
# save the image data to a PNG file


if __name__ == "__main__":
    decoded_image_data = get_qr_code_binary()
    with open("Qr.png", "wb") as f:
        f.write(decoded_image_data)





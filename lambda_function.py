import cloudscraper

def lambda_handler(event, context):
    usuario = 'invitado'
    contraseña = 'invitado'

    # Crear un scraper con autenticación
    scraper = cloudscraper.create_scraper()
    scraper.headers.update({'User-Agent': 'Mozilla/5.0'})

    # Realizar la autenticación
    login_url = 'https://infomar.imarpe.gob.pe/Acceso/Login?ReturnUrl=%2FHome%2FIndex'
    login_data = {'user': usuario, 'password': contraseña}
    login_response = scraper.post(login_url, data=login_data)

    # Verificar si la autenticación fue exitosa
    if login_response.ok:
        # Ahora puedes acceder a la página de datos que necesitas
        data_url = 'https://infomar.imarpe.gob.pe/Reportes/EspeciesPuerto?LUGAR_ID=29&fecha=02%2F04%2F2024'
        data_response = scraper.get(data_url)

        # Imprimir el contenido de la página de datos
        print(data_response.text)
    else:
        print('Error al iniciar sesión:', login_response.status_code)
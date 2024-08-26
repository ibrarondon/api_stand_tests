import configuration, requests, data

def get_docs(): #Usamos para conseguir DOCS de la API
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs(): #Usamos para conseguir LOGS del servidor de la API
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})

def get_users_table(): #Usamos para conseguir tabla de usuarios de la API
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body): #Usamos para crear usuarios de la API
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)
#response = post_new_user(data.user_body)
#print(response.status_code)
#print(response.json())

def post_product_kits(products_ids): #Usamos para buscar kits por ID producto
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids, headers=data.headers)

response = post_product_kits(data.products_ids)
print(response.status_code)
print(response.json())
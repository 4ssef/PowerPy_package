
# pwerpy

Este paquete de Python, facilita la comunicación entre la REST API de Microsoft Power BI y un cliente.



## Requisitos
* Python >= 3.7 y < 4

## Instalación
```bash
pip install pwerpy
```
## Antes de Usar
Es obligatorio contar con lo siguiente para poder hacer un uso correcto de `pwerpy`, de lo contrario, no se podrá hacer ninguna petición/solicitud a la REST API de Power BI:
* El Client ID de su Azure Active Directory (AD)
* El usuario de su Azure AD
* La contraseña de su Azure AD 

## Uso/Ejemplos
Una vez obtenido su client ID, el usuario y contraseña del área de trabajo, empezamos

Para obtener el tenant ID de su Azure Active Directory
```python
from pwerpy import powerpy

domain_name = 'EL_NOMBRE_DE_SU_DOMINIO'

tenant_id = powerpy.get_tenant_id(domain_name)
```

Para obtener el token de autenticación de acceso, con el fin de obtener el token de autorización Bearer
```python
from pwerpy import powerpy

tenant_id = 'SU_TENANT_ID'
client_id = 'SU_CLIENT_ID'
user = 'SU_USUARIO_DEL_AREA_DE_TRABAJO'
pwd = 'SU_CONTRASEÑA_DEL_AREA_DE_TRABAJO'

access_token = powerpy.get_access_token(tenant_id, client_id, user, pwd)
```

Para obtener el token de autorización Bearer
```python
from pwerpy import powerpy

access_token = 'SU_TOKEN_DE_ACCESO'

auth = powerpy.get_authorization_token(access_token)
```

Para hacer una petición GET
```python
from pwerpy import powerpy

url = 'URL_DE_POWER_BI_REST_API'
auth = 'TOKEN_DE_AUTORIZACION_BEARER'

response = powerpy.get(url, auth)
```

Para hacer una petición POST
```python
from pwerpy import powerpy

url = 'URL_DE_POWER_BI_REST_API'
auth = 'TOKEN_DE_AUTORIZACION_BEARER'

response = powerpy.post(url, auth)
```
En esencia, estas son todas las funciones para poder comunicarse correctamente con la REST API de Power BI.
## Funciones
### powerpy
* get_tenant_id()
* get_access_token()
* get_authorization_token()
* get()
* post()

### skills
* get_token_usage()
* get_datasets_in_group()
* get_datasets_names_in_group()
* refresh_dataset_in_group_by_name()
* refresh_dataset_by_id()
* get_refresh_history_by_dataset_id()

## Licencia

Pwerpy está bajo la licencia de [MIT](https://choosealicense.com/licenses/mit/).

Todos los derechos reservados © 2022, Fernando Assef (4ssef)
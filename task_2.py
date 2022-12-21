import requests


TOKEN = ''


class Yandex:

    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_upload_link(self, disk_file_name):
        uri = 'v1/disk/resources/upload/'
        url = self.host + uri
        params = {'path': f'/{disk_file_name}', 'overwrite': 'true'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload_from_pc(self, local_file_name, disk_file_name):
        upload_link = self.get_upload_link(disk_file_name)
        response = requests.put(upload_link, headers=self.get_headers(), data=open(local_file_name, 'rb'))
        if response.status_code == 201:
            return print('Операция прошла успешно')
        else:
            return print(f'Произошла ошибка {response.status_code}')


if __name__ == '__main__':
    ya = Yandex(TOKEN)
    ya.upload_from_pc('test.json', 'file_for_disk.json')

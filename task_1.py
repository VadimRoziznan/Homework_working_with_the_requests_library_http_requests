import requests


class SuperHeroes:

    def parameter_loading(self):
        url = 'https://akabab.github.io/superhero-api/api/all.json'
        return requests.get(url).json()

    def intelligence(self, *args):
        response = self.parameter_loading()
        max_intelligence = 0
        name = ''
        for parameter in response:
            if parameter['name'] in args:
                if parameter['powerstats']['intelligence'] > max_intelligence:
                    max_intelligence = parameter['powerstats']['intelligence']
                    name = parameter['name']
        return f'Самый умный {name}, его уровень {max_intelligence} баллов'


if __name__ == '__main__':
    SuperHero = SuperHeroes()
    print(SuperHero.intelligence('Hulk', 'Captain America', 'Thanos'))
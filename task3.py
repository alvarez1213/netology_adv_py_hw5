from task2 import logger
from hw_api1 import get_smartest_hero


@logger('task3.log')
def main():
    ret = get_smartest_hero('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
    return ret


if __name__ == '__main__':
    print(main())

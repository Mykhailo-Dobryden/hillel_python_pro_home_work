"""
Реалізувати функцію parse (див. модуль main.py)
Реалізувати функцію parse_coockie (див. модуль main.py)
**написати 5 тестів (assert) до кожної функції
"""

from urllib.parse import urlparse, parse_qs


def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    return {k: v[0] for k, v in parse_qs(parsed_url.query).items()}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=red') == {'name': 'ferret', 'color': 'red'}
    assert parse('http://example.com/path/to/page?name=ferret&color=red') == {'name': 'ferret', 'color': 'red'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}
    assert parse('http://example.com/?name=John&lastname=Black') == {'name': 'John', 'lastname': 'Black'}


def parse_cookie(query: str) -> dict:
    pairs_of_values = parse_qs(query, separator=';')
    return {k: pairs_of_values[k][0] for k in pairs_of_values}


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('name=Diana;') == {'name': 'Diana'}
    assert parse_cookie('name=Diana;title=princess') == {'name': 'Diana', 'title': 'princess'}
    assert parse_cookie('name=John;size=xl=xxl') == {'name': 'John', 'size': 'xl=xxl'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}

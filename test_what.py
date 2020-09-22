#!/usr/bin/env python3
from pathlib import Path
from re import findall

TEST_LINE = '109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"'


# def log_request(ip, x1='-', x2='-', date, request, status, size, referer='-', user_agent, x3='-'):
#     assert ' ' not in x1
#     assert ' ' not in x2
#     assert date ... formattata come da xx/Mmm/yyy:hh
#     return f'{ip} {x1} {x2} [{date}] "{request}" {status} {size} "{referer}" "{user_agent}" "{x3}"'


def parse_line(line: str):
    """
    @solution
    """
    try:
        (ip, _, _, date, request, status, length, _, user_agent, _) = findall(
            '^([0-9.:]+) ([^ ]+) ([^ ]+) \[([^\]]+)\] "([^"]+)" ([0-9]+) ([0-9]+) "([^"]+)" "([^"]+)" "([^"]+)"$',
            line,
        )[0]
    except ValueError as e:
        # se ho meno di 9 campi posso decidere cosa
        # lanciare, eg.
        # 1- c'è un errore nella riga?
        if ...: raise ValueError(f"La riga non rispetta il formato atteso: {line}")
        # 2- non è implementato il parser di quella funzione
        if ...: raise NotImplementedError(f"Il parser non supporta il formato: {line}")
    return (ip, date, request)


def test_parse_line():
    ip, date, request = parse_line(TEST_LINE)
    assert ip == "109.169.248.247"
    assert date == "12/Dec/2015:18:25:11 +0100"
    assert request == "GET /administrator/ HTTP/1.1"


def test_main():
    fpath = "access.log"
    assert main(fpath, "GET") == 21


def main(fpath: str, http_method: str) -> int:
    """Count the occurrences of http_method in access.log.

    param: fpath - a posix path
    param: http_method - an http method
    return: an integer with the number of occurrencies
    @solution
    """
    p = Path(fpath)
    count = 0
    with p.open() as f:
        for line in f.readlines():
            if not line: continue
            try:
                ip, date, request = parse_line(line)
            except:
                ...
                
            if line.strip():
                ip, date, request = parse_line(line)
                if request.startswith(http_method +" "):
                    count += 1
    return count


if __name__ == "__main__":
    from sys import argv

    progname, fpath, http_method = argv
    result = main(fpath, http_method)
    print(f"Result is: {result}")

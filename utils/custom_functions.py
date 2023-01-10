def plural_records(num: str):
    num = int(num)

    if num == 0:
        return 'Nenhum registro encontrado'
    elif num == 1:
        return f'{num} registro encontrado'
    else:
        return f'{num} registros encontrados'

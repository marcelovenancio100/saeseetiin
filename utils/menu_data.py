MENU_ITEMS = {
    'home': {
        'name': 'Home',
        'route': 'home:home',
        'icon': 'fa-solid fa-store fa',
    },
    'user': {
        'name': 'Usuário',
        'route': '',
        'icon': 'fa-solid fa-user-tie fa',
        'childrens': [
            {
                'name': 'Listar Usuários',
                'route': 'user:list',
                'icon': 'fa-solid fa-caret-right fa',
            },
            {
                'name': 'Incluir Usuário',
                'route': 'user:create',
                'icon': 'fa-solid fa-caret-right fa',
            }
        ]
    },
    'brand': {
        'name': 'Marca',
        'route': '',
        'icon': 'fa-solid fa-tag fa',
        'childrens': [
            {
                'name': 'Listar Marcas',
                'route': 'brand:list',
                'icon': 'fa-solid fa-caret-right fa',
            },
            {
                'name': 'Incluir Marca',
                'route': 'brand:create',
                'icon': 'fa-solid fa-caret-right fa',
            }
        ]
    },
    'model': {
        'name': 'Modelo',
        'route': '',
        'icon': 'fa-solid fa-palette fa',
        'childrens': [
            {
                'name': 'Listar Modelos',
                'route': 'model:list',
                'icon': 'fa-solid fa-caret-right fa',
            },
            {
                'name': 'Incluir Modelo',
                'route': 'model:create',
                'icon': 'fa-solid fa-caret-right fa',
            }
        ]
    },
    'group': {
        'name': 'Grupo',
        'route': '',
        'icon': 'fa-solid fa-layer-group fa',
        'childrens': [
            {
                'name': 'Listar Grupos',
                'route': 'group:list',
                'icon': 'fa-solid fa-caret-right fa',
            },
            {
                'name': 'Incluir Grupo',
                'route': 'group:create',
                'icon': 'fa-solid fa-caret-right fa',
            }
        ]
    },
    'situation': {
        'name': 'Situação',
        'route': '',
        'icon': 'fa-solid fa-chart-line fa',
        'childrens': [
            {
                'name': 'Listar Situações',
                'route': 'situation:list',
                'icon': 'fa-solid fa-caret-right fa',
            },
            {
                'name': 'Incluir Situação',
                'route': 'situation:create',
                'icon': 'fa-solid fa-caret-right fa',
            }
        ]
    },
    'collection': {
        'name': 'Coleção',
        'route': '',
        'icon': 'fa-solid fa-th fa',
        'childrens': [
            {
                'name': 'Listar Coleções',
                'route': 'collection:list',
                'icon': 'fa-solid fa-caret-right fa',
            },
            {
                'name': 'Incluir Coleção',
                'route': 'collection:create',
                'icon': 'fa-solid fa-caret-right fa',
            }
        ]
    },
    'item': {
        'name': 'Item da Coleção',
        'route': '',
        'icon': 'fa-solid fa-gamepad fa',
        'childrens': [
            {
                'name': 'Listar Itens',
                'route': 'item:list',
                'icon': 'fa-solid fa-caret-right fa',
            },
            {
                'name': 'Incluir Item',
                'route': 'item:create',
                'icon': 'fa-solid fa-caret-right fa',
            },
            {
                'name': 'Exposição de Itens',
                'route': 'item:show',
                'icon': 'fa-solid fa-caret-right fa',
            }
        ]
    }
}

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
                'name': 'Incluir Novo Usuário',
                'route': 'user:create',
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
                'name': 'Incluir Novo Grupo',
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
                'name': 'Incluir Nova Situação',
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
                'name': 'Incluir Nova Coleção',
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
                'name': 'Incluir Novo Item',
                'route': 'item:new',
                'icon': 'fa-solid fa-caret-right fa',
            }
        ]
    }
}

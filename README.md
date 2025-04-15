<<<<<<< HEAD
# fastapi_router
=======
# FastAPI AutoRoutes

Gere endpoints do FastAPI automaticamente com base na estrutura de arquivos do sistema.

Este projeto é uma extensão para FastAPI que permite organizar suas rotas e middlewares por pastas, sem precisar declarar tudo manualmente. Ideal para quem gosta de estruturação inspirada em frameworks como Next.js ou Nuxt.

---

## ✅ O que ele faz

- Mapeia a pasta `routes/` e registra endpoints com base na estrutura de subpastas.
- Define o método HTTP com base no nome da função (`get`, `post`, etc).
- Suporte a parâmetros dinâmicos usando colchetes: `routes/users/[id]/route.py` → `/users/{id}`
- Suporte a **tags automáticas** com base na primeira subpasta.
- Suporte a **middlewares por rota**, com duas formas:
  - `routes/x/middleware.py` com função `handler(request, call_next)`
  - `routes/x/middleware/` com arquivos `.py` contendo `handler(...)` (executados em ordem)

---

## 📁 Estrutura esperada

```
routes/ 
├── index/
│   └── route.py → GET / 
├── blog/ 
│   ├── [id]/
│   │   └── route.py → GET /blog/{id} 
│   └── route.py → GET /blog 
└── admin/ 
    └── route.py → GET /admin
```

---

## ✔️ Checklist

- [x] Geração automática de rotas com base na pasta `routes/`
- [x] Suporte a métodos HTTP (`get`, `post`, etc) por nome de função
- [x] Conversão de `[param]` para `{param}`
- [x] Tag automática por nome da subpasta principal
- [ ] Suporte a middlewares por rota:
  - [ ] Arquivo `middleware.py`
  - [ ] Pasta `middleware/` com múltiplos arquivos

---

## 🚀 Como usar

```python
from fastapi import FastAPI
from autoroutes import auto_load_routes

app = FastAPI()
auto_load_routes(app)
```

Coloque sua estrutura de arquivos em routes/ seguindo os padrões.

---

### 🔧 Requisitos
Python 3.8+

FastAPI

---
>>>>>>> ed3cc3f (feat: First commit)

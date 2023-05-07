
# Cloud-Native-Kube-Django

Aplicação de um CRUD com Django usando uma abordagem Cloud Native

### Deploy com Docker

Para fazer o deploy desse projeto com Docker

#### Clonando repositório
```bash
https://github.com/isaias0rt0n/cloud-native-kube-Django.git
```

#### Entrando na pasta
```bash
cd cloud-native-kube-Django
```

#### Crie um arquivo .env com o seguinte conteúdo
```bash
POSTGRES_HOST=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=5432
```

#### Inicie a aplicação
```bash
docker compose --env-file .env up -d
```

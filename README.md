# Crocodile Game AZ BOT
Bu bot söz oyunu botudur və AZƏRBAYCANDA ilk botdur! Telegramda vaxtınızı dahada maraqlı keçirin :)

Əsas bot: https://t.me/CrocodileGameAZ_bot

## Quraşdırma
```
go get -u github.com/play2pay/croco-az
```

## İşə salmaq
1. .ENV Faylı redaktə et
```
cp .env{.example,}                               # Copy
vim .env                                         # Edit
source <(cat .env | awk '{print "export", $1}')  # Set variables
```

2. Redis və postgresql quraşdır
```
docker-compose up -d redis
docker-compose up -d postgresql
```

3. DATA migrasiyasını yerinə yetir
```
make migrate-up
```

## Botun klonlaşdırılması:
```
cp -r croco-az croco-
rm -rf postgres-data/
vim .env
vim docker-compose.yml
vim Makefile
docker-compose up -d postgresql
make migrate-up
docker-compose up -d --build
```

## Contact
- Telegram: https://t.me/foxgowner
- Mail: soc4up@gmail.com

- Project link: https://github.com/play2pay/croco-az

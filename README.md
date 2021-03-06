# weather-api
日本の主要都市の天候情報を取得する。

## features
* flask
* gunicorn
* nginx
## requirements
* docker
* docker-compose
* mysqlデータベース  
*マイグレーションについてはweather-servicesレポジトリを参照

## build
イメージビルド
```
# api
docker build -t weather-services/weather-api:0.0.1 \
             -f deploy/app/Dockerfile . --no-cache
# nginx
docker build -t weather-services/nginx:0.0.1 \
             -f deploy/nginx/Dockerfile . --no-cache
```
ローカルで動かす
```
docker compose up -d
```

*/test_db_confにDB設定の記載が必要

## usage
daily data
```
curl -s http://<hostname>:80/daily?city=tokyo
curl -s http://<hostname>:80/daily?city=tokyo\&range=6 # 現時刻から６時間先まで
```

hourly data
```
curl -s http://<hostname>:80/hourly?city=tokyo
curl -s http://<hostname>:80/hourly?city=tokyo\&range=3 # 本日から３日先まで
```

docker-compose環境
```
curl localhost:8080/daily?city=tokyo
```

取得可能都市
* tokyo
* osaka
* nagoya
* fukuoka

時間指定の範囲
* hourly：1~12
* daily：1~7

公開エンドポイントへのリクエスト
```
curl -s http acec9966a0915405789abf657102a2da-1472559408.ap-northeast-1.elb.amazonaws.com:80/daily?city=tokyo
```

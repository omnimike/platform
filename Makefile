
.PHONY: app proxy

app:
	docker build -t hello app

proxy:
	docker build -t hello-proxy proxy

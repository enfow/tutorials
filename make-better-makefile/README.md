# Make better Makefile

## make `something`

```Makefile
# ./Makefile
format:
	black src/
	isort src/

lint: 
	pytest src/ --pylint
```

## Use constant value

```
# docker/Makefile
IMAGE_NAME = hello-world-python

docker-build:
	docker build -t ${IMAGE_NAME} .

docker-run:
	docker run --rm ${IMAGE_NAME} 
```

## Pass input parameter to make command

```
# ./Makefilw
TXT = "Default Message"

print-text:
  python src/print_input.py --txt {TXT}
```

- Input을 전달하지 않는 경우 -> Constant 출력

```
$ make print-txt
python src/print_input.py --txt "Default Message"
Default Message
```

- Input을 전달한 경우 -> Input 출력

```
$ make print-text TXT="NoDefault"
python src/print_input.py --txt NoDefault
NoDefault

```

## Use makefile on the different directory.

- 다음과 같이 `-C` option을 사용하면 다른 directory의 Makefile 커맨드를 실행할 수 있다.

```
make -C [Makefile_Dir] [Makefile_keyword]
```

```
./Makefile
docker-build-on-docker-dir:
	make -C docker docker-build

docker-run-on-docker-dir:
	make -C docker docker-run
```

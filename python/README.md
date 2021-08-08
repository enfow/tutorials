# Python Exmaples

1. Scope

- Python Scope는 function을 기준으로 나누어진다.
- Global variable은 어디에서나 접근이 가능하다.
- Local variable, 즉 어떤 함수 내에서 선언된 variable은 해당 함수 내에서만 접근할 수 있다.
- 함수의 호출 위치와 무관하게 Outer Function은 Local variable에 접근할 수 없다.
- 함수의 내에서 정의되는 Inner Function(Nested Function)은 Local variable에 접근할 수 있다.

2. List Comprehension

- For-Itearation, If-Else Statement 등을 List 내에서 사용할 수 있다.
- List 내에서 먼저 선언된 Statement가 이후의 Statement들을 감싸고 있는 것으로 이해할 수 있다.
- 즉 아래 두 코드의 실행 결과는 동일하다.

```python
products = [(num1, num2) for num1 in range(5) for num2 in range(num1)]
```

```python
products = []
for num1 in range(5):
    for num2 in range(num1):
            products.append((num1, num2))
```

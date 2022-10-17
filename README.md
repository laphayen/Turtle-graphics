# Turtle-graphics

## 사용 방법
* 파이썬에서 제공하는 라이브러리로 import가 필요하다.
<pre><code>import turtle</code></pre>

* shape()함수를 통해 거북이의 모양을 변경한다.
* 모양은 “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”등으로 변경 가능하다.
<pre><code>turtle.shape('arrow')</code></pre>
<pre><code>turtle.shape('turtle')</code></pre>
<pre><code>turtle.shape('circle')</code></pre>
<pre><code>turtle.shape('square')</code></pre>
<pre><code>turtle.shape('triangle')</code></pre>
<pre><code>turtle.shape('classic')</code></pre>

* 거북이 크기 변경
<pre><code>turtle.shapesize(10)</code></pre>

* 거북이 이동
<pre><code>turtle.forward</code></pre>

* 거북이 오른쪽 방향 회전
<pre><code>turtle.right(90)</code></pre>

* 윈도창 제목 설정
<pre><code>turtle.title('제목')</code></pre>

* 선 두께 설정
<pre><code>turtle.pensize(펜 두께)</code></pre>

* 마우스 클릭 설정
* 윈도창에서 마우스 클릭 시 설정한 함수가 동작한다.
* 1 - 마우스 왼쪽 버튼, 2- 마우스 가운데 버튼, 3 - 마우스 오른쪽 버튼
<pre><code>turtle.onscreenclick(함수명, 번호)</code></pre>


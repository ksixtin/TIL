# Java Study	by LEO

1) 2주간 배운 내용 정리하기

**필수**

- 단순 폴더 이동

**추천**

* 핵심 개념(코드)들 마크다운으로 정리
* 기타 알고리즘 등 문제 풀었던 내용 마크다운으로 정리



혹시 정리를 다 한사람은 새롭게 폴더(test) 만들고 a.txt를 만들고 b.txt는 .gitignore 지정해놓고 원격저장소 올리기까지 반드시 실습.





### 5. 배열

* 배열은 같은 타입의 변수들로 이루어진 유한 집합으로 정의
* 배열을 구성하는 각각의 값을 배열요소(element)라고 하며, 배열에서의 위치를 가리키는 숫자를 인덱스(index)라고 한다.
* 인덱스는 언제나 0부터 시작하며, 0을 포함한 양의 정수만을 가질 수 있다.

#### 1차원 배열(array)

~~~ 배열 기본 문법
문법 - 선언 (가능하면 1번 방식으로 사용할 것, 이유는 모름)
1. 타입[ ] 배열이름;	//int[] arry1;
2. 타입 배열이름[ ];	//int arry1[];
~~~

~~~ 배열생성
문법 - 생성
배열이름 = new 타입[배열길이]; //arry1 = new int[4];
~~~

~~~ 배열의 선언과 생성
동시에 선언과 생성하기 + 초기화
int[ ] arry1 = new int[3];	//길이가 3인 int형 배열의 선언 및 생성
int[ ] arry2 = new int[5];	//길이가 5인 int형 배열의 선언 및 생성
arry1[0]=85;
arry1[1]=65;
arry1[2]=90;

arry2[0]=85;

for(int i=0;i<arry1.length;i++) {
	System.out.print(arry1[i]+" ");
}
for(int i=0;i<arry2.length;i++) {
	System.out.print(arry2[i]+" ");
}
결괏값
85 65 90
85 0 0 0 0	//배열의 길이보다 적은 수의 배열 요소만을 초기화 할 경우, 나머지 배열 요소들은 배열의 타입에 맞게 자동으로 초기화 된다.
※ 타입에 따른 초깃값 = char '\u0000', byte&short&int 0, long 0L 등

~~~

~~~ 배열의 초기화
1. 타입[ ] 배열이름 = {배열요소1, 배열요소2, ..};
2. 타입[ ] 배열이름 = new 타입[ ] {배열요소1, 배열요소2, ..};

	// int[] arry1 = {10, 20, 30};
		int[] arry2 = new int[] {10, 20, 30, 40, 50};
		for(int i=0;i<arry2.length;i++) {
			System.out.print(arry2[i]+" ");
		}	
~~~

~~~ 배열 예제
배열 예제 : 배열 요소의 합과 평균을 구하라.
		int[] arry3 = new int[] {85, 65, 90};
		int sum = 0;
		for(int i=0;i<arry3.length;i++){
			sum += arry3[i];
		}
		System.out.println("총점은"+sum+"입니다");
		System.out.println("평균은"+sum/arry3.length+"입니다");
		}
		//총점은240입니다
		//평균은80입니다	
~~~

#### 2차원 배열(two dimensional array)

대괄호[ ]를 두번 사용하여 선언하며 첫번째 대괄호에는 세로크기, 두번째 대괄호에는 가로 크기를 지정한다. 즉 세로x가로로 표기한다

~~~ 2차원 배열
문법 - 선언 3가지 방법
1. 타입[][] 배열이름 ;
2. 타입 배열이름[][] ;
3. 타입[] 배열이름[] ;

문법 - 선언과 동시에 초기화
타입 배열이름[열의길이][행의길이]={
{배열요소[0][0],배열요소[0][1],...},
{배열요소[1][0],배열요소[1][1],...},
{배열요소[2][0],배열요소[2][1],...}
};

~~~

~~~ 2차원 배열 예제
2차원 배열 예제
int[][] arry4 = {
			{10, 20, 30, 40, 50},
			{50, 60, 70, 80, 90},
			{11, 12, 13, 14, 15}
			};
			for(int i=0;i<arry4.length;i++) {
				for(int j=0;j<arry4[i].length;j++) {
					System.out.print(arry4[i][j]+" ");
				}
				System.out.println();
			}
			//10 20 30 40 50 
			//50 60 70 80 90 
			//11 12 13 14 15 

~~~

#### 가변 배열(dynamic array)

길이를 명시하지 않고 행마다 다른 길이의 배열을 요소로 저장하는 배열

~~~가별배열 예제
		int[][] arry = {
				{10,20},
				{30,40,50,60},
				{100}
		};
		for(int i=0;i<arry.length;i++) {
			for(int j=0;j<arry[i].length;j++) {
				System.out.print(arry[i][j]+" ");
			}
			System.out.println();
		}
		//10 20 
		//30 40 50 60 
		//100 
~~~

#### 배열의 복사

배열은 한번 생성하면 그 길이를 변경할 수 없다 따라서 데이터를 추가하려면 더 큰 배열을 만들고 이전 배열의 데이터를 새로 만든 배열로 복사해야 한다.

배열의 복사 방법

* System클래스의 arrycopy() 메소드 : 가장 성능이 좋음.(배열 복사 전문)
* Arrays클래스의 copyOf() 메소드 : 좀 더 유현항 방식으로 가장 많이 사용
* Object클래스의 clone()메소드
* for문과 인덱스를 이용한 복사

~~~ 배열복사 예제
		int[]arr1 = new int[] {1,2,3,4,5};
		int newLen=10;
		
		int[]arr2=new int[newLen];
		System.arraycopy(arr1, 0, arr2, 0, arr1.length);
		for(int i=0;i<arr2.length;i++) {
			System.out.print(arr2[i]+" ");
		}
		//1 2 3 4 5 0 0 0 0 0 
~~~




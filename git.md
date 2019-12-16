# Git 기초

## 0. 준비 사항

* [git bash](http://https://gitforwindows.org/)
  * git을 활용하기 위한 'CLI(Command Line Interface)를 제공한다.
  * source tree, github desktop 등을 통해 GUI 환경에서도 활용 가능하다.

## 1. 로컬 저장소 활용하기

### 1. 저장소 초기화

``` bash
$ git init
Initialized empty Git repository in C:/LEO/til/.git/
(master) $
```



* 저장소(repository)를 초기화 하게 되면, '.git 폴더가 해당 디렉토리에 생성된다.
* bash 창에서는 (master)라고 표기된다.
  * 현재 브랜치가 master라는 것을 의미함.

## 2. add - staging area

> git으로 관리되는 파일들은 Working directory(작업 환경), Staging Area, commit 단계를 거쳐 이력에 저장된다.

~~~ bash
$ git add a.txt # 파일명
$ git add images/ # 폴더명
$ git add . # 현재


~~~

* add 후 상태

  ~~~ bath
  $ git add .
  $ git status
  $ git status
  On branch master
  
  No commits yet
  
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
          git.md
          image/
          markdown.md
          penguin.jpg
  
  
  ~~~

  

## commit

> 커밋은 코드의 이력을 남기는 과정이다.

~~~ bash
$ git commit -m {커밋 메시지}
~~~
* 커밋 메시지는 항상 해당 이력에 대한 정보를 담을 수 있도록 작성하는 것이 좋다.
* 일반적인 커밋 메시지를 작성하는 습관을 들이자.

~~~ bash
$ git log
commit

~~~

**항상 status 명령어를 통해 git의 상태를 확인하자! commit 이후에는 log 명령어를 통해 이력들을 확인하자!**


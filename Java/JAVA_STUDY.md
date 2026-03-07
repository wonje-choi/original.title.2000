# Java Study Note

## 1) Java란?
- 플랫폼 독립성: JVM 위에서 실행
- 객체지향 중심 언어
- 문법이 비교적 엄격해서 기초 잡기에 좋음

## 2) 개발 환경
- JDK 설치
- `java -version`, `javac -version` 확인
- IDE: IntelliJ / VS Code

## 3) 첫 프로그램
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

컴파일/실행:
```bash
javac Main.java
java Main
```

## 4) 꼭 익힐 문법
- 변수와 자료형: `int`, `double`, `boolean`, `String`
- 조건문: `if`, `switch`
- 반복문: `for`, `while`
- 배열과 컬렉션: `ArrayList`, `HashMap`
- 메서드 작성과 호출

## 5) 객체지향 핵심
- 클래스/객체
- 캡슐화
- 상속
- 다형성
- 인터페이스

## 6) 예외 처리
- `try-catch-finally`
- `throws`

## 7) 다음 단계
- 파일 입출력
- Stream API
- 람다식
- 간단한 콘솔 프로젝트 만들기

## 8) 2주 학습 루틴 예시
- 1~3일: 기본 문법
- 4~6일: 메서드/배열/컬렉션
- 7~10일: 객체지향
- 11~14일: 예외처리 + 미니 프로젝트

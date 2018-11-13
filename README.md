# FSM FOR TCP
## 1. 답안 소스 코드 설명
### 1) 접근 방법
 - TCP 모델의 각 상태와 이벤트(작업)처리의 결과를 클래스 내부에 정의
 - 클래스 선언 시 현재 상태(self.status)를 CLOSE로 초기화
 - next_status 메소드를 정의한 후 event 값을 받아 현재 상태를 다음 상태로 초기화 함.
 - current_status 메소드를 정의 한 후 현재 상태를 가져올 수 있도록 함
 
### 2) 답안 소스 코드 실행 방법
 - fsm_for_tcp 모듈 import 
  * import fsm_for_tcp
 - FSM TCP 모델 인스턴스를 생성
  * fsm_status = fsm_for_tcp.FmsStatus()
 

# FSM FOR TCP
## 1. 답안 소스 코드 설명
### 1) 접근 방법
 (1) TCP 모델의 각 상태와 이벤트(작업)처리의 결과를 클래스 내부에 정의
 (2) 클래스 선언 시 현재 상태(self.status)를 CLOSE로 초기화
 (3) next_status 메소드를 정의한 후 event 값을 받아 현재 상태를 다음 상태로 초기화 함.
 (4) current_status 메소드를 정의 한 후 현재 상태를 가져올 수 있도록 함
 
### 2) 답안 소스 코드 실행 방법
 (1) fsm_for_tcp 모듈 import 
   - import fsm_for_tcp
 (2) FSM TCP model 인스턴스를 생성
   - fsm_status = fsm_for_tcp.FmsStatus()
 (3) 작업 리스트를 선언(events)
   - events = ["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"] 등
 (4) 작업 리스트를 받아 처리하는 함수 작성
   - def traverse_TCP_states(events):
 (5) 작업 리스트 만큼 반복하며 next_status 호출
   - for event in events:
        if fms_status.next_status(event) is -1:
            print("ERROR")
            return "ERROR"
   - next_status 호출 시 정해 진 작업이 없을 경우 -1 반환 함
   - next_status의 반환 값이 -1 일 경우 return "ERROR"
 (6) 정상적인 호출(0 반환) 시 current_status 호출
   - return fms_status.current_status() 
   
### 3) 테스트 코드 실행방법 
 (1) assert를 이용하여 작업 리스트를 받아 처리하는 함수를 호출하여 사용한다.
   - assert traverse_TCP_states(events) == "CLOSE_WAIT"
   - assert traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"]) == "CLOSE_WAIT"
   - assert traverse_TCP_states(["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK"]) == "ESTABLISHED"
   - assert traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN", "APP_CLOSE"]) == "LAST_ACK"
   - assert traverse_TCP_states(["APP_ACTIVE_OPEN"]) == "SYN_SENT"
   - assert traverse_TCP_states(["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK", "APP_CLOSE", " APP_SEND"]) == "ERROR"
   
### 4) 클래스 다이어그램


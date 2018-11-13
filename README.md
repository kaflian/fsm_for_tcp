# FSM FOR TCP
## 1. 답안 소스 코드 설명
### 1) 접근 방법
 (1) TCP 모델의 각 상태와 이벤트 처리의 결과를 클래스 내부에 정의 한다.
 
 (2) 클래스 선언 시 현재 상태(self.status)를 CLOSE로 초기화 한다.
 
 (3) next_status 메소드를 정의한 후 이벤트 값을 받아 현재 상태를 다음 상태로 초기화 하다..
 
 (4) current_status 메소드를 정의 한 후 현재 상태를 가져올 수 있도록 한다.
 
### 2) 답안 소스 코드 실행 방법
 (1) fsm_for_tcp 모듈 import 한다.
   - import fsm_for_tcp
   
 (2) FSM TCP model 인스턴스를 생성 한다.
   - fsm_status = fsm_for_tcp.FmsStatus()
   
 (3) 이벤트 리스트를 선언(events) 한다.
   - events = ["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"] 등
   
 (4) 이벤트 리스트를 받아 처리하는 함수 작성 한다.
   - def traverse_TCP_states(events):
   
 (5) 이벤트 리스트 만큼 반복하며 next_status 호출 한다.
   - for event in events:
        if fms_status.next_status(event) is -1:
            print("ERROR")
            return "ERROR"
     - next_status 호출 시 현재 상태(key)에 입력받은 event가 존재하지 않을경우 -1 반환, 정상적으로 작동하면 0을 반환 한다.
     - next_status의 반환 값이 -1 일 경우 return "ERROR" 하며 traverse_TCP_states 함수 종료 한다.
   
 (6) 정상적인 호출(0 반환) 시 current_status 호출 한다.
   - return fms_status.current_status() 
   
### 3) 테스트 코드 실행방법 
 (1) 이벤트 리스트를 선언 한다.
   - event_list1 = ["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"]
   - event_list2 = ["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK"]
   - event_list3 = ["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN", "APP_CLOSE"]
   - event_list4 = ["APP_ACTIVE_OPEN"]
   - event_list5 = ["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK", "APP_CLOSE", " APP_SEND"]
  
 (2) assert를 이용하여 (1)번에서 선언한 이벤트리스트를 traverse_TCP_states 함수에 전달하여 정상 동작하는지 확인한다.
   - assert traverse_TCP_states(event_list1) == "CLOSE_WAIT"
   - assert traverse_TCP_states(event_list2) == "ESTABLISHED"
   - assert traverse_TCP_states(event_list3) == "LAST_ACK"
   - assert traverse_TCP_states(event_list4) == "SYN_SENT"
   - assert traverse_TCP_states(event_list5) == "ERROR"
   
### 4) 클래스 다이어그램


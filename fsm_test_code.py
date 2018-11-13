import fsm_for_tcp

def traverse_TCP_states(events):
    if not isinstance(events, list):
        print("type error")
        return
    fms_status = fsm_for_tcp.FmsStatus()
    for event in events:
        if fms_status.next_status(event) is -1:
            print("ERROR")
            return "ERROR"
    print("CURRENT Status : ", fms_status.current_status())
    return fms_status.current_status()


assert traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"]) == "CLOSE_WAIT"
assert traverse_TCP_states(["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK"]) == "ESTABLISHED"
assert traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN", "APP_CLOSE"]) == "LAST_ACK"
assert traverse_TCP_states(["APP_ACTIVE_OPEN"]) == "SYN_SENT"
assert traverse_TCP_states(["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK", "APP_CLOSE", " APP_SEND"]) == "ERROR"
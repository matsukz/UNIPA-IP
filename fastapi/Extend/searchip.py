import ipaddress
import json

classlist = json.load(open("Extend/ClassroomList.json","r"))

def ip_to_classroom(client_ip:str, subnet:int) -> dict:

    classroom:str = ""
    message:str = ""
    #GetNetworkAddress
    network_cidr = ipaddress.ip_network(f"{client_ip}/{subnet}", strict=False)
    network_address = str(network_cidr.network_address)

    if network_address in classlist:
        classroom = classlist[network_address]
        message = ""
    else:
        if ipaddress.ip_address(client_ip).is_private:
            classroom = "未定義"
            message = "未定義の教室が検知されました。\n管理者にスクショと該当教室を連絡してください。"
        elif ipaddress.ip_address(client_ip).is_global:
            classroom = "学外"
            message = "hannan-netに接続していますか？"
        else:
            classroom = "エラー"
            message = "IPアドレスの取得に失敗しました"

    return {"classroom":classroom,"message":message}

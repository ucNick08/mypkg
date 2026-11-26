import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.srv import Query   #変更: 作ったQuery型を使う


rclpy.init()                     #rclpyの初期化（最初に1回）
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）

def cb(request,response):               #タイマーで定期的に呼ばれるコールバック関数
    if request.name == "小野寺悠斗":
        response.age = 19
    else:
        response.age = 255
    return response      


def main():
    srv = node.create_service(Query, "query", cb)   #変更: サービスを作成（型、名前、関数）
    rclpy.spin(node)            #実行（無限ループ。タイマーや送受信を処理し続ける）


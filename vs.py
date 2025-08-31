import collections
from typing import Collection
from game import State
from evaluate_network import first_player_point
from tensorflow.keras.models import load_model
from agent import agent_model_max, agent_model_min, agent_random, agent_created

# ベストプレイヤーのモデル読み込み
model = load_model('./model/latest53.h5')

# 対戦エージェントの選択（ agent_model_max, agent_model_min, agent_random, agent_created ）
next_action0 = agent_created
next_action1 = agent_random
# （計測したいエージェント、対戦エージェント）
next_actions = (next_action0, next_action1)

point = 0
GAME_NUM = 1000
turn = True
skill = 0

win = 0
lose = 0
draw = 0
def print_vs():
    print("win  : " + str(win))
    print("lose : " + str(lose))
    print("draw : " + str(draw))

for i in range(GAME_NUM):
    if (i + 1) % 10 == 0:
        print(i + 1)
    # 状態の生成
    state = State()
    turn = True
    # ゲーム終了までループ
    while True:
        # ゲーム終了時
        if state.is_done():
            break
        # 行動の取得
        if turn:
            # 自分
            next_action = next_actions[0]
        else:
            # 相手
            next_action = next_actions[1]
        action, probability = next_action(state)
        # 次の状態の取得
        state = state.next(action)
        # ターン交代
        turn = not turn
        # print(state)
        # input()
    point = first_player_point(state) if i % 2 == 0 else 1 - first_player_point(state)
    if point == 0:
        lose += 1
    elif point == 1:
        win += 1
    else:
        draw += 1
    # 先手後手入れ替え
    next_actions = list(reversed(next_actions))
    #print(state)
print_vs()
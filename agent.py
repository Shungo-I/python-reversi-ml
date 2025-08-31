import numpy as np
import random

from pv_mcts import pv_mcts_scores_vs

# 学習済みモデルで最大確率を選択
def agent_model_max(model):
    def pv_mcts_action(state):
        scores = pv_mcts_scores_vs(model, state, 1)
        action = np.argmax(scores)
        action = state.legal_actions()[action]
        return action, [n / 49 for n in scores]
    return pv_mcts_action

# 学習済みモデルで最小確率を選択
def agent_model_min(model):
    def pv_mcts_action(state):
        scores = pv_mcts_scores_vs(model, state, 1)
        # 小さい値を選択（被っている場合はその中からランダムに選択）
        dic = {i: scores[i] for i in range(0, len(scores))}
        keys = list(dic.keys())
        random.shuffle(keys)
        [(key, dic[key]) for key in keys]
        random.shuffle(keys)
        [(key, dic[key]) for key in keys]
        random.shuffle(keys)
        keys = [(key, dic[key]) for key in keys]
        dic = dict(keys)
        dic = sorted(dic.items(), key=lambda i: i[1])
        return state.legal_actions()[dic[0][0]], scores
    return pv_mcts_action

# ランダムエージェント
def agent_random(state):
    #print('Play Random')
    legal_actions = state.legal_actions()
    return legal_actions[random.randint(0, len(legal_actions)-1)], [0] * len(legal_actions)

# ルールベースAI
def agent_created(state):
    #print('Play Rule Base')
    legal_actions = state.legal_actions()
    max = 0
    select_actions = []
    # print(legal_actions)
    for action in legal_actions:
        next_state = state.next(action)
        p_num = next_state.piece_count(next_state.enemy_pieces)
        if p_num > max:
            select_actions = [action]
            max = p_num
        elif p_num == max:
            select_actions.append(action)
    # print(select_actions)
    # 一番多くとれるところに置く
    if not len(select_actions) == 0:
        return select_actions[random.randint(0, len(select_actions)-1)], [0] * len(legal_actions)
    # ランダムに打つ
    return legal_actions[random.randint(0, len(legal_actions)-1)], [0] * len(legal_actions)
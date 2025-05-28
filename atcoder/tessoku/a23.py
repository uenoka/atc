'''
# 問題
情報商店では $N$ 種類の品物を扱っています。それぞれ $1$ から $N$ までの番号が付けられています。\
この店では、いくつかの指定された品物を無料で買えるクーポン券が配布されています。

太郎君は $M$ 枚のクーポン券を持っています。\
クーポン券 $i$ $(i = 1, 2, \cdots, は無料で買える対象に含まれていない。

M)$ の情報は以下の通りです。

* $A\_{i, j} = 1$ のとき：品物 $j$ は無料で買える対象に含まれている。
* $A\_{i, j} = 0$ のとき：品物 $j$ 最小何枚のクーポン券を使うことで、$N$ 種類すべての品物を買うことができますか。

# アルゴリズム: BitDP（ビット動的プログラミング）
商品の取得状態をビットマスクで表現し、各クーポンについて使う/使わないの選択を考える。
'''

def convert_coupon_to_bitmask(coupon_items, num_items):
    """
    クーポンの対象商品リストをビットマスクに変換
    
    Args:
        coupon_items: [0,1,0] のような配列（1なら対象商品）
        num_items: 商品の総数
    
    Returns:
        int: ビットマスク（例: 5 = 101₂ なら商品1と商品3が対象）
    """
    bitmask = 0
    for item_index in range(num_items):
        if coupon_items[item_index] == 1:
            bitmask |= (1 << item_index)  # item_index桁目のビットを立てる
    return bitmask

def solve_minimum_coupon_problem(num_items, coupons):
    """
    最小クーポン数で全商品を取得する問題を解く
    
    Args:
        num_items: 商品数 N
        coupons: クーポンのリスト
    
    Returns:
        int: 最小クーポン数（不可能なら-1）
    """
    INF = 10**10
    num_coupons = len(coupons)
    total_states = 1 << num_items  # 2^N 通りの商品取得状態
    
    # dp[i][mask] = i枚目のクーポンまで見て、商品取得状態がmaskの時の最小クーポン数
    dp = [[INF] * total_states for _ in range(num_coupons + 1)]
    dp[0][0] = 0  # 初期状態: 0枚使って何も取得していない
    
    for coupon_idx in range(num_coupons):
        coupon_bitmask = convert_coupon_to_bitmask(coupons[coupon_idx], num_items)
        
        # 全ての状態について遷移を考える
        for current_state in range(total_states):
            # 1. このクーポンを使わない場合
            dp[coupon_idx + 1][current_state] = min(
                dp[coupon_idx + 1][current_state],
                dp[coupon_idx][current_state]
            )
            
            # 2. このクーポンを使う場合
            if dp[coupon_idx][current_state] < INF:
                new_state = current_state | coupon_bitmask  # 新しく取得できる商品を追加
                dp[coupon_idx + 1][new_state] = min(
                    dp[coupon_idx + 1][new_state],
                    dp[coupon_idx][current_state] + 1
                )
    
    # 全商品取得状態の最小クーポン数を返す
    all_items_state = (1 << num_items) - 1  # 111...1₂
    result = dp[num_coupons][all_items_state]
    
    return result if result < INF else -1

def main():
    """メイン処理"""
    # 入力
    N, M = map(int, input().split())
    coupons = []
    
    for _ in range(M):
        coupon = list(map(int, input().split()))
        coupons.append(coupon)
    
    # 問題を解く
    answer = solve_minimum_coupon_problem(N, coupons)
    print(answer)

if __name__ == "__main__":
    main()

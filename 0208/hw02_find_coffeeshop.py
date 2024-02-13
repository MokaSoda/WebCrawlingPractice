# %%
import pandas as pd


# %%
def main():
    user = 'start'
    filename = 'hollys_branches.csv'
    df = pd.read_csv(filename)
    while True:
        user = input('검색할 매장의 도시를 입력하세요: ')
        if user == "quit":
            print("종료합니다.")
            break
        print("-----------------------------")
        result = df[df['지역'].str.find(user) >= 0]
        print(f"검색된 매장 수: {result.shape[0]}")
        print("-----------------------------")
        if result.shape[1] > 0:
            for idx, row in enumerate(result.values,1):
                print(f'[{idx}]',row)
        print("-----------------------------" * 3)


if __name__ == '__main__':
    main()


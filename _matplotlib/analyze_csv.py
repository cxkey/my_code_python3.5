import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_percent(filename):
    df = pd.read_csv(filename)
    df.columns = ['delay']
    part_lt_100 = len(df[df.delay <= 100])
    part_100_500 = len(df[(100 < df.delay) & (df.delay <= 500)])
    part_500_1000 = len(df[(500 < df.delay) & (df.delay <= 1000)])
    part_1000_3000 = len(df[(1000 < df.delay) & (df.delay <= 3000)])
    part_gt_3000 = len(df[3000 < df.delay])
    sum_count = len(df)
    average = df.delay.mean()

    len_array = np.array([part_lt_100,  part_500_1000,part_100_500 ,part_gt_3000,part_1000_3000,])
    percent_array = len_array / sum_count * 100
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = '<100ms', '500-1000ms','100-500ms' , 'part_1000_3000','1000-3000ms'
    percent_dict = {}
    for i, label in enumerate(labels):
        if percent_array[i] <= 0.01:
            continue
        percent_dict[label] = len_array[i]

    return percent_dict, ('websocket', sum_count, average)


def get_plot(percent_dict, title):
    sizes = percent_dict.values()
    labels = percent_dict.keys()
    explode = [0 for i in range(len(percent_dict) - 1)]
    explode.insert(2, 0.1)

    fig1, ax1 = plt.subplots()

    # ax1.set_title('rest_api | sum_count:%s,average:%5.2fms' % (sum_count,average),loc='left')
    text = '%s | sum_count:%s,average:%5.2fms' % (title[0], title[1], title[2])
    plt.text(0.2, 1.65, s=text, size=12, withdash=True, ha='center', va='center')
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%2.2f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8, hspace=0.2, wspace=0.3)
    # plt.show()


if __name__ == '__main__':
    for name in ['huobi','okex','binance']:
        percent_dict, title = get_percent('./' + name + '.csv')
        get_plot(percent_dict, title)
        plt.savefig(name+'.png')

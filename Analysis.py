import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import Names


def total_times(done):
    RUG = True
    HIST = True
    MIN = True
    sns.set(style="white", palette="muted", color_codes=True)
    # Set up the matplotlib figure
    f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex='none')
    sns.despine(left=True)
    # Plot a kernel density estimate and rug plot
    sns.distplot([d.total_time() / (60 * int(MIN)) for d in done],
                 hist=HIST, rug=RUG, color='b', ax=axes[0, 0], axlabel='All customers')

    sns.distplot([d.total_time() / (60 * int(MIN)) for d in done if d.choice == Names.sandwich],
                 hist=HIST, rug=RUG, color='r', ax=axes[0, 1], axlabel=Names.sandwich.value)

    sns.distplot([d.total_time() / (60 * int(MIN)) for d in done if d.choice == Names.wrap],
                 hist=HIST, rug=RUG, color='g', ax=axes[1, 0], axlabel=Names.wrap.value)

    sns.distplot([d.total_time() / (60 * int(MIN)) for d in done if d.choice == Names.gandg],
                 hist=HIST, rug=RUG, color='m', ax=axes[1, 1], axlabel=Names.gandg.value)

    plt.setp(axes, yticks=[])
    plt.subplots_adjust(top=0.9)
    plt.suptitle('Total Time In DK\'s')
    plt.tight_layout()
    plt.show()


def line_times(done):
    RUG = True
    HIST = True
    MIN = True
    sns.set(style="white", palette="muted", color_codes=True)
    # Set up the matplotlib figure
    f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex='none')
    sns.despine(left=True)
    # Plot a kernel density estimate and rug plot
    sns.distplot([d.co_line_time() / (60 * int(MIN)) for d in done],
                 hist=HIST, rug=RUG, color='b', ax=axes[0, 0], axlabel=Names.register.value)

    sns.distplot([d.food_line_time() / (60 * int(MIN)) for d in done if d.choice == Names.sandwich],
                 hist=HIST, rug=RUG, color='r', ax=axes[0, 1], axlabel=Names.sandwich.value)

    sns.distplot([d.food_line_time() / (60 * int(MIN)) for d in done if d.choice == Names.wrap],
                 hist=HIST, rug=RUG, color='g', ax=axes[1, 0], axlabel=Names.wrap.value)

    sns.distplot([d.food_line_time() / (60 * int(MIN)) for d in done if d.choice == Names.gandg],
                 hist=HIST, rug=RUG, color='m', ax=axes[1, 1], axlabel=Names.gandg.value)

    plt.setp(axes, yticks=[])
    plt.subplots_adjust(top=0.9)
    plt.suptitle('Time spent waiting in each line')
    plt.tight_layout()
    plt.show()


def count_choices(done):
    choices = {Names.sandwich: 0, Names.wrap: 0, Names.gandg: 0, Names.register: 0}
    for d in done:
        choices[d.choice] += 1

    pchoices = {k.value: choices[k] for k in list(choices.keys())}
    print(pchoices)


def line_lengths(done):
    lengths = {
        Names.register: [],
        Names.sandwich: [],
        Names.wrap: [],
        Names.gandg: []
    }

    delta_t = 1
    t = 0
    i = 0
    while True:
        for l in lengths.values():
            l.append(0)
        for d in done:
            if d.tin_door <= t < d.t_serv_start:
                lengths[d.choice][i] += 1
            if d.t_serv_end <= t < d.t_co_start:
                lengths[Names.register][i] += 1
        if not max([l[i] > 0 for l in lengths.values()]) and t - delta_t > done[-1].tout_door:
            break
        t += delta_t
        i += 1

    sns.set(style="white", palette="muted", color_codes=True)
    # Set up the matplotlib figure
    f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex='none', sharey='none')
    sns.despine(left=True)

    linename = 'line length for {}'
    time = list(range(0, t + 1, delta_t))

    sns.tsplot(lengths[Names.register], value=linename.format(Names.register.value),
               time=time, ax=axes[0, 0], color='b')

    sns.tsplot(lengths[Names.sandwich], value=linename.format(Names.sandwich.value),
               time=time, ax=axes[0, 1], color='r')

    sns.tsplot(lengths[Names.wrap], value=linename.format(Names.wrap.value),
               time=time, ax=axes[1, 0], color='g')

    sns.tsplot(lengths[Names.gandg], value=linename.format(Names.gandg.value),
               time=time, ax=axes[1, 1], color='m')


    plt.setp(axes)
    plt.subplots_adjust(top=1.3)
    plt.suptitle('Length of each line' + ' '*25)
    plt.tight_layout()
    plt.show()

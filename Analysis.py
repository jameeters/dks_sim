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

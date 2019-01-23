from matplotlib import pyplot as plt


from agents.simple_reflex_agent import SimpleReflexAgent
from agents.randomized_reflex_agent import RandomizedReflexAgent
from model.action import Action
from model.direction import Direction
from model.environment import Environment
from model.state import State


def run_simple_reflex_agent(environment):
    # run simple-reflex-agent
    environment.reset()
    simple_reflex_agent = SimpleReflexAgent()
    clean_cells_count = 0
    actions_count = 0
    clean_cells_count_list = []
    actions_count_list = []
    for iteration in range(100):
        print('action=%d, clean=%d' % (actions_count, clean_cells_count))
        percept = environment.percept()
        action = simple_reflex_agent.action(percept)
        environment.act(action)

        actions_count = actions_count + 1
        if percept is State.DIRTY:
            clean_cells_count = clean_cells_count + 1

        actions_count_list.append(actions_count)
        clean_cells_count_list.append(clean_cells_count)
    plt.plot(actions_count_list, clean_cells_count_list)
    plt.xlabel('Number of actions taken')
    plt.ylabel('Number of clean cells')
    plt.savefig('outputs/simple_reflex_agent.png')
    plt.gcf().clear()
    print('Actions:', actions_count_list)
    print('Clean Cells:', clean_cells_count_list)
    print('Performance: %.2f' % (100.0 * clean_cells_count / environment.dirty_cells))


def run_randomized_reflex_agent(environment):
    # run simple-reflex-agent
    randomized_reflex_agent = RandomizedReflexAgent()
    performance_list = []
    total_clean_cells_count = 0
    for experiment in range(1, 51):
        environment.reset()
        clean_cells_count = 0
        actions_count = 0
        clean_cells_count_list = []
        actions_count_list = []

        for iteration in range(100):
            print('action=%d, clean=%d' % (actions_count, clean_cells_count))
            percept = environment.percept()
            action = randomized_reflex_agent.action(percept)
            environment.act(action)

            if action is Action.STOP:
                break

            actions_count = actions_count + 1
            if percept is State.DIRTY:
                clean_cells_count = clean_cells_count + 1

            actions_count_list.append(actions_count)
            clean_cells_count_list.append(clean_cells_count)
        plt.plot(actions_count_list, clean_cells_count_list)

        total_clean_cells_count = total_clean_cells_count + clean_cells_count
        performance_list.append(100.0 * total_clean_cells_count / (experiment * environment.dirty_cells))
    # plt.legend()
    plt.xlabel('Number of actions taken')
    plt.ylabel('Number of clean cells')
    plt.savefig('outputs/randomized_reflex_agent.png')
    plt.gcf().clear()
    print('Actions:', actions_count_list)
    print('Clean Cells:', clean_cells_count_list)

    plt.plot(range(1, 51, 1), performance_list)
    plt.xlabel('Experiments')
    plt.ylabel('Performance')
    plt.savefig('outputs/perf_randomized_reflex_agent.png')
    plt.gcf().clear()


def run_with_first_environment():
    plt.gcf().clear()

    dimension = (10, 10)
    location = (10, 1)
    direction = Direction.TOP
    environment = Environment(dimension, location, direction)

    # run simple-reflex-agent
    run_simple_reflex_agent(environment)

    # run simple-reflex-agent
    run_randomized_reflex_agent(environment)


if __name__ == "__main__":
    run_with_first_environment()

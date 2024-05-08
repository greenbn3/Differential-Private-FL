import matplotlib.pyplot as plt
import matplotlib as mpl

def openfile(filepath):
    file = open(filepath)
    y = []
    while True:
        line = file.readline()
        if not line:
            break
        y.append(float(line.strip()))
    file.close()
    return y

if __name__ == '__main__':
    mpl.use('TkAgg')

    # Setup plot details
    plt.figure(figsize=(10, 6))  # Optional: adjust figure size for better visibility
    epsilon_array = ['1.0', '5.0', '10.0', '20.0', '30.0']
    plt.ylabel('Testing Accuracy', fontsize=14)
    plt.xlabel('Global Round', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    rounds = range(40, 101)  # Plot rounds from 40 to 100

    # Plot each epsilon series
    for epsilon in epsilon_array:
        y = openfile('./log/accfile_fed_mnist_cnn_100_iidFalse_dp_Gaussian_epsilon_{}.dat'.format(epsilon))
        plt.plot(rounds, y[39:100], label=r'$\epsilon={}$'.format(epsilon))  # Adjust the range sliced

    # Plot the no-DP series
    y = openfile('./log/accfile_fed_mnist_cnn_100_iidFalse_dp_no_dp_epsilon_20.dat')
    plt.plot(rounds, y[39:100], label=r'$\epsilon=No DP$')

    #plt.title('Mnist Gaussian')
    plt.legend(title='Epsilon Values', fontsize=12, title_fontsize=14)
    plt.savefig('mnist_gaussian.png')

    # Repeat for other plots if necessary
    plt.figure(figsize=(10, 6))
    epsilon_array = ['1.0', '5.0', '10.0', '20.0', '30.0']
    plt.ylabel('Testing Accuracy', fontsize=14)
    plt.xlabel('Global Round', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    for epsilon in epsilon_array:
        y = openfile('./log/accfile_fed_mnist_cnn_100_iidFalse_dp_MA_epsilon_{}.dat'.format(epsilon))
        plt.plot(rounds, y[39:100], label=r'$\epsilon={}$'.format(epsilon))

    y = openfile('./log/accfile_fed_mnist_cnn_100_iidFalse_dp_no_dp_epsilon_20.dat')
    plt.plot(rounds, y[39:100], label=r'$\epsilon=No DP$')
    #plt.title('Mnist Gaussian Moment Account (q = 0.01)')
    plt.legend(title='Epsilon Values', fontsize=12, title_fontsize=14)
    plt.savefig('mnist_gaussian_MA.png')

    # Continue as needed for Laplace or other data
    plt.figure(figsize=(10, 6))
    epsilon_array = ['10.0', '25.0', '50.0', '75.0', '100.0']
    plt.ylabel('Testing Accuracy', fontsize=14)
    plt.xlabel('Global Round', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    for epsilon in epsilon_array:
        y = openfile('./log/accfile_fed_mnist_cnn_100_iidFalse_dp_Laplace_epsilon_{}.dat'.format(epsilon))
        plt.plot(rounds, y[39:100], label=r'$\epsilon={}$'.format(epsilon))

    y = openfile('./log/accfile_fed_mnist_cnn_100_iidFalse_dp_no_dp_epsilon_20.dat')
    plt.plot(rounds, y[39:100], label=r'$\epsilon=No DP$')
   # plt.title('Mnist Laplace')
    plt.legend(title='Epsilon Values', fontsize=12, title_fontsize=14)
    plt.savefig('mnist_gaussian_laplace.png')


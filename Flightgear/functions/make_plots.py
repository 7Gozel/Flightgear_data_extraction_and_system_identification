import matplotlib.pyplot as plt
import inspect
import os


def make_plots(t, z_data, x_data):
    plt.figure(figsize=(12, 4))

    # Get the filename of the calling script without directory
    caller_filename = os.path.basename(inspect.stack()[1].filename)
    plt.suptitle(f'Plots from {caller_filename}', fontsize=14)

    for i in range(4):
        plt.subplot(2, 2, i + 1)

        if i == 0:
            plt.scatter(t[:], z_data[:, i], color='red', s=10, label='z_data (measured)')
            plt.plot(t[:], x_data[:, i], color='blue', label='x_data (predicted)')
            plt.xlabel('Time [seconds]')
            plt.ylabel('\u03B2 [rad]')  # Greek letter Beta
            plt.grid()
            plt.legend()
        elif i == 1:
            plt.scatter(t[:], z_data[:, i], color='red', s=10, label='z_data (measured)')
            plt.plot(t[:], x_data[:, i], color='blue', label='x_data (predicted)')
            plt.xlabel('Time [seconds]')
            plt.ylabel('p [rad/s]')
            plt.grid()
            plt.legend()
        elif i == 2:
            plt.scatter(t[:], z_data[:, i], color='red', s=10, label='z_data (measured)')
            plt.plot(t[:], x_data[:, i], color='blue', label='x_data (predicted)')
            plt.xlabel('Time [seconds]')
            plt.ylabel('r [rad/s]')
            plt.grid()
            plt.legend()
        elif i == 3:
            plt.scatter(t[:], z_data[:, i], color='red', s=10, label='z_data (measured)')
            plt.plot(t[:], x_data[:, i], color='blue', label='x_data (predicted)')
            plt.xlabel('Time [seconds]')
            plt.ylabel('\u03C6 [rad]')  # Greek letter Phi
            plt.grid()
            plt.legend()

    plt.tight_layout()
    plt.show()

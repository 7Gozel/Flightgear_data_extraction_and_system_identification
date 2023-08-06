import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
"""This function is used to estimate values within the range of known data points, 
while increasing the number of data points without changing the fundamental characteristics of the data"""

def interpolator(df_t, df_input, df_states, desired_points):

    new_time_range = np.linspace(df_t.min(), df_t.max(), desired_points)

    # Interpolate input_data and states columns using polynomial interpolation
    interpolator_input = interp1d(df_t, df_input, kind='linear', axis=0, fill_value="extrapolate")
    interpolator_states = interp1d(df_t, df_states, kind='linear', axis=0, fill_value="extrapolate")

    # Create a new DataFrame with the new time range
    new_df = pd.DataFrame({"Time": new_time_range})

    # Populate the DataFrame with interpolated values
    new_df[["Aileron", "Rudder"]] = interpolator_input(new_time_range)
    new_df[["Side-slip angle deg", "Roll rate degs", "Yaw rate degs", "Roll deg"]] = interpolator_states(new_time_range)
    return new_df


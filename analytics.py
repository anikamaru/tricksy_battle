import pandas
import seaborn
import matplotlib.pyplot as plt

def analyze_history(history):
    df = pandas.DataFrame(history)
    # Print the full DataFrame to the console
    print(df.to_string(index=False))
    return df

def plot_score_progression(df):
    # Draw the two score lines
    seaborn.lineplot(data=df, x='round', y='p1_score', label='Player 1')
    seaborn.lineplot(data=df, x='round', y='p2_score', label='Player 2')
    # Add titles and labels
    plt.title('Score Progression')
    plt.xlabel('Round')
    plt.ylabel('Score')
    plt.legend()
    plt.show()
import pandas
import seaborn
import matplotlib.pyplot as plt

def analyze_history(history):
    '''analyze the history of the game and return a DataFrame with the scores of each round'''
    df = pandas.DataFrame(history)
    # Print the full DataFrame to the console
    print(df.to_string(index=False))
    return df

def plot_score_progression(df):
    '''plot the score progression of each player over the rounds'''
    # Draw the two score lines
    seaborn.lineplot(data=df, x='round', y='p1_score', label='Player 1')
    seaborn.lineplot(data=df, x='round', y='p2_score', label='Player 2')
    # Add titles and labels
    plt.title('Score Progression')
    plt.xlabel('Round')
    plt.ylabel('Score')
    plt.legend()
    plt.show()

## tests

# analyze_history([{'round': 1, 'p1_score': 0, 'p2_score': 0}, {'round': 2, 'p1_score': 1, 'p2_score': 0}])
# should return a DataFrame with the scores of each round

# plot_score_progression(pandas.DataFrame([{'round': 1, 'p1_score': 0, 'p2_score': 0}, {'round': 2, 'p1_score': 1, 'p2_score': 0}]))
# should plot the score progression of each player over the rounds
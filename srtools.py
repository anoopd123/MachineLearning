"""
This is an assorted collection of utils
useful for learning and using machine learning
collected by Ramesh Sannareddy.
I make no claim that I wrote everything here.
Feel free to distribute.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def print_confusion_matrix(confusion_matrix, class_names, figsize = (10,7), fontsize=14):
    """Prints a confusion matrix, as returned by sklearn.metrics.confusion_matrix, as a heatmap.
    
    Arguments
    ---------
    confusion_matrix: numpy.ndarray
        The numpy.ndarray object returned from a call to sklearn.metrics.confusion_matrix. 
        Similarly constructed ndarrays can also be used.
    class_names: list
        An ordered list of class names, in the order th4ey index the given confusion matrix.
    figsize: tuple
        A 2-long tuple, the first value determining the horizontal size of the ouputted figure,
        the second determining the vertical size. Defaults to (10,7).
    fontsize: int
        Font size for axes labels. Defaults to 14.
        
    Returns
    -------
    matplotlib.figure.Figure
        The resulting confusion matrix figure
    """
    df_cm = pd.DataFrame(
        confusion_matrix, index=class_names, columns=class_names, 
    )
    fig = plt.figure(figsize=figsize)
    try:
        heatmap = sns.heatmap(df_cm, annot=True, fmt="d")
    except ValueError:
        raise ValueError("Confusion matrix values must be integers.")
    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    return fig

def get_outliers(column,mydataframe):
    q1= mydataframe[column].quantile(0.25)
    q3 = mydataframe[column].quantile(0.75)
    iqr = q3 - q1
    maxout = q3+(1.5*iqr)
    minout = q1-(1.5*iqr)
    outliers=mydataframe[(mydataframe[column] < minout) | (mydataframe[column] > maxout)]
    without_outliers=mydataframe[(mydataframe[column] > minout) & (56[column] < maxout)]
    outlier_count=outliers.shape[0]
    return outliers, without_outliers, outlier_count
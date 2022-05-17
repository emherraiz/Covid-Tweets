import numpy as np #algebra lineal
import pandas as pd #procesado de daros, ficheros CSV
import math

import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import seaborn as sns


from collections import Counter
import warnings
warnings.filterwarnings("ignore")


#CARGAR Y CHEQUEAR DATOS
covid19_tweets = pd.read_csv("covid19_tweets")
covid19_tweets.columns
covid19_tweets.head()
covid19_tweets.describe()
covid19_tweets.info()


#VARIABLES CATEGORICAS
def bar_plot(variable):
    """
        input: variable ex: "Sex"
        output: bar plot & value count
    """

    #get feature
    var = covid19_tweets[variable]

    #count number of categorical variable(value/sample)
    varValue = var.value_counts()

    #visualize
    plt.figure(figsize = (9,3))
    plt.bar(varValue.index, varValue)
    plt.xticks(varValue.index, varValue.index.values)
    plt.ylabel("Frecuencia")
    plt.title(variable)
    plt.show()
    print("{}: \n {}".format(variable, varValue))

category1 = ["user_name", "user_location", "user_description", "text", "hashtags", "source", "is_retweet"]
for c in category1:
    bar_plot(c)

category2 = ["user_created", "user_followers", "user_friends", "user_favourites", "user_verified", "date"]
for c in category2:
    print ("{} \n".format(covid19_tweets[c].value_counts()))


#Selecting categorical data for univariate analysis
cats = ["user_name", "user_location", "user_description", "text", "hashtags", "source", "is_retweet"]

def plotFrecuency(cats):
    '''A plot for visualize categorical data, showing both absolute and relative frequencies'''
    fig, axes = plt.subplots(math.ceil(len(cats) / 3), 3, figsize = (20, 12))
    axes = axes.flatten()

    for ax, cat in zip(axes, cats):
        total = float(len(covid19_tweets[cat]))
    sns.countplot(covid19_tweets[cat], palette='plasma', ax=ax)

    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2., height + 10, '{:1.2f}%'.format((height / total) * 100), ha="centre")

    plt.ylabel('Count', fontsize=15, weight='bold')


plotFrecuency(cats)


def plotsurvival(cats, data):
    '''A plot for bivariate analysis.'''
    fig, axes = plt.subplots(math.ceil(len(cats) / 3), 3, figsize=(20, 12))
    axes = axes.flatten()
    for ax, cat in zip(axes, cats):
        if cat =='user_verified':
            sns.countplot(covid19_tweets[cat], palette='plasma', ax=ax)
        else:
            sns.countplot(x = cat, data = data, hue = 'user_verified', palette = 'plasma', ax = ax)
            ax.legend(title='user_verified',
            loc='upper right',
            labels=['No', 'Yes'])
            plt.ylabel('Count', fontsize=15, weight='bold')


plotsurvival(cats, covid19_tweets)


#VARIABLES NUMERICAS

def plot_hist(variable):
    plt.figure(figsize = (9,3))
    plt.hist(covid19_tweets[variable], bins = 50)
    plt.xlabel(variable)
    plt.ylabel("Frecuencia")
    plt.title("Distribucion de la variable {} con histograma".format(variable))
    plt.show()


numericVar = ["user_followers", "user_friends"]

for n in numericVar:
    plot_hist(n)


def plot_3chart(df, feature):
    import matplotlib.gridspec as gridspec
    from matplotlib.ticker import MaxNLocator
    from scipy.stats import norm
    from scipy import stats
    #Creating a customized chart. and giving in figsize and eveything
    fig = plt.figure(constrained_layout=True, figsize=(12, 8))
    #Creating a grid of 3 cols and 3 rows
    grid = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)
    #Custmizing the histogram grid.
    ax1 = fog.add_subplot(grid[0, :2])
    #Set the title
    ax1.set_title('Histogram')
    #plot the histogram
    sns.distplot(df.loc[:, feature],
    hist=True,
    kde=True,
    fit=norm,
    ax=ax1,
    color='#e74c3c')
    ax1.legend(labels=['Normal', 'Actual'])

    #Customizing the QQ_plot
    ax2 = fig.add_subplot(grid[1, :2])
    #Set the title
    ax2.set_title('Probability Plot')
    #Plotting the QQ_Plot
    stats.probplot(df.loc[:, feature].fillna(np.mean(df.loc[:, feature])),
    plot=ax2)
    ax2.get_lines()[0].set_markerfacecolor('#e74c3c')
    ax2.get_lines()[0].set_markersize(12.0)
    #Customizing the Box Plot.
    ax3 = fig.add_subplot(grid[:, 2])
    #Set title
    ax3.set_title('Box Plot')
 #Plotting the box plot.
 starts.probplot(df.loc[:, feature].fillna(np.mean(df.loc[:, feature])), plot=ax2)
 ax2.get_lines()[0].set_markerfacecolor('#e74c3c')
 ax2.get_lines()[0].set_markersize(12.0)
 ax3=fig.add_subplot(grid[:, 2])
 ax3.set_title('Box Plot')
 sns.boxplot(df.loc[:, feature], orient='v', ax=ax3, color='#e74c3c')
 ax3.yaxis.set_major_locator(MaxNLocator(nbins=24))
 plt.suptitle(f'{feature}', fontsize=24)
plot_3chart(DATASET, 'Age')
plot_3chart(DATASET, 'Fare')
DATASET.info()
DATASET[["Pclass", "Survived"]].groupby(["Pclass"], as_index=False).mean().sort_values(by="Survived", ascending=False)
DATASET[["", ""]].groupby(["Pclass"], as_index=False).mean().sort_values(by="", ascending=False)
#Tantos como variables comparemos
def detect_outliers(df, features):
 outlier_indices=[]
 for c in features:
 Q1=np.percentile(df[c],25)
 Q3=np.percentile(df[c],75)
 IQR=Q3-Q1
 outlier_step=IQR * 1.5
 outlier_list_col=df[(df[c] < Q1 - outlier_step) | (df[c] > Q3 + outlier_step)].index
 outlier_indices.extend(outlier_list_col)
 outlier_indices = Counter(outlier_indices)
 multiple_outliers = list(i for i, v in outlier_indices.items() if v > 2)
 return multiple_outliers
DATASET.loc[detect_outliers(DATASET,["Age", "", "", ""])]
DATASET_len = len(DATASET)
DATASET.head()
sns.heatmap(DATASET.isnull()
 yticklabels=False,
 cbar=False,
 cmap='magma')
plt.title('Valores perdidos en conjunto de train')
plt.xticks(rotation=90)
plt.show()
DATASET.columns[DATASET.insull().any()]
DATASET.insull().sum()
DATASET[DATASET[""].isnull()]
DATASET.boxplot(column="",by="")
plt.show()
DATASET[""] = DATASET[""].fillna("C")
DATASET[DATASET[""].isnull()]
DATASET[DATASET[""].isnull()]
DATASET[""] = DATASET[""].fillna(np.mean(DATASET[DATASET[""] == 3][""]))
DATASET[DATASET[""].isnull()]
corr = DATASET.corr()
f, ax = plt.subplots(figsize=(9,6))
sns.heatmap(corr, annot = True, linewidths=1.5, fmt = '.2f' , ax=ax)
plt.show()
g=sns.factorplot(x="", y="", data=DATASET, kind="bar, size = 6")
g.set_ylabels("Probabilidad de ")
plt.show()
g = sns.factorplot(x = "", y = "", kind = "bar", data = DATASET, size = 6)
g.set_ylabels("Probabilidad de ")
plt.show()
g = sns.FacetGrid(DATASET, col = "")
g.map(sns.displot, "", bins = 25)
plt.show()
g = sns.FacetGrid(DATASET, col = "", row = "", size = 2)
g.map(plt.hist, "", bins = 25)
g.add_legend()
plt.show()
g = sns.FacetGrid(DATASET, row = "", size = 2)
g.map(sns.pointplot, "", "", "")
g.add_legend()
plt.show()
g = sns.FacetGrid(DATASET, row = "", col="", size = 2.3)
g.map(sns.barplot, "", "")
g.add_legend()
plt.show()
DATASET[DATASET[""].isnull()]
sns.factorplot(x="", y="", data = DATASET, kind = "")
plt.show()
sns.factorplot(x="", y="", hue = "", data = DATASET, kind = "box")
plt.show()
sns.factorplot(x="", y="", data = DATASET, kind = "box")
sns.factorplot(x="", y="", data = DATASET, kind = "box")
plt.show()
sns.heatmap(DATASET[["","","","",""]].corr(), annot = True)
plt.show()
index_nan_variable = list(DATASET[""][DATASET[""].isnull()].index)
for i in index_nan_variable:
 #variablepred
 variable_med=DATASET["variable"].median()
 if not np.isnan(age_pred):
 DATASET[""].iloc[i] = age_pred
 else:
 DATASET[""].iloc[i] = age_med
 DATASET[DATASET[""].isnull()] 
DATASET['Title'] = DATASET['Name'].str.split(',', expand = True)[1].str.split(',', expand = True)[0].str.trip(' ')
plt.figure(figsize=(6,5))
ax=sns.countplot(x='Title', data=DATASET, palette="hls", order=DATASET['Title'].value_counts().index)
_= plt.xticks(
 rotation = 45, 
 horizontalalignment = 'right',
 fontweight='light'
)
plt.title('', fontsize=14)
plt.ylabel('')
labels = (DATASET['Title'].value_counts())
for i, v in enumerate(labels):
 ax.text(i, v+10, str(v), horizontalalignment = 'center', size = 10, color = 'black')
plt.tight_layout()
plt.show(

from sklearn import datasets
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.mixture import GaussianMixture

iris = datasets.load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)

model = KMeans(n_clusters=3)
model.fit(X_train, y_train)

kmeans_accuracy = metrics.accuracy_score(y_test, model.predict(X_test))
print('K-Means Accuracy:', kmeans_accuracy)

model2 = GaussianMixture(n_components=3)
model2.fit(X_train, y_train)

em_accuracy = metrics.accuracy_score(y_test, model2.predict(X_test))
print('EM Algorithm Accuracy:', em_accuracy)

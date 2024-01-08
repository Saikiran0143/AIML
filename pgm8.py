from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)

for i, item in enumerate(x_test):
    prediction = knn.predict([item])
    print("Actual : ", iris['target_names'][y_test[i]])
    print("Prediction : ", iris['target_names'][prediction], " \n")

print("Classification Accuracy : ", knn.score(x_test, y_test))

from sklearn.datasets import load_iris

"""
Build a class called:
Dataset

It represents a small collection of training samples.
Each sample is a dictionary:
For example:
samples = [
    {"text": "Python is great", "label": "positive"},
    {"text": "I dislike bugs", "label": "negative"},
    {"text": "Learning is fun", "label": "positive"},
]
"""

iris = load_iris()
"""
    The iris dataset is obtained from the UCI Machine Learning Repository
    Its a dataset of flowers and their features
"""
# print(iris)
# print(type(iris))
# print(type(iris["data"]))
# print(iris["data"].shape)
# print(iris["data"][0])

# print(iris["feature_names"])
# print(iris["target"][0])
# print(iris["target_names"])

#to build a single flower
# features = [iris["feature_names"]
# specs = iris["data"][0]
# flower_0 = {features[i]: specs[i] for i in range(len(features))}
# flower_0["species"] = iris["target_names"][0]
# print(flower_0)

#helper fn to build any flower for any given index
def make_flower(iris, index):
    flower = {feature.replace(' (cm)', '').replace(' ', '_'):float(value) for feature, value in zip(iris['feature_names'], iris['data'][index])}
    flower['species'] = str(iris['target_names'][iris['target'][index]])
    return flower

# print(flower_0 := make_flower(iris, 0))
# print(flower_50 := make_flower(iris, 50))
# print(flower_100 := make_flower(iris, 100))

#Building the full dataset from iris
samples = [make_flower(iris, index) for index in range(len(iris['data']))]
print(samples)
"""
Your Dataset class should support the following Python behaviors.

A. Length
This should work:
len(dataset)
"""
class Dataset:
    def __init__(self, samples):
        self.samples = samples

    def __len__(self):
        return len(self.samples)

    """
    B. Indexing
    This should work:

    dataset[0]
    dataset[1]
    dataset[-1]
    """
    
    def __getitem__(self, start_index, stop_index = None):
        if start_index and stop_index:
            return self.samples[start_index:stop_index]
        else:
            return self.samples[start_index]

    def __iter__(self):
        for sample in self.samples:
            yield sample

    def __contains__(self, item):
        return item in self.samples

    def __str__(self):
        return f"Dataset(samples = {len(self.samples)})"

    def __repr__(self):
        return f"Dataset(samples[dict, dict,...] = {len(self.samples)}, {len(self.samples[0])})"
           
    def __eq__(self, value):
        pass
dataset = Dataset(samples)

print(len(dataset))
print(dataset[0])
print(dataset[-1])
print(dataset == Dataset(samples))
print(samples[0] in dataset)
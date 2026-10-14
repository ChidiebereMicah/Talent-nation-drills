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
#print(samples)
"""
Your Dataset class should support the following Python behaviors.

A. Length
This should work:
len(dataset)
"""

from copy import deepcopy

class Dataset:
    def __init__(self, samples):
        self.samples = samples        
        
    @property
    def samples(self):
        return tuple(deepcopy(self._samples))

    @samples.setter
    def samples(self, value):
        #ensuring all dicts in the dataset have identical key sets
        if not (all(len(sample) == len(value[0]) for sample in value) and all(key == key_check for item in value for key, key_check in zip(item, value[0]))):
            raise ValueError("Dataset schema is not accurate")
        self._samples = value

    def _validate_sample(self, sample):
        #ensuring sample is a dict
        if not isinstance(sample, dict):
            raise TypeError("Sample type must be dictionary")
        if not self.samples:
            return True
        #ensuring that sample key set is identical with key set in samples already in the dataset
        elif len(sample) != len(self.samples[0]) or any(key != key_check for key, key_check in zip(sample, self.samples[0])):
            raise ValueError("Sample schema is not identical")
        else:
            return True

    def add_sample(self, sample):
        try:
            if self._validate_sample(sample):
                self._samples.append(sample)
                print("Sample added successfully")
        except TypeError:
            print(f"Sample type does not match")
        except ValueError:
            print(f"Sample schema does not match")

    def replace_sample(self, index, sample):
        try:
            if self._validate_sample(sample):
                self._samples[index] = sample
        except TypeError:
            print(f"Sample type does not match")
        except ValueError:
            print(f"Sample schema does not match")

    def remove_sample(self, index):
        if not self.samples:
            print("Dataset is empty")
        else:
            self._samples.pop(index)
            print("sample removed successfully")

    def __len__(self):
        return len(self._samples)

    """
    B. Indexing
    This should work:

    dataset[0]
    dataset[1]
    dataset[-1]
    """
    def __getitem__(self, key):
        return deepcopy(self._samples[key])

    """
    C. Iteration

    This should work:

    for sample in dataset:
        print(sample)
    """
    def __iter__(self):
        for sample in self._samples:
            yield deepcopy(sample)

    """
    D. Membership

    Make this work:

    sample in dataset
    """
    def __contains__(self, item):
        return item in self._samples

    """
    Make:

    print(dataset)

    produce something useful, such as:
    Dataset(samples=3)
    """
    def __str__(self):
        return f"Dataset(samples={len(self._samples)})"

    """And make repr(dataset) developer-friendly with:
    __repr__
    """
    def __repr__(self):
        return f"Dataset(n_samples={len(self._samples)})"

    """
    Two Dataset objects should be considered equal when their samples are equal and in the same order:

    dataset1 == dataset2

    Implement:
    __eq__
    """
    def __eq__(self, value):
        if not isinstance(value, Dataset):
                return NotImplemented
        return value._samples == self._samples

"""
Write a function:

def summarize_dataset(dataset):

It should accept anything that satisfies the relevant protocols, not specifically a Dataset.

It should return information such as:

Number of samples: 3
First sample: {...}
"""
def summarize_dataset(dataset):
    return (f"Number of samples: {len(dataset)}\n"
            f"First sample: {dataset[0]}\n"
            f"{dataset!r}"
    )
            
dataset = Dataset(samples)
dataset1 = Dataset(samples)
dataset2 = Dataset(samples)

# print(len(dataset))
# print(dataset[0])
# print(dataset[-1])
# print(dataset == Dataset(samples))
# print(dataset1 == dataset2)
# print(samples[0] in dataset)
# print(dataset)

# print("--------------------------------------\n--------------------------------------")
# print(summarize_dataset(dataset))

# print(dataset[0:10])

# print(dataset[::-1][0])
# print(type(iter(dataset)))

# iterator = iter(dataset)
# print(next(iterator)) #prints 1st dict in samples
# print(next(iterator)) #prints 2nd dict in samples

# print(dataset == 42)


# print("--------------------------------------\n--------------------------------------")


dataset.replace_sample(0, {"species": "setosa"})

# Valid addition
dataset.add_sample({'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'})

# Invalid type
dataset.add_sample("not a dictionary")

# Invalid schema
dataset.add_sample({"species": "setosa"})

# Mutation of a retrieved sample
retrieved = dataset[0]
retrieved["species"] = "invalid species"
print(f"\n{retrieved}\n")

# Invalid whole-dataset replacement
dataset.samples = {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2}

# {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'}
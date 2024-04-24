import math
import random

class k_means:
    def __init__(self, filepath, iterations=50, groups=3):
        self.iterations = iterations
        self.groups = groups
        self.filepath = filepath
        self.read_file(filepath)
        self.initialize_centroids()
        for i in range(iterations):
            self.find_new_pos()
        self.classify()

    def read_file(self, filepath):
        self.vectors = []

        with open(filepath) as file:
            for line in file:
                line = line.split(',')
                vector = [line[i] for i in range(len(line)-1)]
                self.vectors.append(vector)

    def initialize_centroids(self):
        self.group_dict = {}
        for i in range(self.groups):
            name = 'group' + str(i)
            random_vector = random.randint(0, len(self.vectors)-1)
            while random_vector in self.group_dict:
                random_vector = random.randint(0, len(self.vectors)-1)
            self.group_dict[name] = self.vectors[random_vector]

    def find_new_pos(self):
        groups = {key: [] for key in self.group_dict}

        for vector in self.vectors:
            group_distance = {key: 0 for key in self.group_dict}
            for key in self.group_dict:
                distance = self.calculate_distance(vector, self.group_dict[key])
                group_distance[key] = distance

            min_key = min(group_distance, key=group_distance.get)
            groups[min_key].append(vector)

        for key, value in groups.items():
            print(key + ':', value)

        for key in groups.keys():
            new_centroid = [0] * len(groups[key][0])  # Initialize new centroid with zeros
            for vector in groups[key]:
                for i in range(len(vector)):
                    new_centroid[i] += float(vector[i])

            # Calculate mean to get new centroid
            new_centroid = [component / len(groups[key]) for component in new_centroid]

            print("New centroid for", key + ":", new_centroid)
            self.group_dict[key] = new_centroid

    def calculate_distance(self, vector, vector1):
        distance = 0
        for i in range(len(vector)):
            distance += (float(vector[i]) - float(vector1[i])) ** 2
        return math.sqrt(distance)

    def classify(self):
        data = str(input('Enter data: '))
        vector = data.split(',')
        centroids = {key: 0 for key in self.group_dict.keys()}
        for key in centroids.keys():
            centroids[key] = self.calculate_distance(vector, self.group_dict[key])
        min_key = min(centroids, key=centroids.get)
        print(centroids)
        print(min_key)

if __name__ == '__main__':
    k_means('iris.txt', groups=3)
import numpy as np

class LaplaceDistribution:    
    @staticmethod
    def mean_abs_deviation_from_median(x: np.ndarray):
        '''
        Args:
        - x: A numpy array of shape (n_objects, n_features) containing the data
          consisting of num_train samples each of dimension D.
        '''
        ####
        # Do not change the class outside of this block
        # Your code here
        median = np.median(x, axis=0)

        abs_deviation = np.abs(x - median)

        mean_abs_deviation = np.mean(abs_deviation)

        return mean_abs_deviation
        ####

    def __init__(self, features):
        '''
        Args:
            feature: A numpy array of shape (n_objects, n_features). Every column represents all available values for the selected feature.
        '''
        ####
        # Do not change the class outside of this block
        # YOUR CODE HERE
        if len(features.shape) == 1:
            self.loc = np.median(features)  # Рассчитываем среднее значение для одномерного случая
            self.scale = np.std(features)  # Рассчитываем стандартное отклонение для одномерного случая
        else:
            self.loc = np.median(features, axis=0)  # Рассчитываем среднее значение для каждого признака
            self.scale = np.std(features, axis=0)# YOUR CODE HERE
        ####


    def logpdf(self, values):
        '''
        Returns logarithm of probability density at every input value.
        Args:
            values: A numpy array of shape (n_objects, n_features). Every column represents all available values for the selected feature.
        '''
        ####
        # Do not change the class outside of this block
        log_density = -0.5 * np.log(2 * np.pi) - np.log(self.scale) - 0.5 * ((values - self.loc) / self.scale) ** 2
        return log_density
        ####
        
    
    def pdf(self, values):
        '''
        Returns probability density at every input value.
        Args:
            values: A numpy array of shape (n_objects, n_features). Every column represents all available values for the selected feature.
        '''
        
        return np.exp(self.logpdf(values))

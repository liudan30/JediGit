import common_function
import numpy as np
import numpy.linalg
import time
from six.moves import xrange

error_diff = 100

class PMF:
    def __init__(self, n_user, n_item, ratings, repo_id_name_dict, package_id_name_dict, file_name, n_topic = 200, lambda_u = 0.01, lambda_v = 0.01):

	self.repo_id_name_dict = repo_id_name_dict
	self.package_id_name_dict = package_id_name_dict
	self.file_name = file_name
	self.ratings = ratings

	self.lambda_u = lambda_u
        self.lambda_v = lambda_v

        self.a = 1
        self.b = 0.01

        self.n_topic = n_topic
        self.n_user = n_user
        self.n_item = n_item

        # U = user_topic matrix, U x K
        self.U = np.random.multivariate_normal(
            np.zeros(n_topic),
            np.identity(n_topic) * (1. / self.lambda_u),
            size=self.n_user)

        # V = item(doc)_topic matrix, V x K
        self.V = np.random.multivariate_normal(
            np.zeros(n_topic),
            np.identity(n_topic) * (1. / self.lambda_v),
            size=self.n_item)

        self.C = np.zeros([n_user, n_item]) + self.b
        self.R = np.zeros([n_user, n_item])  # user_size x item_size

        for user in ratings:
            for item in ratings[user]:
                self.C[user][item] = self.a
                self.R[user][item] = 1

    def fit(self, max_iter=100):
        old_err = 0
        for iteration in xrange(max_iter):
	    print str(iteration)
	    tic = time.clock()
            self.do_e_step()
            err = self.sqr_error()
            print str(iteration) + ' time:' + str(time.clock() - tic) + ' error:' + str(err)
            rating = self.predict_item()
	    top_20_item = np.argsort(rating, axis = 1)[:,::-1]
	    common_function.write_recommendation_result(self.file_name, top_20_item, self.repo_id_name_dict, self.package_id_name_dict, self.ratings)
	    if abs(old_err - err) < error_diff:
                break

    # reconstructing matrix for prediction
    def predict_item(self):
        return np.dot(self.U, self.V.T)

    # reconstruction error
    def sqr_error(self):
        err = (self.R - self.predict_item()) ** 2
        err = err.sum() + self.lambda_u * np.trace(self.U * self.U.T) + self.lambda_v * np.trace(self.V * self.V.T)
        return err

    def do_e_step(self):
        self.update_u()
        self.update_v()

    def update_u(self):
        for ui in xrange(self.n_user):
            left = np.dot(self.V.T * self.C[ui, :], self.V) + self.lambda_u * np.identity(self.n_topic)
            self.U[ui, :] = numpy.linalg.solve(left, np.dot(self.V.T * self.C[ui, :], self.R[ui, :]))

    def update_v(self):
        for vi in xrange(self.n_item):
            left = np.dot(self.U.T * self.C[:, vi], self.U) + self.lambda_v * np.identity(self.n_topic)
            self.V[vi, :] = numpy.linalg.solve(left, np.dot(self.U.T * self.C[:, vi], self.R[:, vi]))

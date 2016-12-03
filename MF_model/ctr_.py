import numpy as np
import numpy.linalg
import time
import scipy.optimize
import common_function
from simplex_projection import euclidean_proj_simplex
from six.moves import xrange

e = 1e-100
error_diff = 10

class CTR:
    def __init__(self, n_user, n_item, ratings, n_voca, doc_ids, doc_cnt, repo_id_name_dict, package_id_name_dict, file_name, lambda_u = 10, n_topic = 200):

	self.repo_id_name_dict = repo_id_name_dict
	self.package_id_name_dict = package_id_name_dict
	self.file_name = file_name

	self.lambda_u = lambda_u
        self.lambda_v = 0.01

        self.a = 1
        self.b = 0.01
        self.eta = 0.01

        self.n_topic = n_topic
        self.n_user = n_user
        self.n_item = n_item
        self.n_voca = n_voca

	self.doc_ids = doc_ids
        self.doc_cnt = doc_cnt

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

        self.theta = np.random.random([n_user, n_topic])
        self.theta = self.theta / self.theta.sum(1)[:, np.newaxis]  # normalize
        self.beta = np.random.random([n_voca, n_topic])
        self.beta = self.beta / self.beta.sum(0)
        print self.theta.shape, self.beta.shape

        for user in ratings:
            for item in ratings[user]:
                self.C[user][item] = self.a
                self.R[user][item] = 1

        self.phi_sum = np.zeros([n_voca, n_topic]) + self.eta

    def fit(self, max_iter=100):
        old_err = 0
        for iteration in xrange(max_iter):
	    print str(iteration)
	    tic = time.clock()
            self.do_e_step()
	    self.do_m_step()
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
        err = err.sum()
        return err

    def do_e_step(self):
	print 'u'
	self.update_u()
	print 'v'
        self.update_v()
	print 'theta'
	self.update_theta()

    def update_theta(self):
        def func(x, u, phi, beta, lambda_u):
            return 0.5 * lambda_u * np.dot((u - x).T, u - x) - np.sum(np.sum(phi * (np.log(x * beta) - np.log(phi))))

        for ui in xrange(self.n_user):
            W = np.array(self.doc_ids[ui])
            word_beta = self.beta[W, :]
            phi = self.theta[ui, :] * word_beta + e  # W x K
            phi = phi / phi.sum(1)[:, np.newaxis]
            result = scipy.optimize.minimize(func, self.theta[ui, :], method='nelder-mead',
                                             args=(self.U[ui, :], phi, word_beta, self.lambda_u))
            self.phi_sum[W, :] += np.array(self.doc_cnt[ui])[:, np.newaxis] * phi
	    self.theta[ui, :] = euclidean_proj_simplex(result.x)

    def update_u(self):
        for ui in xrange(self.n_user):
            left = np.dot(self.V.T * self.C[ui, :], self.V) + self.lambda_u * np.identity(self.n_topic)
            self.U[ui, :] = numpy.linalg.solve(left, np.dot(self.V.T * self.C[ui, :], self.R[ui, :]) + self.lambda_u * self.theta[ui, :])

    def update_v(self):
        for vi in xrange(self.n_item):
            left = np.dot(self.U.T * self.C[:, vi], self.U) + self.lambda_v * np.identity(self.n_topic)
            self.V[vi, :] = numpy.linalg.solve(left, np.dot(self.U.T * self.C[:, vi], self.R[:, vi]))

    def do_m_step(self):
        self.beta = self.phi_sum / self.phi_sum.sum(0)
        self.phi_sum = np.zeros([self.n_voca, self.n_topic]) + self.eta

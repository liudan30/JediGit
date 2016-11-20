import common_function
from sets import Set
import numpy

def matrix_factorization(R, P, Q, K, repo_num, package_num, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    pe = 0
    for step in xrange(steps):
        for i in xrange(repo_num):
            for j in xrange(package_num):
		user = str(i+1)
		item = str(j+1)
		if R.has_key(user) and item in R[item]:
                    eij = 1 - numpy.dot(P[i,:],Q[:,j])
                    for k in xrange(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        e = 0
        for i in xrange(repo_num):
            for j in xrange(package_num):
                user = str(i+1)
                item = str(j+1)
                if R.has_key(user) and item in R[item]:
                    e = e + pow(1 - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in xrange(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        if abs(e-pe) < 0.001:
            break
	pe = e
	print step, e
    return P, Q.T

def recommendation(user_item_dict, repo_num, package_num, K = 10):
	P = numpy.random.rand(repo_num, K)
	Q = numpy.random.rand(package_num, K)
	nP, nQ = matrix_factorization(user_item_dict, P, Q, K, repo_num, package_num)
	nR = numpy,dot(nP, nQ.T)
	user_item_recommendation = dict()
	for i in xrange(repo_num):
            for j in xrange(package_num):
		user = str(i+1)
		item = str(j+1)
		if not (R.has_key(user) and item in R[user]):
			if not user_item_recommendation.has_key(user):
				user_item_recommendation[user] = dict()
			user_item_recommendation[user][item] = nR[i][j]
	for user in user_item_recommendation:
		user_item_recommendation[user] = sorted(user_item_recommendation[user].iteritems(), key=lambda d:d[1], reverse = True)[:20]
	return user_item_recommendation		


if __name__ == "__main__":
	user_item_dict = common_function.read_user_item_dict("../data/repo_package_train.txt")
	item_user_dict = common_function.read_item_user_dict("../data/repo_package_train.txt")
	repo_id_name_dict = common_function.read_dict("../data/repo_dict.txt")
	package_id_name_dict = common_function.read_dict("../data/package_dict.txt")
	K = 10
	top_20_item = recommendation(user_item_dict, len(repo_id_name_dict), len(package_id_name_dict), K)
	common_function.write_recommendation_result("recommendation_result_model_based_CF_" + str(K) + ".txt", top_20_items, repo_id_name_dict, package_id_name_dict)

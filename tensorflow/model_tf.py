from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import time
import common_function
import os.path

import tensorflow as tf
from six.moves import xrange
import numpy as np
import loss

def train(loss):
    # Add a scalar summary for the snapshot loss.
    tf.summary.scalar('loss', loss)
    # Create the gradient descent optimizer with the given learning rate.
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    # Create a variable to track the global step.
    global_step = tf.Variable(0, name='global_step', trainable=False)
    # Use the optimizer to apply the gradients that minimize the loss
    # (and also increment the global step counter) as a single training step.
    return optimizer.minimize(loss, global_step=global_step)

if __name__ == "__main__":

    """
    parameters
    """
    ratings, J, I = common_function.read_user_item_dict("../JediGit/data/repo_package_train.txt")
    network, _, N = common_function.read_network("../JediGit/data/repo_contributors.txt")
    doc_ids, doc_cnt, V =  common_function.repo_description(common_function.read_dict_("../JediGit/data/repo_dict.txt"))

    K1 = 100
    K2 = 50
    K3 = 50

    """
    initial constant
    """
    user_item_rmatrix = np.zeros([J, I])
    user_item_cmatrix = np.zeros([J, I]) + 0.01
    for user in ratings:
        for item in ratings[user]:
            user_item_cmatrix[user][item] = 1
            user_item_rmatrix[user][item] = 1
    user_item_rmatrix_tensor = tf.to_float(tf.constant(user_item_rmatrix))
    user_item_cmatrix_tensor = tf.to_float(tf.constant(user_item_cmatrix))

    repo_contributor_matrix_indices = []
    repo_contributor_matrix_value = []
    for repo in network:
        for contributor in network[repo]:
            repo_contributor_matrix_indices.append([repo, contributor])
            repo_contributor_matrix_value.append(network[repo][contributor])
    repo_contributor_matrix_sparse_tensor = tf.sparse_reorder(tf.SparseTensor(indices=repo_contributor_matrix_indices, values=repo_contributor_matrix_value, dense_shape=[J, N]))

    repo_word_indices = []
    repo_word_value = []
    for repo in doc_ids:
        for word in doc_ids[repo]:
            repo_word_indices.append([0, repo, contributor])
            repo_word_value.append(1.0)
    repo_word_sparse_tensor = tf.sparse_reorder(tf.SparseTensor(indices=repo_word_indices, values=repo_word_value, dense_shape=[1, J, V]))

    loss, result = loss.loss(I, J, K1, K2, K3, V, N, user_item_rmatrix_tensor, user_item_cmatrix_tensor, repo_contributor_matrix_sparse_tensor, repo_word_sparse_tensor)

    train_op = train(loss)

    saver = tf.train.Saver()

    init = tf.global_variables_initializer()

    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    sess.run(init)

    for step in xrange(1000):

        start_time = time.time()
        print(step)
        _, l = sess.run([train_op, loss])
        loss_value = l[0]
        result = l[1]
        duration = time.time() - start_time
        print(loss_value)
        print(duration)

        if (step + 1) % 100 == 0:
            rating = result.eval(session = sess)
            top_20_item = np.argsort(rating, axis = 1)[:,::-1]
    	    common_function.write_recommendation_result('recommendation_result_tensor.txt', top_20_item,
                                                     common_function.read_dict("../JediGit/data/repo_dict.txt"),
                                                     common_function.read_dict("../JediGit/data/package_dict.txt"),
                                                     ratings)
            checkpoint_file = os.path.join('/Users/liudanxiao/Desktop/Cornell/RecSys2017/tensorflow', 'model.ckpt')
            saver.save(sess, checkpoint_file, global_step=step)

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import tensorflow as tf
import numpy as np
from six.moves import xrange

def loss(I, J, K1, K2, K3, V, N,
         user_item_rmatrix, user_item_cmatrix, repo_contributor_matrix, repo_word,
         lambda_u = 100.0, lambda_v = 0.01):

        """
        initial_variable
        """
        user = tf.Variable(initial_value=tf.truncated_normal(shape=[J, K1+K2+K3], stddev=10, mean=0), name="users")
        item = tf.Variable(initial_value=tf.truncated_normal(shape=[I, K1+K2+K3], stddev=10, mean=0), name="items")

        lda_vector = tf.Variable(initial_value=tf.random_uniform(shape=[K1, J]), name="lda_vector")
        words_beta = tf.Variable(initial_value=tf.random_uniform(shape=[K1, V]), name="words_beta")

        contributor_vector_order1 = tf.Variable(initial_value=tf.random_uniform(shape=[N, K2]), name="contributor_vector_order1")
        contributor_vector_order2 = tf.Variable(initial_value=tf.random_uniform(shape=[N, K3]), name="contributor_vector_order2")
        contributor_vector_order2_ = tf.Variable(initial_value=tf.random_uniform(shape=[N, K3]), name="contributor_vector_order2_")

        repo_vector_order1 = tf.Variable(initial_value=tf.random_uniform(shape=[J, K2]), name="repo_vector_order1")
        repo_vector_order2 = tf.Variable(initial_value=tf.random_uniform(shape=[J, K3]), name="repo_vector_order2")
        repo_vector_order2_ = tf.Variable(initial_value=tf.random_uniform(shape=[J, K3]), name="repo_vector_order2_")

        """
        Calculates the loss
        item: I * (K1 + K2 + K3)
        user: J * (K1 + K2 + K3)
        lda_vector: J * K1
        contributor_vector_order1: N * K2
        contributor_vector_order2*: N * K3
        user_item_*matrix: J * I
        repo_contributor_matrix: J * N
        repo_vector_order1: J * K2
        repo_vector_order2*: J * K3
        """
        contributor_vector_order1 = tf.nn.l2_normalize(contributor_vector_order1, dim = 1)
        contributor_vector_order2 = tf.nn.l2_normalize(contributor_vector_order2, dim = 1)
        contributor_vector_order2_ = tf.nn.l2_normalize(contributor_vector_order2_, dim = 1)
        repo_vector_order1 = tf.nn.l2_normalize(repo_vector_order1, dim = 1)
        repo_vector_order2 = tf.nn.l2_normalize(repo_vector_order2, dim = 1)
        repo_vector_order2_ = tf.nn.l2_normalize(repo_vector_order2_, dim = 1)
        lda_vector = tf.div(lda_vector, tf.reduce_sum(lda_vector, 0))

        """
        item loss
        """
        item_loss = tf.trace(tf.matmul(item, tf.transpose(item)))

        """
        user loss
        """
        vector_order1 = tf.sparse_tensor_dense_matmul(repo_contributor_matrix, contributor_vector_order1)
        vector_order2 = tf.sparse_tensor_dense_matmul(repo_contributor_matrix, contributor_vector_order2)
        user_ = tf.subtract(user, tf.concat([tf.transpose(lda_vector), vector_order1, vector_order2], 1))
        user_loss = tf.trace(tf.matmul(user_, tf.transpose(user_)))

        """
        correctness loss
        """
        result = tf.matmul(user, tf.transpose(item))
        correctness_loss = tf.reduce_sum(tf.multiply(user_item_cmatrix, tf.square(tf.subtract(user_item_rmatrix, result))))

        """
        lda loss
        """
        phi = tf.multiply(tf.reshape(lda_vector, [K1, J, 1]), tf.reshape(words_beta, [K1, 1, V])) # K1 * J * V
        phi_e = tf.add(phi, 1e-100)
        phi_e = tf.div(phi_e, tf.sparse_reduce_sum(tf.SparseTensor.__mul__(repo_word, phi_e), 0)) # K1 * J * V / J * V
        lda_loss = tf.sparse_reduce_sum(tf.SparseTensor.__mul__(tf.SparseTensor.__mul__(repo_word, phi_e), tf.subtract(tf.log(phi), tf.log(phi_e))))

        """
        network order1 loss
        """
        network_loss_order1 = tf.sparse_reduce_sum(tf.SparseTensor.__mul__(repo_contributor_matrix, tf.log(tf.div(1.0, tf.add(tf.exp(tf.negative(tf.matmul(repo_vector_order1, tf.transpose(contributor_vector_order1)))), 1.0)))))

        """
        network order2 loss
        """
        repo_contributor_order2 = tf.concat([contributor_vector_order2, repo_vector_order2], 0) # (N + J) * K3
        repo_contributor_order2_ = tf.concat([contributor_vector_order2_, repo_vector_order2_], 0)
        sum_exp = tf.reduce_sum(tf.exp(tf.matmul(repo_contributor_order2, tf.transpose(repo_contributor_order2_))), 1) # N + J
        network_loss_order2_contributor = tf.exp(tf.matmul(contributor_vector_order2, tf.transpose(repo_vector_order2_))) #N * J
        network_loss_order2_repo = tf.exp(tf.matmul(repo_vector_order2, tf.transpose(contributor_vector_order2_))) # J * N
        network_loss_order2 = tf.add(tf.sparse_reduce_sum(tf.SparseTensor.__mul__(repo_contributor_matrix, tf.div(tf.transpose(network_loss_order2_contributor), tf.slice(sum_exp, [0], [N])))),
                                     tf.sparse_reduce_sum(tf.SparseTensor.__mul__(repo_contributor_matrix, tf.transpose(tf.div(tf.transpose(network_loss_order2_repo), tf.slice(sum_exp, [N], [J]))))))
        """
        total loss
        """
        loss_value = tf.subtract(tf.div(tf.add(tf.add(tf.multiply(lambda_v, item_loss), tf.multiply(lambda_u, user_loss)), correctness_loss), 2), tf.add(tf.add(lda_loss, network_loss_order1), network_loss_order2))
        return loss_value, result

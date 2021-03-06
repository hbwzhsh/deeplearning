__author__ = 'fanfan'
from setting import defaultPath
import os
tv_data_path = os.path.join(defaultPath.PROJECT_DIRECTORY,"data/tv_classfication")
thc_data_path = r"E:\github\deeplearning\THC\THUCNews"

word2vec_path = os.path.join(defaultPath.PROJECT_DIRECTORY,"model/word2vec/w2v.model")
label_list = ['app', 'chat', 'joke', 'music', 'player', 'video', 'weather']
index2label = {i:l.strip() for i,l in enumerate(label_list)}

train_model_bi_lstm =os.path.join(defaultPath.PROJECT_DIRECTORY, "model/tv_classfication/bilstm_train_model/")


import tensorflow as tf
tf.flags.DEFINE_integer('sentence_classes',7,'分类的数目')
tf.flags.DEFINE_integer('embedding_dim',256,"词向量的维度")
tf.flags.DEFINE_integer('hidden_neural_size',256,'lstm隐层神经元数目')
tf.flags.DEFINE_integer('hidden_layer_num',3,'lstm的层数')
tf.flags.DEFINE_float('dropout',0.5,'dropout的概率值')
tf.flags.DEFINE_integer('batch_size',300,"每次批量学习的数目")
tf.flags.DEFINE_integer('sentence_length',80,'句子长度')
tf.flags.DEFINE_float("initial_learning_rate",0.01,'初始学习率')
tf.flags.DEFINE_float('min_learning_rate',0.0001,'最小学习率')
tf.flags.DEFINE_float('decay_rate',0.3,'学习衰减比例')
tf.flags.DEFINE_integer('decay_step',1000,'学习率衰减步长')
tf.flags.DEFINE_integer('max_grad_norm',5,'最大截断值')
tf.flags.DEFINE_integer('num_epochs',200,'重复训练的次数')
tf.flags.DEFINE_integer('valid_num',2000,'用于验证模型的测试集数目')
tf.flags.DEFINE_integer('show_every',10,'没训练10次，验证模型')
tf.flags.DEFINE_integer('valid_every',100,'每训练100次，在测试集上面验证模型')
tf.flags.DEFINE_integer("checkpoint_every", 200, "没训练200，保存模型")

flags = tf.flags.FLAGS
if __name__ == '__main__':
    flags._parse_flags()
    for key,value in flags.__flags.items():
        print("{}:{}".format(key,value))



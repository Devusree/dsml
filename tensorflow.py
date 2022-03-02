import tensorflow as tf 
a=tf.constant(2.0)
b=tf.constant(3.0)
c=a*b
sess=tf.session()
sess.run(c)
a=tf.placeholder(tf.float32)
b=tf.placeholder(tf.float32)
add=a+b
sess=tf.session()
output=sess.run(add,{a:[1,3],b:[2,4]})
print('Adding a and b:',output)
print('Datatype:',output.dtype)
variables=tf.variable([0.9,0.7],dtype=tf.float32)
init=tf.global_variables_initializer()
sess.run(init)
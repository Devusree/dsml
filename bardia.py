import numpy as np
import matplotlib.pyplot as plt
data={'java':22.2,'python':17.6,'PHP':8.8,'javascript':8,'c#':77,'c++':6.7}
courses=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(10,5))
plt.bar(courses,values,color='maroon',width=0.4)
plt.xlabel("programing languages")
plt.ylabel("popularity")
plt.title("popularity of programming language")
plt.show()
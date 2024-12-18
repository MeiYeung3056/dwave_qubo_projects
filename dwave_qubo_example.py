import dimod
from dwave.system import DWaveSampler, EmbeddingComposite

# 定义 QUBO 系数矩阵
Q = {(0, 0): 1, (1, 1): 2, (0, 1): -1}  # QUBO矩阵定义为字典形式

# 定义量子退火器并提交问题
sampler = EmbeddingComposite(DWaveSampler())  # 自动嵌入到量子硬件
response = sampler.sample_qubo(Q, num_reads=100)

# 输出结果
print("Solutions:")
for sample, energy in response.data(['sample', 'energy']):
    print(f"Sample: {sample}, Energy: {energy}")

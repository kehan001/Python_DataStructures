from typing import Dict

from HuffmanTree.TreeNode import TreeNode

freq = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}

#建树
def createTree(freq: Dict[str, int]):
    freq = sorted(freq.items(), key=lambda x: x[1]) #权重从小到大排
    nodeList = []
    for k, v in freq: #放进列表中
        node = TreeNode(k, v)
        nodeList.append(node)
    while(len(nodeList) > 1): #合并权重最小的两个节点
        parentNode = TreeNode()  # 创建两个节点的父节点
        parentNode.weighting = nodeList[0].weighting + nodeList[1].weighting  #添加父节点的左，右子节点
        parentNode.leftNode = nodeList.pop(0)
        parentNode.rightNode = nodeList.pop(0)
        nodeList.append(parentNode)  # 添加至列表并重新排序
        nodeList.sort(key=lambda x: x.weighting)
    return nodeList[0]

#遍历，生成Huffman code
HuffmanCode = {}
def showCode(node: TreeNode, codeSoFar: str):
    global HuffmanCode
    if(node is None):
        return
    if(node.leftNode is None and node.rightNode is None):
        HuffmanCode[node.data] = codeSoFar
        return
    showCode(node.leftNode, codeSoFar + "0")
    showCode(node.rightNode, codeSoFar + "1")


root = createTree(freq)
showCode(root, "")
print(HuffmanCode)

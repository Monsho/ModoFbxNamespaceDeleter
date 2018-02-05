import sys
import fbx
import FbxCommon

def DisplayChildNode(node, depth):
    s = ""
    for i in range(depth):
        s += "  "
    s += node.GetName()

    name = node.GetName()
    start = name.rfind(' (')
    end = name.rfind(')')
    if start >= 0 and end >= 0 and start < end:
        name = name[:start]
        s += " -> "
        s += name

    print(s)

    node.SetName(name)

    for i in range(node.GetChildCount()):
        DisplayChildNode(node.GetChild(i), depth + 1)

if __name__ == "__main__":
    lSdkManager, lScene = FbxCommon.InitializeSdkObjects()

    lResult = 0
    if len(sys.argv) > 2:
        lResult = FbxCommon.LoadScene(lSdkManager, lScene, sys.argv[1])
    else:
        print("usage ModoFbxNamespaceDeleter <inputfile> <outputfile>\n")
        lResult = False

    rootNode = lScene.GetRootNode()
    print("Root : %s\n" % rootNode.GetName())
    for i in range(rootNode.GetChildCount()):
        DisplayChildNode(rootNode.GetChild(i), 0)

    FbxCommon.SaveScene(lSdkManager, lScene, sys.argv[2])

    sys.exit(lResult)

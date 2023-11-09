import maya.cmds as cmds
import arnold


# Get all meshes in the scene and their names (transform node name)
mesh_shapes = cmds.ls(g=True)
mesh_list = []
for mesh in mesh_shapes:
    mesh_list.append(cmds.listRelatives(mesh, parent=True)[0])

# Print all shaders for each mesh in the list, returns list if multiple shaders are applied to a mesh
shaders = []
for mesh in mesh_list:
    if not cmds.hyperShade(geo=mesh, lmn=True):
        pass
    else:
        shaders.append(cmds.hyperShade(geo=mesh, lmn=True)[0])

# Get all texture nodes, connected to each shader
texture_nodes = []
for shader in shaders:
    texture_nodes.append(cmds.listConnections(shader, t='file')) #, c=True))


# Get the path of the texture
file_path = texture_nodes[0][0] + '.fileTextureName'
# Get the file path using getAttr
print(cmds.getAttr(file_path))
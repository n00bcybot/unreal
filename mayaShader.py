import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds
import os
import json

cmds.file("C:/Users/fresh/Desktop/maya/rendertest/buttress.ma", o=True)
# Create list of all meshes in teh scene
def getAllMeshes():
    mesh_shapes = cmds.ls(g=True)
    mesh_list = []
    for mesh in mesh_shapes:
        mesh_list.append(cmds.listRelatives(mesh, parent=True)[0])
    return mesh_list


# Get all materials applied to the mesh
def getMeshMaterials(mesh):
    # Print all shaders for each mesh in the list, returns list if multiple shaders are applied to a mesh
    material = ''
    if not cmds.hyperShade(geo=mesh, lmn=True):
        pass
    else:
        material = cmds.hyperShade(geo=mesh, lmn=True)

    return material


# Get all attributes of a material shader, utility
def getMaterialAttrs(material):
    return cmds.listAttr(material)


# Get all nodes connected to the material and are textures (files) and build dictionary with the name of the node
# as key, the basename (that includes the extension) and the file path as values (dictionary)
def getMaterialNodes(material):
    connected_nodes = {}
    # all_attributes = getMaterialAttrs(material)
    connected_attributes = cmds.listConnections(material, t='file', c=True)  # , c=True))

    even = []
    odds = []

    if connected_attributes is not None:
        for attr in connected_attributes:
            if connected_attributes.index(attr) % 2 == 0:
                even.append(attr.replace(material + '.', ''))
            else:
                odds.append(attr)
    for i, j in zip(even, odds):
        file_path = cmds.getAttr(j + '.fileTextureName')
        node_base_name = os.path.basename(file_path)
        dir_name = os.path.dirname(file_path)
        # Get the file path using getAttr
        new_dict = {'basename': node_base_name, 'path': file_path, 'folder': dir_name}
        connected_nodes[i] = new_dict

    return connected_nodes


# Make a dictionary from a material with nested dictionaries for the nodes as values
def makeMaterialDict(material):
    materials_dict = {}
    for mat in material:
        materials_dict[mat] = getMaterialNodes(mat)

    return materials_dict


# Put it all together. Create dictionary containing all the meshes in the scene and nested dictionaries for the
# materials and the nodes connected to them, to recreate later in Unreal Engine
assets = {}

for mesh in getAllMeshes():
    material = getMeshMaterials(mesh)
    assets[mesh] = makeMaterialDict(material)

# Export to JSON
file_path = "C:/Users/fresh/Desktop/maya/rendertest/materials.json"

with open(file_path, 'w') as json_file:
    json.dump(assets, json_file, indent=2)

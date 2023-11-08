import unreal

# Define the material name and folder path
asset_name = 'NewMaterial20'
dest_path = '/Game/Materials'
material_path = dest_path + "/" + asset_name
texture_path = '/Game/Textures/bark07'

# Create new material
new_mat = unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name, dest_path, unreal.Material, unreal.MaterialFactoryNew())

texture = unreal.EditorAssetLibrary.load_asset(texture_path)


texture_sample = unreal.MaterialEditingLibrary.create_material_expression(new_mat, unreal.MaterialExpressionTextureSample, -200, -200)
texture_sample.texture = texture

# Connect texture sampler to base color
unreal.MaterialEditingLibrary.connect_material_property(texture_sample, 'RGB', unreal.MaterialProperty.MP_BASE_COLOR)

# Compile
unreal.MaterialEditingLibrary.recompile_material(new_mat)

# Save new material
unreal.EditorAssetLibrary.save_asset(material_path)

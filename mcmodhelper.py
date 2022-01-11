# GalaxyGamingBoy - Author

from os import path, read
import os
import typer, json

cli = typer.Typer();

def readJSONFile(file_path: str):
    file = open(file_path)
    return json.load(file)

def writeJSONFile(file_path: str, data: str):
    with open(file_path, 'w') as f:
        json.dump(data, f)

@cli.command()
def itemconfig(modid: str, item_mod_name: str, lang_name: str, lang_file: str, texture_name: str):
    # Edit Lang
    language_file_data = readJSONFile('./assets/{0}/lang/{1}.json'.format(modid, lang_file))
    language_file_data['item.{0}.{1}'.format(modid, item_mod_name)] = lang_name
    writeJSONFile('./assets/{0}/lang/{1}.json'.format(modid, lang_file), language_file_data)
    # Create Model
    model_template_data = readJSONFile('./template/item_model_template.json')
    model_template_data["textures"]["layer0"] = "{0}:items/{1}".format(modid, texture_name)
    writeJSONFile('./assets/{0}/models/item/{1}.json'.format(modid, item_mod_name), model_template_data)

@cli.command()
def blockconfig(modid: str, block_mod_name: str, lang_name: str, lang_file: str, texture_name: str):
    # Edit Lang
    language_file_data = readJSONFile('./assets/{0}/lang/{1}.json'.format(modid, lang_file))
    language_file_data['block.{0}.{1}'.format(modid, block_mod_name)] = lang_name
    writeJSONFile('./assets/{0}/lang/{1}.json', language_file_data)
    # Create Model - Block
    model_template_data = readJSONFile('./template/block_model_template.json')
    model_template_data["textures"]["all"] = "{0}:blocks/{1}".format(modid, texture_name)
    writeJSONFile('./assets/{0}/models/block/{1}.json'.format(modid, block_mod_name), model_template_data)
    # Create Model - Blockitem
    model_template_data_item = readJSONFile('./template/block_item_template.json')
    model_template_data_item["parent"] = "{0}:block/{1}".format(modid, block_mod_name)
    writeJSONFile('./assets/{0}/models/item/{1}.json'.format(modid, block_mod_name), model_template_data_item)
    # Create Blockstate
    blockstate_template_file = readJSONFile('./template/block_blockstate_template.json')
    blockstate_template_file["variants"][""]["model"] = "{0}:block/{1}".format(modid, block_mod_name)
    writeJSONFile('./assets/{0}/blockstates/{1}.json'.format(modid, block_mod_name), blockstate_template_file)

@cli.command()
def tooltiplang(modid: str, tooltip: str, target: str, entry_num: str, lang_file: str):
    # Edit Lang
    language_file_data = readJSONFile('./assets/{0}/lang/{1}.json'.format(modid, lang_file))
    language_file_data['tooltip.{0}.{1}_{2}'.format(modid, target, entry_num)] = tooltip
    writeJSONFile('./assets/{0}/lang/{1}.json'.format(modid, lang_file), language_file_data)

@cli.command()
def loottable(modid: str, block: str):
    # Loot Table
    loot_template_data = readJSONFile('./template/basic_loottable.json')
    loot_template_data['pools'][0]['entries'][0]['name'] = '{0}:{1}'.format(modid, block)
    writeJSONFile('./data/{0}/loot_tables/blocks/{1}.json'.format(modid, block), loot_template_data)

@cli.command()
def needstool(modid: str, tool: str, tool_type: str, block: str):
    path = "needs_{0}_tool.json".format(tool)
    path_type = "{0}.json".format(tool_type)
    file_path = './data/minecraft/tags/blocks/{0}'.format(path)
    file_path_type = './data/minecraft/tags/blocks/mineable/{0}'.format(path_type)
    block_name = "{0}:{1}".format(modid, block)
    if(os.path.isfile(file_path)):
        file_data = readJSONFile(file_path)
        file_data["values"].append(block_name)
        writeJSONFile(file_path, file_data)
    else:
        template_data = readJSONFile('./template/basic_needs.json')
        writeJSONFile(file_path, template_data)
        file_data = readJSONFile(file_path)
        file_data["values"].append(block_name)
        writeJSONFile(file_path, file_data)
    
    if(os.path.isfile(file_path_type)):
        file_data = readJSONFile(file_path_type)
        file_data["values"].append(block_name)
        writeJSONFile(file_path_type, file_data)
    else:
        template_data = readJSONFile('./template/basic_needs.json')
        writeJSONFile(file_path_type, template_data)
        file_data = readJSONFile(file_path_type)
        file_data["values"].append(block_name)
        writeJSONFile(file_path_type, file_data)
    
    
if __name__ == "__main__":
    cli()
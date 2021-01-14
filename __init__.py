import os


class Mod:
    def createMod(filename, mod_version):
        
        mod = open(filename, 'w+')

        mod.write('''package com.example.examplemod;

    import net.minecraft.init.Blocks;
    import net.minecraftforge.fml.common.Mod;
    import net.minecraftforge.fml.common.Mod.EventHandler;
    import net.minecraftforge.fml.common.event.FMLInitializationEvent;
    import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;
    import org.apache.logging.log4j.Logger;

    @Mod(modid = ''' + filename.replace(' ', '').replace('.java', '') +'''.MODID, name = '''+ filename.replace(' ', '').replace('.java', '') +'''.NAME, version = '''+ filename.replace(' ', '') +'''.VERSION)
    public class ''' + filename.replace(' ', '').replace('.java', '') +'''
    {
        public static final String MODID = "'''+ filename.replace(' ', '').replace('.java', '').lower() +'''";
        public static final String NAME = "'''+ filename.replace('.java', '') +'''";
        public static final String VERSION = "'''+ mod_version +'''";

        private static Logger logger;

        @EventHandler
        public void preInit(FMLPreInitializationEvent event)
        {
            logger = event.getModLog();
        }

        @EventHandler
        public void init(FMLInitializationEvent event)
        {
            // some example code
            logger.info("DIRT BLOCK >> {}", Blocks.DIRT.getRegistryName());
        }
    }
    ''')

        mod.close()
        mcmod = open('mcmod.info', 'w+')
        mcmod.write('''[
{
  "modid": "'''+ filename.replace(' ', '').replace('.java', '') +'''",
  "name": "'''+ filename.replace('.java', '') +'''",
  "description": "'''+ filename.replace('.java', '') +''' mod",
  "version": "'''+ mod_version +'''",
  "mcversion": "1.12.2",
  "url": "",
  "updateUrl": "",
  "authorList": [""],
  "credits": "The Forge and FML guys, for making this example",
  "logoFile": "",
  "screenshots": [],
  "dependencies": []
}
]
''')




                
        
    def addCustomSword(filename, name, harvestLevel, maxUses, efficiency, damage, enchantability):


        input_file = open(filename, 'r+')
        data_read = input_file.read()
            
        public_static = data_read.replace('    private static Logger logger;', f'    private static Logger logger;\n    public static ToolMaterial Tool_{name.replace(" ", "")};\n    public static Item Item_{name.replace(" ", "")};')
        import_package = public_static.replace('package com.example.examplemod;', 'import net.minecraft.item.ItemSword;\n\npublic class CustomSword extends ItemSword {\n\n    public CustomSword() {\n        super({name.replace(" ", "")}.Tool_{name.replace(" ", "")})\n\n        this.setRegistryName("{name.replace(" ", "")}");\n        this.setUnlocalizedName("{name.replace(" ", "")}");\n         this.setCreativeTab(CreativeTabs.COMBAT);\n    }')
        custom_sword = import_package.replace('        logger = event.getModLog();', f'        logger = event.getModLog();\n        Tool_{name.replace(" ", "")} = EnumHelpe.addToolMaterial({name}, {harvestLevel}, {maxUses}, {efficiency}, {damage}, {enchantability});\n        Item_{name.replace(" ", "")} = new CustomSword();')

        input_file.close()
        output_file = open(filename, 'w+')
        output_file.write(public_static)
        output_file.write(import_package)
        output_file.write(custom_sword)
        output_file.close()

         


        return f'Item{filename.replace(".java", "").replace(" ", "")}'
    def registerItems(teste, mod_path, customItem):
        input_file = open(mod_path, 'r+')
        data_read = input_file.read()
            
        ComonProxy = data_read.replace('package com.example.examplemod;', 'package com.example.examplemod;\n\nimport net.minecraft.item.Item;\nimportnet.minecraftforge.event.RegistryEvent;\nimport net.minecraftforge.fml.comon.Mod;\nimport net.minecraftforge.fml.comon.eventhandler.SubscribeEvent;\n\n@Mod.EventBusSubscriber\npublic class ComonProxy {\n    @SubscribeEvent\n    public static void registerItems(RegistryEvent.Register<Item> event) {\n        event.getRegistry().registerAll(ExampleMod.{customItem}\n    }\n}')
        input_file.close()
        output_file = open(mod_path, 'w+')
  
        output_file.write(ComonProxy)
 
        output_file.close()        











































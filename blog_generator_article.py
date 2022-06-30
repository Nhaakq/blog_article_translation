from transformers import pipeline
from googletrans import Translator

# Creating a TextGenerationPipeline for text generation
generator = pipeline(task='text-generation', model='gpt2')
# Generating
text = generator("take pictures in Zoo", min_length=200,max_length=2500)
new_text = text[0]['generated_text']
#generator("It takes time to write a good blog post.", max_length=60, num_return_sequences=5)

#text = [{'generated_text': 'work from home can be quite costly.\n\nThe UESPWiki – Your source for The Elder Scrolls since 1995\n\nThis item is part of the Unofficial Skyrim Patch.\n\nPatch changes:\n\nJuly 7, 2015: Added three new unique weapons.\n\nMidsummer 2014: Added a new weapon, the Fencer\n\nJanuary 29, 2018: Added two new unique weapons.\n\nThe following weapons are no longer added in this list.\n\nVoid Weapon/Armor\n\nUnits that are no longer exclusive to one character at once\n\n\nUnits: None Unique weapon/armor Unique weapon armor no longer required weapons Unique weapon armor may be removed for a particular weapon within the given set order\n\n\nUnits will no longer give a fixed bonus against enchantment or enchantments. It should be possible to replace uniques by replacing vanilla\n\nItems that are not crafted from crafted items now only contain the "Crafted Uniques" drop for each Unsigned Unsigned Unique equipped. All items can be crafted by using the Alchemy recipe\n\nThe following weapons are no longer crafted from uniques enchanted by a crafted item\n\n\nItems that are not crafted from crafted enchantments and equipped through a crafted enchantments will now contain the "Crafted Uniques" drop for each Unsigned Unsigned Unique\n\nAll items with an enchanted name can be crafted\n\nAll items with an unowned name will no longer have unenchanted properties for the'}]

#print(text[0]['generated_text'])

translator = Translator()
article_fr = translator.translate(new_text, dest='fr')
print('######################################')
print(new_text)
print('----------------------------------------')
print(article_fr.text)

# print(article_fr.text)
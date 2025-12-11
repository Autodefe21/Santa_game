with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Заменяем все src=" на src="game/"
fixed_content = content.replace('src="', 'src="game/')

# Также заменяем manifest
fixed_content = fixed_content.replace('href="manifest.webmanifest"', 'href="game/manifest.webmanifest"')

with open('index_fixed.html', 'w', encoding='utf-8') as file:
    file.write(fixed_content)

print("Создан index_fixed.html с исправленными путями!")

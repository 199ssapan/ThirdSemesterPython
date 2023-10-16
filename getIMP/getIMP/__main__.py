import pefile

pe = pefile.PE('BinConverting.exe')

for lib in pe.DIRECTORY_ENTRY_IMPORT:
    print("Imported from", lib.dll)
    for func in lib.imports:
        print(f"{func.name}")

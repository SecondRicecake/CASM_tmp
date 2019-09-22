# -*- mode: python -*-

block_cipher = None


a = Analysis(['CASM_txt2csv_GUI.py'],
             pathex=['C:\\Users\\Suz\\Desktop\\2019-2LIFS\\CASM_tmp\\txt2csv'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='CASM_txt2csv_GUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='txt2csv_logo.ico')

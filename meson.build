project('darn')

yml2fea = find_program('yml2fea')
ligatures_feature = custom_target('ligatures',
  input: 'ligatures.yml',
  output: 'ligatures.fea',
  command: [ yml2fea, '@INPUT@', '@OUTPUT@' ],
)

bitsnpicas = find_program('bitsnpicas')

sizes = ['7x15', '6x13']
ttfs = []

foreach size : sizes
  name = 'DarnMedium' + '-' + size
  source_dir = 'src/' + size
  ttfs += custom_target(name,
    input: source_dir + '/' + name + '.bdf',
    output: name + '.ttf',
    command: [bitsnpicas, 'convertbitmap', '-f', 'sbit', '-o', '@OUTPUT@', '@INPUT@'],
    build_by_default: true,
  )
endforeach

combine_font = find_program('./combine.py')
combined = custom_target('DarnMedium-combined.ttf',
  input: ttfs,
  output: 'DarnMedium-combined.ttf',
  command: [combine_font, '@INPUT@', '@OUTPUT@']
)

fonttools = find_program('fonttools')
final_font = 'DarnMedium.ttf'
custom_target(final_font,
  input: [ligatures_feature, combined],
  output: final_font,
  command: [fonttools, 'feaLib', '-o', '@OUTPUT@', '@INPUT@'],
  build_by_default: true,
  install_dir: 'share/fonts',
  install: true,
)

project('darn')

yml2fea = find_program('yml2fea')
ligatures_feature = custom_target('ligatures',
  input: 'ligatures.yml',
  output: 'ligatures.fea',
  command: [ yml2fea, '@INPUT@', '@OUTPUT@' ],
)

bdf2ttf = find_program('bdf2ttf')

sizes = ['7x15', '6x13', '9x19']
ttfs = []

foreach size : sizes
  name = 'DarnMedium' + '-' + size
  source_dir = 'src/' + size
  custom_target(name,
    input: source_dir + '/' + name + '.bdf',
    output: name + '.ttf',
    command: [bdf2ttf, '@INPUT@', '--feature-file', ligatures_feature, '-o', '@OUTPUT@'],
    build_by_default: true,
  )
endforeach

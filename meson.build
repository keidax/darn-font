project('darn')

yml2fea = find_program('yml2fea')
ligatures_feature = custom_target('ligatures',
  input: 'ligatures.yml',
  output: 'ligatures.fea',
  command: [ yml2fea, '@INPUT@', '@OUTPUT@' ],
)

bdf2ttf = find_program('bdf2ttf')

source_files = [
  'src/9x19/DarnMedium-9x19.bdf',
  'src/9x19/DarnBold-9x19.bdf',
  'src/18x38/DarnMedium-18x38.bdf',
]

foreach source_file : source_files
  output_file = source_file.split('/')[2].replace('.bdf', '.ttf')

  custom_target(output_file,
    input: source_file,
    output: output_file,
    command: [bdf2ttf, '@INPUT@', '--feature-file', ligatures_feature, '-o', '@OUTPUT@'],
    build_by_default: true,
  )
endforeach

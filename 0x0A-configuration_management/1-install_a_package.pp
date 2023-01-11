# Install Flask from pip3
# Flask version should be 2.1.0

package {'Flask':
  ensure   => '2.1.0',
  name     => 'Flask',
  provider => 'pip3',
}

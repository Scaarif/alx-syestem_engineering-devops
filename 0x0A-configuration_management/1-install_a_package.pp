# Install Flask from pip3
# Flask version should be 2.1.0

package {'Flask':
  ensure   => 'latest',
  provider => 'pip3',
}

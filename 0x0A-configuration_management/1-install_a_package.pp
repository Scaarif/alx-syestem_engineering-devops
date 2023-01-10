# Install Flask from pip3
# Flask version should be 2.1.0

exec {'pip3 install Flask':
  command => '/usr/bin/pip install -Iv Flask==1.2.2'
}

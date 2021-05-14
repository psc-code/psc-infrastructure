# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gtensor(CMakePackage):
    """The gtensor performance portability library."""

    homepage = "https://github.com/wdmapp/gtensor"
    url = "https://github.com/wdmapp/gtensor/fake.tar.gz"
    git = "https://github.com/wdmapp/gtensor"

    maintainers = ['germasch', 'bd4']

    version('develop', branch='main')

    variant('device', default='host',
            description='Default device backend',
            values=('host', 'cuda', 'hip', 'sycl'),
            multi=False)
    variant('tests', default=False,
            description='Build with unit testing')

    depends_on('cmake@3.18.0:')

    depends_on('googletest@1.10.0:', when='+tests')

    depends_on('cuda', when='device=cuda')
    depends_on('thrust@1.10.0:', when='device=cuda')

    def cmake_args(self):
        spec = self.spec

        args = ['-DCPM_USE_LOCAL_PACKAGES=ON']
        args += ['-DGTENSOR_DEVICE={}'.format(
            self.spec.variants['device'].value)]
        args += ['-DBUILD_TESTING={}'.format(
            'ON' if '+tests' in self.spec else 'OFF')]

        return args

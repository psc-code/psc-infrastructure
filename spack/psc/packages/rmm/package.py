# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Rmm(CMakePackage):
    """RMM: RAPIDS Memory Manager"""

    homepage = "https://github.com/rapidsai/rmm"
    url      = "https://github.com/rapidsai/rmm/archive/refs/tags/v0.16.0.tar.gz"
    git      = "https://github.com/rapidsai/rmm"

    maintainers = ['germasch']

    version('develop', branch='main')
    version('0.19.0', sha256='eddd5b35b016d665eb4e8ea2dd31497d913b3e1eb831124e4cb27cba747267a0')
    version('0.18.0', sha256='0cb4275a686e986563772188923f892988ee388cee25706c0572326c00cf83d9', preferred=True)
    version('0.17.0', sha256='84ba6fbbdbc550b70ca1a6c63dc24dd9a5084f7701e319b9a982b9ce5a0889f6')
    version('0.16.0', sha256='972fcdd3b5ab5af9a8e89671f0dbd47cfe1559ff8c4031c515ab89a487201ae2')

    variant('tests', default=False, description="Build tests")
    
    depends_on('cuda')
    depends_on('spdlog@1.7.0')
    #depends_on('thrust@1.10.0:')
    depends_on('googletest@1.10.0 +gmock', type='build', when='+tests')

    patch('rmm-summit.patch', when='@0.16.0')

    def cmake_args(self):
        spec = self.spec

        args = []
        args += ['-DBUILD_TESTS:BOOL={}'.format(
            'ON' if '+tests' in spec else 'OFF')]

        return args
    

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='rroi_align',
    ext_modules=[
        CUDAExtension('rroi_align', [
            'rroi_align_cuda.cpp',
            'rroi_align_kernel.cu',
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    })

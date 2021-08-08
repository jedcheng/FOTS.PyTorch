from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='rroi_align',
    ext_modules=[
        CUDAExtension('rroi_align', [
            'src/rroi_align_cuda.cpp',
            'src/rroi_align_kernel.cu',
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    })

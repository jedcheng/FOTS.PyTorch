from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='rotated_roi',
    ext_modules=[
        CUDAExtension('rotated_roi', [
            'rroi_align_cuda.cpp',
            'rroi_align_kernel.cu',
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    })

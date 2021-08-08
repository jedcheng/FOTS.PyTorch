from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='rotate_roi',
    ext_modules=[
        CUDAExtension('rotate_roi', [
            'src/rroi_align_cuda.cpp',
            'src/rroi_align_kernel.cu',
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    })

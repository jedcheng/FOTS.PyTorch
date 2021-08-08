from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='rotated_roi',
    ext_modules=[
        CUDAExtension('rotated_roi', [
            'src/rroi_align_cuda.cpp',
            'src/rroi_align_kernel.cu',
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    })

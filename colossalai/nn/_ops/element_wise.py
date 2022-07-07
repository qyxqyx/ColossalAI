import torch
import torch.nn.functional as F
from torch import Tensor
from colossalai.tensor.op_wrapper import colo_op_impl
from colossalai.tensor import ColoTensor, ColoTensorSpec
from ._utils import GeneralTensor


def register_elementwise_op(op):

    @colo_op_impl(op)
    def elementwise_op(input_tensor: GeneralTensor, *args, **kwargs):
        """
        Handles ``__torch_function__`` dispatch for the elementwise op such
        as ``torch.nn.functional.gelu`` or ``torch.nn.functional.relu``.
        This method computes on either a normal tensor or a sharded tensor.
        """

        output = op(input_tensor, *args, **kwargs)
        if isinstance(input_tensor, ColoTensor):
            if not isinstance(output, torch.Tensor):
                raise NotImplementedError
            return ColoTensor.from_torch_tensor(output,
                                                spec=ColoTensorSpec(input_tensor.get_process_group(),
                                                                    dist_attr=input_tensor.dist_spec))


# Tensor op
register_elementwise_op(Tensor.abs)
register_elementwise_op(Tensor.absolute)
register_elementwise_op(Tensor.acos)
register_elementwise_op(Tensor.arccos)
register_elementwise_op(Tensor.angle)
register_elementwise_op(Tensor.asin)
register_elementwise_op(Tensor.arcsin)
register_elementwise_op(Tensor.atan)
register_elementwise_op(Tensor.arctan)
register_elementwise_op(Tensor.all)
register_elementwise_op(Tensor.any)
register_elementwise_op(Tensor.bernoulli)
register_elementwise_op(Tensor.bfloat16)
register_elementwise_op(Tensor.bitwise_not)
register_elementwise_op(Tensor.bool)
register_elementwise_op(Tensor.byte)
register_elementwise_op(Tensor.ceil)
register_elementwise_op(Tensor.char)
register_elementwise_op(Tensor.clamp)
register_elementwise_op(Tensor.clamp_max)
register_elementwise_op(Tensor.clamp_min)
register_elementwise_op(Tensor.clip)
register_elementwise_op(Tensor.clone)
register_elementwise_op(Tensor.contiguous)
register_elementwise_op(Tensor.copysign)
register_elementwise_op(Tensor.cos)
register_elementwise_op(Tensor.cosh)
register_elementwise_op(Tensor.acosh)
register_elementwise_op(Tensor.arccosh)
register_elementwise_op(Tensor.cpu)
register_elementwise_op(Tensor.cuda)
register_elementwise_op(Tensor.deg2rad)
register_elementwise_op(Tensor.detach)
register_elementwise_op(Tensor.digamma)
register_elementwise_op(Tensor.double)
register_elementwise_op(Tensor.erf)
register_elementwise_op(Tensor.erfc)
register_elementwise_op(Tensor.erfinv)
register_elementwise_op(Tensor.exp)
register_elementwise_op(Tensor.expm1)
register_elementwise_op(Tensor.fix)
register_elementwise_op(Tensor.trunc)
register_elementwise_op(Tensor.float)
register_elementwise_op(Tensor.float_power)
register_elementwise_op(Tensor.floor)
register_elementwise_op(Tensor.frac)
register_elementwise_op(Tensor.half)
register_elementwise_op(Tensor.hardshrink)
register_elementwise_op(Tensor.heaviside)
register_elementwise_op(Tensor.i0)
register_elementwise_op(Tensor.int)
register_elementwise_op(Tensor.isfinite)
register_elementwise_op(Tensor.isinf)
register_elementwise_op(Tensor.isposinf)
register_elementwise_op(Tensor.isneginf)
register_elementwise_op(Tensor.isnan)
register_elementwise_op(Tensor.lgamma)
register_elementwise_op(Tensor.log)
register_elementwise_op(Tensor.log10)
register_elementwise_op(Tensor.log1p)
register_elementwise_op(Tensor.log2)
register_elementwise_op(Tensor.logical_not)
register_elementwise_op(Tensor.logit)
register_elementwise_op(Tensor.long)
register_elementwise_op(Tensor.nan_to_num)
register_elementwise_op(Tensor.neg)
register_elementwise_op(Tensor.negative)
register_elementwise_op(Tensor.positive)
register_elementwise_op(Tensor.pow)
register_elementwise_op(Tensor.rad2deg)
register_elementwise_op(Tensor.reciprocal)
register_elementwise_op(Tensor.round)
register_elementwise_op(Tensor.rsqrt)
register_elementwise_op(Tensor.short)
register_elementwise_op(Tensor.sigmoid)
register_elementwise_op(Tensor.sign)
register_elementwise_op(Tensor.signbit)
register_elementwise_op(Tensor.sgn)
register_elementwise_op(Tensor.sin)
register_elementwise_op(Tensor.sinc)
register_elementwise_op(Tensor.sinh)
register_elementwise_op(Tensor.asinh)
register_elementwise_op(Tensor.arcsinh)
register_elementwise_op(Tensor.sqrt)
register_elementwise_op(Tensor.square)
register_elementwise_op(Tensor.to)
register_elementwise_op(Tensor.tan)
register_elementwise_op(Tensor.tanh)
register_elementwise_op(Tensor.atanh)
register_elementwise_op(Tensor.arctanh)
register_elementwise_op(Tensor.type)
register_elementwise_op(Tensor.type_as)

# torch OP
register_elementwise_op(torch.abs)
register_elementwise_op(torch.absolute)
register_elementwise_op(torch.acos)
register_elementwise_op(torch.arccos)
register_elementwise_op(torch.angle)
register_elementwise_op(torch.asin)
register_elementwise_op(torch.arcsin)
register_elementwise_op(torch.atan)
register_elementwise_op(torch.arctan)
register_elementwise_op(torch.all)
register_elementwise_op(torch.any)
register_elementwise_op(torch.bernoulli)
register_elementwise_op(torch.bitwise_not)
register_elementwise_op(torch.ceil)
register_elementwise_op(torch.clamp)
register_elementwise_op(torch.clamp_max)
register_elementwise_op(torch.clamp_min)
register_elementwise_op(torch.clip)
register_elementwise_op(torch.clone)
register_elementwise_op(torch.copysign)
register_elementwise_op(torch.cos)
register_elementwise_op(torch.cosh)
register_elementwise_op(torch.acosh)
register_elementwise_op(torch.arccosh)
register_elementwise_op(torch.deg2rad)
register_elementwise_op(torch.digamma)
register_elementwise_op(torch.erf)
register_elementwise_op(torch.erfc)
register_elementwise_op(torch.erfinv)
register_elementwise_op(torch.exp)
register_elementwise_op(torch.expm1)
register_elementwise_op(torch.fix)
register_elementwise_op(torch.trunc)
register_elementwise_op(torch.float_power)
register_elementwise_op(torch.floor)
register_elementwise_op(torch.frac)
register_elementwise_op(torch.hardshrink)
register_elementwise_op(torch.heaviside)
register_elementwise_op(torch.i0)
register_elementwise_op(torch.isfinite)
register_elementwise_op(torch.isinf)
register_elementwise_op(torch.isposinf)
register_elementwise_op(torch.isneginf)
register_elementwise_op(torch.isnan)
register_elementwise_op(torch.lgamma)
register_elementwise_op(torch.log)
register_elementwise_op(torch.log10)
register_elementwise_op(torch.log1p)
register_elementwise_op(torch.log2)
register_elementwise_op(torch.logical_not)
register_elementwise_op(torch.logit)
register_elementwise_op(torch.nan_to_num)
register_elementwise_op(torch.neg)
register_elementwise_op(torch.negative)
register_elementwise_op(torch.positive)
register_elementwise_op(torch.pow)
register_elementwise_op(torch.rad2deg)
register_elementwise_op(torch.reciprocal)
register_elementwise_op(torch.round)
register_elementwise_op(torch.rsqrt)
register_elementwise_op(torch.sigmoid)
register_elementwise_op(torch.sign)
register_elementwise_op(torch.signbit)
register_elementwise_op(torch.sgn)
register_elementwise_op(torch.sin)
register_elementwise_op(torch.sinc)
register_elementwise_op(torch.sinh)
register_elementwise_op(torch.asinh)
register_elementwise_op(torch.arcsinh)
register_elementwise_op(torch.sqrt)
register_elementwise_op(torch.square)
register_elementwise_op(torch.tan)
register_elementwise_op(torch.tanh)
register_elementwise_op(torch.atanh)
register_elementwise_op(torch.arctanh)

# nn.functional OP
register_elementwise_op(F.threshold)
register_elementwise_op(F.relu)
register_elementwise_op(F.hardtanh)
register_elementwise_op(F.hardswish)
register_elementwise_op(F.relu6)
register_elementwise_op(F.elu)
register_elementwise_op(F.selu)
register_elementwise_op(F.celu)
register_elementwise_op(F.leaky_relu)
register_elementwise_op(F.prelu)
register_elementwise_op(F.rrelu)
register_elementwise_op(F.gelu)
register_elementwise_op(F.logsigmoid)
register_elementwise_op(F.hardshrink)
register_elementwise_op(F.tanhshrink)
register_elementwise_op(F.softsign)
register_elementwise_op(F.softplus)
register_elementwise_op(F.softmin)
register_elementwise_op(F.softmax)
register_elementwise_op(F.softshrink)
register_elementwise_op(F.gumbel_softmax)
register_elementwise_op(F.log_softmax)
register_elementwise_op(F.tanh)
register_elementwise_op(F.sigmoid)
register_elementwise_op(F.hardsigmoid)
register_elementwise_op(F.silu)
register_elementwise_op(F.mish)
# TODO(ver217): dropout handles seed
register_elementwise_op(F.dropout)
register_elementwise_op(F.alpha_dropout)
register_elementwise_op(F.feature_alpha_dropout)

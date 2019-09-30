#include "cupy_cufft.h"


cufftResult setCallback(cufftHandle plan, void **callbackRoutine,
                        cufftXtCallbackType type, void **callerInfo)
{
    return cufftXtSetCallback(plan, callbackRoutine, type, callerInfo);
}


cufftResult clearCallback(cufftHandle plan, cufftXtCallbackType type)
{
    return cufftXtClearCallback(plan, type);
}

/*
 * Copyright (c) 2016, Oracle and/or its affiliates.
 *
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification, are
 * permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice, this list of
 * conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright notice, this list of
 * conditions and the following disclaimer in the documentation and/or other materials provided
 * with the distribution.
 *
 * 3. Neither the name of the copyright holder nor the names of its contributors may be used to
 * endorse or promote products derived from this software without specific prior written
 * permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 * GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 */
package com.oracle.truffle.llvm.nodes.intrinsics.llvm;

import com.oracle.truffle.api.dsl.Cached;
import com.oracle.truffle.api.dsl.NodeChild;
import com.oracle.truffle.api.dsl.NodeChildren;
import com.oracle.truffle.api.dsl.Specialization;
import com.oracle.truffle.api.frame.VirtualFrame;
import com.oracle.truffle.llvm.runtime.LLVMAddress;
import com.oracle.truffle.llvm.runtime.LLVMTruffleObject;
import com.oracle.truffle.llvm.runtime.LLVMVirtualAllocationAddress;
import com.oracle.truffle.llvm.runtime.global.LLVMGlobal;
import com.oracle.truffle.llvm.runtime.memory.LLVMMemSetNode;
import com.oracle.truffle.llvm.runtime.memory.UnsafeIntArrayAccess;
import com.oracle.truffle.llvm.runtime.nodes.api.LLVMExpressionNode;
import com.oracle.truffle.llvm.runtime.nodes.api.LLVMToNativeNode;

@NodeChildren({@NodeChild(type = LLVMExpressionNode.class), @NodeChild(type = LLVMExpressionNode.class), @NodeChild(type = LLVMExpressionNode.class), @NodeChild(type = LLVMExpressionNode.class),
                @NodeChild(type = LLVMExpressionNode.class)})
public abstract class LLVMMemSet extends LLVMBuiltin {

    @Child private LLVMMemSetNode memSet;

    public LLVMMemSet(LLVMMemSetNode memSet) {
        this.memSet = memSet;
    }

    @SuppressWarnings("unused")
    @Specialization
    protected Object doOp(VirtualFrame frame, LLVMAddress address, byte value, int length, int align, boolean isVolatile) {
        memSet.executeWithTarget(frame, address, value, length);
        return address;
    }

    @SuppressWarnings("unused")
    @Specialization
    protected Object doOp(VirtualFrame frame, LLVMGlobal address, byte value, int length, int align, boolean isVolatile,
                    @Cached("createToNativeWithTarget()") LLVMToNativeNode globalAccess) {
        memSet.executeWithTarget(frame, globalAccess.executeWithTarget(frame, address), value, length);
        return address;
    }

    @SuppressWarnings("unused")
    @Specialization
    protected Object doOp(VirtualFrame frame, LLVMAddress address, byte value, long length, int align, boolean isVolatile) {
        memSet.executeWithTarget(frame, address, value, length);
        return address;
    }

    @SuppressWarnings("unused")
    @Specialization
    protected Object doOp(VirtualFrame frame, LLVMGlobal address, byte value, long length, int align, boolean isVolatile,
                    @Cached("createToNativeWithTarget()") LLVMToNativeNode globalAccess) {
        memSet.executeWithTarget(frame, globalAccess.executeWithTarget(frame, address), value, length);
        return address;
    }

    @SuppressWarnings("unused")
    @Specialization
    protected Object doOp(LLVMVirtualAllocationAddress address, byte value, long length, int align, boolean isVolatile,
                    @Cached("getUnsafeIntArrayAccess()") UnsafeIntArrayAccess memory) {
        for (int i = 0; i < length; i++) {
            address.writeI8(memory, value);
        }
        return address;
    }

    @SuppressWarnings("unused")
    @Specialization
    protected Object doOp(VirtualFrame frame, LLVMTruffleObject address, byte value, int length, int align, boolean isVolatile) {
        memSet.executeWithTarget(frame, address, value, length);
        return address;
    }

    @SuppressWarnings("unused")
    @Specialization
    protected Object doOp(VirtualFrame frame, LLVMTruffleObject address, byte value, long length, int align, boolean isVolatile) {
        memSet.executeWithTarget(frame, address, value, length);
        return address;
    }
}
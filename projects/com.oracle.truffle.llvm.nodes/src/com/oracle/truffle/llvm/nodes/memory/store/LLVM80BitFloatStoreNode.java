/*
 * Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
package com.oracle.truffle.llvm.nodes.memory.store;

import com.oracle.truffle.api.dsl.Cached;
import com.oracle.truffle.api.dsl.Specialization;
import com.oracle.truffle.llvm.runtime.debug.scope.LLVMSourceLocation;
import com.oracle.truffle.llvm.runtime.floating.LLVM80BitFloat;
import com.oracle.truffle.llvm.runtime.global.LLVMGlobal;
import com.oracle.truffle.llvm.runtime.nodes.api.LLVMToNativeNode;
import com.oracle.truffle.llvm.runtime.pointer.LLVMManagedPointer;
import com.oracle.truffle.llvm.runtime.pointer.LLVMNativePointer;

public abstract class LLVM80BitFloatStoreNode extends LLVMStoreNodeCommon {

    public LLVM80BitFloatStoreNode() {
        this(null);
    }

    public LLVM80BitFloatStoreNode(LLVMSourceLocation sourceLocation) {
        super(sourceLocation);
    }

    @Specialization
    protected Object doOp(LLVMGlobal address, LLVM80BitFloat value,
                    @Cached("createToNativeWithTarget()") LLVMToNativeNode globalAccess) {
        getLLVMMemoryCached().put80BitFloat(globalAccess.executeWithTarget(address), value);
        return null;
    }

    @Specialization(guards = "!isAutoDerefHandle(addr)")
    protected Object doOp(LLVMNativePointer addr, LLVM80BitFloat value) {
        getLLVMMemoryCached().put80BitFloat(addr, value);
        return null;
    }

    @Specialization(guards = "isAutoDerefHandle(addr)")
    protected Object doOpDerefHandle(LLVMNativePointer addr, LLVM80BitFloat value) {
        return doForeign(getDerefHandleGetReceiverNode().execute(addr), value);
    }

    // TODO (chaeubl): we could store this in a more efficient way (short + long)
    @Specialization
    protected Object doForeign(LLVMManagedPointer address, LLVM80BitFloat value) {
        byte[] bytes = value.getBytes();
        LLVMManagedPointer currentPtr = address;
        for (int i = 0; i < bytes.length; i++) {
            getForeignWriteNode().execute(currentPtr, bytes[i]);
            currentPtr = currentPtr.increment(I8_SIZE_IN_BYTES);
        }
        return null;
    }

    @Override
    protected LLVMForeignWriteNode createForeignWrite() {
        return LLVMForeignWriteNodeGen.create();
    }
}
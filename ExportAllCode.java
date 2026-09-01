// Ghidra script to decompile all functions in binary
// @category Analysis

import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import java.io.PrintWriter;
import java.io.File;

public class ExportAllCode extends GhidraScript {
    @Override
    public void run() throws Exception {
        File outFile = new File("C:/Users/Admin/Downloads/AliceGreenfingers_RE/reconstructed-source/AliceGreenfingers_reconstructed.cpp");
        PrintWriter writer = new PrintWriter(outFile);

        writer.println("// ==========================================================================");
        writer.println("// RECONSTRUCTED C++ SOURCE DECOMPILED FROM ALICEGREENFINGERS.DLL");
        writer.println("// Generated via Ghidra Decompiler Engine");
        writer.println("// ==========================================================================");
        writer.println();

        DecompInterface decompiler = new DecompInterface();
        decompiler.openProgram(currentProgram);

        FunctionIterator functions = currentProgram.getFunctionManager().getFunctions(true);
        int count = 0;

        while (functions.hasNext() && !monitor.isCancelled()) {
            Function f = functions.next();
            writer.println("// --------------------------------------------------------------------------");
            writer.println("// Function: " + f.getName() + " at " + f.getEntryPoint());
            writer.println("// --------------------------------------------------------------------------");

            DecompileResults res = decompiler.decompileFunction(f, 30, monitor);
            if (res != null && res.getDecompiledFunction() != null) {
                writer.println(res.getDecompiledFunction().getC());
            } else {
                writer.println("// [Decompilation failed or empty]");
            }
            writer.println();
            count++;
        }

        writer.close();
        decompiler.dispose();
        println("Successfully decompiled " + count + " functions to " + outFile.getAbsolutePath());
    }
}

// Ghidra script to export actual decompiled C control flow for all functions
// @category Analysis

import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import java.io.PrintWriter;
import java.io.File;

public class ExportActualDecompiledCode extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        String outputPath = "C:/Users/Admin/Downloads/AliceGreenfingers_RE/reconstructed-source/ACTUAL_GHIDRA_DECOMPILED_EXE.c";
        if (args != null && args.length > 0) {
            outputPath = args[0];
        }

        File outFile = new File(outputPath);
        PrintWriter writer = new PrintWriter(outFile);

        writer.println("// ==========================================================================");
        writer.println("// ALICE GREENFINGERS - ACTUAL DECOMPILED C LOGIC FROM BINARY");
        writer.println("// Target: " + currentProgram.getName());
        writer.println("// Generated via Ghidra Decompiler Engine (NO STUBS / FULL CONTROL FLOW)");
        writer.println("// ==========================================================================");
        writer.println();

        DecompInterface decompiler = new DecompInterface();
        decompiler.openProgram(currentProgram);

        FunctionIterator functions = currentProgram.getFunctionManager().getFunctions(true);
        int total = 0;
        int decompiled_count = 0;
        int empty_count = 0;

        while (functions.hasNext() && !monitor.isCancelled()) {
            Function f = functions.next();
            total++;
            
            DecompileResults res = decompiler.decompileFunction(f, 30, monitor);
            if (res != null && res.getDecompiledFunction() != null && res.getDecompiledFunction().getC() != null) {
                String code = res.getDecompiledFunction().getC();
                if (code.length() > 50) {
                    writer.println("// --------------------------------------------------------------------------");
                    writer.println("// Function: " + f.getName() + " at " + f.getEntryPoint() + " (Param Count: " + f.getParameterCount() + ")");
                    writer.println("// --------------------------------------------------------------------------");
                    writer.println(code);
                    writer.println();
                    decompiled_count++;
                } else {
                    empty_count++;
                }
            } else {
                empty_count++;
            }
        }

        writer.close();
        decompiler.dispose();
        println("SUMMARY: Target=" + currentProgram.getName() + ", Total Functions=" + total + ", Successfully Decompiled=" + decompiled_count + ", Empty/Thunks=" + empty_count);
    }
}

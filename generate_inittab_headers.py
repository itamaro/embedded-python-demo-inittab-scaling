import argparse

def generate_headers(num_extensions):
    # Generate generated_inittab_modules.h
    with open("generated_inittab_modules.h", "w") as f:
        f.write("#include \"extension_module_macro.h\"\n")
        for i in range(num_extensions):
            f.write(f"GENERATE_EXTENSION_MODULE({i})\n")

    # Generate generated_inittab_entries.h
    with open("generated_inittab_entries.h", "w") as f:
        f.write("#ifndef GENERATED_INITTAB_ENTRIES_H\n")
        f.write("#define GENERATED_INITTAB_ENTRIES_H\n\n")
        f.write("#include \"Python.h\"\n\n")
        f.write("#include \"generated_inittab_modules.h\"\n\n")
        f.write("typedef PyObject* (*init_function_ptr)(void);\n\n")
        f.write("// Define a structure to hold module name and init function pointer\n")
        f.write("struct InittabEntry {\n")
        f.write("    const char* name;\n")
        f.write("    init_function_ptr init_func;\n")
        f.write("};\n\n")
        f.write("// Array of all dynamically generated extension module entries\n")
        f.write("static const InittabEntry generated_inittab_extensions[] = {\n")
        for i in range(num_extensions):
            f.write(f"    {{\"inittab_ext_{i}\", &PyInit_inittab_ext_{i}}},\n")
        f.write("    {NULL, NULL} // Sentinel\n")
        f.write("};\n\n")
        f.write("#endif // GENERATED_INITTAB_ENTRIES_H\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate C header files for dynamic Python extensions.")
    parser.add_argument("--num_extensions", type=int, default=10,
                        help="Number of dynamic extensions to generate (default: 10)")
    args = parser.parse_args()
    generate_headers(args.num_extensions)

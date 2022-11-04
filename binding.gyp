{
    "targets": [
        {
            "target_name": "andb",
            "win_delay_load_hook": "false",
            "sources": [],
            "include_dirs": [
                'src',
                '<!(node -e "require(\'nan\')")'
            ],
            "cflags_cc!": ["-fno-exceptions"],
            "conditions": [
                ["OS == 'linux'", {
                    "cflags": [
                        "-O3",
                        "-std=c++17",
                        "-Wno-sign-compare",
                        "-Wno-cast-function-type",
                    ],
                    "defines": [],
                    "sources": []
                }],
                ["OS == 'mac'", {
                    "xcode_settings": {
                        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                        "GCC_OPTIMIZATION_LEVEL": "3",
                        "OTHER_CFLAGS": [
                            "-std=c++17",
                            "-Wconversion",
                            "-Wno-sign-conversion",
                        ]
                    },
                    "defines": [],
                    "sources": []
                }],
                ["OS == 'win'", {
                    "libraries": ["dbghelp.lib", "Netapi32.lib", "PsApi.lib", "Ws2_32.lib"],
                    "dll_files": ["dbghelp.dll", "Netapi32.dll", "PsApi.dll", "Ws2_32.dll"],
                    "msvs_settings": {
                        "VCCLCompilerTool": {
                            "ExceptionHandling": "2",
                            "Optimization": "3",
                        },
                    },
                    "defines": [],
                    "sources": []
                }],
            ],
            "defines": [],
        },
        {
            "target_name": "action_after_build",
            "type": "none",
            "dependencies": ["<(module_name)"],
            "copies": [
                {
                    "files": ["<(PRODUCT_DIR)/<(module_name).node"],
                    "destination": "<(module_path)"
                }
            ]
        },
    ],
}

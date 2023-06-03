rule shebang {
    strings:
        $shebang = /^#!(\/[^\/ ]*)+\/?/
    condition:
        $shebang
}
rule maybe_python_executable {
    strings:
        $ident = /python(2|3)\r*\n/
    condition:
        shebang and $ident
}

rule hoge {
    strings:
        $ident = /ctf4b{[\x20-\x7e]{28}}/
    condition:
        $ident
}
rule s0x20,0x20 { strings: $ident = /ctf4b{[\x20-\x7e]{28}}/ condition: $ident }

フラグは28文字
section .data 	; data segment
msg db "Hello, World!", 0x0a ; String and Newline Char

section .text 	; text segment
global _start 	; Default entry point for ELF Linking

_start:

mov rax, 4
mov rbx, 1
mov rcx, msg
mov rdx, 14
int 0x80

mov rax, 1
mov rbx, 0
int 0x80

; To Compile:
; nasm -f elf64 helloworld.asm
; ld -o helloInAsm helloworld.o

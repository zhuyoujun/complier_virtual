	.file	"absdiff.c"
	.text
.globl absdiff
	.type	absdiff, @function
absdiff:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %eax
	movl	12(%ebp), %edx
	cmpl	%edx, %eax
	jge	.L2
	subl	%eax, %edx
	movl	%edx, %eax
	jmp	.L3
.L2:
	subl	%edx, %eax
.L3:
	popl	%ebp
	ret
	.size	absdiff, .-absdiff
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

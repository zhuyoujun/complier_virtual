	.file	"dw_loop.c"
	.text
.globl dw_loop
	.type	dw_loop, @function
dw_loop:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %eax
	movl	12(%ebp), %ecx
	movl	16(%ebp), %edx
.L2:
	addl	%edx, %eax
	imull	%edx, %ecx
	subl	$1, %edx
	testl	%edx, %edx
	jle	.L5
	cmpl	%edx, %ecx
	jl	.L2
.L5:
	popl	%ebp
	ret
	.size	dw_loop, .-dw_loop
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

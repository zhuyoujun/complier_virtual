	.file	"fact_while.c"
	.text
.globl fact_while
	.type	fact_while, @function
fact_while:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %edx
	movl	$1, %eax
	cmpl	$1, %edx
	jle	.L3
.L6:
	imull	%edx, %eax
	subl	$1, %edx
	cmpl	$1, %edx
	jne	.L6
.L3:
	popl	%ebp
	ret
	.size	fact_while, .-fact_while
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

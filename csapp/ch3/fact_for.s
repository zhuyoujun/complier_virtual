	.file	"fact_for.c"
	.text
.globl fact_for
	.type	fact_for, @function
fact_for:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %ecx
	movl	$1, %eax
	movl	$1, %edx
	cmpl	$1, %ecx
	jle	.L3
.L6:
	imull	%edx, %eax
	addl	$1, %edx
	cmpl	%ecx, %edx
	jne	.L6
.L3:
	popl	%ebp
	ret
	.size	fact_for, .-fact_for
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

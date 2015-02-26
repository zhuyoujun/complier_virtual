	.file	"fact.c"
	.text
.globl fact_do
	.type	fact_do, @function
fact_do:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %edx
	movl	$1, %eax
.L2:
	imull	%edx, %eax
	subl	$1, %edx
	cmpl	$1, %edx
	jg	.L2
	popl	%ebp
	ret
	.size	fact_do, .-fact_do
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

	.file	"arith.c"
	.text
.globl arith
	.type	arith, @function
arith:
	pushl	%ebp
	movl	%esp, %ebp
	movl	16(%ebp), %eax
	leal	(%eax,%eax,2), %edx
	sall	$4, %edx
	movl	12(%ebp), %eax
	addl	8(%ebp), %eax
	andl	$65535, %eax
	imull	%edx, %eax
	popl	%ebp
	ret
	.size	arith, .-arith
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

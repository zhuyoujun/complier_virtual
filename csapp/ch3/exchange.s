	.file	"exchange.c"
	.text
.globl exchange
	.type	exchange, @function
exchange:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %edx
	movl	(%edx), %eax
	movl	12(%ebp), %ecx
	movl	%ecx, (%edx)
	popl	%ebp
	ret
	.size	exchange, .-exchange
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

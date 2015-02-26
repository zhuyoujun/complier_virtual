	.file	"cond.c"
	.text
.globl cond
	.type	cond, @function
cond:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %edx
	movl	12(%ebp), %eax
	testl	%eax, %eax
	je	.L3
	testl	%edx, %edx
	jle	.L3
	addl	%edx, (%eax)
.L3:
	popl	%ebp
	ret
	.size	cond, .-cond
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

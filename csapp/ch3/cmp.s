	.file	"cmp.c"
	.text
.globl cmp
	.type	cmp, @function
cmp:
	pushl	%ebp
	movl	%esp, %ebp
	movl	12(%ebp), %eax
	cmpl	%eax, 8(%ebp)
	setg	%al
	movzbl	%al, %eax
	popl	%ebp
	ret
	.size	cmp, .-cmp
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

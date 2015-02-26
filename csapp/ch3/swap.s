	.file	"swap.c"
	.text
.globl swap
	.type	swap, @function
swap:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$12, %esp
	movl	%ebx, (%esp)
	movl	%esi, 4(%esp)
	movl	%edi, 8(%esp)
	movl	8(%ebp), %ebx
	movl	12(%ebp), %ecx
	movl	16(%ebp), %edx
	movl	(%ebx), %eax
	movl	(%edx), %esi
	movl	(%ecx), %edi
	movl	%edi, (%ebx)
	movl	%esi, (%ecx)
	movl	%eax, (%edx)
	sarl	$3, %eax
	subl	$1, %eax
	negl	%eax
	movl	(%esp), %ebx
	movl	4(%esp), %esi
	movl	8(%esp), %edi
	movl	%ebp, %esp
	popl	%ebp
	ret
	.size	swap, .-swap
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

	.file	"ex3_56.c"
	.text
.globl loop
	.type	loop, @function
loop:
	pushl	%ebp
	movl	%esp, %ebp
	pushl	%esi
	pushl	%ebx
	movl	8(%ebp), %ebx
	movl	12(%ebp), %ecx
	movl	$-1, %edx
	movl	$1431655765, %eax
.L2:
	movl	%edx, %esi
	andl	%ebx, %esi
	xorl	%esi, %eax
	sarl	%cl, %edx
	testl	%edx, %edx
	jne	.L2
	popl	%ebx
	popl	%esi
	popl	%ebp
	ret
	.size	loop, .-loop
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

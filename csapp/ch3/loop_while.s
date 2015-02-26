	.file	"loop_while.c"
	.text
.globl loop_while
	.type	loop_while, @function
loop_while:
	pushl	%ebp
	movl	%esp, %ebp
	pushl	%ebx
	movl	8(%ebp), %edx
	movl	12(%ebp), %ebx
	movl	$1, %eax
	cmpl	%ebx, %edx
	jge	.L3
	leal	(%ebx,%edx), %ecx
.L4:
	imull	%ecx, %eax
	addl	$1, %edx
	addl	$1, %ecx
	cmpl	%edx, %ebx
	jg	.L4
.L3:
	popl	%ebx
	popl	%ebp
	ret
	.size	loop_while, .-loop_while
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

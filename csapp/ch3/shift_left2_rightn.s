	.file	"shift_left2_rightn.c"
	.text
.globl shift_left2_rightn
	.type	shift_left2_rightn, @function
shift_left2_rightn:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %eax
	sall	$2, %eax
	movl	12(%ebp), %ecx
	sarl	%cl, %eax
	popl	%ebp
	ret
	.size	shift_left2_rightn, .-shift_left2_rightn
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5.1) 4.4.3"
	.section	.note.GNU-stack,"",@progbits

!Universidade de Brasília
!Métodos computacionais 
!Israel Garcia de Oliveira
!Decomposição LU


program decomposicao_lu
   implicit none
   real, dimension(6,6) :: a, l, u !Matriz de coeficientes, e as matrizes de decomposição L e U
   real, dimension (6)  :: x, b, y    !Vetor resposta e vetor constante
   integer              :: i, j, k, m, p !Índices
   real                 :: soma_a, soma_b, soma_c !Somatórios
   
   !Abrindo arquivos
   open(unit=10, file='coeficientes.txt', status='old')
   open(unit=11, file='vetor de constantes.txt', status='old')
   open(unit=12, file='Vetor resposta.txt', status='unknown')
   
   !Lendo as matrizes e vetores
   do i=1,6
      read(10,*)(a(i,j), j=1,6)
      read(11,*)b(i)
   end do
   
   !Definindo valores
   
   !Passo1
   do i=1,6
      u(i,i)=1
   end do	  
   l(1,1)=a(1,1)
   
   !Passo 2
   do j=2,6
      u(1,j)=a(1,j)/l(1,1)
	  l(j,1)=a(j,1)
   end do
  
  !Passo 3
   do i=2,6
      
	  !Passo 4
	  soma_a=0
	  do k=1,i-1
	     soma_a=soma_a+l(i,k)*u(k,i)
      end do
      l(i,i)=a(i,i)-soma_a
      
	  !Passo 5
      do j=i+1,6
         soma_b=0
         do p=1,i-1
            soma_b=soma_b+l(i,p)*u(p,j)
         end do
         u(i,j)=(a(i,j)-soma_b)/l(i,i)
         soma_c=0
         do m=1,i-1
            soma_c=soma_c+l(j,m)*u(m,i)
         end do
         l(j,i)=(a(j,i)-soma_c)
      end do		 
   end do
   
   !Parte 6
   y(1)=b(1)/l(1,1)
   do i=2,6
      soma_a=0
	  do j=1,i-1
	     soma_a=soma_a+l(i,j)*y(j)
      end do
      y(i)=(b(i)-soma_a)/l(i,i)
   end do
   
   !Parte 7
   x(6)=y(6)/u(6,6)	  
   do i=5,1,-1
      soma_a=0
      do j=i+1,6
          soma_a=soma_a+u(i,j)*x(j)
	  end do
	  x(i)=y(i)-soma_a
   end do
   
   !Parte 8
   do i=1,6
      write(12,*)x(i)
   end do
   
   !Fechando arquivos
   close(unit=10)
   close(unit=11)
   close(unit=12)
end program decomposicao_lu




















#include "stm32f10x.h"
#include "pwm_output.h"
#include "USART1_Config.h"
#include <stdio.h>


//extern uint16_t time ;

int main(void)
{
	TIM3_PWM_Init();
	USART1_Config();
  NVIC_Config();
  	
	printf("׼������");	
//	printf("\r\n ���ڳ����ն˻��ߴ��ڵ������������ַ� \r\n");	
	
	
	
	for(;;)
	{
	
	}

	 
}

